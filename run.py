import time
import requests
import datetime
import re
from urllib.parse import quote
from pprint import pprint
from dateutil.relativedelta import relativedelta

from bs4 import BeautifulSoup

# So many pubmed libaries
from Bio import Entrez #pubmed search
from pubmed_lookup import PubMedLookup, Publication
import metapub

# USPTO search that would be great if it worked
import pypatent 

# USPTO tool that's kludgy af
# from uspto.pbd.tasks import UsptoPairBulkDataDownloader

# Tell pubmed who we be
Entrez.email = "alex.makijokela@gmail.com"

class PMCSearchResult:

    def __init__(self, pubmed_id, pmc_id, url, title, journal, pub_date, abstract):
        self.pubmed_id=pubmed_id
        self.pmc_id=pmc_id
        self.url=url
        self.pmc_url="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC{}/".format(pmc_id)
        self.title=title
        self.journal=journal
        self.pub_date=pub_date.date() #datetime -> date
        self.abstract=abstract

# Was tempting to write a PatentSearchResult class, but the pypatent.Patent class is sufficient here



def now_as_str():
    return datetime.datetime.strftime(datetime.datetime.now(),'%Y%m%d%H%M')


# Lil helper function for Entrez efetch/esummary queries
#
def pmc_id_list_to_string(pmc_ids):
    pmc_ids_string=','.join(pmc_ids)
    return pmc_ids_string

# Query that returns a list of IDs
# 
def pubmed_central_search_return_ids(search_term, results_limit, min_date):
    min_date_as_str=min_date.strftime('%Y/%m/%d')
    max_date_as_str=datetime.datetime.now().strftime('%Y/%m/%d')
    handle = Entrez.esearch(db="pmc", 
                            retmax=results_limit, 
                            datetype='pdat', 
                            mindate=min_date_as_str, 
                            maxdate=max_date_as_str,
                            term=search_term)
    record = Entrez.read(handle)
    handle.close()
    time.sleep(0.4) #rate limit
    pmc_ids=record['IdList']
    return pmc_ids

# Get a PubMed Central article and put it in the PMCSearchResult class
# Sort of kludgy
# These can also be pulled in bulk using the Entrez efetch or esummary functions
# Unfortunately, esummary doesn't include abstracts :( 
# And efetch seems to have some issues with PMC where Entrez parse/read can't
# use the output. I've tried debugging it to no avail.
#
# There are more fields in the metapub article object if we ever need them
#
# The timedelta subtraction is because the metapub package seems to add a day
# 
def get_pmc_article(pmc_id):
    fetch = metapub.PubMedFetcher()
    try:
        article_raw = fetch.article_by_pmcid(pmc_id) 
        article = PMCSearchResult(pubmed_id=article_raw.pmid,
                      pmc_id=article_raw.pmc,
                      url=article_raw.url,
                      title=article_raw.title,
                      journal=article_raw.journal,
                      pub_date=article_raw.history['pubmed']-datetime.timedelta(days=1), 
                      abstract=article_raw.abstract
                      )
    except metapub.exceptions.MetaPubError:
        #TODO: Find some better means of retrieval
        article = PMCSearchResult(pubmed_id="Unknown - Retrieval Error",
                      pmc_id=pmc_id,
                      url="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC{}/".format(pmc_id),
                      title="Unknown - Retrieval Error",
                      journal="Unknown - Retrieval Error",
                      pub_date=datetime.datetime(1980,1,1), 
                      abstract="Unknown - Retrieval Error"
                      )
    return article

# Pull all of the pubmed article IDs and then retrieve the article for each.
#
def get_pubmed_articles(search_term, results_limit, min_date):
    pmc_ids=pubmed_central_search_return_ids(search_term, results_limit, min_date)
    pmc_articles=[]
    for pmc_id in pmc_ids:
        article=get_pmc_article(pmc_id)
        time.sleep(0.34) #rate limiter per pubmed api - with an api key this can be 10/s instead of 3/s
        print(vars(article))
        pmc_articles.append(article)
    pmc_articles.sort(key=lambda x:x.pub_date, reverse=True)
    return pmc_articles


# Bulk patent pull
# Doesn't work. 
# It's a more elegant solution, but sadly there's an unresolved bug in pypatent
# It effects all searches with multiple word inputs.
# See: https://github.com/daneads/pypatent/issues/6 
# If it gets resolved, it may be worth switching over.
#
# def get_patents_pypatent(search_term):
#    results=pypatent.Search(search_term)
#    if results:
#        print(results)



# Current solution for getting patent data
# Scrapes the patent listing page and then uses the guts of pypatent to pull the patent data
# If pypatent ever gets fixed, use the more elegant solution above
# Upgrade: Integrate the min date into the search term
#
def get_patents(search_term, results_limit, min_date):
    url_safe_search_term=quote(search_term)
    url='http://patft.uspto.gov/netacgi/nph-Parser?Sect1=PTO2&Sect2=HITOFF&u=%2Fnetahtml%2FPTO%2Fsearch-adv.htm&r=0&p=1&f=S&l=50&Query={}&d=PTXT'.format(url_safe_search_term)
    r = requests.get(url, headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'})
    
    soup = BeautifulSoup(r.text, 'html.parser')
    
    patents_base_url='http://patft.uspto.gov'
    patents_links_raw = soup.find_all('a', href=re.compile('netacgi'))
    patents_raw_list = [[i.text.replace('\n', '').strip(), patents_base_url + i['href']] for i in patents_links_raw if i.text.replace('\n', '').strip() != '']
    
    patents=[]
    for patent_num_idx in range(0, len(patents_raw_list), 2):
        if results_limit and (patent_num_idx + 1) > results_limit:
            break
        print("Fetching patent...")
        patent_title = patents_raw_list[patent_num_idx + 1][0]
        patent_title = re.sub(' +', ' ', patent_title)
        patent_link = patents_raw_list[patent_num_idx][1]
        patent_data = pypatent.Patent(patent_title, patent_link)
        patent_data.fetch_details()
        patent_date = datetime.datetime.strptime(patent_data.patent_date,"%B %d, %Y")
        if patent_date >= min_date:
            patents.append(patent_data)
        print("Fetched patent {}".format(patent_data.patent_num))
        time.sleep(0.34)

    return patents

# The output document
# This writes it
def write_output_document_html(search_term, min_date, pubmed_articles, patents):
    with open("output/{}.html".format(now_as_str()),'w') as f:
        f.write("<!DOCTYPE html>")
        f.write("<html>")
        f.write("<body>")
        f.write('<b>Search Term: </b>{}<br>'.format(search_term))
        f.write('<b>Date run: </b>{}<br>'.format(datetime.datetime.now().date().strftime("%Y/%m/%d")))
        f.write('<b>Results recency: </b>{}<br>'.format(min_date.date().strftime("%Y/%m/%d")))
        f.write("<br>")
        f.write("<h2>PubMed Articles</h2> <br>")
        f.write("<br>")
        for article in pubmed_articles:
            f.write("<b>Title:</b> {}<br>".format(article.title))
            f.write("<b>Abstract:</b> {}<br>".format(article.abstract))
            f.write("<b>Publication date:</b> {}<br>".format(article.pub_date))
            f.write("<b><a href=\"{}\">Link</a></b><br>".format(article.url))
            f.write("<br>")       
        f.write("<br>") 
        f.write("<h2>Patents</h2> <br>")
        f.write("<br>")
        for patent in patents:
            f.write("<b>Title:</b> {}<br>".format(patent.title))
            f.write("<b>Abstract:</b> {}<br>".format(patent.abstract))
            f.write("<b>Patent date:</b> {}<br>".format(patent.patent_date))
            f.write("<b>File date:</b> {}<br>".format(patent.file_date))
            f.write("<b><a href=\"{}\">Link</a></b><br>".format(patent.url))
            f.write("<br>")
        f.write("<body>")
        f.write("<html>")
    return True

if __name__=="__main__":
    
   #search term
   search_term = "\"hematopoietic stem cells\" AND CRISPR AND AAV AND (\"sickle cell disease\" OR \"beta thalassemia\")"
   
   #Max number of results
   results_limit=100

   #Recency: one year
   min_date=datetime.datetime.now()-relativedelta(years=1)

   pubmed_articles = get_pubmed_articles(search_term, results_limit, min_date)
   patents = get_patents(search_term, results_limit, min_date)
   write_output_document_html(search_term, min_date, pubmed_articles, patents)









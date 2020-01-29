import time
import requests
import datetime
import re
import os
import csv
import importlib
from urllib.parse import quote
from pprint import pprint
from dateutil.relativedelta import relativedelta

from bs4 import BeautifulSoup

# So many pubmed libaries
from Bio import Entrez #pubmed search

# USPTO search that would be great if it worked all the way
import pypatent 

from companysearch import metalist as companylist
from companysearch import LinkedInResult
from config import config

#default params
PATENT_TIME_DELAY=0.1
RESULTS_LIMIT=100
ENTREZ_TIME_DELAY=0.34
BASE_OUTPUT_URL="https://alexmakijokela.github.io/"

# USPTO tool that's kludgy af
# from uspto.pbd.tasks import UsptoPairBulkDataDownloader

# config = importlib.util.find_spec("config")
# if config is None:
#     config = importlib.util.find_spec("configGeneric")

if config["ncbi_api_key"]:
    os.environ["NCBI_API_KEY"] = config["ncbi_api_key"]
    # # Tell pubmed who we be
    Entrez.email = config["email"]
    Entrez.api_key = config["ncbi_api_key"]
    ENTREZ_TIME_DELAY=0.101

#have to import these after setting environment variables
from pubmed_lookup import PubMedLookup, Publication
import metapub

class ScimagoRanking:
    def __init__(self, issn):
        self.issn=issn.replace('-','')
        self.get_rankings_per_issn()

    def get_rankings_per_issn(self):
        with open("resources/scimagojr.csv","r") as f:
            rdr = csv.reader(f,delimiter=';')
            found_issn=False
            for row in rdr:
                if self.issn in row[4]:
                    found_issn=True
                    self.sjr=row[5].replace(',','.')
                    self.twoyearif=row[13].replace(',','.')
                    break
        if not found_issn:
            self.sjr='0.0'
            self.twoyearif='0.0'

class PMCSearchResult:

    def __init__(self, pubmed_id, pmc_id, url, title, author_list, journal, issn, pub_date, abstract, relevance_score, relevance_score_rough):
        self.pubmed_id=pubmed_id
        self.pmc_id=pmc_id
        self.url=url
        self.pmc_url="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC{}/".format(pmc_id)
        self.title=title
        self.parse_authors(author_list)
        self.journal=journal
        self.issn=issn
        self.pub_date=pub_date.date() #datetime -> date
        self.abstract=abstract
        self.relevance_score=relevance_score #could do this inside of this function
        self.relevance_score_rough=relevance_score_rough #could do this inside of this function
        self.rankings=ScimagoRanking(self.issn)

    def parse_authors(self, author_list):
        authors_as_list=[]
        for author in author_list:
            author_name='{} {}'.format(author.fore_name, author.last_name)
            authors_as_list.append(author_name)
        self.authors=', '.join(authors_as_list)

# Was tempting to write a PatentSearchResult class, but the pypatent.Patent class is sufficient here

class PatentSearchResult:

    def __init__(self, patent_data, relevance_score, relevance_score_rough):
        self.patent_data = patent_data
        self.relevance_score = relevance_score
        self.relevance_score_rough = relevance_score_rough


def now_as_str():
    return datetime.datetime.strftime(datetime.datetime.now(),'%Y%m%d%H%M')


# Lil helper function for Entrez efetch/esummary queries
#
def pmc_id_list_to_string(pmc_ids):
    pmc_ids_string=','.join(pmc_ids)
    return pmc_ids_string

  

    #for easy reference, remove when possible
    # search_term0 = "\"hematopoietic stem cells\" AND CRISPR AND AAV AND (\"sickle cell disease\" OR \"beta thalassemia\")"
    # search_term1 = "(\"sickle cell disease\" OR \"beta thalassemia\") AND (\"gene therapy\" OR \"genome editing\" OR \"mRNA therapy\")"
    # search_term2 = "\"cystic fibrosis\" AND (\"gene therapy\" OR \"genome editing\" OR \"mRNA therapy\")"

#search_term7 = "(\"sickle cell disease\" OR \"beta thalassemia\" OR \"beta-thalassemia\") AND (\"gene therapy\" OR \"genome editing\" OR \"mRNA therapy\" OR (\"hematopoietic stem cells\" AND CRISPR AND (AAV OR "adeno-associated virus"))"


# "(\"sickle cell disease\" OR \"beta thalassemia\") AND (\"gene therapy\" OR \"genome editing\" OR \"mRNA therapy\")"

# TODO: This function is the embodied definition of hard coded duct tape.
# Replace it as soon as possible
#
def search_term_text_check(search_term, text):
  #  print(search_term)
  #  print(text)
    if text is None: #empty text handler
        return False
    if isinstance(text, list): #some objects come through as lists - particularly patent claims/desc
        text=' '.join(text)
    if "thalassemia" in search_term: #Aaahhhhh it hurts it hurts noooo hardcoded values
        check1 = "sickle cell disease" in text.lower()
        check2 = "thalassemia" in text.lower()
        check3 = "gene therapy" in text.lower()
        check4 = "genome editing" in text.lower()
        check5 = "mrna therapy" in text.lower()
        check6 = "hematopoietic" in text.lower()
        check7 = "crispr" in text.lower()
        if ((check1 or check2) and (check3 or check4 or check5 or (check6 and check7))):
            return True
        else:
            return False
    if "cystic fibrosis" in search_term: #Aaahhhhh it hurts it hurts noooo hardcoded values
        check1 = "cystic fibrosis" in text.lower()
        check2 = "gene therapy" in text.lower()
        check3 = "genome editing" in text.lower()
        check4 = "mrna therapy" in text.lower()
        if (check1 and (check2 or check3 or check4)):
            return True
        else:
            return False
    if "cellular reprogramming" in search_term: #Aaahhhhh it hurts it hurts noooo hardcoded values
        check1 = "cellular reprogramming" in text.lower()
        check2 = "ageing" in text.lower()
        check3 = "aging" in text.lower()
        check4 = "mtor" in text.lower()
        check5 = "senescence" in text.lower()
        check6 = "lysosome" in text.lower()
        if (check1 and (check2 or check3) and (check4 or check5 or check6)):
            return True
        else:
            return False
    if "regulatory T cells" in search_term: #Aaahhhhh it hurts it hurts noooo hardcoded values
        check1 = "regulatory t cells" in text.lower()
        check2 = "autoimmune" in text.lower()
        check3 = "cancer" in text.lower()
        if (check1 and (check2 or check3)):
            return True
        else:
            return False



    search_term9 = "\"cellular reprogramming\" AND (ageing OR aging) OR mTOR OR senescence OR lysosome"
    search_term10 = "\"cellular reprogramming\" AND ((ageing OR aging) OR (mTOR OR senescence OR lysosome))"
    search_term11 = "\"cellular reprogramming\" AND (ageing OR aging) AND (mTOR OR senescence OR lysosome)"
    search_term12 = "\"regulatory T cells\" AND (autoimmune OR cancer)" 





# TODO: This function is the embodied definition of hard coded duct tape.
# Replace it as soon as possible
#
def search_term_rough_score(search_term, text):
  #  print(search_term)
  #  print(text)
    if text is None: #empty text handler
        return 0
    if isinstance(text, list): #some objects come through as lists - particularly patent claims/desc
        text=' '.join(text)
    text=text.lower()
    search_term_derezzed = re.sub(r'[^a-zA-Z\d\s:]', '', search_term.lower())
    all_words=set(search_term_derezzed.split(' '))
    all_words.discard('and')
    all_words.discard('or')
    #print(all_words)
    total_score=0.0
    for word in all_words:
        if word in text:
            total_score+=1.0
    normalized_score = total_score / len(all_words)
    return normalized_score



def get_relevance_score_pmc(article_raw, search_term):
    relevance_score=0
    highest_possible=4 + 2 + 1
    in_title = 4 if search_term_text_check(search_term, article_raw.title) else 0
    in_abstract = 2 if search_term_text_check(search_term, article_raw.abstract) else 0
    in_text = 1 #full text not available via current means
    relevance_score = in_title+in_abstract+in_text
    normalized_score=round(relevance_score/highest_possible,2)
    return normalized_score



def get_relevance_score_patent(patent_object, search_term):
    relevance_score=0
    highest_possible = 8 + 4 + 2 + 1
    in_title = 8 if search_term_text_check(search_term, patent_object.title) else 0
    in_abstract = 4 if search_term_text_check(search_term, patent_object.abstract) else 0
    in_claims = 2 if search_term_text_check(search_term, patent_object.claims) else 0
    in_description = 1 if search_term_text_check(search_term, patent_object.description) else 0
    relevance_score = in_title + in_abstract + in_claims + in_description
    normalized_score=round(relevance_score/highest_possible,2)
    return normalized_score




def get_relevance_score_rough_pmc(article_raw, search_term):
    relevance_score=0
    highest_possible = 4 + 2 + 1
    in_title = 4 * search_term_rough_score(search_term, article_raw.title)
    in_abstract = 2 * search_term_rough_score(search_term, article_raw.abstract)
    in_text = 1 #full text not available via pmc
    relevance_score = in_title+in_abstract
    normalized_score=round(relevance_score/highest_possible,2)
    return normalized_score



def get_relevance_score_rough_patent(patent_object, search_term):
    relevance_score=0
    highest_possible = 8 + 4 + 2 + 1
    in_title = 8 * search_term_rough_score(search_term, patent_object.title)
    in_abstract = 4 * search_term_rough_score(search_term, patent_object.abstract)
    in_claims = 2 * search_term_rough_score(search_term, patent_object.claims)
    in_description = 1 * search_term_rough_score(search_term, patent_object.description)
    relevance_score = in_title + in_abstract + in_claims + in_description
    normalized_score=round(relevance_score/highest_possible,2)
    return normalized_score




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
def get_pmc_article(pmc_id, search_term):
    fetch = metapub.PubMedFetcher()
    try:
        article_raw = fetch.article_by_pmcid(pmc_id) 
      #  print(vars(article_raw)) #for debugging
        relevance_score = get_relevance_score_pmc(article_raw, search_term) or 0
        relevance_score_rough = get_relevance_score_rough_pmc(article_raw, search_term) or 0
        authors=[]
        article = PMCSearchResult(pubmed_id=article_raw.pmid,
                      pmc_id=article_raw.pmc,
                      url=article_raw.url,
                      title=article_raw.title,
                      author_list=article_raw.author_list,
                      journal=article_raw.journal,
                      issn=article_raw.issn,
                      pub_date=article_raw.history['pubmed']-datetime.timedelta(days=1), 
                      abstract=article_raw.abstract,
                      relevance_score=relevance_score,
                      relevance_score_rough=relevance_score_rough
                      )
    except metapub.exceptions.MetaPubError:
        #TODO: Find some better means of retrieval for articles without a pubmed ID (creates metapub error)
        article = PMCSearchResult(pubmed_id="Unknown - Retrieval Error, only exists in PMIC",
                      pmc_id=pmc_id,
                      url="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC{}/".format(pmc_id),
                      title="Unknown - Retrieval Error",
                      author_list=[],
                      issn="Unknown - Retrieval Error",
                      journal="Unknown - Retrieval Error",
                      pub_date=datetime.datetime(1980,1,1), 
                      abstract="Unknown - Retrieval Error",
                      relevance_score=0,
                      relevance_score_rough=0
                      )
    return article

# Pull all of the pubmed article IDs and then retrieve the article for each.
#
def get_pubmed_articles(search_term, results_limit, min_date):
    pmc_ids=pubmed_central_search_return_ids(search_term, results_limit, min_date)
    time.sleep(ENTREZ_TIME_DELAY) #rate limiter per pubmed api - with an api key this can be 10/s instead of 3/s    
    pmc_articles=[]
    for pmc_id in pmc_ids:
        article=get_pmc_article(pmc_id, search_term)
        time.sleep(ENTREZ_TIME_DELAY) #rate limiter per pubmed api - with an api key this can be 10/s instead of 3/s
        print("Fetching PubMed Article: {}, {}, {}".format(article.title, article.relevance_score, article.relevance_score_rough))
        if (float(article.rankings.twoyearif) >= 7.0):
            pmc_articles.append(article)
    pmc_articles.sort(key=lambda x:(x.relevance_score, x.relevance_score_rough, float(x.rankings.twoyearif)), reverse=True)
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
   #     print(vars(patent_data)) #for debugging
        if patent_date >= min_date:
            relevance_score = get_relevance_score_patent(patent_data, search_term) or 0
            relevance_score_rough = get_relevance_score_rough_patent(patent_data, search_term) or 0
            print(patent_data.title, relevance_score, relevance_score_rough)
            patent_result = PatentSearchResult(patent_data, relevance_score, relevance_score_rough)
            patents.append(patent_result)
        else:
            break # Works because patents are returned ordered by date.
        time.sleep(PATENT_TIME_DELAY)
    patents.sort(key=lambda x:(x.relevance_score, x.relevance_score_rough, x.patent_data.patent_date), reverse=True)
    return patents

def get_companies(index):
    return companylist[index]

# The output document
# This writes it
def write_output_document_html(search_term, min_date, pubmed_articles, companies, patents):
    file_name_first_word=re.sub(r'[^a-zA-Z\d\s:]', '', search_term).lower().split(' ')[0]
    filename="{}_{}.html".format(now_as_str(),file_name_first_word)
    filepath="output/{}".format(filename)
    with open(filepath,'w') as f:
        f.write("<!DOCTYPE html>")
        f.write("<html>")
        f.write("<head>")
        f.write("<link href='https://fonts.googleapis.com/css?family=Spectral' rel='stylesheet'>")
        f.write("<style>")
        f.write("body {")
        f.write("    font-family: 'Spectral';font-size: 14px;")
        f.write("}")
        f.write("</style>")
        f.write("</head>")
        f.write("<body>")
        f.write('<b>Search Term: </b>{}<br>'.format(search_term))
        f.write('<b>Date run: </b>{}<br>'.format(datetime.datetime.now().date().strftime("%Y/%m/%d")))
        f.write('<b>Results recency: </b>{}<br>'.format(min_date.date().strftime("%Y/%m/%d")))
        f.write("<br>")
        f.write("Jump to: <a href=\"#pubmed\">PubMed Articles</a> | <a href=\"#companies\">Companies</a> | <a href=\"#patents\">Patents</a>")
        f.write("<br>")
        f.write("<a name=\"pubmed\"></a>")
        f.write("<h2>PubMed Articles</h2> <br>")
        f.write("<br>")
        for article in pubmed_articles:
            f.write("<b>Title:</b> {}<br>".format(article.title))
            f.write("<b>Abstract:</b> {}<br>".format(article.abstract))
            f.write("<b>Publication date:</b> {}<br>".format(article.pub_date))
            f.write("<b>Authors:</b> {}<br>".format(article.authors))
            f.write("<b>Journal:</b> {}<br>".format(article.journal))
            f.write("<b>ISSN:</b> {}<br>".format(article.issn))
            f.write("<b>Relevance score 1:</b> {}<br>".format(article.relevance_score))
            f.write("<b>Relevance score 2:</b> {}<br>".format(article.relevance_score_rough))
            f.write("<b>Two-year IF:</b> {}<br>".format(article.rankings.twoyearif))
            f.write("<b>SJR:</b> {}<br>".format(article.rankings.sjr))
            f.write("<b><a href=\"{}\">Link</a></b><br>".format(article.url))
            f.write("<br>")       
        f.write("<br>") 
        f.write("<a name=\"companies\"></a>")
        f.write("<h2>Companies</h2> <br>")
        f.write("<br>")
        for company in companies:
            f.write("<b>Company Name:</b> {}<br>".format(company.company_name))
            f.write("<b>Overview:</b> {}<br>".format(company.overview))
            f.write("<b>Specialties:</b> {}<br>".format(company.specialties))
            f.write("<b><a href=\"{}\">LinkedIn Profile</a></b><br>".format(company.linkedin_url))
            f.write("<b><a href=\"{}\">Website</a></b><br>".format(company.company_url))
            f.write("<br>")       
        f.write("<br>") 
        f.write("<a name=\"patents\"></a>")
        f.write("<h2>Patents</h2> <br>")
        f.write("<br>")
        for patent in patents:
            f.write("<b>Title:</b> {}<br>".format(patent.patent_data.title))
            f.write("<b>Abstract:</b> {}<br>".format(patent.patent_data.abstract))
            f.write("<b>Patent date:</b> {}<br>".format(patent.patent_data.patent_date))
            f.write("<b>File date:</b> {}<br>".format(patent.patent_data.file_date))
            f.write("<b>Relevance score 1:</b> {}<br>".format(patent.relevance_score))
            f.write("<b>Relevance score 2:</b> {}<br>".format(patent.relevance_score_rough))
            f.write("<b><a href=\"{}\">Link</a></b><br>".format(patent.patent_data.url))
            f.write("<br>")
        f.write("</body>")
        f.write("</html>")
    return filename



# The output document
# This writes it
def write_output_document_preview(search_term, min_date, pubmed_articles, companies, patents, filename):
    filepath="output/{}_preview.html".format(filename)
    with open(filepath,'w') as f:
        f.write("<!DOCTYPE html>")
        f.write("<html>")
        f.write("<head>")
        f.write("<link href='https://fonts.googleapis.com/css?family=Spectral' rel='stylesheet'>")
        f.write("<style>")
        f.write("body {")
        f.write("    font-family: 'Spectral';font-size: 14px;")
        f.write("}")
        f.write("</style>")
        f.write("</head>")
        f.write("<body>")
        f.write('<b>Search Term: </b>{}<br>'.format(search_term))
        f.write('<b>Date run: </b>{}<br>'.format(datetime.datetime.now().date().strftime("%Y/%m/%d")))
        f.write("<br>")
        f.write("<h2>PubMed Articles</h2> <br>")
        for article in pubmed_articles[:3]:
            f.write("<b><a href=\"{}\">{}</a></b><br>".format(article.url, article.title))
            f.write("<b>Journal:</b> {}<br>".format(article.journal))
            f.write("<b>Two-year IF:</b> {}<br>".format(article.rankings.twoyearif))
            f.write("<br>")       
        f.write("<b><a href=\"{}\">More Results...</a></b><br>".format(BASE_OUTPUT_URL+filename+"#pubmed"))
        f.write("<br>") 
        f.write("<h2>Companies</h2> <br>")
        for company in companies[:3]:
            f.write("<b><a href=\"{}\">{}</a></b><br>".format(company.linkedin_url, company.company_name))
            f.write("<br>")      
        f.write("<b><a href=\"{}\">More Results...</a></b><br>".format(BASE_OUTPUT_URL+filename+"#companies")) 
        f.write("<br>") 
        f.write("<h2>Patents</h2> <br>")
        for patent in patents[:3]:
            f.write("<b><a href=\"{}\">{}</a></b><br>".format(patent.patent_data.url, patent.patent_data.title))
            f.write("<b>Patent date:</b> {}<br>".format(patent.patent_data.patent_date))
            f.write("<br>")
        f.write("<b><a href=\"{}\">More Results...</a></b><br>".format(BASE_OUTPUT_URL+filename+"#patents"))
        f.write("<br>")
        f.write("<br>")
        f.write("<b><a href=\"{}\">Link to Full Search Results</a></b><br>".format(BASE_OUTPUT_URL+filename))
        f.write("</body>")
        f.write("</html>")
    print("URL: {}".format(BASE_OUTPUT_URL+filename))
    return True

# Download the latest sgimago journal rankings
# The csv from http://scimagojr.com/journalrank.php
# Place it in the resources folder
# And rename it to a generic name (from 'scimagojr 2018.csv' to 'scimagojr.csv')
def downloadScimago():
    pass #todo





if __name__=="__main__":

    # #search term
    # search_terms = []
    # search_term = "\"hematopoietic stem cells\" AND CRISPR AND AAV AND (\"sickle cell disease\" OR \"beta thalassemia\")"
    # search_term2 = "\"hepatitis A\" AND \"gene therapy\""
    # search_term3 = "\"Parkinson's\" AND \"gene therapy\""
    # search_term4 = "\"cystic fibrosis\" AND (\"gene therapy\" OR \"genome editing\" OR \"mRNA therapy\")"
    # search_term5 = "(sarcopenia OR osteoarthritis) AND mRNA"
    # search_terms.append(search_term)
    # search_terms.append(search_term2)
    # search_terms.append(search_term3)
    # search_terms.append(search_term4)
    # search_terms.append(search_term5)



    search_terms = []
    search_term0 = "\"hematopoietic stem cells\" AND CRISPR AND AAV AND (\"sickle cell disease\" OR \"beta thalassemia\")"
    search_term1 = "(\"sickle cell disease\" OR \"beta thalassemia\") AND (\"gene therapy\" OR \"genome editing\" OR \"mRNA therapy\")"
    search_term2 = "\"cystic fibrosis\" AND (\"gene therapy\" OR \"genome editing\" OR \"mRNA therapy\")"
    search_term3 = "\"hemophilia A\" AND (\"gene therapy\" OR \"genome editing\" OR \"mRNA therapy\")"
    search_term4 = "\"Parkinson's\" AND (\"gene therapy\" OR \"genome editing\" OR \"mRNA therapy\")"
    search_term5 = "(sarcopenia OR osteoarthritis) AND (\"gene therapy\" OR \"genome editing\" OR \"mRNA therapy\")"
    
    search_term7 = "(\"sickle cell disease\" OR \"beta thalassemia\" OR \"beta-thalassemia\") AND (\"gene therapy\" OR \"genome editing\" OR \"mRNA therapy\" OR (\"hematopoietic stem cells\" AND CRISPR))"

    search_term8 = "((\"sickle cell disease\"[Abstract]) OR (\"beta thalassemia\"[Abstract]) OR (\"beta-thalassemia\"[Abstract])) AND ((\"gene therapy\"[Abstract]) OR (\"genome editing\"[Abstract]) OR (\"mRNA therapy\"[Abstract]) OR ((\"hematopoietic stem cells\"[Abstract]) AND CRISPR[Abstract]))"


    search_term9 =  "\"cellular reprogramming\" AND (ageing OR aging) OR mTOR OR senescence OR lysosome"
    search_term10 = "\"cellular reprogramming\" AND ((ageing OR aging) OR (mTOR OR senescence OR lysosome))"
    search_term11 = "\"cellular reprogramming\" AND (ageing OR aging) AND (mTOR OR senescence OR lysosome)"
    search_term12 = "\"regulatory T cells\" AND (autoimmune OR cancer)" 

    search_term13 = "(ageing OR aging) AND (mTOR OR senescence OR lysosome OR \"cellular reprogramming\")"

    search_term14 = "\"cellular reprogramming\"[Abstract] AND (ageing[Abstract] OR aging[Abstract]) AND (mTOR[Abstract] OR senescence[Abstract] OR lysosome[Abstract])"
    search_term15 = "\"regulatory T cells\"[Abstract] AND (autoimmune[Abstract] OR cancer[Abstract])" 
    search_term16 = "(ageing[Abstract] OR aging[Abstract]) AND (mTOR[Abstract] OR senescence[Abstract] OR lysosome[Abstract] OR \"cellular reprogramming\"[Abstract])"
 


    #search_terms.append(search_term0)
    # search_terms.append(search_term9)
    search_terms.append(search_term14)
    search_terms.append(search_term15)
    search_terms.append(search_term16)
  #  search_terms.append(search_term2)
    # search_terms.append(search_term3)
    # search_terms.append(search_term4)
    # search_terms.append(search_term5)

# from company search page
# beta_thal_sickle_cell_results=[]
# cystic_fibr_results=[]
# hemophilia_results=[]
# parkinsons_results=[]
# sarcopenia_or_osteoarthritis_results=[]



   # company_search_term = "hematopoietic stem cells"

    #Max number of results
    results_limit=RESULTS_LIMIT
    
    #Recency: one year
    min_date=datetime.datetime.now()-relativedelta(years=1)
   # test_pmc="PMC6493311"
   # get_pmc_article(test_pmc)
#    test_issn='23290501'
#    get_rankings_per_issn(test_issn)

    for i,search_term in enumerate(search_terms):
        pubmed_articles = get_pubmed_articles(search_term, results_limit, min_date)
        patents = get_patents(search_term, results_limit, min_date)
        companies = [] #get_companies(i)
        filename=write_output_document_html(search_term, min_date, pubmed_articles, companies, patents)
        write_output_document_preview(search_term, min_date, pubmed_articles, companies, patents, filename)









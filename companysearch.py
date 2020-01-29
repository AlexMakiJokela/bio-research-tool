class LinkedInResult:
	def __init__(self, company_name, linkedin_url=None, company_url=None, overview=None, specialties=None):
		self.company_name=company_name
		self.linkedin_url=linkedin_url
		self.company_url=company_url
		self.overview=overview
		self.specialties=specialties or "Not listed"


# cystic fibrosis AND gene therapy OR mRNA (just the disease and 2 technology modalities)
# "cystic fibrosis" AND ("gene therapy" OR "gene editing" OR "genome editing" OR mrna) 
# "cystic fibrosis" AND ("gene therapy" OR "gene editing" OR "genome editing" OR mrna OR CRISPR)
# ("beta thalassemia" OR "sickle cell") AND ("gene therapy" OR "gene editing" OR "genome editing" OR mrna OR CRISPR)  
# Parkinson's AND gene therapy
# sarcopenia OR osteoarthritis AND mRNA


metalist=[]

beta_thal_sickle_cell_results=[]
cystic_fibr_results=[]
hemophilia_results=[]
parkinsons_results=[]
sarcopenia_or_osteoarthritis_results=[]


company_name="CRISPR Therapeutics"
linkedin_url="https://www.linkedin.com/company/crispr-therapeutics/about/"
company_url="http://www.crisprtx.com"
overview="""CRISPR Therapeutics is a leading gene-editing company focused on the development of transformative medicines using its proprietary CRISPR/Cas9 gene-editing platform. CRISPR/Cas9 is a revolutionary technology that allows for precise, directed changes to genomic DNA. Our multi-disciplinary team of world-class researchers and drug developers is working to translate this technology into breakthrough human therapeutics in a number of serious diseases. Our lead programs in beta-thalassemia and sickle cell disease have advanced to IND/CTA-enabling studies with a CTA filing planned by the end of 2017, and we are advancing additional programs in ex vivo and in vivo disease areas. In addition to our fully-owned programs, our strategic collaborations with Bayer AG and Vertex Pharmaceuticals expand our portfolio and enable us with unique capabilities. Through our private financings, partnerships, and IPO we have raised >$400M to fund and accelerate our portfolio. We have licensed the foundational CRISPR/Cas9 patent estate for human therapeutic use from our scientific founder, Dr. Emmanuelle Charpentier, who co-invented the application of CRISPR/Cas9 for gene editing. Our company is headquartered in Zug, Switzerland with R&D operations in Cambridge, Massachusetts, USA and some business operations in London, United Kingdom."""
specialties="""Gene Editing, AAV, Hematology, and Immuno-Oncology"""
linkedin_add=LinkedInResult(company_name,linkedin_url,company_url,overview,specialties)
beta_thal_sickle_cell_results.append(linkedin_add)
cystic_fibr_results.append(linkedin_add)





company_name="Orchard Therapeutics"
linkedin_url="https://www.linkedin.com/company/orchard-therapeutics/about/"
company_url="http://www.orchard-tx.com"
specialties="""Stem cell technology, Gene therapy, Orphan diseases, and Paediatric diseases"""
overview="""Orchard Therapeutics is a leading global fully integrated commercial-stage company dedicated to transforming the lives of patients with rare diseases through innovative gene therapies.

Orchard’s portfolio of autologous ex vivo gene therapy programs has demonstrated sustained clinical benefit in over 150 patients across five disease areas. These programs include Strimvelis®, the first autologous ex vivo gene therapy approved by the EMA in 2016, 3 programs in advanced registrational studies in MLD (metachromatic leukodystrophy), WAS (Wiskott Aldrich syndrome) and ADA-SCID (adenosine deaminase severe combined immunodeficiency), 2 other clinical programs in X-CGD (X-linked chronic granulomatous disease) and beta-thalassemia, as well as an extensive preclinical pipeline.

The company is partnered with world-leading institutions in gene therapy, including University College London, Great Ormond Street Hospital, the University of Manchester and Central Manchester University Hospitals, the University of California Los Angeles and Boston Children’s Hospital, and Telethon Institute of Gene Therapy/Ospedale San Raffaele.

Orchard is a publicly traded company (NASDAQ: ORTX) with offices in the UK and the US, including London, San Francisco and Boston."""
linkedin_add=LinkedInResult(company_name,linkedin_url,company_url,overview,specialties)
beta_thal_sickle_cell_results.append(linkedin_add)




company_name="Trucode Gene Repair, Inc."
linkedin_url="https://www.linkedin.com/company/trucode-gene-repair-inc/about/"
specialties=""""""
company_url="http://www.trucodegene.com"
overview="""Trucode Gene Repair is advancing its novel triplex gene editing platform to potentially cure devastating genetic diseases, with initial focus on sickle cell disease and cystic fibrosis. The elegance of triplex gene editing lies in its ability to harness natural, high-fidelity DNA repair mechanisms, and its independence from the requirement for exogenous nucleases and viral vectors. """
linkedin_add=LinkedInResult(company_name,linkedin_url,company_url,overview,specialties)
beta_thal_sickle_cell_results.append(linkedin_add)
cystic_fibr_results.append(linkedin_add)




company_name="addmedica"
linkedin_url="https://www.linkedin.com/company/addmedica/about/"
company_url="http://www.addmedica.com"
specialties="""transplantation, wound-healing, and sickle-cell-disease"""
overview="""addmedica is a fast growing company focused on developing and marketing medical products for:
• rare diseases
• unmet medical needs in developed and emerging countries
• serious conditions

addmedica is dedicated to providing high medical value to physicians, patients, and managed care organizations, by developing, registering and marketing a wide range of medical products in several rare and debilitating diseases. 

addmedica’s strategic areas of interest comprise:
• wound healing, tissue growth and cell regeneration
• organ transplant, tissue replacement 
• genetic diseases, drug or substitute therapy, cell or gene therapy

addmedica, complying with its pharmaceutical status, is proud to offer a range of products in the fields of 
• lung transplantation,
• wound healing and deep burn care. 
• sickle cell disease (European Orphan Medicinal Product)

addmedica is constantly looking for new opportunities and partnerships, to develop and commercialize products with high medical demand. 

As a result of its know-how, its commitment and its positioning, addmedica is ready to become a leading firm for the provision of medical products and innovative techniques for rare diseases with the best quality of services."""
linkedin_add=LinkedInResult(company_name,linkedin_url,company_url,overview,specialties)
beta_thal_sickle_cell_results.append(linkedin_add)


company_name="Aruvant"
linkedin_url="https://www.linkedin.com/company/aruvant/"
company_url="http://aruvant.com/"
specialties=""""""
overview="""Aruvant Sciences is a clinical-stage gene therapy company focused on hematological conditions, with an emphasis on helping patients suffering from sickle cell disease and β-thalassemia. ARU-1801, the lead candidate in Aruvant's pipeline, is an investigational lentiviral gene therapy for sickle cell disease and transfusion-dependent β-thalassemia. ARU-1801 incorporates a patented gene payload for a modified gamma-globin delivered into autologous stem cells via a proprietary vector construct, with the aim of restoring normal red blood cell function through increased levels of fetal hemoglobin. The high potency of the modified gamma globin enables ARU-1801 engraftment with only Reduced Intensity Conditioning (RIC)."""
linkedin_add=LinkedInResult(company_name,linkedin_url,company_url,overview,specialties)
beta_thal_sickle_cell_results.append(linkedin_add)


company_name="Translate Bio"
linkedin_url="https://www.linkedin.com/company/translate-bio/about/"
company_url="http://www.translate.bio"
specialties="""Biotechnology, RNA Therapeutics, and Rare Diseases
"""
overview="""Translate Bio is a leading mRNA therapeutics company developing a new class of potentially transformative medicines to treat diseases caused by protein or gene dysfunction. Our proprietary mRNA therapeutic platform (MRTTM) is designed to develop product candidates that deliver mRNA carrying instructions to produce intracellular, transmembrane and secreted proteins for therapeutic benefit. We believe that our MRTTM platform is applicable to a broad range of diseases caused by insufficient protein production or where production of proteins can modify disease, including diseases that affect the lung, liver, eye, central nervous system, lymphatic system and circulatory system. Our two lead programs are being developed as treatments for cystic fibrosis (CF) and ornithine transcarbamylase (OTC) deficiency. """
linkedin_add=LinkedInResult(company_name,linkedin_url,company_url,overview,specialties)
cystic_fibr_results.append(linkedin_add)

company_name="Santhera Pharmaceuticals"
linkedin_url="https://www.linkedin.com/company/santhera-pharmaceuticals-ltd/about/"
company_url="http://www.santhera.com"
specialties=""""""
overview="""Santhera Pharmaceuticals (SIX: SANN) is a Swiss specialty pharmaceutical company focused on the development and commercialization of innovative medicines for rare neuromuscular and pulmonary diseases with high unmet medical need. Santhera is building a Duchenne muscular dystrophy (DMD) product portfolio to treat patients irrespective of causative mutations, disease stage or age. A marketing authorization application for Puldysa® (idebenone) is currently under review by the European Medicines Agency. Santhera has an option to license vamorolone, a first-in-class dissociative steroid currently investigated in a pivotal study in patients with DMD to replace standard corticosteroids. The clinical stage pipeline also includes POL6014 to treat cystic fibrosis (CF) and other neutrophilic pulmonary diseases, as well as omigapil and an exploratory gene therapy approach targeting congenital muscular dystrophies. Santhera out-licensed ex-North American rights to its first approved product, Raxone® (idebenone), for the treatment of Leber's hereditary optic neuropathy (LHON) to Chiesi Group.   

For more information, please visit the Company's website www.santhera.com"""
linkedin_add=LinkedInResult(company_name,linkedin_url,company_url,overview,specialties)
cystic_fibr_results.append(linkedin_add)




company_name="Vertex Pharmaceuticals"
linkedin_url="https://www.linkedin.com/company/vertex-pharmaceuticals/about/"
company_url="http://www.vrtx.com"
specialties="""Cystic Fibrosis, Alpha-1 Antitrypsin (AAT) deficiency, Sickle Cell Disease, Polycystic Kidney Disease (PKD), and Beta Thalassemia"""
overview="""Vertex is a global biotechnology company that invests in scientific innovation to create transformative medicines for people with serious and life-threatening diseases.

We discovered and developed the first medicines to treat the underlying cause of cystic fibrosis (CF), a rare, life-threatening genetic disease. In addition to clinical development programs in CF, Vertex has more than a dozen ongoing research programs focused on the underlying mechanisms of other serious diseases. 

Founded in 1989 in Cambridge, Massachusetts, our corporate headquarters is now located in Boston’s Innovation District, and our international headquarters is in London, United Kingdom. We currently employ approximately 2,500 people in the United States, Europe, Canada, Australia and Latin America with nearly two-thirds of our staff dedicated to research and development.

Vertex is consistently recognized as one of the industry’s top places to work by Science Magazine, The Boston Globe, Boston Business Journal and the San Diego Business Journal. Our research and medicines have also received esteemed recognitions, including the Robert J. Beall Therapeutics Development Award, the French Prix Galien and the British Pharmacological Society awards."""
linkedin_add=LinkedInResult(company_name,linkedin_url,company_url,overview,specialties)
cystic_fibr_results.append(linkedin_add)





company_name="Arcturus Therapeutics"
linkedin_url="https://www.linkedin.com/company/arcturus-therapeutics/about/"
company_url="http://www.arcturusrx.com"
specialties="""mRNA, siRNA, RNAi, Nucleic Acid Medicines, Lipid-Mediated Delivery, Rare Diseases, OTC Deficiency, and Cystic Fibrosis"""
overview="""Arcturus Therapeutics is a preclinical drug delivery and nucleic acid medicines company. We are focused on developing novel technologies to build the next generation of safe, effective RNA and DNA medicines. We have proprietary technologies, validating partnerships, and an experienced team with deep expertise in delivery and nucleic acid-based therapeutics.

Arcturus Therapeutics is presently recruiting outstanding candidates with experience in the field of RNA technologies and nanoparticle sciences. Only exceptional applicants need apply. Compensation and equity position is commensurate. Please email your resume to Careers@ArcturusRx.com, or visit https://arcturusrx.com/careers/"""
linkedin_add=LinkedInResult(company_name,linkedin_url,company_url,overview,specialties)
cystic_fibr_results.append(linkedin_add)




company_name="Editas Medicine"
linkedin_url="https://www.linkedin.com/company/editas-medicine/about/"
company_url="http://www.editasmedicine.com"
specialties="""Genome Editing, In Vivo (in body) Editing, Engineered Cell Medicines, Ocular Medicines, Genetic Diseases, Blood Diseases, Sickle Cell Disease, Cancer, Rare Diseases, and Immunogenetics"""
overview="""What if you could repair broken genes? That is the question we ask ourselves every day at Editas Medicine. We’re a leading genome editing company focused on translating the power and promise of our proprietary genome editing systems into medicines to help transform the lives of people with genetically-defined diseases. Our goal is to discover, develop, manufacture, and commercialize transformative medicines for a range of serious diseases, including eye diseases, blood diseases, and cancer. 

We are a vibrant company full of hope, possibilities, and a belief that, working together as One Editas, we can truly revolutionize the development of medicines. We are on an important journey to unlock the full potential of genome editing technology. A journey fueled by our distinct culture, expert team of Editas Medicine ‘Editors’, and the patients we aspire to help around the world. Connect with us to hear about the tremendous progress and scientific advancements we’ve already made and the next breakthrough on the horizon. If you are ingenious, passionate and resilient, come join the revolution. Repairing broken genes is only the beginning. """
linkedin_add=LinkedInResult(company_name,linkedin_url,company_url,overview,specialties)
beta_thal_sickle_cell_results.append(linkedin_add)
cystic_fibr_results.append(linkedin_add)




company_name="Spirovant Sciences, Inc."
linkedin_url="https://www.linkedin.com/company/spirovant/about/"
company_url="http://www.spirovant.com"
specialties=""""""
overview="""Spirovant Sciences is developing novel gene therapies for cystic fibrosis and other pulmonary diseases. We are the only company advancing programs with both AAV and lentivirus vectors."""
linkedin_add=LinkedInResult(company_name,linkedin_url,company_url,overview,specialties)
cystic_fibr_results.append(linkedin_add)





company_name="Abeona Therapeutics"
linkedin_url="https://www.linkedin.com/company/abeonatherapeutics/about/"
company_url="http://www.abeonatherapeutics.com"
specialties="""Gene Therapy, Infantile Batten Disease, Biotechnology, Cell Therapy, Rare Disease, Epidermolysis Bullosa, Lysosomal Storage Disease, Sanfiippo Syndrome Type A, Sanfiippo Syndrome Type B, juvenile Batten Disease, Pediatric Rare Diseases, and manufacturing"""
overview="""Abeona Therapeutics (Nasdaq: ABEO) is a fully-integrated gene and cell therapy company at the forefront of the rapidly-advancing field of genetic medicine. The Company’s multi-platform expertise across the manufacture, delivery, development, and discovery of novel gene and cell therapies has it uniquely positioned for success. Underpinning the Company’s robust pipeline is its fully-operational manufacturing facility producing therapies and vectors for preclinical and clinical studies. Abeona is also developing the AIM™ Vector Platform: 100+ next-generation AAV capsids for delivering gene therapies targeting a wide range of organs and multiple routes of delivery. A robust and diverse pipeline is led by a novel gene-corrected cell therapy poised to enter Phase 3 in mid-2019 and complemented by one-time gene therapy candidates across four lysosomal storage diseases. Several preclinical discoveries are led by an emerging program in cystic fibrosis that uses the AIM vector platform and a capsid that has shown potential across inherited and acquired retinal diseases.  """
linkedin_add=LinkedInResult(company_name,linkedin_url,company_url,overview,specialties)
cystic_fibr_results.append(linkedin_add)

company_name="Trucode Gene Repair, Inc."
linkedin_url="https://www.linkedin.com/company/trucode-gene-repair-inc/about/"
company_url="http://www.trucodegene.com"
specialties=""""""
overview="""Trucode Gene Repair is advancing its novel triplex gene editing platform to potentially cure devastating genetic diseases, with initial focus on sickle cell disease and cystic fibrosis. The elegance of triplex gene editing lies in its ability to harness natural, high-fidelity DNA repair mechanisms, and its independence from the requirement for exogenous nucleases and viral vectors. """
linkedin_add=LinkedInResult(company_name,linkedin_url,company_url,overview,specialties)
cystic_fibr_results.append(linkedin_add)

company_name="Eloxx Pharmaceuticals"
linkedin_url="https://www.linkedin.com/company/eloxx-pharmaceuticals/about/"
company_url="http://www.eloxxpharma.com"
specialties="""Biotech, Rare Diseases, Pharmaceuticals, Drug Development, Life Sciences, and Healthcare"""
overview="""Eloxx Pharmaceuticals, Inc. is a clinical-stage biopharmaceutical company developing novel RNA-modulating drug candidates that are designed to treat rare and ultra-rare premature stop codon diseases. Premature stop codons are point mutations that disrupt protein synthesis from messenger RNA. As a consequence, patients with premature stop codon diseases have reduced or eliminated protein production from the mutation bearing allele accounting for some of the most severe phenotypes in these genetic diseases. These premature stop codons have been identified in over 1,800 rare and ultra-rare diseases. Read-through therapeutic development is focused on extending mRNA half-life and increasing protein synthesis by enabling the cytoplasmic ribosome to read through premature stop codons to produce full-length proteins. Eloxx’s lead product candidate, ELX-02, is a small molecule drug candidate designed to restore production of full-length functional proteins. ELX-02 is in the early stages of clinical development focusing on cystic fibrosis and cystinosis. ELX-02 is an investigational drug that has not been approved by any global regulatory body. Eloxx is headquartered in Waltham, MA, with R&D operations in Rehovot, Israel."""
linkedin_add=LinkedInResult(company_name,linkedin_url,company_url,overview,specialties)
cystic_fibr_results.append(linkedin_add)

company_name="Talee Bio"
linkedin_url="https://www.linkedin.com/company/talee-bio/about/"
company_url="http://taleebio.com/"
specialties="""biotechnology, gene therapy, and cystic fibrosis"""
overview="""Our mission at Talee Bio is to change the course of cystic fibrosis and other genetic lung diseases by developing novel genetic treatments.  Our gene therapy technologies are designed to overcome the barriers that have so far prevented effective genetic treatments for cystic fibrosis.

Talee Bio has two gene therapy product candidates to treat cystic fibrosis. The major hurdles of gene therapy for cystic fibrosis are poor efficacy (i.e., transduction efficiency, expression persistence, packaging capacity, avoidance of immunogenicity), low safety and tolerability (including genotoxicity for those vectors that result in genomic integration), and inability to manufacture sufficient vector.  Our proprietary platform technologies and our product candidates are designed to address all of these deficiencies."""
linkedin_add=LinkedInResult(company_name,linkedin_url,company_url,overview,specialties)
cystic_fibr_results.append(linkedin_add)

company_name="Copernicus Therapeutics, Inc."
linkedin_url="https://www.linkedin.com/company/copernicus-therapeutics-inc/about/"
company_url="http://www.cgsys.com"
specialties=""""""
overview="""Copernicus Therapeutics, Inc. (CTI) is a clinical stage biopharmaceutical company and a leader in the emerging field of precision medicine and gene therapy. Through their proprietary, non-viral, nucleic acid nanoparticle platform, they are able to achieve robust gene transfer in several tissues without the immune response and limited treatment window of AAV. Combined with world-class intellectual property in plasmid design for long-term and controlled expression, CTI is poised to become a leader in the 21st century pharmaceutical industry.

Current programs include:

Cystic Fibrosis (Phase I/II Complete)
Eye (Pre-clinical)
Brain (Pre-clinical)

Founded on technologies developed at Case Western Reserve University in Cleveland, Ohio, CTI has a strong connection to the growing biotechnology industry in Northeast Ohio."""
linkedin_add=LinkedInResult(company_name,linkedin_url,company_url,overview,specialties)
cystic_fibr_results.append(linkedin_add)




company_name="Spark Therapeutics, Inc."
linkedin_url="https://www.linkedin.com/company/spark-therapeutics-inc/about/"
company_url="http://www.sparktx.com"
specialties="""Biotechnology and Gene therapy"""
overview="""At Spark Therapeutics, we don’t follow footsteps. We create the path.
 
We were born of innovation, springing from the curiosity, imagination and dedication of remarkable scientists and healthcare visionaries. Our mission is seemingly impossible to others, but not to us: Challenge the inevitability of genetic disease by discovering, developing and delivering treatments in ways unimaginable – until now.
 
Since our founding, we have been committed to bringing a wide range of expertise to build a fully integrated gene therapy company focused on inherited retinal diseases (IRDs), neurodegenerative diseases, as well as diseases that can be addressed by targeting the liver, such as hemophilia. We are seeking talented individuals with diverse experiences, abilities and interests who have the curiosity, courage and drive to reimagine a new health care paradigm.
 
Join us on a journey through uncharted territory – seeking to bring gene therapy for genetic diseases to people worldwide. The resilience of the people we serve is our inspiration to break barriers, as we strive to turn genes into medicine for those with inherited diseases. 
 
Know that working at Spark Therapeutics is not just another job; it is a once-in-a-lifetime opportunity. We embrace the challenges before us and the uncertainty inherent in them. Ultimately, we are working to create a world free of genetic disease. To learn more about Spark and our open positions, visit www.sparktx.com. You can also find us on Twitter at @Spark_tx."""
linkedin_add=LinkedInResult(company_name,linkedin_url,company_url,overview,specialties)
hemophilia_results.append(linkedin_add)



company_name="Dimension Therapeutics"
linkedin_url="https://www.linkedin.com/company/dimension-therapeutics/about/"
company_url="http://www.dimensiontx.com"
specialties=""""""
overview="""Dimension Therapeutics is a gene therapy company focused on developing novel treatments for rare diseases. Our team comprises biotech industry veterans and thought leaders in gene therapy and rare diseases.

The company is focused on advancing its platform of gene therapy programs in rare diseases through clinical development, starting with lead programs in hemophilia, and building out a world-class product engine for adeno-associated virus (AAV) therapeutics.

In June 2014, Dimension announced a collaboration and license agreement with Bayer HealthCare, a worldwide leader in hemophilia, for the development and commercialization of a novel gene therapy for the treatment of hemophilia A. Dimension is responsible for all pre-clinical development activities and the Phase 1/2a clinical trial, with funding from Bayer. Bayer will conduct the confirmatory Phase 3 trial, make all regulatory submissions, and will have worldwide rights to commercialize the potential future product for the treatment of hemophilia A.

Through its license and collaboration with REGENX, Dimension acquired preferred access to NAV vector technology and rights within REGENX product programs in multiple rare disease indications. REGENX holds exclusive rights to a portfolio of over 100 patents and patent applications pertaining to its NAV vector technology and related applications."""
linkedin_add=LinkedInResult(company_name,linkedin_url,company_url,overview,specialties)
hemophilia_results.append(linkedin_add)


company_name="LATINABA"
linkedin_url="https://www.linkedin.com/company/blanchard-y-asociados/about/"
company_url="http://www.blanchardyasociados.com"
specialties="""Clinical Monitoring, Regulatory set up, Managing clinical research projects, GCP Training, GCP audits, CRO, Market Research, Latin America, Feasibility Asessments, Medical Devices, Rare Diseases, Oncology, Infectious Diseases, Argentina, Brazil, and Chile"""
overview="""Our Senior Management Team includes: 
CEO and Clinical Operations Officer.
Chief Scientific Officer
Country Management in all of our countries 
CFO/Finance Manager
Legal Affairs
Regulatory Affairs
Training Management
Quality Assurance

Our experience covers several therapeutic areas and 
- perinatal and pediatric population 
- includes gene therapy clinical studies
- includes medical device studies
- covers indications including orphan drugs and rare diseases.

Anti Infectives
Chagas Disease
Hepatitis C
Hepatitis B
HIV / AIDS
Herpes Simplex
Community Acquired Pneumonia
ADRS
Influenza

Cardiovascular
Abdominal Aorta Aneurism
Atrial Fibrillation
Cardiovascular Risk & Osteoporosis
Cardiovascular Risk & Diabetes
Congestive Heart Failure
Coronary Lesions
Hypertension
Heart Failure

Central Nervous System
Epilepsy
Alzheimer
Depression
Bipolar Disorder
Multiple Sclerosis
Anxiety Disorder
Smoking Cessation
Adrenoleukodystrophy
Spasticity
Dermatology
Acne Vulgaris
Actinic Keratosis
Psoriasis
Cutaneous Leishmaniosis
Melasma
Tinea pedis
Impetigo

Immunology
Rheumatoid Arthritis
Juvenile Rheumatoid Arthritis
Hereditary Angiedema

Oncology
Breast Cancer
Cervix Cancer
Chronic Myeloid Leukemia
Colorectal Cancer
Gist (QOL)
Lung Cancer
Melanoma
Prostate Cancer
Head & Neck Cancer

Ophthalmology
Uveitis
Glaucoma
Keratoconjunctivitis

Vaccines
H1N1 Influenza
Respiratory Syncytial Virus
Hookworm

Endocrino-Metabolics
Osteoporosis
Hipercholesterolaemia
Diabetes M. Type I and II
Early Puberty

Other Indications
Stroke
COPD
Von Willebrand Disease
Renal Impairment
Traumatic Brain Injury
Primary Biliary Cirrhosis
Hemophilia"""
linkedin_add=LinkedInResult(company_name,linkedin_url,company_url,overview,specialties)
hemophilia_results.append(linkedin_add)


company_name="Precision Virologics"
linkedin_url="https://www.linkedin.com/company/precision-virologics/about/"
company_url="https://www.precisionvx.com/"
specialties="""Virology, Gene Therapy, Vaccines, and Adenovirus"""
overview="""Precision’s technology platform provides unique opportunities to accomplish targeted genetic therapies. Our novel targeted genetic knock-in allows long term correction for gene therapy cures. Precision’s technology platform combines effective in vivo gene delivery with CRISPR/Cas9 gene editing allowing adenovirus to achieve long term correction of hemophilia and other inherited genetic disorders. Our novel vector approach allows distinct advantages compared to AAV vectors. We are presently progressing programs for hemophilia and alpha1-antitrypsin deficiency lung disease with National Institute of Health support.

Our platform vaccine approach delivers antigens directly to the key immune activating dendritic cells. This achieved optimized potency based on our unrivaled ability to target the key biologic axis orchestrating effective immunization. Vaccine candidates for Zika and Chikungunya are presently being progressed in our pipeline with National Institute of Health support."""
linkedin_add=LinkedInResult(company_name,linkedin_url,company_url,overview,specialties)
hemophilia_results.append(linkedin_add)


company_name="aaVective, Inc."
linkedin_url="https://www.linkedin.com/company/aavective-inc/about/"
company_url="http://www.aaVective.com"
specialties="""gene therapy, hemophilia, and adeno associated viral vectors"""
overview="""aaVective is a biotechnology company focused on developing a cure for hemophilia A and B, and other liver mediated diseases, through gene therapy utilizing proprietary AAV vectors."""
linkedin_add=LinkedInResult(company_name,linkedin_url,company_url,overview,specialties)
hemophilia_results.append(linkedin_add)


company_name="Voyager Therapeutics, Inc."
linkedin_url="https://www.linkedin.com/company/voyager-therapeutics-inc-/about/"
company_url="http://www.voyagertherapeutics.com"
specialties="""Gene Therapy, biotechnology, adeno associated virus, Research, Parkinson's Disease, clinical operations, Huntington's Disease, vector engineering, SF9, Alzheimer's disease, ALS, Amyotrophic Lateral Sclerosis, VY-SOD101, Friedrich's Ataxia, SOD-1, Tauopathies, and gene therapy"""
overview="""Voyager Therapeutics is developing life-changing gene therapies from discovery, preclinical and clinical development, through to commercialization. We focus on people living with severe neurological diseases that lack safe and effective treatment options, particularly in the areas of Parkinson's disease, monogenic forms of amyotrophic lateral sclerosis (ALS), Friedreich's ataxia, Huntington's disease, Alzheimer's Disease and other tau-related neurodegenerative diseases, and severe, chronic pain.

We are also committed to advancing the field of AAV (adeno-associated virus) gene therapy through innovation and investment in vector engineering and optimization, dosing techniques, as well as process development and production. 

Our management team and founders represent some of the most esteemed scientific and clinical leaders in the fields of AAV gene therapy, expressed RNA interference, neuroscience preclinical and clinical development, and manufacturing. We have broad strategic collaborations with Genzyme, a Sanofi company, AbbVie and the University of Massachusetts Medical School (UMMS). We have also entered into license and other agreements with UMMS, the University of California San Francisco and Stanford University to access relevant technology and data. 

Contact:
Voyager Therapeutics
75 Sidney St.
Cambridge, MA 02139
info@voyagertherapeutics.com
857-259-5340"""
linkedin_add=LinkedInResult(company_name,linkedin_url,company_url,overview,specialties)
parkinsons_results.append(linkedin_add)


company_name="DeBere Capital Partners"
linkedin_url="https://www.linkedin.com/company/debere-capital-partners/about/"
company_url="http://www.deberepartners.com"
specialties="""Private Placement, Corporate Advisory, Fund Marketing, Capital Raising, Investment Banking, Corporate Finance, Venture Capital, Life Science , Biotechnology , M&A, and Beauty and Skincare"""
overview="""DeBere Capital Partners is a hybrid private investment boutique, aligned interest fundraiser and corporate finance firm that invests in and represents a portfolio of innovative growth companies, private equity and infrastructure funds. We take a macro view of the entire ecosystem of investment themes that advance, sustain and contribute to the growth of humanity. As part of our aligned investment strategy, we invest directly in the funds and companies we identify.

DeBere Capital Partners have a specialist interest in Life Science's and will actively invest and organise investment syndicate with pedigree institutional Venture Capitalists and Corporate Partners. We will add strategic value across the lifecycle of the company, facilitating fundraising to exit.

We are interested in the following Life science themes:

Oncology:

- Drug development and therapeutics that are groundbreaking in the treatment and cure of cancer

Degenerative Diseases:

- Treatment and cure of Alzheimer's and Parkinson's disease

Innovative Medical Technology:

-Medical Devices
-Digital Medicine 

Gene Therapy and Regenerative Medicine 

We are interested in the following Wellness themes:

- Organic/ Botanical Skincare and Suncare 
- Anti Ageing Therapeutics """
linkedin_add=LinkedInResult(company_name,linkedin_url,company_url,overview,specialties)
parkinsons_results.append(linkedin_add)


company_name="PharmaCompany, Inc"
linkedin_url="https://www.linkedin.com/company/pharmacompany-inc/about/"
company_url=""
specialties="""Disease and Therapeutic Area Strategy, R&D Planning and Portfolio Valuation, Business Development and Licensing, Epidemiology and Forecasting, Product Life-Cycle Management, New Product Planning, Strategic Market Assessments, and Emerging Markets Advisory Services"""
overview="""PharmaCompany Inc focusses on shaping the future of pharmaceutical business by providing strategic insights and services to its global bio-pharma clients. 

We work with Fortune 500 as well as small to mid-size biopharma clients and enable strategic decision-making along the R&D and marketing continuum.  Our approach relies on a solid understanding of the pharmaceutical market which is rooted in research, clinical, and market perspectives.

Therapeutic Area Expertise: Neuroscience, Neuroinflammatory Disorders, Neurodegenerative Disorders, Neuroprotective Therapy, Oncology, Cardiovascular (Arterial and Venous Occlusive Diseases), Metabolic Diseases, Dermatology, Immunology, Macular Degeneration, Stem Cell Therapy, Gene Therapy, Infectious Diseases (Community and Hospital-Acquired Infections), and Rare/Orphan Diseases.
 
Neuroscience Disease Area Expertise: Epilepsy, Stroke, TBI and Spinal Cord Injury, Multiple Sclerosis and Neuromyelitis Optica, Alzheimer's Disease, Huntigton's Disease, Parkinson's Disease, ALS, Spinal Muscular Atrophy, Myasthenia Gravis, Motor Neuron Disorders, Muscular Dystrophies, Neural Stem Cells, and Neuroregeneration.
 
Cardiovascular Disease Area Expertise: Acute Coronary Syndrome, Arterial Thrombosis and PAOD, Deep Vein Thrombosis, and Surgical Procedures.
 
Oncology Disease Area Expertise: Breast, Colorectal, Lung (NSCLC and SCLC), Prostate, Ovarian, Gastric, Hepatic, Glioblastoma, Leukemias, Lymphomas , Multiple Myeloma, and Cancer Vaccines."""
linkedin_add=LinkedInResult(company_name,linkedin_url,company_url,overview,specialties)
parkinsons_results.append(linkedin_add)


company_name="Novellus, Inc."
linkedin_url="https://www.linkedin.com/company/novellus-inc/about/"
company_url="Websitehttp://novellus-inc.com"
specialties="""gene editing, cell reprogramming, and biological technology"""
overview="""Novellus is an Engineered Cellular Medicine company located in Cambridge, MA. We use our patented, high efficiency platforms of mRNA-based Gene Editing and Cell Reprogramming to develop medicines for patients with devastating diseases such as AAT deficiency, Parkinson's, Crohn's disease, Dystrophic Epidermolysis Bullosa, etc. We engineer precision medicines for patient segments, and select from our technology toolbox for in vivo, ex vivo, allogeneic and autologous delivery. We have robust IP for RNA gene editing and RNA cell reprogramming, including over 30 granted broad patents. """
linkedin_add=LinkedInResult(company_name,linkedin_url,company_url,overview,specialties)
parkinsons_results.append(linkedin_add)


company_name="Canavan Research Foundation"
linkedin_url="https://www.linkedin.com/company/the-canavan-research-foundation/about/"
company_url="http://www.canavan.org"
specialties="""Non-Profit, Stem Cell Research, Medical Research, and Gene Therapy"""
overview="""The Canavan Research Foundation is a groundbreaking organization dedicating to finding cures for genetic brain disease. Founded in 1994, two Canavan children became the recipients of the first gene therapy in the world for brain disease. Seven months later, myelin appeared in their brains. Over successive years two more gene therapy trials and this past month, the results were published in a landmark study- gene therapy had stabilized eighteen children with Canavan disease, saving them from early deaths and changing the face of brain disease everywhere. The next step is stem cell treatments, which have the capability to cure Canavan Disease entirely- and lead to cures for Alzheimer's, Parkinson's, Taysach's, MS, and other degenrative diseases.  To find out more, visit www.canavan.org. Want to get involved? Message Samantha Karlin, n Linkedin."""
linkedin_add=LinkedInResult(company_name,linkedin_url,company_url,overview,specialties)
parkinsons_results.append(linkedin_add)


company_name="Medrego"
linkedin_url="https://www.linkedin.com/company/medrego/"
company_url="http://www.medrego.com"
specialties="""stem cells, biotech, gene therapy, Dog stem cell treatments, Horse stem cell treatments, Camel stem cell treatments, Biotechnology innovations, Allogenic stem cells, Autologous stem cells, Cell laboratory, Biotechnology, Stem Cell treatments, Stem Cell Therapy, CaniCell, and EquiCell"""
overview="""✤ Our innovative biotech company ✤

Medrego is a multi-profile company targeting area of Life Sciences and Biotechnology.

One of our main pillars is an improvement in the condition of animals with regenerative solutions, such as stem cell therapy. Our areas of expertise in this field are recovery after injuries, improvement of performance (energy boost) and productivity increase.

In our laboratory, we develop stem cell treatments, gene therapy and other custom solutions for human’s best friends: Dogs, Horses, Cats and Camels. We can actually treat any animal you care about, also the world’s rarest species like white lion or snow leopard.

✤ Most popular treatments ✤

We have a great experience in the most popular Horse and Dog injury types. Our Medrego EquiCell product works great for tendon and ligament injuries for horses, and our Medrego CaniCell has a high success rate for osteoarthritis, arthritis, and dysplasia injuries for dogs. We are also using stem cells for immunomodulation purposes to improve the weakest part of animal health, as well as successful recovery after surgeries.

We constantly follow the latest medicine trends and cell innovations from the human area and apply them to animals to get the treatment of the future. Research and development is an essential part of our work. We use our patented technology and company know-how to offer more effective treatments.

✤ Our expertise ✤

Medrego team is an expert in allogeneic and autologous cell therapy medicinal product development, full in-vitro testing services and contract manufacturing.

Our team has gained more than 15 years of continues experience in stem cell treatments. Using our knowledge and laboratory equipment we can work privately on developing custom solutions for your needs, to improve your animal performance, boost energy and let them become even better!

We ship our products Worldwide. We are also opened for any kind of collaboration and knowledge sharing.

"""
linkedin_add=LinkedInResult(company_name,linkedin_url,company_url,overview,specialties)
sarcopenia_or_osteoarthritis_results.append(linkedin_add)




metalist.append(beta_thal_sickle_cell_results)
#metalist.append(beta_thal_sickle_cell_results) #intentionally done twice
metalist.append(cystic_fibr_results)
#metalist.append(hemophilia_results)
#metalist.append(parkinsons_results)
#metalist.append(sarcopenia_or_osteoarthritis_results)
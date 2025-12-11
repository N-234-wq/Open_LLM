from pymed import PubMed
import xml.etree.ElementTree as ET
import csv
import re

query = r'("medlinestatus medline"[All Fields] NOT ("indexingmethod curated"[All Fields] OR "indexingmethod automated"[All Fields])) AND ((fha[Filter]) AND (classicalarticle[Filter] OR introductoryjournalarticle[Filter]) AND (english[Filter]) AND (2015:2015[pdat]))'

pubmed = PubMed(tool="HumanIndexingSamples", email="nstrauc3@smail.uni-koeln.de")
results = pubmed.query(query, max_results=500)

# create csv file with data
with open('articles.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        field = ["id", "title", "publication_date", "abstract", "MeSH"]

        writer.writerow(field)

for article in results:

    # Extract information from the article
    article_id = article.pubmed_id
    title = article.title
    publication_date = article.publication_date
    abstract = article.abstract

    path = ".//MeshHeading/DescriptorName"
    xml_element = article.xml
    mesh = []
    
    for item in xml_element.findall(path):
        m = re.search(r"(?<=>).*(?=<)", ET.tostring(item, encoding="unicode"))
        mesh.append(m.group())
   
    with open('articles.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([article_id, title, publication_date, abstract, "|".join(mesh)])
        
 


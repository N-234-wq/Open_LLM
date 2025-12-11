from sentence_transformers import SentenceTransformer
import xml.etree.ElementTree as ET
import pickle

model = SentenceTransformer("lokeshch19/ModernPubMedBERT")

tree = ET.parse(r"desc2022.xml") 

data = {
    "headings": [],
    "embeddings": []
}

path = r".//DescriptorName"
root = tree.getroot()

for elem in root.findall(path):
    heading = elem.find("String").text
    data["headings"].append(heading)
    data["embeddings"].append(model.encode(heading))


           




with open("embeddings.pkl", "wb") as f:
    pickle.dump(data, f)
""""
with open("embeddings.pkl", "rb") as f:
    loaded = pickle.load(f)
"""

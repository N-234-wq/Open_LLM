# LLM-gestützte inhatliche Erschließung medizinischer Fachliteratur 

## Beschreibung
Dieses Projekt untersucht wie geeignet Open Source Large Language Models für die inhaltliche Erschließung medizinischer Fachliteratur. Das Ziel ist es zu analysieren, ob ein Open Source LLM in der Lage ist, frei gewählte Schlagwörter zu generieren, die den Inhalt medizinischer Fachliteratur widerspiegeln. Als Datengrundlage dienen hierbei Abstracts aus PubMed, die über die [PubMed API](https://www.ncbi.nlm.nih.gov/home/develop/api/) zugänglich sind.

## Umsetzung
Zur inhaltlichen Beschreibung von Dokumenten im Bereich der Medizin werden [Medical Subject Headings](https://www.nlm.nih.gov/databases/download/mesh.html) (kurz MeSH) verwendet, das rund 30.000 Deskriptoren umfasst. Aufgrund der Menge der möglichen Begriffe, die für eine Beschreibung der Dokumente herangezogen werden können, können diese nicht direkt in der Prompt bereit gestellt werden. Um dieses Problem zu umgehen wird der folgende Ansatz verfolgt

1. LLM generiert freie Schlagwörter anhand eines Abstracts
2. Mithilfe eines Embedding Modells werden die Schlagwörter in Vektoren umgewandelt
3. Dieser Schritt wird für die MeSH Deskriptoren wiederholt
4. Mithilfe von Nearest-Neighbor-Search wird der ähnlichste MeSH-Term ermittelt
5. Der zugeordnete MeSH-Term wird mit dem tatsächlich vergebenen Term verglichen
6. Evaluierung (Precision/Recall/F1-Score)


## Modelle die in Frage kommen

- teknium/OpenHermes-13B
- teknium/OpenHermes-2.5-Mistral-7B
- meta-llama/Meta-Llama-3-8B-Instruct
- openchat/openchat-3.5-0106

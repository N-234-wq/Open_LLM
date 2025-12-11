import ollama
import csv


titles = []
abstracts = []

with open("keywords.csv", "w", newline="") as f:
    writer = csv.writer(f)
    field = ["keywords"]
    writer.writerow(field)

with open(r"articles.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        title = row["title"]
        abstract = row["abstract"]


        stream = ollama.chat(
            model="HammerAI/openhermes-2.5-mistral",
            stream=True,
            options={
                "temperature": 0.1,
                "seed": 0,
            },
            messages=[
                {
                    "role": "system",
                    "content": f"You are an expert in scientific literature analysis, given the title and abstract of an article, generate a list of keywords that best describe the main topics discussed. The requirements are as followed: generate between 3-6 keywords, prioritize specific terms over generic ones",
                },
                {
                    "role": "user",
                    "content": f"Give me some keywords that best describe the following document with the title: {title} and the abstract: {abstract}",
                },
            ],
        )

        message = ""

        for chunk in stream:
            if hasattr(chunk["message"], "thinking") and chunk["message"].get("thinking"):
                print(chunk["message"]["thinking"], end="", flush=True)
            message += chunk["message"]["content"]
            #print(chunk["message"]["content"], end="", flush=True)

        #print()  # Final newline
        with open("keywords.csv", "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([message])
        

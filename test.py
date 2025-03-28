from transformers import pipeline

classifier = pipeline("text-classification", model="sentiment-analysis-french-folder")
result = classifier("C'est une belle journée.")
print(result)

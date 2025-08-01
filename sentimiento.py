from transformers import pipeline
from deep_translator import GoogleTranslator
#input
texto_or = input (str("Text:\n"))

# Translation
texto = GoogleTranslator(source='auto', target='en').translate(texto_or)

print(f"Original text:\n{texto_or}\nEnglish translation:\n{texto}")

#pipeline analysis
sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
result = sentiment_pipeline(texto)
print(f"es {result} ")


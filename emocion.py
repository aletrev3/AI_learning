from transformers import pipeline
from deep_translator import GoogleTranslator

#input
texto_or = input (str("Text:\n"))

# Translation
texto = GoogleTranslator(source='auto', target='en').translate(texto_or)

print(f"Original text:\n{texto_or}\nEnglish translation:\n{texto}")


#emotional pipeline using top_k=None
emotion_pipeline = pipeline("text-classification",
                            model="j-hartmann/emotion-english-distilroberta-base",
                            top_k=None)


emociones = emotion_pipeline(texto)[0]  # [0] porque devuelve una lista con una entrada

# Results ordered by dominance
print("Emotions:")
for e in sorted(emociones, key=lambda x: x['score'], reverse=True):
    print(f" - {e['label']}: {e['score']*100:.1f}%")

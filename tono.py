from transformers import pipeline
from textblob import TextBlob
from deep_translator import GoogleTranslator





def analizar_tono_porcentual(texto):
    # 2.  multilabel emotion
    emotion_pipeline = pipeline("text-classification",
                                model="j-hartmann/emotion-english-distilroberta-base",
                                top_k=None)
    emociones = emotion_pipeline(texto)[0]
    emociones_ordenadas = sorted(emociones, key=lambda x: x['score'], reverse=True)
    emocion_dominante = emociones_ordenadas[0]

    # Subjectivity level
    subjetividad = TextBlob(texto).sentiment.subjectivity

    # Emotion percenage
    peso_subj = 0.6
    peso_emoc = 0.4
    tono_emocional = (peso_subj * subjetividad + peso_emoc * emocion_dominante['score']) / (peso_subj + peso_emoc)
    tono_emocional_pct = tono_emocional * 100
    tono_analitico_pct = 100 - tono_emocional_pct

    # Results
    print(f" Original text: {texto_or}")
    print(f" English translation: {texto}")
    print(f"\n Dominant emotion: {emocion_dominante['label']} ({emocion_dominante['score']*100:.1f}%)")
    print(f" Subjectivity level: {subjetividad:.2f}")
    print(f"\n Tone: {tono_analitico_pct:.1f}%")
    print(f" Emotional tone: {tono_emocional_pct:.1f}%")

# EJEMPLO
#input
texto_or = input (str("Text:\n"))

# Translation
texto = GoogleTranslator(source='auto', target='en').translate(texto_or)
analizar_tono_porcentual(texto)

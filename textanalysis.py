import spacy
from collections import Counter
import pandas as pd
import numpy as np

# Chose language
idioma = input (str("To analise a text in English, press 'E'\nTo analise a text in Spanish press 'S'\nTo analise a text in German pres 'G'\n"))
if idioma == 'E':
    nlp = spacy.load("en_core_web_lg")
if idioma == 'S':
    nlp = spacy.load("es_core_news_lg")
if idioma == 'G':
    nlp = spacy.load("de_core_news_lg")

text = input (str("Texto:\n"))
# Process text
doc = nlp(text)

# 1. Sentence Boundary Detection (SBD)
print("\n=== Sentences ===")
for sent in doc.sents:
    print(sent.text)

# 2.  Lemmatization + Dependency Parsing
print("\n=== Tokens, Lemmas, POS & Dependencies ===")
for token in doc:
    print(f"{token.text:15} | Lemma: {token.lemma_:10} | POS: {token.pos_:8} | Dep: {token.dep_:10} | Head: {token.head.text}")

# 3.  Named Entity Recognition (NER)
print("\n=== Named Entities ===")
for ent in doc.ents:
    print(f"{ent.text:20} | Label: {ent.label_} | Explanation: {spacy.explain(ent.label_)}")

# Counters
pos_counts = Counter()
dep_counts = Counter()
head_counts = Counter()

for token in doc:
    pos_counts[token.pos_] += 1
    dep_counts[token.dep_] += 1
    head_counts[token.head.text] += 1

# Mostrar en forma de tabla
df_pos = pd.DataFrame(pos_counts.items(), columns=["POS", "Count"]).sort_values(by="Count", ascending=False)
df_dep = pd.DataFrame(dep_counts.items(), columns=["Dependency", "Count"]).sort_values(by="Count", ascending=False)
df_head = pd.DataFrame(head_counts.items(), columns=["Head Token", "Count"]).sort_values(by="Count", ascending=False)

print("\n=== POS ===")
print(df_pos)

print("\n=== Dependency Labels ===")
print(df_dep)

print("\n=== Head Tokens ===")
print(df_head)

sent_lengths = [len(sent) for sent in doc.sents]
avg_sent_length = np.mean(sent_lengths)

# Word lenght
token_lengths = [len(token.text) for token in doc if not token.is_punct and not token.is_space]
avg_word_length = np.mean(token_lengths)

# POS variety
pos_variety = len(pos_counts)

# Dependency variety
dep_variety = len(dep_counts)

# Named entities
num_entities = len(doc.ents)

# === Complexity score ===
# Each has a value from 0 to 1
score = (
    (avg_sent_length / 20) * 0.25 +      # long sentences: 25%
    (avg_word_length / 8) * 0.2 +        # long words: 20%
    (pos_variety / 15) * 0.2 +           # grammar complexity: 20%
    (dep_variety / 20) * 0.2 +           # sintantic complexity: 20%
    (num_entities / 5) * 0.15            # information: 15%
)

#  0–1
score = min(score, 1.0)
nivel = "HIGH" if score > 0.7 else "MEDIUM" if score > 0.4 else "LOW"

# Results
print("\n=== TEXTUAL COMPLEXITY ===")
print(f"- Average sentence lenght: {avg_sent_length:.2f}")
print(f"- Average word lenght: {avg_word_length:.2f}")
print(f"- POS variety: {pos_variety}")
print(f"- Dependency variety: {dep_variety}")
print(f"- Number of named entities: {num_entities}")
print(f"\n Complexity score: {score*100:.1f}% →  {nivel}")


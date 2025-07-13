import spacy
from collections import Counter
import pandas as pd

# Carga el modelo en inglés
nlp = spacy.load("de_core_news_lg")

# Texto de ejemplo
text = "Unsicherheit ist wie das Stehen auf dünnem Eis bei Nebel – jeder Schritt könnte der falsche sein, und obwohl vielleicht nichts unter dir bricht, hält dich die Angst fest, als wäre jeder Moment dein letzter Halt."
# Procesa el texto
doc = nlp(text)

# 1. 🔹 Sentence Boundary Detection (SBD)
print("\n=== Sentences ===")
for sent in doc.sents:
    print(sent.text)

# 2. 🔹 Lemmatization + Dependency Parsing
print("\n=== Tokens, Lemmas, POS & Dependencies ===")
for token in doc:
    print(f"{token.text:15} | Lemma: {token.lemma_:10} | POS: {token.pos_:8} | Dep: {token.dep_:10} | Head: {token.head.text}")

# 3. 🔹 Named Entity Recognition (NER)
print("\n=== Named Entities ===")
for ent in doc.ents:
    print(f"{ent.text:20} | Label: {ent.label_} | Explanation: {spacy.explain(ent.label_)}")

# Contadores
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


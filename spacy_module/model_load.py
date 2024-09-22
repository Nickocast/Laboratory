import spacy

# Se carga el modelo en español
nlp = spacy.load("es_core_news_md")

# Text de ejemplo para probar el análisis
doc = nlp("¿Cómo está el clima en Argentina?")

# Imprime tokends procesados
for token in doc:
    print(token.text, token.pos, token.dep_)
import spacy
from spacy.matcher import Matcher

# LEVEL INTERMEDIO

# Carga el modelo en español
nlp = spacy.load("es_core_news_md")

# Crear el matcher con el vocabulario del modelo
matcher = Matcher(nlp.vocab)

# Patrón para detectar preguntas sobre el clima
pattern_clima = [{"LOWER": "clima"}]

# Patrón para detectar preguntas sobre la hora
pattern_hora = [{"LOWER": "hora"}]

# Añadir los patrones al matcher
matcher.add("PREGUNTA_CLIMA", [pattern_clima])
matcher.add("PREGUNTA_HORA", [pattern_hora])

# Procesar una frase y usar el matcher
doc = nlp("¿Cómo está el clima mañana en Madrid?")
matches = matcher(doc)

intents = {
    "PREGUNTA_CLIMA": "pregunta_clima",
    "PREGUNTA_HORA": "pregunta_hora"
}

for match_id, start, end in matches:
    span = doc[start:end]
    intent = intents.get(nlp.vocab.strings[match_id], "unknown")
    print(f"intento: {intent}, Texto: {span.text}")
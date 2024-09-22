import spacy
from spacy.matcher import Matcher

# Se carga el modelo en español
nlp = spacy.load("es_core_news_md")

# Crear el matcher con el vocabulario del modelo
matcher = Matcher(nlp.vocab)

# Patrón para detectar preguntas sobre el clima
pattern_clima = [{"LOWER": "clima"}]

# Patrón para detectar preguntas de hora
pattern_hora = [{"LOWER": "hora"}]

# Se añade los patrones al matcher
matcher.add("PREGUNTA_CLIMA", [pattern_clima])
matcher.add("PREGUNTA_HORA", [pattern_hora])

# Procesar una frase y usar el matcher

doc = nlp("¿que hora es ahora?")
matches = matcher(doc)

# Mostrar coincidencias
for match_id, start, end in matches:
    span = doc[start:end]
    print("intento detectado: ", span.text)


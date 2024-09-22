import spacy
from spacy.matcher import Matcher

# Cargar el modelo de spaCy
nlp = spacy.load("es_core_news_md")  # Modelo en español
matcher = Matcher(nlp.vocab)  # Inicializar matcher

pattern_clima_actual = [
    {"LOWER": {"IN": ["clima", "tiempo", "frío", "calor", "abrigo"]}},
    {"LOWER": {"IN": ["hoy", "ahora", "actual", "momento", "en este momento"]}, "OP": "?"},  # Contexto de tiempo actual
    {"LOWER": {"IN": ["está", "haciendo", "cómo", "es", "hay"]}, "OP": "?"},  # Verbos de tiempo presente
    {"LOWER": {"NOT_IN": ["mañana", "próxima", "noche", "tarde", "fin de semana"]}}  # Evitar palabras clave de futuro
]


pattern_clima_futuro = [
    {"LOWER": {"IN": ["clima", "tiempo", "frío", "calor", "grados", "pronóstico"]}},
    {"LOWER": {"IN": ["mañana", "noche", "tarde", "próxima", "futuro", "fin de semana"]}},  # Contexto de tiempo futuro
    {"LOWER": {"IN": ["estará", "hará", "habrá", "pronostican", "esperan"]}, "OP": "?"}  # Verbos en futuro
]


# Agregar los patrones al matcher
matcher.add("PREGUNTA_CLIMA_ACTUAL", [pattern_clima_actual])
matcher.add("PREGUNTA_CLIMA_FUTURO", [pattern_clima_futuro])


# Función para detectar intenciones
def detectar_intencion(texto):
    doc = nlp(texto)  # Procesar el texto con spaCy
    matches = matcher(doc)

    if matches:
        for match_id, start, end in matches:
            span = doc[start:end]  # Obtener coincidencia
            intencion = nlp.vocab.strings[match_id]  # Obtener nombre de la intención
            print(f"Intención detectada: {intencion}, Texto: {span.text}")
    else:
        print("No se detectaron intenciones.")

    # Mostrar las entidades reconocidas por el modelo
    print("Entidades reconocidas:", [(ent.text, ent.label_) for ent in doc.ents])


# Ejemplo de prueba
textos = [
    "¿Cómo está el clima?",
    "Hace frío?",
    "¿Debo ponerme abrigo?",
    "¿Cómo estará el tiempo hoy?"
]

for texto in textos:
    print(f"\nTexto: {texto}")
    detectar_intencion(texto)

import spacy
from spacy.training import Example

# DATOS DE ENTRENAMIENTO:
TRAIN_DATA = [
    ("¿Qué tiempo hace en Madrid hoy?", {"entities": [(21, 27, "LOC")]}),
    ("¿Cuál es el clima en Nueva York?", {"entities": [(22, 32, "LOC")]}),
    ("El clima en Barcelona es cálido.", {"entities": [(11, 20, "LOC")]}),
    ("¿Cómo está el clima en Buenos Aires?", {"entities": [(22, 34, "LOC")]}),
    ("El tiempo en Tokio es lluvioso.", {"entities": [(11, 16, "LOC")]}),
    ("¿Cuál es el pronóstico del clima en Berlín?", {"entities": [(35, 41, "LOC")]}),
    ("¿Habrá sol en París mañana?", {"entities": [(13, 18, "LOC")]}),
    ("¿Qué temperatura habrá en Ciudad de México?", {"entities": [(25, 40, "LOC")]}),
    ("El clima en Londres es frío.", {"entities": [(11, 17, "LOC")]}),
    ("¿Cómo está el clima en Roma?", {"entities": [(22, 26, "LOC")]}),
    ("La temperatura en Buenos Aires está subiendo.", {"entities": [(18, 30, "LOC")]}),
    ("En São Paulo el clima está nublado.", {"entities": [(3, 12, "LOC")]}),
    ("¿Qué temperatura hace en Moscú?", {"entities": [(23, 28, "LOC")]}),
    ("En Bogotá llueve durante todo el día.", {"entities": [(3, 9, "LOC")]}),
    ("¿Qué tiempo hará en Tokio la semana que viene?", {"entities": [(18, 23, "LOC")]}),
    ("¿Qué tal el clima en Río de Janeiro?", {"entities": [(18, 32, "LOC")]}),
    ("El clima en Montevideo es cálido en esta época.", {"entities": [(11, 21, "LOC")]}),
    ("El tiempo en Santiago de Chile es seco.", {"entities": [(11, 28, "LOC")]}),
    ("¿Cómo estará el clima en Dublín mañana?", {"entities": [(24, 30, "LOC")]}),
    ("¿Cuál es el pronóstico del clima en Toronto?", {"entities": [(35, 42, "LOC")]}),
    ("El clima en San Francisco es soleado.", {"entities": [(11, 24, "LOC")]}),
    ("¿Qué tiempo hace en El Cairo hoy?", {"entities": [(21, 29, "LOC")]}),
    ("El tiempo en Washington DC es variable.", {"entities": [(11, 25, "LOC")]}),
    ("¿Habrá lluvias en Ciudad del Cabo mañana?", {"entities": [(17, 31, "LOC")]}),
    ("¿Cómo estará el clima en Miami esta tarde?", {"entities": [(24, 29, "LOC")]}),
    ("El clima en Chicago es impredecible.", {"entities": [(11, 18, "LOC")]}),
    ("¿Qué tiempo hace en Los Ángeles ahora?", {"entities": [(21, 31, "LOC")]}),
    ("¿Cuál es el pronóstico en México?", {"entities": [(28, 34, "LOC")]}),
    ("El clima en Quito es frío.", {"entities": [(11, 16, "LOC")]}),
    ("¿Qué tiempo hará en Seúl mañana?", {"entities": [(18, 22, "LOC")]}),
    ("En Pekín el clima es seco durante el invierno.", {"entities": [(3, 8, "LOC")]}),
    ("¿Qué temperatura hace en Estocolmo?", {"entities": [(23, 32, "LOC")]}),
    ("El clima en Buenos Aires hoy es soleado.", {"entities": [(11, 23, "LOC")]}),
    ("En Johannesburgo el clima es cálido y húmedo.", {"entities": [(3, 17, "LOC")]}),
    ("¿Qué tal el clima en Singapur esta semana?", {"entities": [(18, 26, "LOC")]}),
    ("¿Cómo estará el clima en Atenas mañana?", {"entities": [(24, 30, "LOC")]}),
    ("El clima en Caracas es muy tropical.", {"entities": [(11, 18, "LOC")]}),
    ("¿Qué tiempo hará en Ciudad de Guatemala?", {"entities": [(18, 37, "LOC")]}),
    ("En Nueva Delhi el clima es húmedo.", {"entities": [(3, 14, "LOC")]}),
    ("¿Qué tal el clima en Ciudad de Panamá?", {"entities": [(18, 33, "LOC")]}),
    ("¿Cómo está el clima en La Habana ahora?", {"entities": [(22, 30, "LOC")]}),
    ("¿Habrá lluvias en Ciudad de Guatemala?", {"entities": [(17, 36, "LOC")]}),
    ("El tiempo en Casablanca es soleado.", {"entities": [(11, 20, "LOC")]}),
    ("¿Cuál es el pronóstico del tiempo en Bangkok?", {"entities": [(36, 43, "LOC")]}),
    ("¿Qué tal el clima en Ciudad de México?", {"entities": [(18, 33, "LOC")]}),
    ("¿Cómo estará el clima en Oslo esta tarde?", {"entities": [(24, 28, "LOC")]}),
    ("¿Qué tiempo hace en Ámsterdam hoy?", {"entities": [(21, 30, "LOC")]}),
    ("En Marrakech hace calor hoy.", {"entities": [(3, 12, "LOC")]}),
    ("¿Qué tiempo hará en Dubái la próxima semana?", {"entities": [(18, 23, "LOC")]}),
    ("El clima en Estambul es lluvioso en otoño.", {"entities": [(11, 19, "LOC")]}),
    ("¿Cómo estará el clima en Ciudad del Cabo este viernes?", {"entities": [(24, 38, "LOC")]}),
    ("¿Qué tal el clima en Johannesburgo?", {"entities": [(18, 32, "LOC")]}),
    ("El tiempo en Sydney es templado en primavera.", {"entities": [(11, 17, "LOC")]}),
    ("¿Cuál es el pronóstico del clima en Kuala Lumpur?", {"entities": [(35, 48, "LOC")]}),
    ("En Hong Kong el tiempo es impredecible.", {"entities": [(3, 12, "LOC")]}),
    ("¿Cómo estará el clima en La Paz mañana?", {"entities": [(24, 30, "LOC")]}),
    ("El tiempo en Milán es agradable.", {"entities": [(11, 16, "LOC")]}),
    ("¿Habrá lluvias en Montreal mañana?", {"entities": [(17, 25, "LOC")]}),
    ("¿Cuál es el clima en Sao Paulo ahora mismo?", {"entities": [(20, 29, "LOC")]}),
    ("En Nueva Zelanda hace frío en invierno.", {"entities": [(3, 15, "LOC")]}),
    ("¿Qué temperatura habrá en Buenos Aires el sábado?", {"entities": [(25, 37, "LOC")]}),
    ("El clima en Ginebra es seco en otoño.", {"entities": [(11, 18, "LOC")]}),
    ("¿Cómo estará el clima en Venecia mañana?", {"entities": [(24, 31, "LOC")]}),
    ("¿Qué tiempo hace en Moscú ahora mismo?", {"entities": [(21, 26, "LOC")]}),
    ("El tiempo en Manila es soleado.", {"entities": [(11, 17, "LOC")]}),
    ("¿Habrá tormentas en Buenos Aires esta semana?", {"entities": [(18, 30, "LOC")]}),
]


# Se carga un modelo existente para entrenar
nlp = spacy.load("es_core_news_md")
ner = nlp.get_pipe("ner")

# Se añade la etiqueta de localización si no existe
ner.add_label("LOC")

# Deshabilitar otros componentes del pipeline para no alterar el entrenamiento
pipe_exceptions = [pipe for pipe in nlp.pipe_names if pipe != "ner"]
with nlp.disable_pipes(*pipe_exceptions):
    # Entrenamiento
    for epoch in range(10): # Número de écpocas
        for text,  annotations in TRAIN_DATA:
            doc = nlp.make_doc(text)
            example = Example(doc, annotations)
            nlp.update([example])

nlp.to_disk("es_core_md_aurora")

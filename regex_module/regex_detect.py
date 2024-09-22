import re


def detectar_intencion(texto):
    texto = texto.lower()

    # 1. Detectar si el usuario está hablando del clima o condiciones relacionadas (como si llevar abrigo)
    palabras_clave_clima = ["clima", "tiempo", "temperatura", "llover", "sol", "frío", "calor", "abrigo", "paraguas",
                            "tormenta"]

    # Si no se menciona nada sobre el clima, asumir que no es una pregunta sobre el clima
    if not any(palabra in texto for palabra in palabras_clave_clima):
        return "No se detectó intención relacionada al clima."

    # 2. Definir patrones para diferentes tiempos (solo se activan si hay palabras clave relacionadas al clima)
    patron_clima_actual = r"(hoy|ahora|actual|afuera|día de hoy|llevo|debo|cómo está|cómo está el)"
    patron_clima_futuro_horas = r"(más tarde|en unas horas|esta tarde|esta noche|en la tarde|en la noche)"
    patron_clima_futuro = r"(mañana|próximo día|el día de mañana)"
    patron_clima_semana = r"(semana|próximos días|esta semana|los próximos días|semana que viene)"
    patron_alertas_clima = r"(alertas|evento climático|tormenta|huracán|advertencias)"

    # 3. Detectar las diferentes intenciones basadas en el tiempo

    # Clima actual (hoy)
    if re.search(patron_clima_actual, texto):
        return "Intención detectada: clima actual (hoy)"

    # Clima en unas horas (futuro cercano)
    elif re.search(patron_clima_futuro_horas, texto):
        return "Intención detectada: clima en unas horas (futuro cercano)"

    # Clima de mañana
    elif re.search(patron_clima_futuro, texto):
        return "Intención detectada: clima de mañana"

    # Clima durante la semana
    elif re.search(patron_clima_semana, texto):
        return "Intención detectada: clima durante la semana"

    # Alertas o eventos climáticos
    elif re.search(patron_alertas_clima, texto):
        return "Intención detectada: alertas o eventos climáticos"

    # Si no se encuentra un tiempo específico, asumir clima actual
    else:
        return "Intención detectada: clima actual (hoy, por defecto)"


# Ejemplos de uso
texto1 = "¿Debo llevar un abrigo esta noche?"  # Clima en unas horas
texto2 = "¿Cómo está el clima ahora?"  # Clima actual
texto3 = "¿Qué clima hará mañana?"  # Clima de mañana
texto4 = "¿Habrá tormenta esta semana?"  # Clima durante la semana
texto5 = "Agenda una reunión para la próxima semana"  # NO es clima
texto6 = "¿Cómo estará el tiempo esta semana?"  # Clima durante la semana

print("1 ", detectar_intencion(texto1))  # Debería detectar clima en unas horas
print("2 ", detectar_intencion(texto2))  # Debería detectar clima actual
print("3 ", detectar_intencion(texto3))  # Debería detectar clima de mañana
print("4 ", detectar_intencion(texto4))  # Debería detectar clima durante la semana
print("5 ", detectar_intencion(texto5))  # Debería NO detectar clima
print("6 ", detectar_intencion(texto6))  # Debería detectar clima durante la semana

nombre_archivo = "/Users/odavid/Downloads/train-balanced-sarcasm.csv"  # Actualización con la ruta correcta del archivo

# Diccionario de palabras positivas y negativas
diccionario_sentimientos = {
    "positivas": ["happy", "glad", "positive", "honest"],
    "negativas": ["bad", "negative", "sad","angry","upset"]
}

# Inicializar contadores
contador_positivas = 0
contador_negativas = 0

# Paso 2: Abrir y leer el archivo
with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
    lineas = archivo.readlines()

# Paso 3: Comparar y clasificar cada frase
for linea in lineas:
    palabras = linea.split()
    sentimiento_frase = None  # Inicializar el sentimiento de la frase como desconocido
    for palabra in palabras:
        if palabra.lower() in diccionario_sentimientos["positivas"]:
            sentimiento_frase = "positiva"
            break  # Romper el bucle si se encuentra una palabra positiva
        elif palabra.lower() in diccionario_sentimientos["negativas"]:
            sentimiento_frase = "negativa"
            break  # Romper el bucle si se encuentra una palabra negativa

    print(f"Frase: {linea.strip()}")
    if sentimiento_frase:
        print(f"Sentimiento: {sentimiento_frase}\n")
    else:
        print("Sentimiento: Desconocido\n")

    if sentimiento_frase == "positiva":
        contador_positivas += 1
    elif sentimiento_frase == "negativa":
        contador_negativas += 1

# Paso 4: Mostrar el resultado
print("Total de frases positivas:", contador_positivas)
print("Total de frases negativas:", contador_negativas)

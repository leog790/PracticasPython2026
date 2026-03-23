import random
import string
"""words = [
    "python",
    "programa",
    "variable",
    "funcion",
    "bucle",
    "cadena",
    "entero",
    "lista",
    ]"""  
categorias = { "programacion": ["python","variable", "funcion", "bucle"],
               "general": ["programa"],
               "estructuras": ["listas", "cadena", "entero"]
               }

letras = string.ascii_letters
guessed = []
attempts = 6
puntos = 0 #Inicio del puntaje
print("¡Bienvenido al Ahorcado!")
print()
#Mostrar categorias
print("Categorias disponibles:")
for i in categorias:
    print("-", i)
eleccion = input("Elegir categoria: ").lower()
words = categorias.get(eleccion)
#Verificar si la categoria existe
if not words:
    print("Categoria invalida. Se usara una por defecto.")
    words=categorias["general"]
#Eleccion al azar de la lista    
word = random.choice(words)
while attempts > 0:
    # Mostrar progreso: letras adivinadas y guiones para las que faltan
    progress = ""
    for letter in word:
        if letter in guessed:
            progress += letter + " "
        else:
            progress += "_ "
    print(progress)
    # Verificar si el jugador ya adivinó la palabra completa
    if "_" not in progress:
        print("¡Ganaste!")
        puntos += 6 #Suma 6 puntos si gano
        break
    print(f"Intentos restantes: {attempts}")
    print(f"Letras usadas: {', '.join(guessed)}")
    letter = input("Ingresá una letra: ")
    #Validar letra
    if len(letter)!=1 or letter not in letras:
        print("Entrada no valida")
        continue
    if letter in guessed:
        print("Ya usaste esa letra.")
    elif letter in word:
        guessed.append(letter)
        print("¡Bien! Esa letra está en la palabra.")
    else:
        guessed.append(letter)
        attempts -= 1
        puntos -= 1 #Resta un punto si falla en una letra
        print("Esa letra no está en la palabra.")
    print()
else:
    print(f"¡Perdiste! La palabra era: {word}")
    puntos = 0 #Perder deja el puntaje en 0
print (f"Tu puntaje final es: {puntos}") #Muestra el puntaje final del jugador    
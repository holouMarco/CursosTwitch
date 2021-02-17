  
# random es una de las multiples librerías que nos puede proporcionar python.
# choice es una funcionalidad de esta librería que escoge un elemento aleatorio
# Por lo tanto, importamos choice y obtendrá un elemento aleatorio de opciones(Eso será nuestro oponente)

from random import choice

opciones = ['piedra', 'papel', 'tijera']

# Creamos una variable que valdrá una elección aleatoria de opciones
eleccionOrdenador = choice(opciones)

# Dado ya nuestro oponente. Crea el juego ----piedra, papel, tijera----
# Se deben utilizar condicionales y operadores lógicos.
# En cada condición cumplida hay que printear el mensaje de empate, victoria o derrota

eleccionJugador = 'piedra'



if eleccionJugador == eleccionOrdenador:
    print('Habeis empatado')

elif eleccionJugador == 'piedra' and eleccionOrdenador == 'tijera':
    print('Hemos ganado')

elif eleccionJugador == 'papel' and eleccionOrdenador == 'piedra':
    print('Hemos ganado')

elif eleccionJugador == 'tijera' and eleccionOrdenador == 'papel':
    print('Hemos ganado')

else:
    print('Hemos perdido')
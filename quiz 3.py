#importamos la biblioteca random como r 

import random as r
#escribimos nuestros nombres pa que se vean bien divinos ^_^
print("------------------------------------------------------------------------------------------------")
print("Los creadores de este codigo fueron: Samuel Redondo, Juan Jose Jaramillo y, Luis Miguel Brito.")
print("------------------------------------------------------------------------------------------------")

#definimos las opciones que tanto el usuario como la maquina pueden escoger
opciones = ["piedra", "papel", "tijera"]


#creamos y definimos la clase "juego", declarando los valores vacios para asignarles valores mas adelante
class Juego():
    def __init__(self):
        self.eleccion_usuario = None
        self.eleccion_computadora = None
    
    
    #creamos el metodo para que el usuario escoga que opcion usara, y se almacena el dato en "eleccion"
    def obtener_eleccion_usuario(self):
        while True:
            eleccion = input("Ingrese su elección (piedra, papel o tijera): ").lower()
            if eleccion in opciones:
                self.eleccion_usuario = eleccion
                break
            else:
                print("Por favor, ingrese una opción válida (piedra, papel o tijera).")
    
    #se genera la eleccion de la computadora usando la biblioteca importada random e imprimos ese resultado
    def generar_eleccion_computadora(self):
        self.eleccion_computadora = r.choice(opciones)
        print("La computadora escoge:" , self.eleccion_computadora)


#creamos el metodo para definir el ganador dependiendo de las elecciones del usuario y de la computadora
    def determinar_ganador(self):
        if self.eleccion_usuario == self.eleccion_computadora:
            return "¡Empate!"
        elif(self.eleccion_usuario == "piedra" and self.eleccion_computadora == "tijera") or \
            (self.eleccion_usuario == "papel" and self.eleccion_computadora == "papel") or \
            (self.eleccion_usuario == "tijera" and self.eleccion_computadora == "papel"):
            return "¡Has ganado!"
        else:
            return "¡La computadora gana!"
        


#se crea el metodo para inicializar el juego y se crea la opcion de volver a jugar
    def jugar(self):
        print("Bienvenido al juego de Piedra, papel o tijera, ¿listo para jugar?")
        while True:
            self.obtener_eleccion_usuario()
            self.generar_eleccion_computadora()
            resultado = self.determinar_ganador()
            print(resultado)
            jugar_nuevamente = input("¿Desea jugar de nuevo? (si/no): ").lower()
            if jugar_nuevamente != "si":
                print("-------------------------------------------------------------------")
                print("Gracias por jugar, espero que lo intentes de nuevo en otra ocasión.")
                print("-------------------------------------------------------------------")
                break

#finalmente se define el main que incializa y comienza
game = Juego()
game.jugar()

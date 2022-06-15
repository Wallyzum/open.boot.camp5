class Vehiculo:
    color = ""
    ruedas = 4
    puertas = 0  
    
class Coche(Vehiculo):
    cilindradas = 0
    velocidad = 0
    def __init__(self,cilindradas,puertas,color):
        self.cilindradas = cilindradas
        self.velocidad = cilindradas/50+120
        self.puertas = puertas
        self.color = color
    def showCar(self):
        print("Color:",self.color, "-Puertas:",self.puertas,"-Velocidad Maxima:",self.velocidad)

car = Coche(3000,4,"Rojo")
car.showCar()






class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 50
        print(f"{self.marca} {self.modelo} acelerando. Velocidade atual: {self.velocidade} km/h")

    def frear(self):
        self.velocidade -= 10
        print(f"{self.marca} {self.modelo} freando. velocidade atual: {self.velocidade} km/h")

class Carro (Veiculo):
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidade = 0

class Bicicleta (Veiculo):
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidade = 0

#meu_carro = Carro("Renault","Sandero")
#meu_carro.acelerar()
#meu_carro.frear()

minha_bicicleta = Bicicleta("Scott", "Aro 29")
minha_bicicleta.acelerar()
minha_bicicleta.frear()




        
    


class Veiculo:
    def __init__(self, modelo, cor):
        self.modelo = modelo
        self.cor = cor
        pass

class Carro(Veiculo):
    def __init__(self, modelo, cor):
        return
    
class Bicicleta(Veiculo):
    def __init__(self, modelo, cor):
        return
    
carro = Carro("Renault", "Branco")
bicicleta = Bicicleta("Aro 29", "Preto")

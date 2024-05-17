import math
class Forma:
    def calc_perimetro(self):
        pass

    def calc_area(self):
        pass



class Circulo(Forma):
    def __init__(self, raio:float):
        self.raio=raio

    def calc_area(self):
        area = math.pi * self.raio**2
        return f"{area:.2f}"
    
    def calc_perimetro(self):
        peri = 2*math.pi*self.raio
        return f"{peri:.2f}"

class Retangulo(Forma):
    def __init__(self,base:float,altura:float):
        self.base =base
        self.altura = altura
        

    def calc_area(self):
        area = self.base*self.altura
        return f"{area}"

    def calc_perimetro(self):
        peri = (self.altura + self.base)*2
        return f"{peri}"

class Triangulo(Forma):
    def __init__(self,base:float, altura:float,tipo:str):
        self.base=base
        self.altura=altura
        self.tipo = tipo

    def calc_perimetro(self):

        if self.tipo ==  "iso":
            soma = (self.altura**2/2)
            lado = math.sqrt(soma)
            peri = self.base + lado*2 
        elif self.tipo == "equi":
            peri = self.base*3
        
        return f"{peri:.2f}"

    def calc_area(self):
        if self.tipo == "iso":
            area = (self.altura * self.base)/2
        elif self.tipo == "equi":
            area = (self.base**2 * math.sqrt(3))/4
        return  f"{area:.2f}"


# circulo = Circulo(10)
# print(circulo.calc_area())
# print(circulo.calc_perimetro())
# retan = Retangulo(base=10,altura=20)
# print(retan.calc_area())
# print(retan.calc_perimetro())

trianguloIso = Triangulo(base=4,altura=6,tipo="iso")
print(trianguloIso.calc_perimetro())
print(trianguloIso.calc_area())

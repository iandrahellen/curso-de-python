
class Calculadora:
    def soma(self, x, y):
        return x + y

    
calc = Calculadora()

resultado_int = calc.soma(10, 3)
print("Soma de numeros inteiros:", resultado_int) 

resultado_str = calc.soma("Oi", " mundo!")
print("Soma de strings:", resultado_str) 


print("PESQUISA ")

nome = input("Nome completo: ")
idade = int(input("Idade: "))
fone = int(input("Telefone: "))
email = input("Email: ")
altura = float(input("Altura: "))
genero = input("Gênero: ")
filho = input("Você tem filhos (Sim/Não) ? ")
if filho.lower() == 'sim':
    filho = True
elif filho.lower() == "não" or filho.lower() == "nao":
    filho = False
else:
    print("Resposta inválida. Por favor responda 'Sim' ou 'Não'.")
    
  
print(f"Olá seja bem vindo (a), {nome}!!!") 
print(f"Você mede {altura} de altura, e tem {idade} anos, se identifica com gênero: {genero}, possui filhos: {filho} seu telefone para contato é o {fone} e endereço de email {email}") 
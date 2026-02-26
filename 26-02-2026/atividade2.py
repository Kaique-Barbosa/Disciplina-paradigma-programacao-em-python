valor_inicial = int(input("Digite um valor inteiro inicial: \n"))

valor_final= int(input("Digite um valor inteiro final: \n"))

multiplicador = int(input("Digite o multiplicador: \n"))

for m in range (valor_inicial,  valor_final+1):
    print(f"{m} x {multiplicador} = {m * multiplicador}")
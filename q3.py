while True:
    try:
        numero = int(input("Digite o número: "))
        
        for i in range(1, 11):
            resultado = numero * i
            print(f"{numero} x {i} = {resultado}")
            
        break
    except ValueError:
        print("Dado inválido, digite apenas números.")
while True:
    try:
        primeiro_numero = int(input("Primeiro numero: "))
        segundo_numero = int(input("Segundo numero: "))
        
        soma = primeiro_numero + segundo_numero
        print(f"a soma é igual a: {soma}")
        break
    except:
        print("Dado invalido, digite só numeros")
idade = int(input("Digite a sua idade: "))

while True:
    try:
        if(idade >=18):
            print("Voce é maior de idade")
            break
        else:
            print("voce é menor de idade")
            break
    except:
            print("dado invalido")
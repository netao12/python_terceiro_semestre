while True:
    try:
        nota1 = float(input("Digite a primeira nota: "))
        nota2 = float(input("Digite a segunda nota: "))
        nota3 = float(input("Digite a terceira nota: "))
        
        media = (nota1 + nota2 + nota3) / 3
        
        print(f"\nMédia: {media:.1f}")
        
        if media >= 7.0:
            print("Situação: Aprovado")
        elif media >= 5.0:
            print("Situação: Recuperação")
        else:
            print("Situação: Reprovado")
            
        break
        
    except ValueError:
        print("\nErro: digite apenas números!\n")
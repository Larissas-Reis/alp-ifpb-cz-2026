estojo = []
print ("Olá usuário, aqui temos um estojo vazio, digite abaixo se deseja colocar algum item(Um item por vez): ")
res = ""
it = ""
while res != 0 :
    res = int(input("Deseja colocar algum item(1 para sim e 0 para não): "))
    if res == 1:
        item = input("Digite qual item você quer adicionar: " )
        estojo.append(item)
        for item in estojo:
            print(item)
    else:
        print ("Tudo bem, aqui abaixo está o seu estojo")
        for item in estojo:
            print(item)
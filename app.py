
def Rotas():
    print("\nLista de Rotas:") 
    print("Rota 1 - Umirim")
    print("Rota 2 - Croatá")
    print("Rota 3 - São Luis do Curu")
    print("Rota 4 - Itapajé")
    print("Rota 5 - Uruburetama")
    print("Rota 6 - Itapipoca")

def turno(hora):
    if hora >= 6 and hora < 8:
        return "Manhã"
    
    elif hora >= 12 and hora < 14:
        return "Tarde"
    
    elif hora >= 16 and hora < 18:
        return "Final da Tarde"
    
    else:
        return "Não temos transporte neste horário."
    
def Cadastro(nome,rota,turno):
    mensagem = f"Aluno {nome} cadastrado na rota {rota} para o turno da(o) {turno}."
    return mensagem


print("Registro de Alunos - Ônibus IFCE Campus Umirim")
c = 0

for c in range(3):
    print("\nCadastro do Aluno", c+1)
    nome = input("Insira o nome do aluno: ")

    Rotas()
    select = int(input("Insira a rota do aluno: "))

    if select == 1:
        rota = "Rota 1 - Umirim"
    elif select == 2:
        rota = "Rota 2 - Croatá"
    elif select == 3:
        rota = "Rota 3 - São Luis do Curu"
    elif select == 4:
        rota = "Rota 4 - Itapajé"
    elif select == 5:
        rota = "Rota 5 - Uruburetama"
    elif select == 6:
        rota = "Rota 6 - Itapipoca"
    else:
        print("O número da rota inserida não existe.")

    hr = int(input("Insira o horário da aula(7h-18h): "))
    
    tur = turno(hr)
    res = Cadastro(nome,rota,tur)
    
    print(res)
    c+=1

print("\nSistema encerrado.")
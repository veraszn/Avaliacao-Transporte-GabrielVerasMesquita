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
    mensagem = "Aluno " +nome+ "cadastrado na rota" +rota+ " para o turno da(o) " +turno+ "."
    return mensagem






'''função apostar ou não(não terminei)'''
def apostar():
    resp=input("\nvocê gostaria de apostar nessa rodada ou sair do jogo?\nDigite'apostar'ou'sair'\n")
    if (resp =='apostar'):
        return True
    else:
        return False

'''funções para modos de jogo'''
def plb():
    global fichas 
    global z
    global apostap
    print("o número sorteado é:",z)
    if(z== 7 or z== 11):
        fichas=fichas+apostap 
        print("Agora você tem o total de: {}".format(fichas))
    elif(z== 2 or z== 3 or z== 12):
        fichas=fichas-apostap
        print("Agora você tem o total de: {}".format(fichas))
    elif(z== 4 or z== 5 or z== 6 or z== 8 or z== 9 or z== 10):   
        def loop_point():
            w=sorteio()
            global n
            global fichas
            print("Agora você se encontra na fase point referente ao modo plb pela {}° vez\n".format(n))
            print("O valor {} retirado no priemiro sorteio é seu point".format(z))
            print("O novo valor sorteado é",w)
            n=n+1
            print("agora você possui{}fichas",format(fichas))
            if(w==z):
                fichas=fichas+apostap
                print(fichas)
                return True
            elif(w==7):
                fichas=fichas-apostap
                print("você perdeu tudo!!!")
                return True
            else:
                return False
        while(loop_point()!=True):
            loop_point()
        apostapoint()









    




















 def anycraps():
    global fichas
    global z
    global apostaa
    print("o número sorteado é:",z)
    if(z==2 or z==3 or z==12):
        fichas=fichas+7*apostaa
        print("Agora você tem o total de: {}".format(fichas))
    else:
        fichas=fichas-apostaa
        print("Agora você tem o total de: {}".format(fichas))   
    



































































print("\nBem vindo ao Craps Insper, você inicia com 100 fichas \n")

if (apostar()==True):
    while(fichas>0):
        apostas()
else:
    print("até mais")

    
'''Sorteio e soma'''
import random
dado1=[1,2,3,4,5,6]
dado2=[1,2,3,4,5,6]
fichas=100







def sorteio():
    x=random.choice(dado1)
    y=random.choice(dado2)
    resultado=x+y
    return resultado











































    def field():
    global fichas
    global z
    global apostaf
    print("O número sorteado é:",z)
    if(z==5 or z==6 or z==7 or z==8):
        fichas=fichas-apostaf
        print('Você perdeu tudo !!!')
        print("Agora você tem o total de: {}".format(fichas))
    elif(z==3 or z==4 or z==9 or z==10 or z==11):
        fichas=fichas
        print("Você contínua com o total de: {}".format(fichas))
    elif(z==2):
        fichas=fichas+2*apostaf
        print("Agora você tem o total de: {}".format(fichas))
    else:
        fichas=fichas+3*apostaf
        print("Agora você tem o total de: {}".format(fichas))











        def twelve():
    global fichas
    global z
    global apostat
    print("o número sorteado é:",z)
    if(z==12):
        fichas=fichas+30*apostat
        print("Agora você tem o total de: {}".format(fichas))
    else:
        fichas=fichas-apostat
        print("Agora você tem o total de: {}".format(fichas))

        def apostas():
    tipos=[]
    while True:
        global z
        z=sorteio()
        tipo=input("Você se encontra na fase Come Out\n \nQuais tipos de aposta você gostaria de fazer?\n \n Digite 'plb' e/ou 'field' e/ou'anycraps' e/ou'twelve' separado por virgulas\nQuando terminar de escolher digite 'acabei' ")
        if (tipo =='acabei'):
            break
        tipos.append(tipo)
    for word in tipos:
        global apostaa,apostaf,apostap,apostat
        if word=='plb':
            apostap=int(input("Quantas fichas gostaria de jogar? lembrando que você só pode jogar um número inteiro de fichas"))
        elif word=='field':
            apostaf=int(input("Quantas fichas gostaria de jogar? lembrando que você só pode jogar um número inteiro de fichas"))   
        elif word=='anycraps':
            apostaa=int(input("Quantas fichas gostaria de jogar? lembrando que você só pode jogar um número inteiro de fichas"))
        elif word=='twelve':
            apostat=int(input("Quantas fichas gostaria de jogar? lembrando que você só pode jogar um número inteiro de fichas"))     
    for word in tipos:
        if word=='plb':
            print("PlB:\n")
            plb()
            
        elif word=='field':
            print("FIELD:\n")
            field()
            
        elif word=='anycraps':
            print("ANYCRAPS:\n")
            anycraps()
            
        elif word=='twelve':
            print("TWELVE:\n")
            twelve()
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
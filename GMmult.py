#concurso tablas mult para una persona
#n=int(raw_input('CUantos jugadores son?'))
from random import randint

def espera(s):
    raw_input(s+'.   Oprima "Entrar"' )

b=True
while b:
    try:
        l=input('CUales tablas voy a preguntar?')
        if type(l) is int:
            l=[l]
        if not (type(l) is list):
            raise ValueError('Ingresar como 4 o [4,3,2]')
        if len(l)==0:
            raise ValueError('Ingrsar como 4 o [4,3,2]')
        else:
            tab=list()
            j=l.pop(0)
            for i in range(2,10):
                tab.append([j,i])
                tab.append([j,i])
            while len(l)>0:
                j=l.pop(0)
                for i in range(3):
                    tab.append([j,randint(2,9)])
                    #tab.append([j,randint(2,9)])
                    #tab.append([j,randint(2,9)])
        b=False
    except :
        print('Ingrsar como 4 o [4,3,2]')
    
while len(tab)>0:
    if len(tab)==1:
        print('Ya sOlo falta una')
    else:
        print('Faltan '+str(len(tab)))
    [i,j]=tab.pop(randint(0,len(tab)-1))
    try:
        k=int(raw_input('Cuanto es    '+str(i)+' x '+str(j)+'\n'))
    except:
        k=0
    if k==i*j:
        espera('Muy Bien,    '+str(i)+' x '+str(j)+' = '+str(k))
    else:
        tab.append([i,j])
        espera('Recuerde que '+str(i)+' x '+str(j)+' = '+str(i*j))
        s=raw_input('Escribe     "'+str(i)+' x '+str(j)+' = '+str(i*j)+'"\n')
        if s.replace(' ','').replace('\n','').replace('*','x').lower() == (str(i)+'x'+str(j)+'='+str(i*j)):
            espera ('Bien         '+ str(i)+' x '+str(j)+' = '+str(i*j))
        else:
            tab.append([i,j])
            espera ('Recuerde que '+ str(i)+' x '+str(j)+' = '+str(i*j))
espera('FELICITACIONES!!!')

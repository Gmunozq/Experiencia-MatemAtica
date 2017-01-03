#concurso tablas mult para una persona
#n=int(raw_input('CUantos jugadores son?'))
from random import randint

def espera(s):
    raw_input(s+'.   Oprima "Entrar"' )

def lee_lista(s):
    while True:
        try:
            l=input(s)
            if type(l) is int:
                if l==0:
                    l=[]
                elif l<0:
                    raise ValueError('Ingresar como 4 o [4,3,2]')
                else:
                    l1=[l%10]
                    l=l/10
                    while l > 0:
                        l1.append(l%10)
                        l=l/10
                    l=l1
            if not (type(l) is list):
                raise ValueError('Ingresar como 4 o [4,3,2]')
    #        if len(l)==0:
    #            raise ValueError('Ingrsar como 4 o [4,3,2]')
            else:
                return l
        except :
            print('Ingrsar como 4 o [2,3,4] o 234 o range(2,10)')
    
tab=[]
l=lee_lista('CUales tablas voy a preguntar? (pregunta toda la tabla)')
while len(l)>0:
    j=l.pop(0)
    for i in range(2,10):
        tab.append([j,i])
        tab.append([j,i])
l=lee_lista('CUales tablas voy a repasar? (pregunta una parte)')
while len(l)>0:
    j=l.pop(0)
    for i in range(3):
        tab.append([j,randint(2,9)])
    
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

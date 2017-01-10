#bucar <->
#intercambiar renglones

#buscar ->
#deerminar renglon destino
#buscar +-
#Si no hay pasa a 
#confirmar que uno de los operandos es el de destino y su factor es 1
#encontrar el otro operando y por cuanto estA multiplicado

#f1 ra<->rb
#f2 krb->rb
#f3 kra+rb->rb
#f4 rb+kra->rb
#f5 rb-kra->rb

#si hay (<->)
    #asume f1
    #identifica ra
    #identifica rb
    #retorna matriz que intercambia ra y rb
#si no, pero si hay (->)    
    #identifica rb
    #si hay (+)
        #asume f3 o f4
        #identifica kra
        #retorna matriz que suma kra a rb
    #si no, pero si hay (-) cuidado que pueden haber dos menos
        #asume f5
        #identifica kra
        #retorna matriz que suma -kra a rb
    #si no 
        #asume f2
        #identifica krb 
        #retorna matriz que multiplica k veces rb
#si no presenta error

#def interpreta(s):#asume s=kra, k es constante y a es un digito
#devuelve (k:int,a:int,error:String)
from AlgLinMat import *
s="4r1  -> r1"
s=s.lower()
print(s)
def interpretaRenglon(s1):
    s=s1.strip()
    print("interpretando "+s)
    d=s.find("r")
    if d==-1:
        raise ValueError("fala la 'r'. Error en "+s)
    elif d==0:
        k=1
    else:
        try:
            k=int(s[:d])
        except:
            raise ValueError("antes de 'r' sOlo debe haber un entero. Error en "+s)
    #a1=s[d+1:]
    #if not a1.isdigit():
    try:
        a=int(s[d+1:])
    except:
        raise ValueError("despuEs de 'r' sOlo debe haber un dIgito. Error en "+s)
    #a=int(a1)
    return (k,a)
        
#print (str(k)+", "+str(a))
size=6
m=matriz.identidad(size,size)
d=s.find("<->")
if d!=-1:
    (k1,a1)=interpretaRenglon(s[:d])
    (k2,a2)=interpretaRenglon(s[d+3:])
    if (k1 != 1) or (k2 != 1):
        raise ValueError("al intercambiar renglones no se puede multiplicar. Error en "+s)
    print("Se entendiO 'R"+str(a1)+" <-> R"+str(a2)+"'")
    m[a1,a1]=0    
    m[a1,a2]=1    
    m[a2,a1]=1    
    m[a2,a2]=0    
    print(str(m))
else:
    d=s.find("->")
    if d==-1:
        raise ValueError("no se encontrO ni '->' ni '<->'. Error en "+s)
    else:
        (k2,a2)=interpretaRenglon(s[d+3:])
        e=s[:d].find("+")
        f=s[:d].find("-")
        if e!=-1:
            (k11,a11)=interpretaRenglon(s[:e])
            (k12,a12)=interpretaRenglon(s[e+1:d])
            if (a11==a2) and (a12==a2):
                raise ValueError("en este caso es mejor multiplicar el renglOn por "+str(k11+k12)+". Error en "+s)
            elif (a11==a2):
                if (k11!=1):
                    raise ValueError("el renglOn destino no se multiplica por "+str(k11)+". Error en "+s)
                print("Se entendiO '"+str(k12)+"R"+str(a12)+"+"+"R"+str(a2)+" -> R"+str(a2)+"'")
                m[a2,a12]=k12
                print(str(m))
            elif (a12==a2):
                if (k12!=1):
                    raise ValueError("el renglOn destino no se multiplica por "+str(k12)+". Error en "+s)
                print("Se entendiO '"+str(k11)+"R"+str(a11)+"+"+"R"+str(a2)+" -> R"+str(a2)+"'")
                m[a2,a11]=k11
                print(str(m))
            else:#if (a11!=a2) and (a12!=a2):
                raise ValueError("el renglOn destino y un origen deben coincidir. Error en "+s)
        elif f!=-1:
            c=s[:d].count('r')
            if c==0:
                raise ValueError("faltan 'R' en "+s[:d])
            elif c==2:
                (k11,a11)=interpretaRenglon(s[:f])
                (k12,a12)=interpretaRenglon(s[f+1:d])
                if (a11==a2) and (a12==a2):
                    raise ValueError("en este caso es mejor multiplicar el renglOn. Error en "+s)
                elif (a11==a2):
                    if (k11!=1):
                        raise ValueError("el renglOn destino no se multiplica por "+str(k11)+". Error en "+s)
                    print("Se entendiO '"+str(-k12)+"R"+str(a12)+"+"+"R"+str(a2)+" -> R"+str(a2)+"'")
                    m[a2,a12]=-k12
                    print(str(m))
                elif (a12==a2):
                    raise ValueError("el renglOn destino no se multiplica por "+str(-k12)+". Error en "+s)
                else:#if (a11!=a2) and (a12!=a2):
                    raise ValueError("el renglOn destino y un origen deben coincidir. Error en "+s)
            elif c==1:
                (k1,a1)=interpretaRenglon(s[:d])
                if a1 != a2 :
                    raise ValueError("el renglOn destino y el origen deben coincidir. Error en "+s)
                print("Se entendiO '"+str(k1)+"R"+str(a1)+" -> R"+str(a2)+"'")
                m[a2,a2]=k1
                print(str(m))
             
            else:
                raise ValueError("se operan mAximo dos renglones. Error en "+s)
        else:
          (k1,a1)=interpretaRenglon(s[:d])
          if a1 != a2 :
              raise ValueError("el renglOn destino y el origen deben coincidir. Error en "+s)
          print("Se entendiO '"+str(k1)+"R"+str(a1)+" -> R"+str(a2)+"'")
          m[a2,a2]=k1
          print(str(m))
          

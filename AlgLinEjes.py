from java import awt
from java.awt.geom import *
from java.awt import *
from java.awt.event import *
from javax.swing import * 
from java.awt.event import *
from math import *
from AlgLinMat import *


negro = Color.black
azul = Color.blue
azul_claro = Color.cyan
gris_oscuro = Color.darkGray
gris = Color.gray
verde = Color.green
gris_claro = Color.lightGray
magenta = Color.magenta
naranja = Color.orange
rosado = Color.pink
rojo = Color.red
blanco = Color.white
amarillo = Color.yellow

import time

class UnaFigura:
    deColor=negro
    en=matriz.de_ceros(3,1,'no_mostrar')
    listadeplanos=list()

    
    def se_dibuja(self,g,lista_puntos2D=(Point2D.Double(1,0),Point2D.Double(0,1)),en=matriz.de_ceros(3,1,'no_mostrar')):
        pass

    def ubicad_en(self,x1,x2='nada',x3=0):
        self.en=UnVector3(x1,x2,x3)
        map(lambda n: n.repaint(),self.listadeplanos)
        return self
        
    def de_color(self,color):
        self.deColor=color
        return self

    def dentro_de(self,plano):
        plano.adiciona(self)
        self.listadeplanos.append(plano)
        return self
        
    def se_desplaza(self,despl,pasos=5,tiempo=2):
        paso=frac(1,pasos)
        mov=escalar_por_matriz(paso,despl)
        for i in range(pasos):
            self.ubicad_en(sumar_matrices(self.en,mov))
            time.sleep(tiempo*paso)
            


    
class UnConjuntoDeFiguras(UnaFigura):
    lista_de_figuras=list()
    def __init__(self,lista_de_figuras):
        self.lista_de_figuras=lista_de_figuras
        
    def se_dibuja(self,g,lista_de_puntos2D,en):
        for cada_figura in self.lista_de_figuras:
            cada_figura.se_dibuja(g,lista_de_puntos2D,sumar_matrices(self.en,en))

    def adiciona(self,la_figura):
        self.lista_de_figuras.append(la_figura)
        self.repaint()
        
    def de_color(self,color):
        for cada_figura in self.lista_de_figuras:
            cada_figura.de_color(color)
        return self

    def repaint():
        pass
    
    
    
class UnaUnionDePuntos(UnaFigura):
    
    def __init__(self,matriz_de_puntos):
        self.matriz_de_puntos=matriz_de_puntos
        
    def se_dibuja(self,g,lista_de_puntos2D,en3):
        en2=sumar_matrices(self.en,en3)
        s=Path2D.Double()
        (x1,x2)=(0,0)
        for i in range(len(lista_de_puntos2D)):
            try:
                en1=en2[i+1,1]
            except:
                en1=0
                print('no en '+str(i+1)+', '+str(1))
            try:
                mdp=self.matriz_de_puntos[i+1,1]
            except:
                mdp=0
                print('no mdp '+str(i+1)+', '+str(1))
            x1=x1+lista_de_puntos2D[i].getX()*(mdp+en1)
            x2=x2+lista_de_puntos2D[i].getY()*(mdp+en1)
        s.moveTo(x1,x2)
        (m,n)=self.matriz_de_puntos.size()
        for j in range(1,n):
            (x1,x2)=(0,0)
            for i in range(len(lista_de_puntos2D)):
                try:
                    en1=en2[i+1,1]
                except:
                    en1=0
                    print('no en '+str(i+1)+', '+str(j+1))
                    #raise ValueError('no en '+str(i+1)+', '+str(j+1))
                try:
                    mdp=self.matriz_de_puntos[i+1,j+1]
                except:
                    mdp=0
                    print('no mdp '+str(i+1)+', '+str(j+1))
                x1=x1+lista_de_puntos2D[i].getX()*(mdp+en1)
                x2=x2+lista_de_puntos2D[i].getY()*(mdp+en1)
            s.lineTo(x1,x2)
        g.setColor(self.deColor)
        g.draw(s)

     
class UnVector3(UnConjuntoDeFiguras,matriz):
    def __init__(self,x1,x2='nada',x3=0):
        if x2!='nada':
            matriz.__init__(self,[[x1],[x2],[x3]],'no_mostrar')
        elif isinstance(x1,matriz):
            try:
                x3=x1[3,1]
            except:
                x3=0
            x2=x1[2,1]
            x1=x1[1,1]
            matriz.__init__(self,[[x1],[x2],[x3]],'no_mostrar')
        elif (type(x1) is list) and not(type(x1[0]) is list):
            try:
                x3=x1[2]
            except:
                x3=0
            x2=x1[1]
            x1=x1[0]
            matriz.__init__(self,[[x1],[x2],[x3]],'no_mostrar')
        else:
            matriz.__init__(self,x1,'no_mostrar')

        

class UnaFlecha(UnVector3):
    def __init__(self,x1,x2='nada',x3=0):
        UnVector3.__init__(self,x1,x2,x3)
        x1=self[1,1]
        x2=self[2,1]
        x3=self[3,1]

            
        y12=(0.7*x1-0.7*x2)/10.0
        y21=(0.7*x1+0.7*x2)/10.0
        y23=(0.7*x2-0.7*x3)/10.0
        y32=(0.7*x2+0.7*x3)/10.0
        y31=(0.7*x3-0.7*x1)/10.0
        y13=(0.7*x3+0.7*x1)/10.0
        
        UnConjuntoDeFiguras.__init__(self,[
        UnaUnionDePuntos(matriz([[0,x1],[0,x2],[0,x3]],'no_mostrar')),
        UnaUnionDePuntos(matriz([[x1,x1-y12],[x2,x2-y21],[x3,x3]],'no_mostrar')),
        UnaUnionDePuntos(matriz([[x1,x1-y21],[x2,x2+y12],[x3,x3]],'no_mostrar')),
        UnaUnionDePuntos(matriz([[x1,x1],[x2,x2-y23],[x3,x3-y32]],'no_mostrar')),
        UnaUnionDePuntos(matriz([[x1,x1],[x2,x2-y32],[x3,x3+y23]],'no_mostrar')),
        UnaUnionDePuntos(matriz([[x1,x1-y13],[x2,x2],[x3,x3-y31]],'no_mostrar')),
        UnaUnionDePuntos(matriz([[x1,x1+y31],[x2,x2],[x3,x3-y13]],'no_mostrar'))
        ])

class UnPunto(UnVector3):
    def __init__(self,x1,x2='nada',x3=0):
        UnVector3.__init__(self,x1,x2,x3)
        x1=self[1,1]
        x2=self[2,1]
        x3=self[3,1]
       
        UnConjuntoDeFiguras.__init__(self,[
        UnaUnionDePuntos(matriz([[x1*9/10,x1*11/10],[x2,x2],[x3,x3]],'no_mostrar')),
        UnaUnionDePuntos(matriz([[x1,x1],[x2*9/10,x2*11/10],[x3,x3]],'no_mostrar')),
        UnaUnionDePuntos(matriz([[x1,x1],[x2,x2],[x3*9/10,x3*11/10]],'no_mostrar'))
        ])

class UnPuntito(UnVector3):
    def __init__(self,x1,x2='nada',x3=0):
        UnVector3.__init__(self,x1,x2,x3)
        x1=self[1,1]
        x2=self[2,1]
        x3=self[3,1]
        
        UnConjuntoDeFiguras.__init__(self,[
        UnaUnionDePuntos(matriz([[x1,x1],[x2,x2],[x3,x3]],'no_mostrar'))
        ])

class UnPlanoCoordenado3DInteractivo(awt.Canvas,MouseMotionListener,UnConjuntoDeFiguras):

    lista_de_figuras=list()

    def __init__(self):
        frame1 = JFrame('3D interactivo', defaultCloseOperation = JFrame.EXIT_ON_CLOSE,size = (300, 300))
        frame1.add(self)
        frame1.visible = True
        self.v1=0
        self.v2=0
        self.contenedor=self
        self.contenedor.addMouseMotionListener(self)
        self.puntos2D_de_proyeccion=self.calcula_puntos2D_de_proyeccion()
        self.adiciona(UnaUnionDePuntos(matriz([[0,100],[0,0],[0,0]],'no_mostrar')).de_color(azul))
        self.adiciona(UnaUnionDePuntos(matriz([[0,0],[0,100],[0,0]],'no_mostrar')).de_color(rojo))
        self.adiciona(UnaUnionDePuntos(matriz([[0,0],[0,0],[0,100]],'no_mostrar')).de_color(verde))

    def calcula_puntos2D_de_proyeccion(self):
        m=1-self.v2*self.v2
        m1=sqrt(m)
        self.v3=sqrt(m-self.v1*self.v1)
        m1=1
        m3=sqrt(1-self.v1*self.v1+self.v2*self.v2)
        x=Point2D.Double((1-self.v1*self.v1)/m1,-self.v1*self.v2/m1)
        y=Point2D.Double(-self.v1*self.v2/m1,(1-self.v2*self.v2)/m1)
        z=Point2D.Double(-self.v1/m1,-self.v2/m1)
        s1=self.v1
        s2=self.v2
        c1=sqrt(1-s1*s1)
        c2=sqrt(1-s2*s2)
        return (x,y,z)
        
    def __len__(self):
        return 3     

    def __getitem__(self,i):
      return self.puntos2D_de_proyeccion[i]

    def mouseMoved(self, event):
        return

    def mouseDragged(self,event):
        sz=self.contenedor.getSize()
        self.v1 = (event.getX()/sz.getWidth())*(-1.9)+1;
        self.v2 = (event.getY()/sz.getHeight())*1.9-1;
        try:
            self.puntos2D_de_proyeccion=self.calcula_puntos2D_de_proyeccion()
            self.contenedor.repaint();
        except:
            pass
        
    def paint(self, g):
        self.sz = self.size
        self.minimo=min(self.sz.width,self.sz.height)
        g.translate(self.sz.width/2,self.sz.height/2)
        g.scale(1,-1)
        self.se_dibuja(g,self.puntos2D_de_proyeccion,self.en)


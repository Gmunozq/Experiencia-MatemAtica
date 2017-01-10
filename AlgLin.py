#Realizar operaciones matriciales suma prod escalar inversa determinante valores propios, solucion sist ecuaciones, encontrar base de espacio mirar contenencia de vector


#Mat es una lista renglOn que contiene listas columnas
#Vec es una lisa columna
#esc es Int o Double
import sys
import copy
from fractions import Fraction

#escalar por lista
def escList(esc1,list1):
    listR=list() #Crea una lista
    for a in list1:
        listR.append(esc1*a)      
    return listR 

#suma listas
def addList(list1,list2):
    listR=list() #Crea una lista 
    for i in range(len(list1)):
        listR.append(list1[i] + list2[i])      
    return listR 
    
def sumar_matrices(A,B):
    C=copy.deepcopy(A)
    (m,n)=C.size()
    for i in range(1,m+1):
        for j in range(1,n+1):
          C[i,j]=A[i,j]+B[i,j]      
    return C

def multiplicar_matrices(A,B):
    (Am,An)=A.size()
    (Bm,Bn)=B.size()
    C=matriz.de_ceros(Am,Bn)
    for i in range(1,Am+1):
        for j in range(1,Bn+1):
            t=0
            for k in range(1,An+1):
                t=t+A[i,k]*B[k,j]
                #print "i "+str(i)+"j "+str(j)+"k "+str(k)+"t "+str(t)
            C[i,j]=t     
    return C

def escalar_por_matriz(k,A):
    C=copy.deepcopy(A)
    (m,n)=C.size()
    for i in range(1,m+1):
        for j in range(1,n+1):
          C[i,j]=k*A[i,j]      
    return C


#latex de columna de lista
def col(list1):
    l=list(list1)
    s="\\begin{bmatrix} " +str(l.pop(0))
    for a in l:
        s=s+" \\\\ " +str(a)      
    return s + " \\end{bmatrix}"

#latex de columna de lista
def ren(list1):
    l=list(list1)
    s= str(l.pop(0))
    for a in l:
        s=s+" & " +str(a)      
    return s 

#latex de columna de lista
#def list_str_f(list1,fun):
#    l=list(list1)
#    s="[" +fun(l.pop(0))
#    for a in l:
#        s=s+", " +fun(a)      
#    return s + " ]"
#def list_str(list1):
#    return list_str_f(list1,str)


#vector abstracto
class vecAbs:
    def evalu(self):
        pass
    def latex(self):
        pass
    def __mul__(self,vecAbs1):
        return opBin(self,num(vecAbs1),escList,"")
    __rmul__ = __mul__
    def __add__(self,vecAbs1):
        return opBin(self,vecAbs1,addList," + ")
    __radd__ = __add__
    def evaLat(self):
        return col(self.evalu())


class num:
    def __init__(self,val):
        self.val=val
    def latex(self):
        return str(self.val)   
    def evalu(self):
        return self.val
    
#fraccionario    
class frac(Fraction): 
    def latex(self):
        return "\\frac{"+str(self.numerator)+"}{"+str(self.denominator)+"}"   
    
#Operacion binaria
class opBin(vecAbs):
    def __init__(self,vecAbs1,vecAbs2,fun,simbLatex):
        self.vecAbs1=vecAbs1
        self.vecAbs2=vecAbs2
        self.fun=fun
        self.simbLatex=simbLatex
        #mostrar(self.evalu().latex()=self.latex())
        mostrar(self.evalu().latex()+"="+self.latex())
    def evalu(self):
        p=(self.vecAbs1.evalu(),self.vecAbs2.evalu())
        p1= self.fun(*p)
        #mostrar(self.latex()+""+p1.latex())
        return p1
    def latex(self):
        return self.vecAbs1.latex() + self.simbLatex + self.vecAbs2.latex()


#vector
class vec(vecAbs):
  def __init__(self,lista):
    self.lista=lista
#    mostrar(self.latex())
  def col(self):
    l=list(self.lista)
    s="\\begin{bmatrix} " +str(l.pop(0))
    for a in l:
      s=s+" \\\\ " +str(a)      
    return s + " \\end{bmatrix}"
  def ren(self):
    l=list(self.lista)
    s=str(l.pop(0))
    for a in l:
      s=s+" & " +str(a)      
    return s 
  def reng(self):
    return "\\begin{bmatrix} " + self.ren() + " \\end{bmatrix}"
  latex = col
  def evalu(self):
      return self.lista
  def __rmul__(self,esc):
      return opBin(num(esc),self,escList,"")
  #def __mul__(self,vecAbs1):
      #return opBin(self,num(vecAbs1),escList,"")
  #__rmul__ = __mul__
  def __add__(self,vecAbs1):
      return opBin(self,vecAbs1,addList," + ")
  __radd__ = __add__
  __str__ = col
#  def mul(self,k):
#      return escList(k,self.lista)
#    l=list(self.lista)
#    for i in range(len(l)):
#      l[i]=k*l[i]      
#    return vector(l) 
#  def __rmul__(self,k):
#    l=list(self.lista)
#    for i in range(len(l)):
#      l[i]=k*l[i]      
#    return vector(l) 
#  def add(self,k):
#      return addList(self.lista,k.lista)
#    l=list(self.lista)
#    for i in range(len(l)):
#      l[i]=k.lista[i]+l[i]      
#    return vector(l) 
#  __radd__ = __add__
  
  
  
#matriz  
def matlab2python(lista):
        lista1=lista.split(';')
        lista2=map(lambda n: n.split(),lista1)
        lista3=map(lambda n: map(str2num,n),lista2)
        return lista3

def str2num(s):
    if s.find('.')!=-1:
        return float(s)
    if s.find('/')!=-1:
        return frac(s)
    return int(s)
    
class matriz:# es una columna de renglones
  def __init__(self,lista):
    if type(lista) is list:
        self.lista=lista
    if type(lista) is str:
        self.lista= matlab2python(lista)
    mostrar(self.latex())
    
  @staticmethod
  def de_ceros(m,n):
    C=list()
    for i in range(1,m+1):
      r=list()
      for j in range(1,n+1):
        r.append(0)
      C.append(r)
    return matriz(C)


  def __getitem__(self,(i,j)):
      return self.lista[i-1][j-1]
  def __setitem__(self,(i,j),d):
       self.lista[i-1][j-1]=d
  def size(self):
    return (len(self.lista),len(self.lista[0]))
  def __rmul__(self,vecAbs1):
    return opBin(self,num(vecAbs1),escalar_por_matriz,"")
  def __mul__(self,vecAbs1):
    return opBin(self,vecAbs1,multiplicar_matrices,"")
  def __add__(self,vecAbs1):
    return opBin(self,vecAbs1,sumar_matrices,"+")
  def evalu(self):
      return self
  def latex(self):
    l=list(self.lista)
    s="\\begin{bmatrix} " + ren(l.pop(0))
    for a in l:
      s=s+" \\\\ " +ren(a)      
    return s + " \\end{bmatrix}"
  def a(self,k,i,j):
    lista=self.lista
    s=escList(k,lista[i-1])
    t=addList(s,lista[j-1])
    lista[j-1]=t
    cmd=str(k)+"R"+str(i)+" + R"+str(j)+" \\rightarrow R"+str(j)
#    cmd1="\\stackrel{"+cmd+"}{\\rightarrow}"
    cmd1="\\xrightarrow{"+cmd+"}"
    mostrar("\stackrel{"+cmd1+"}{"+self.latex()+"}")
    #mostrar(cmd1+self.latex())
    return lista 
  def e(self,k,i):
    lista=self.lista
    t=escList(k,lista[i-1])
    lista[i-1]=t
    cmd=str(k)+"R"+str(i)+" \\rightarrow R"+str(i)
    cmd1="\\xrightarrow{"+cmd+"}"
    mostrar("\stackrel{"+cmd1+"}{"+self.latex()+"}")
    #mostrar(cmd1+self.latex())
    return lista 
  def i(self,i,j):
    lista=self.lista
    t=lista[i-1]
    lista[i-1]=lista[j-1]
    lista[j-1]=t
    cmd="R"+str(i)+" \\leftrightarrow R"+str(j)
    cmd1="\\xrightarrow{"+cmd+"}"
    mostrar("\stackrel{"+cmd1+"}{"+self.latex()+"}")
    #mostrar(cmd1+self.latex())
    return lista 
#  def __str__(self):
#    l=list(list1)
#    s="["+ str(l.pop(0))
#    for a in l:
#        s=s+"["       
#        for b in a:
#            s=s+b+","       
#    return s 
 #   l=list(self.lista)
 #    return list_str_f(l,list_str)
  
  
  
from javax.swing import * # JPanel, JFrame, JScrollPane, JLabel
from java.awt.event import *
from org.scilab.forge.jlatexmath import TeXConstants, TeXFormula, TeXIcon
import WrapLayout

frameTxt = JFrame('ClaseUD - LaTex',
            defaultCloseOperation = JFrame.EXIT_ON_CLOSE,
            size = (300, 300)
        )
#def change_text(event):
#    print 'Clicked!'
#button = JButton('Click Me!', actionPerformed=change_text)
panelTxt= JPanel()
areaTexto= JTextArea()
panelTxt.add(areaTexto)
scrollPTxt= JScrollPane(panelTxt)
#scrollB=scrollP.getVerticalScrollBar() 
frameTxt.add( scrollPTxt )
frameTxt.visible = True

frame = JFrame('ClaseUD - Tablero',
            defaultCloseOperation = JFrame.EXIT_ON_CLOSE,
            size = (300, 300)
        )
#def change_text(event):
#    print 'Clicked!'
#button = JButton('Click Me!', actionPerformewd=change_text)
panel= JPanel()
panel.setLayout(  WrapLayout())
scrollP= JScrollPane(panel,ScrollPaneConstants.VERTICAL_SCROLLBAR_ALWAYS ,ScrollPaneConstants.HORIZONTAL_SCROLLBAR_NEVER )
class Ajustable(AdjustmentListener) :
    prvMax=0
    def adjustmentValueChanged( self,e) : 
        self.actMax=e.getAdjustable().getMaximum()
        if(self.actMax != self.prvMax):
            e.getAdjustable().setValue(self.actMax)
            self.prvMax=self.actMax  
    

scrollB=scrollP.getVerticalScrollBar().addAdjustmentListener( Ajustable())
frame.add( scrollP )
frame.visible = True

#Muestra el texto en las dos ventanas
def mostrar(texto):
    TAMANO_LATEX=50
    formula =  TeXFormula(texto)
    icono = formula.createTeXIcon(TeXConstants.STYLE_TEXT,TAMANO_LATEX)
    jl =  JLabel(icono)
    areaTexto.append(texto+"\n")
    panel.add(jl)
    panel.revalidate()
#    scrollB.setValue(scrollB.getMaximum())
    panel.repaint()
#    scrollB.setValue(scrollB.getMaximum())
#    scrollB.setValue(scrollB.getMaximum())
#    scrollB.setValue(scrollB.getMaximum())
    
from java import awt
from java.awt.geom import *
from java.awt import *
#????

#class FiguraLinea:
#    def se_dibuja(self,g):
#        g.drawLine(0,0,100,100)

#class FigGenInf:
#    def __init__(self,x1,x2):
#
#    def dibujar(self,g):
#        g.drawLine(0,0,100,100)

class UnaCoordenada3D:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
        
    def getX(self):
        return x
    
    def getY(self):
        return y
    
    def getZ(self):
        return z
    

class UnaFigura:
    contenedor=0
    
    def se_dibuja(self,g):
        return
    
    # def esta_en(self,contenedor):
        # self.contenedor=contenedor
        
    
    #def que_bordes_tiene(self,g):
    #    return g.getClipBounds() #g.getDeviceConfiguration().getBounds()
        


class UnaFlechaFija(UnaFigura):
    def __init__(self,x1,x2):
        self.x1=x1
        self.x2=x2
        self.linea1=Line2D.Double(0,0,self.x1,self.x2)
        self.y1=(0.7*self.x1-0.7*self.x2)/10.0
        self.y2=(0.7*self.x1+0.7*self.x2)/10.0
        self.linea2=Line2D.Double(self.x1,self.x2,self.x1-self.y1,self.x2-self.y2)
        self.linea3=Line2D.Double(self.x1,self.x2,self.x1-self.y2,self.x2+self.y1)
    def se_dibuja(self,g):
        g.draw(self.linea1)
        g.draw(self.linea2)
        g.draw(self.linea3)

#~ class Coordenadas(list):
    #~ def __init__(self,lista):
        #~ self.lista=lista
    #~ def __getitem__(self,i):
        #~ return self.lista[i-1]
    #~ def __setitem__(self,i,v):
        #~ self.lista[i-1]=v
    #~ def size(self):
        #~ return self.lista.len()

#class CoordenadasDependientes:
#~ class CoordenadasDependientes:
    #~ def __init__(self,puntos,matriz):
        #~ self.puntos=puntos
        #~ self.matriz=matriz
    #~ def getX():
        #~ k=0
        #~ for j in range(puntos.len())
            #~ k=k+puntos[i].getX()*matriz[j,1]
        
    #~ def __getitem__(self,i):
        #~ k=0
        #~ for j in range(1,self.coordenadas.size+1)
            #~ k=k+matriz[i,j]*coordenadas[j]
        #~ return k
        

class UnaFiguraEn3D(UnaFigura):
    def __init__(self,lista_de_puntos2D,matriz_de_puntos):
        self.matriz_de_puntos=matriz_de_puntos
        self.lista_de_puntos2D=lista_de_puntos2D
        
    def se_dibuja(self,g):
        s=Path2D.Double()
        (x1,x2)=(0,0)
        for i in range(len(self.lista_de_puntos2D)):
            x1=x1+self.lista_de_puntos2D[i].getX()*self.matriz_de_puntos[i+1,1]
            x2=x2+self.lista_de_puntos2D[i].getY()*self.matriz_de_puntos[i+1,1]
        s.moveTo(x1,x2)
        (m,n)=self.matriz_de_puntos.size()
        for j in range(1,n):
            (x1,x2)=(0,0)
            for i in range(len(self.lista_de_puntos2D)):
                x1=x1+self.lista_de_puntos2D[i].getX()*self.matriz_de_puntos[i+1,j+1]
                x2=x2+self.lista_de_puntos2D[i].getY()*self.matriz_de_puntos[i+1,j+1]
            s.lineTo(x1,x2)
        g.draw(s)


class UnaFlecha(UnaFigura):
    def __init__(self,punto):
        self.punto=punto
    def se_dibuja(self,g):
        self.x1=punto.x
        self.x2=punto.y
        self.linea1=Line2D.Double(0,0,self.x1,self.x2)
        self.y1=(0.7*self.x1-0.7*self.x2)/10.0
        self.y2=(0.7*self.x1+0.7*self.x2)/10.0
        self.linea2=Line2D.Double(self.x1,self.x2,self.x1-self.y1,self.x2-self.y2)
        self.linea3=Line2D.Double(self.x1,self.x2,self.x1-self.y2,self.x2+self.y1)
        g.draw(self.linea1)
        g.draw(self.linea2)
        g.draw(self.linea3)

from java.awt.event import *




class UnaFlechaInteractiva(UnaFigura,MouseMotionListener):
    def __init__(self,x1,x2,contenedor):
        self.z1=x1
        self.z2=x2
        #super(UnaFlechaInteractiva,self)
        #UnaFlecha.__init__(self,x1,x2)
        self.contenedor=contenedor
        self.contenedor.addMouseMotionListener(self)

    def se_dibuja(self,g):
        p1=Point2D.Double()
        p2=Point2D.Double(self.z1,self.z2)
        ta=g.getTransform() 
        p3=ta.inverseTransform(p2, p1)
        self.x1=p3.x
        self.x2=p3.y
        #print "x1: "+str(self.x1)+"  x2: "+str(self.x2)+"z1: "+str(self.z1)+"  z2: "+str(self.z2)
        self.linea1=Line2D.Double(0,0,self.x1,self.x2)
        self.y1=(0.7*self.x1-0.7*self.x2)/10.0
        self.y2=(0.7*self.x1+0.7*self.x2)/10.0
        self.linea2=Line2D.Double(self.x1,self.x2,self.x1-self.y1,self.x2-self.y2)
        self.linea3=Line2D.Double(self.x1,self.x2,self.x1-self.y2,self.x2+self.y1)
        g.draw(self.linea1)
        g.draw(self.linea2)
        g.draw(self.linea3)
        
    def getX(self):
        return self.x1
        
    def getY(self):
        return self.x2
        
    def mouseMoved(self, event):
        return

    def mouseDragged(self,event):
        #print "x1: "+str(self.x1)+"  x2: "+str(self.x2)
        self.z1 = event.getX();
        self.z2 = event.getY();
        self.contenedor.repaint();
        
from math import *

    
    
class UnPunto(UnaFigura):
    def __init__(self,x1,x2):
        self.x1=x1
        self.x2=x2
        #self.d = (x1+x2)/50
        #self.elipse1=Ellipse2D.Double(self.x1-self.d,self.x2-self.d,self.d,self.d)
    def se_dibuja(self,g):
        bordes=g.getClipBounds()
        self.d = (bordes.height+bordes.width)/100
        self.elipse1=Ellipse2D.Double(self.x1-self.d,self.x2-self.d,self.d,self.d)
        g.setPaint(Color.black);
        g.fill(self.elipse1);
        g.draw(self.elipse1)
        #print "bordes"+str(bordes.height)+" "+str(bordes.width)+" "+str(bordes.x)+" "+str(bordes.y)

#>>> from AlgLin import *
#>>> elPlano = UnPlanoCoordenado()
#>>> elPlano.adiciona(UnaFlecha(30,-80))
class UnPlanoCoordenado(awt.Canvas):
 #   linea=FiguraLinea()
    lista_de_figuras=list()#{UnaFlechaFija(100,0),UnaFlechaFija(0,100)}
    
    def __init__(self):
        frame1 = JFrame('Hello, Jython1!', defaultCloseOperation = JFrame.EXIT_ON_CLOSE,size = (300, 300))
        frame1.add(self)
        frame1.visible = True
        #print "hola mundo"

    def paint(self, g):
        self.sz = self.size
        self.minimo=min(self.sz.width,self.sz.height)
        g.translate(self.sz.width/2,self.sz.height/2)
        g.scale(1,-1)
        #g.scale(sz.width/4,-sz.height/4)
        #g.setStroke(BasicStroke(4.0/minimo))
        #g.drawLine(0,sz.height/2,sz.width,sz.height/2)
        #g.drawLine(sz.width/2,0,sz.width/2,sz.height)
        for cada_figura in self.lista_de_figuras:
            cada_figura.se_dibuja(g)
        #g.drawText(100,100,"hola")

    def adiciona(self,la_figura):
        self.lista_de_figuras.append(la_figura)
        #la_figura.esta_en(self)
        self.repaint()

class UnPlanoCoordenado3DInteractivo(UnPlanoCoordenado,MouseMotionListener):
#class UnaProyeccionInteractiva(MouseMotionListener):
#self.puntos2D_de_proyeccion=list()
    #lista_de_figuras=list()
    def __init__(self):
        #UnPlanoCoordenado.__init__(self)
        frame1 = JFrame('3D interactivo', defaultCloseOperation = JFrame.EXIT_ON_CLOSE,size = (300, 300))
        frame1.add(self)
        frame1.visible = True
        self.v1=0
        self.v2=0
        self.contenedor=self
        self.contenedor.addMouseMotionListener(self)
        #contenedor.adiciona(self)
        self.puntos2D_de_proyeccion=self.calcula_puntos2D_de_proyeccion()
    


    def calcula_puntos2D_de_proyeccion(self):
        m=1-self.v2*self.v2
        m1=sqrt(m)
        ##mm=m*m
        #print "v1="+str(self.v1)+"v2="+str(self.v2)
        self.v3=sqrt(m-self.v1*self.v1)
        ##x=Point2D.Double(self.v3/1,-self.v1*self.v2/1)
        ##y=Point2D.Double(0,m)
        ##z=Point2D.Double(-self.v1/1,-self.v3*self.v2/1)
        #x=Point2D.Double(self.v3/m1,self.v1*self.v2/m1)
        #y=Point2D.Double(0,m1)
        #z=Point2D.Double(-self.v1/m1,self.v3*self.v2/m1)
        m1=1
        m3=sqrt(1-self.v1*self.v1+self.v2*self.v2)
        x=Point2D.Double((1-self.v1*self.v1)/m1,-self.v1*self.v2/m1)
        y=Point2D.Double(-self.v1*self.v2/m1,(1-self.v2*self.v2)/m1)
        z=Point2D.Double(-self.v1/m1,-self.v2/m1)
        s1=self.v1
        s2=self.v2
        c1=sqrt(1-s1*s1)#abs(s1)
        c2=sqrt(1-s2*s2)#1-abs(s2)
        #x=Point2D.Double(c1*c1+c2*s1*s1,-s1*c1+c1*c2*s1)
        #y=Point2D.Double(-s1*c1+c1*c2*s1,c1*c1*c2+s1*s1)
        #z=Point2D.Double(-s1*s2,-s2*c1)
        
        return (x,y,z)
        
    def __len__(self):
        return 3     

    def __getitem__(self,i):
      return self.puntos2D_de_proyeccion[i]
    
    
    #def getXY(self,P):
    #    m=1-self.v2*self.v2
    #    mm=m*m
    #    v3=sqrt(m-self.v1*self.v1)
    #    return (v3*p.getX()/mm-v1*p.getZ()/mm, v1*v2*p.getX()/m+p.getY()+v2*v3*p.getZ()/m)
        

    #~ def getY(self,P):
        #~ m=1-self.v2*self.v2
        #~ v3=sqrt(m-self.v1*self.v1)
        #~ return v1*v2*p.getX()/m+p.getY()+v2*v3*p.getZ()/m
        
    #~ def coordenadas_de(self,vector3):
        
        
    def mouseMoved(self, event):
        return

    def mouseDragged(self,event):
        #print "x1: "+str(self.x1)+"  x2: "+str(self.x2)
        sz=self.contenedor.getSize()
        self.v1 = (event.getX()/sz.getWidth())*(-1.9)+1;
        self.v2 = (event.getY()/sz.getHeight())*1.9-1;
        self.puntos2D_de_proyeccion=self.calcula_puntos2D_de_proyeccion()
        self.contenedor.repaint();
        #print "v1: "+str(self.v1)+"  v2: "+str(self.v2)
        
    def paint(self, g):
        self.lista_de_puntos2D=self.puntos2D_de_proyeccion
        self.sz = self.size
        self.minimo=min(self.sz.width,self.sz.height)
        g.translate(self.sz.width/2,self.sz.height/2)
        g.scale(1,-1)
        #g.scale(sz.width/4,-sz.height/4)
        #g.setStroke(BasicStroke(4.0/minimo))
        #g.drawLine(0,sz.height/2,sz.width,sz.height/2)
        #g.drawLine(sz.width/2,0,sz.width/2,sz.height)
        for cada_figura in self.lista_de_figuras:
            self.matriz_de_puntos=cada_figura
        #g.drawText(100,100,"hola")
#    def se_dibuja(self,g):
            s=Path2D.Double()
            (x1,x2)=(0,0)
            for i in range(len(self.lista_de_puntos2D)):
                x1=x1+self.lista_de_puntos2D[i].getX()*self.matriz_de_puntos[i+1,1]
                x2=x2+self.lista_de_puntos2D[i].getY()*self.matriz_de_puntos[i+1,1]
            s.moveTo(x1,x2)
            (m,n)=self.matriz_de_puntos.size()
            for j in range(1,n):
                (x1,x2)=(0,0)
                for i in range(len(self.lista_de_puntos2D)):
                    x1=x1+self.lista_de_puntos2D[i].getX()*self.matriz_de_puntos[i+1,j+1]
                    x2=x2+self.lista_de_puntos2D[i].getY()*self.matriz_de_puntos[i+1,j+1]
                s.lineTo(x1,x2)
            g.draw(s)
    

#def plano():
#    frame1 = JFrame('Hello, Jython1!', defaultCloseOperation = JFrame.EXIT_ON_CLOSE,size = (300, 300))
#	#p = awt.Panel(layout=awt.BorderLayout())
#    graph = UnPlanoCoordenado()
#	#p.add(graph, 'Center')
#    frame1.add( graph)
#    frame1.visible = True
          
    #elPlano=UnPlanoCoordenado()
    #panel.add(UnPlanoCoordenado())

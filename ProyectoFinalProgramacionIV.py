"""
Proyecto Final Programación 4
Consulta de productos minimercado
Integrantes:
Santiago Hincapié Arango
Camilo Kenguan Sánchez
"""
#Librerías immplementadas
import tkinter      #Librería que permite implementar la parte grádica del programa
from tkinter.constants import CENTER
from PIL import ImageTk, Image      #Librería que permite redimensionar las imagenes creadas

#CREACIÓN DE VENTANA EN DONDE SE EJECUTA EL PROGRAMA
ventana=tkinter.Tk()
ventana.title("Tienda Don Chuzo")
ventana.geometry("600x600")
ventana.configure(bg="black")
#Creación de etiquetas en donde se mostrarán los datos invocados
etiqueta= tkinter.Label(ventana,text="tienda don chuzo",bg="black",font="Gobold",width=20,foreground="white")
etiqueta.grid(row=0,column=1)
etiquetatex= tkinter.Label(ventana,text="estos son nuestros productos:",bg="black",font="Gobold",foreground="white")
etiquetatex.grid(row=1,column=1)
dato1=tkinter.Label(ventana,bg="black",font="Gobold",foreground="white")
dato1.grid(row=6,column=0)
dato2=tkinter.Label(ventana,bg="black",font="Gobold",foreground="white")
dato2.grid(row=6,column=1)
dato3=tkinter.Label(ventana,bg="black",font="Gobold",foreground="white")
dato3.grid(row=6,column=2)
dato4=tkinter.Label(ventana,bg="black",font="Gobold",foreground="white")
dato4.grid(row=6,column=3)
dato5=tkinter.Label(ventana,bg="black",font="Gobold",foreground="white")
dato5.grid(row=6,column=4)
dato6=tkinter.Label(ventana,bg="black",font="Gobold",foreground="white")
dato6.grid(row=6,column=5)

#Creación de imagenes que describen los productos
image= Image.open("pringles.png")
image= image.resize((100,100),Image.ANTIALIAS)
img1= ImageTk.PhotoImage(image)

image2= Image.open("papas.jpg")
image2= image2.resize((100,100),Image.ANTIALIAS)
img2= ImageTk.PhotoImage(image2)

image3= Image.open("cocacola.png")
image3= image3.resize((100,100),Image.ANTIALIAS)
img3= ImageTk.PhotoImage(image3)

image4= Image.open("celular.png")
image4= image4.resize((100,100),Image.ANTIALIAS)
img4= ImageTk.PhotoImage(image4)

image5= Image.open("compu.png")
image5= image5.resize((100,100),Image.ANTIALIAS)
img5= ImageTk.PhotoImage(image5)

image6= Image.open("maxsteel.png")
image6= image6.resize((100,100),Image.ANTIALIAS)
img6= ImageTk.PhotoImage(image6)

image7= Image.open("uno.jpg")
image7= image7.resize((100,100),Image.ANTIALIAS)
img7= ImageTk.PhotoImage(image7)

image8= Image.open("camiseta.jpg")
image8= image8.resize((100,100),Image.ANTIALIAS)
img8= ImageTk.PhotoImage(image8)

image9= Image.open("tenis.png")
image9= image9.resize((100,100),Image.ANTIALIAS)
img9= ImageTk.PhotoImage(image9)

#Creación clase Padre, de aquí se derivan todos los productos
class Producto:
    def __init__(self,codigo,marca,precio,unidades):
        self.codigo=codigo
        self.marca=marca
        self.precio=precio
        self.unidades=unidades
    def mostrarinfo_Producto(self): #Función que muestra información general del producto
        etiqueta1= tkinter.Label(ventana,text="Codigo",width=10,bg="black",font="Gobold",foreground="white")
        etiqueta2= tkinter.Label(ventana,text="Marca",width=10,bg="black",font="Gobold",foreground="white")
        etiqueta3= tkinter.Label(ventana,text="Precio",width=10,bg="black",font="Gobold",foreground="white")
        etiqueta4= tkinter.Label(ventana,text="Unidades",width=10,bg="black",font="Gobold",foreground="white")
        etiqueta1.grid(row=5,column=0)
        etiqueta2.grid(row=5,column=1)
        etiqueta3.grid(row=5,column=2)
        etiqueta4.grid(row=5,column=3)
        dato1["text"]=self.codigo
        dato2["text"]=self.marca
        dato3["text"]=self.precio
        dato4["text"]=self.unidades
        
    
#Clase hijo
class Tecnologia():
    def __init__(self, garantia, color):
        self.garantia=garantia
        self.color=color
#Clase Nieto
class Dispositivo(Producto,Tecnologia):
    def __init__(self, codigo, marca, precio, unidades,ram):
        super().__init__(codigo, marca, precio, unidades)
        self.ram=ram
       
    def mostrarinfo(self):  #Esta función muestra los datos en especifico del nieto, la base se usa para todas las clases nietos
        super().mostrarinfo_Producto()
        etiqueta5= tkinter.Label(ventana,text="Ram",width=10,bg="black",font="Gobold",foreground="white")
        etiqueta5.grid(row=5,column=4)
        dato5["text"]=self.ram
    
        print(self.ram)
        
#Clase Nieto
class Accesorio(Producto,Tecnologia):
    def __init__(self, codigo, marca, precio, unidades,tipo_conexion):
        super().__init__(codigo, marca, precio, unidades)
        self.tipo_conexion=tipo_conexion
    def mostrarinfo(self):
        super().mostrarinfo_Producto()
        etiqueta5= tkinter.Label(ventana,text="Conexion",width=10,bg="black",font="Gobold",foreground="white")
        etiqueta5.grid(row=5,column=4)
        dato5["text"]=self.tipo_conexion
        print(self.tipo_conexion)
#------------ALIMENTO------------------
#Clase Hijo
class Alimento():
    def __init__(self, calorias):
        self.calorias=calorias

#Clase nieto
class Comida(Producto,Alimento):
    def __init__(self, codigo, marca, precio, unidades, gramos):
        super().__init__(codigo, marca, precio, unidades)
        self.gramos=gramos
    def mostrarinfo(self):
        super().mostrarinfo_Producto()
        etiqueta5= tkinter.Label(ventana,text="Gramos",width=10,bg="black",font="Gobold",foreground="white")
        etiqueta5.grid(row=5,column=4)
        dato5["text"]=self.gramos
        print(self.gramos)
#Clase nieto
class Bebidas(Producto,Alimento):
    def __init__(self, codigo, marca, precio, unidades, mililitros):
        super().__init__(codigo, marca, precio, unidades)
        self.mililitros=mililitros
    def mostrarinfo(self):
        super().mostrarinfo_Producto()
        etiqueta5= tkinter.Label(ventana,text="Mililitros",width=10,bg="black",font="Gobold",foreground="white")
        etiqueta5.grid(row=5,column=4)
        dato5["text"]=self.mililitros
        print(self.mililitros)
#------------JUGUETES------------------
#Clase Hijo
class Juguetes():
    def __init__(self, edadmin):
        self.edadmin=edadmin
#Clase nieto
class Muneco(Producto,Juguetes):
    def __init__(self, codigo, marca, precio, unidades, accesorios):
        super().__init__(codigo, marca, precio, unidades)
        self.accesorios=accesorios
    def mostrarinfo(self):
        super().mostrarinfo_Producto()
        etiqueta5= tkinter.Label(ventana,text="Accesorios",width=10,bg="black",font="Gobold",foreground="white")
        etiqueta5.grid(row=5,column=4)
        dato5["text"]=self.accesorios
        print(self.accesorios)
#Clase nieto
class JuegoMesa(Producto,Juguetes):
    def __init__(self, codigo, marca, precio, unidades, npiezas):
        super().__init__(codigo, marca, precio, unidades)
        self.npiezas=npiezas
    def mostrarinfo(self):
        super().mostrarinfo_Producto()
        etiqueta5= tkinter.Label(ventana,text="# de Piezas",width=10,bg="black",font="Gobold",foreground="white")
        etiqueta5.grid(row=5,column=4)
        dato5["text"]=self.npiezas
        print(self.npiezas)

#------------ROPA------------------
#Clase hijo
class Ropa():
    def _init_(self, talla):
        self.talla=talla

#Clase nieto
class Prenda(Producto,Ropa):
    def _init_(self, codigo, marca, precio, unidades, tipo):
        super()._init_(codigo, marca, precio, unidades)
        self.tipo=tipo

    def mostrarinfo(self):
        super().mostrarinfo_Producto()
        etiqueta5= tkinter.Label(ventana,text="Tipo",width=10,bg="black",font="Gobold",foreground="white")
        etiqueta5.grid(row=5,column=4)
        dato5["text"]=self.tipo
#Clae nieto
class Calzado(Producto,Ropa):
    def _init_(self, codigo, marca, precio, unidades, suela):
        super()._init_(codigo, marca, precio, unidades)
        self.suela=suela
    
    def mostrarinfo(self):
        super().mostrarinfo_Producto()
        etiqueta5= tkinter.Label(ventana,text="Suela",width=10,bg="black",font="Gobold",foreground="white")
        etiqueta5.grid(row=5,column=4)
        dato5["text"]=self.suela

#Función Polimorfismo, aquí se entragarán los objetos para que muestren su información
def polimorfismo(objeto):
    objeto.mostrarinfo()

#CREACIÓN DE OBJETOS.
Papitas=Comida('001', 'Pringles', 7000, 10, "300gr")       
Papitas.calorias=1000
print(Papitas.marca) 

Gaseosa=Bebidas('003', 'hinkCola', 2000, 20, "1500ml")
Gaseosa.calorias=200
print(Gaseosa.marca)

Papitas2=Comida('002', 'Margarita', 1500, 15, "100gr")       
Papitas2.calorias=300
print(Papitas2.marca) 



Celular=Dispositivo('007',"Huawei",400000,4,"4GB")
Celular.garantia=3000
Celular.color="Rojito"
print(Celular.color)

Teclado=Accesorio('008',"HP",10000,6,"USB")
Teclado.garantia=2
Teclado.color="Carbon"
print(Teclado.color)



Munequito=Muneco('004', 'Hasbro', 20000, 5, 3)
Munequito.edadmin=9
print(Munequito.marca)

Uno=JuegoMesa('005', 'Mattel', 35000, 2, 100)
Uno.edadmin=7
print(Uno.marca)

Camiseta=Prenda('010', 'Reebok', '55000', 5)
Camiseta.tipo="Deportivo"
Camiseta.talla='s'


Tennis=Calzado('011', 'Nike', '250.000$', '2')
Tennis.suela='de goma'
Tennis.talla='39'


#Creación de Botones, al presionarlos se llama a la función polimorfismo entregandoles el objeto que representa al botón
Boton1=tkinter.Button(image=img1,command= lambda: polimorfismo(Papitas)).grid(row=2,column=0)
Boton2=tkinter.Button(image=img2,command= lambda: polimorfismo(Papitas2)).grid(row=2,column=1)
Boton3=tkinter.Button(image=img3,command= lambda: polimorfismo(Gaseosa)).grid(row=2,column=2)
Boton4=tkinter.Button(image=img4,command= lambda: polimorfismo(Celular)).grid(row=3,column=0)
Boton5=tkinter.Button(image=img5,command= lambda: polimorfismo(Teclado)).grid(row=3,column=1)
Boton6=tkinter.Button(image=img6,command= lambda: polimorfismo(Munequito)).grid(row=3,column=2)
Boton7=tkinter.Button(image=img7,command= lambda: polimorfismo(Uno)).grid(row=4,column=0)
Boton8=tkinter.Button(image=img8,command= lambda: polimorfismo(Camiseta)).grid(row=4,column=1)
Boton9=tkinter.Button(image=img9,command= lambda: polimorfismo(Tennis)).grid(row=4,column=2)

#Método que permite que la ventana se cierre cuando se pida
ventana.mainloop()
class producto:
    def __init__(self, referencia, nombre, precio, descripcion):
        self.referencia = referencia
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion
     
class libro(producto):
    def __init__(self, referencia, nombre, precio, descripcion, autor, ISBN): #El ISBN es el codigo que traen por defecto los libros
        super().__init__(referencia, nombre, precio, descripcion)
        self.autor= autor
        self.ISBN = ISBN
    def __str__(self):
        return """\
Referencia: \t{}
Nombre: \t{}
PVP: \t\t{}
descripcion: \t{}
Autor: \t\t{}
ISBN \t\t{}""".format(self.referencia, self.nombre, self.precio, self.descripcion, self.autor,self.ISBN)


#Introduce todos los libros dentro del Try
try:
    Biblia = libro('000A', 'La Biblia', 50000, 'testamento sobre la existencia de Dios', 'Moises_desconocido','978-8428543231')
    Odisea = libro('001A', 'Odisea', 60000, 'Narra la historia del héroe griego Odiseo','Homero','978-84-670-5005-9')
    La_prehistoria = libro('0002A','La prehistoria ',65000,'Amplio paseo por el origen del ser humano','Cécile Benoist','978-8414016640')
    Abezooocéano = libro('0003A', 'Abezooocéano', 70000, 'Un abecedario con 29 poemas de animales marinos', 'Carlos Reviejo', '978-8413921051')
except TypeError:
    
    print("""
Recuerda dijitar todos los datos necesarios, ejemplo:,\n
Referencia:  \t\t000A
Nombre de la obra: \tLa Biblia
valor: \t\t\t50000
Descripcion \t\ttestamento sobre la existencia de Dios
Autor: \t\t\tMoises_Desconocido
ISBN: \t\t\tCodigo que tiene el libro
""")    
    
print("""\nBuenas tardes Usuario ha entrado en la base de datos de la biblioteca
      
Para añadir al invetario de la biblioteca un libro que alquilo solo ponga los siguientes datos en el codigo:
Nombre del libro = libro(referencia, nombre, precio, descripcion del libro, autor del libro, codigo ISBN)
""")
while True:
    try:
        print("""
1)Si quiere ver los libros en la biblioteca oprima el numero 1
2)Quiere ver los generos que hay? oprima 2
3) si quiere salir del programa """)
        respuesta = int(input('Seleccione: '))
        if respuesta == 1:
            lista = [Biblia, Odisea, La_prehistoria, Abezooocéano]
            for l in lista:
                print (l, '\n')
        elif respuesta == 2:
            pass 
        elif respuesta == 3:
            print('Esta saliendo del programa....')
            break
    except ValueError:
        print('La opcion que intenta dar es erronea')
    #ValueError
    
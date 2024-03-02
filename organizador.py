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
    Biblia = libro('001C', 'La Biblia', 50000, 'testamento sobre la existencia de Dios', 'Moises_desconocido','978-8428543231')
    Odisea = libro('001A', 'Odisea', 60000, 'Narra la historia del héroe griego Odiseo','Homero','978-84-670-5005-9')
    La_prehistoria = libro('0001E','La prehistoria ',65000,'Amplio paseo por el origen del ser humano','Cécile Benoist','978-8414016640')
    Abezooocéano = libro('0001E', 'Abezooocéano', 70000, 'Un abecedario con 29 poemas de animales marinos', 'Carlos Reviejo', '978-8413921051')
    El_Resplandor = libro('0001F','El Resplandor',40000,'REDRUM. Ésa es la palabra que Danny había visto en el espejo','Stephen King','978-9875668478')
    Doctor_sueño = libro('0002F','Doctor sueño',37050,'Secuela de {}'.format(El_Resplandor.nombre),'Stephen King','978-9585579286')
    Moby_Dick = libro ('001K', 'Moby Dick', 59000, 'Un capitán obsesionado con cazar a la ballena blanca, Moby Dick', 'Herman Melville', '978-8445071404')
    Los_miserables = libro ('001L', 'Los miserables', 54000, 'La historia de Jean Valjean y su lucha por la redención en la Francia del siglo XIX', 'Victor Hugo', '978-8423342698')
    La_iliada = libro ('001M', 'La Ilíada', 62000, 'Poema épico que narra los sucesos ocurridos durante la guerra de Troya', 'Homero', '978-8424931791')
    El_padrino = libro ('001O', 'El Padrino', 48000, 'Historia de la familia mafiosa Corleone, especialmente su líder, Don Vito Corleone', 'Mario Puzo', '978-0451205766')
    La_divina_comedia = libro ('001P', 'La Divina Comedia', 55000, 'Poema épico en el que se describe el viaje de Dante por el Infierno, el Purgatorio y el Paraíso', 'Dante Alighieri', '978-8424921280')
    Anna_Karenina = libro ('001Q', 'Anna Karenina', 51000, 'La historia de un triángulo amoroso entre Anna, su esposo Karenin y el oficial Vronsky', 'León Tolstói', '978-8491051681')
    El_retorno_del_rey = libro ('001R', 'El retorno del rey', 60000, 'Última parte de la trilogía de El Señor de los Anillos, donde se resuelve la guerra contra Sauron', 'J.R.R. Tolkien', '978-8445001364')
    La_metamorfosis = libro ('001S', 'La metamorfosis', 47000, 'Gregor Samsa se despierta una mañana y descubre que se ha transformado en un insecto gigante', 'Franz Kafka', '978-8437608427')
    El_extranjero = libro ('001T', 'El extranjero', 49000, 'La historia de Meursault, un hombre indiferente ante la vida y la muerte', 'Albert Camus', '978-8420674208')
    El_principito = libro ('001T', 'El Principito', 35000, 'Una narración poética sobre la amistad y la búsqueda de sentido en la vida', 'Antoine de Saint-Exupéry', '978-0307476121')
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
Se encuentra en el MENU:
1)Si quiere ver los libros en la biblioteca oprima el numero 1
2)Quiere ver los generos que hay? oprima 2
3)Si quiere salir del programa """)
        respuesta = int(input('Seleccione: '))
        if respuesta == 1:
            lista = [Biblia, Odisea, La_prehistoria, Abezooocéano,El_Resplandor,Doctor_sueño,Moby_Dick,Los_miserables, La_iliada, El_padrino,La_divina_comedia,Anna_Karenina,El_retorno_del_rey,La_metamorfosis,El_extranjero,El_principito]
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
    
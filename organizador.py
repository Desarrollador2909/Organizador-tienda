class producto:
    def __init__(self, referencia, nombre, pvp, descripcion):
        self.referencia = referencia
        self.nombre = nombre
        self.pvp = pvp
        self.descripcion = descripcion
    def __str__(self):
       return """\
Referencia: \t{}
Nombre: \t{}
PVP: \t\t{}
descripcion: \t{}""".format(self.referencia, self.nombre, self.pvp, self.descripcion)
        
class adorno(producto):
    pass

class alimento(producto):
    productor = ''
    distribuidor = ''
    def __str__(self):
        return """\
Referencia: \t{}
Nombre: \t{}
PVP: \t\t{}
descripcion: \t{}
Productor: \t{}
Distribuidor: \t{}""".format(self.referencia, self.nombre, self.pvp, self.descripcion, self.productor, self.distribuidor)

class libro(producto):
    autor = ''
    def __str__(self):
        return """\
Referencia: \t{}
Nombre: \t{}
PVP: \t\t{}
descripcion: \t{}
Autor: \t\t{}""".format(self.referencia, self.nombre, self.pvp, self.descripcion, self.autor)

adorno_vaso = adorno('000A','vaso adornado', 15000, 'vaso de porcelana adornado con arboles')

aceite = alimento('111B','aceite', 2000,'250 ML')
aceite.productor = 'la aceitera'
aceite.distribuidor = 'distribuidora SAS'

libro_cocina = libro('222C','Como usar aceite','35.000','Paso a paso')
libro_cocina.autor = 'desconocido'

lista = [adorno_vaso, aceite, libro_cocina]
for p in lista:
    print(p,'\n')
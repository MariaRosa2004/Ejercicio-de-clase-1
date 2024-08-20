class sistema():
    def __init__(self):
        self.__cedula= 0
        self.__nombre= ''
        self.__genero= ''
#Duda- ¿Por que no se asignan en el mismo init?
    #Setters
    def asignarNombre(self,nombre):
        self.__nombre=nombre
    def asignarCedula(self,cedula):
        self.__cedula=cedula
    def asignarGenero(self,genero):
        self.__genero=genero
    
    #Getters
    def VerNombre(self):
        return self.__nombre
    def VerCedula(self):
        return self.__cedula
    def VerGenero(self):
        return self.__genero
    
class paciente(sistema):
    def  __init__(self,nom, ced, gen, serv):
        sistema.__init__(self,nom, ced, gen)
        self.servicio=serv

class empleado(sistema):
    def  __init__(self,nom, ced, gen, turn):
        sistema.__init__(self,nom, ced, gen)
        self.turno=turn

class enfermeras(empleado):
    def  __init__(self,nom, ced, gen,turn,
                  rang):
        empleado.__init__(self,nom, ced, gen, turn)
        self.rango=rang

class medicos(empleado):
    def  __init__(self,nom, ced, gen, turn, esp):
        empleado.__init__(self,nom, ced, gen,turn)
        self.especialidad=esp

p1= paciente()
p2= paciente()
p1.asignarNombre('Maria Rosa')
p1.asignarCedula(1040570498)
p1.asignarGenero('Mujer')
print(p1.VerCedula())


#Ciclo menu
while True:
    pass

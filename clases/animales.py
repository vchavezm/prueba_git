
class Animal():

  def __init__(self,**args):
    self.nombreCientifico = args["nombreCientifico"] if "nombreCientifico" in args else " "

  def setNombreCientifico(self, nombreCientifico):
    self.nombreCientifico = nombreCientifico

  def setNombreComun(self,nombreComun):
    self.nombreComun = nombreComun

  def getNombreCientifico(self):
    return self.nombreCientifico

  def QueSoy(self):
    return "Soy un Animal"

class Perro(Animal):

  def __init__(self,**args):
    self.nombrePropio = args["nombrePropio"] if "nombrePropio" in args else " "

    self.nombreCientifico = "Caninus"

    self.nombreComun = "Perro"

  def setRaza(self, raza):
    self.raza = raza

  def getNombrePropio(self):
    return self.NombrePropio

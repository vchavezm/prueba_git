class Animal():

  def __init__(self,**args):
    self.nombreCientifico = args["nombreCientifico"] if "nombreCientifico" in args else

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
    self.nombrePropio = args["nombrePropio"] if "nombrePropio" in args else

  def setNombreCientifico(self):
    return "Canino"

  def setNombreComun(self):
    return "Perro"

  def setRaza(self,raza):
    self.raza = "Shnawzer"

  def getNombrePropio(self):
    return self.NombrePropio



class Gato(Animal):
  pass

class Puerco(Animal):
  pass

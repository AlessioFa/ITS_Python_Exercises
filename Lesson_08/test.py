from persona import Persona
from studente import Studente

# create a p object of Person's class
p: Persona = Persona('Alessio', 'Farallo', 29)

# visualize the info of P object

print(p)

studente1: Studente = Studente("Franco", "Trento",76, "5777788")

print(studente1)

# controllare se studente1 è istanza della classe studente 
# isistance(obj, Class) -> controlla se l ogggetto obj è istanza della classe Class


if isinstance(studente1, Studente):
    print("\n Studente1 è istanza della classe Studente")



if isinstance(studente1, Persona):
    print("\n Studente1 è istanza della classe studente ma è anche un oggetto della classe Persona")

if isinstance(p, Persona):
    print("\np è un oggetto della classe Persona")

# controllare se p è istanza della classe studente

if isinstance(p, Studente):
    print("\n p è istanza della classe persona ma anche istanza della classe studente")
else:
    print("\n p non è un oggetto della classe studente")

# controllare se una classe è sottoclasse di un altra
# controllo se sottoclasse di studente è sottoclasse di persona 
# issubClass ( vuole due classi , prima la sottoclasse poi la superclasse ), controlla se la classe Class1 è sottoclasse della classe Class2, nel caso affermativo ritorna true e in caso negativo ritorna false

if issubclass(Studente, Persona):
    print("Studente è sottoclasse della classe persona.")
else:
    print("Studente non è sottoclasse della classe persona.")

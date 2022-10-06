
###############################################################################
##                                                                           ##
## adt_test.py: Demonstraktion af Kompleks Abstraktion i Python sproget.     ##
##                                                                           ##
## Written by Keld Kondrup Jensen, Kondrup Invest ApS.                       ##
##                                                                           ##
## Time of creation: Fri Sep 23 20:21:34 2022 (by Keld Kondrup Jensen).      ##
##    Last modified: Fri Sep 23 20:21:34 2022 (by Keld Kondrup Jensen).      ##
##                                                                           ##
###############################################################################

###############################################################################
## Fælle funktioner til brug for Test af Simpel Python Abstraktion           ##
###############################################################################

from common import show_test, show_exit

global x

x = 2
print(x)

def is_same(adt_1, adt_2, id = ("ADT1", "ADT2", "Compare")):
    lead = f"{id[2]}: is_same({id[0]}, {id[1]})"

    if adt_1 is adt_2:
        print(lead, "=>", "They are identical ...")

    elif str(adt_1) == str(adt_2):
        print(lead, "=>", "They look the same ...")

    else:
        print(lead, "=>", "They are different ...")

    return adt_1 is adt_2 or adt_1 == adt_2

###############################################################################
##                                                                           ##
###############################################################################

## NILL Klasse: Kan og gør ingenting.
class Empty:
    pass

class Empty1():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(name, age)
    
    def __str__(self):
        return f"{self.name}({self.age})"

print(Empty1("dwad", 21))

## Bean Klasse: Aflæse og sætte hver enkelt attribut.
class Quale:
    noun = "Quale"

    def new(self, noun = "Token"):
        self.set(noun)

    def has(self, noun = ""):
        if self.noun == "":
            return False

        return noun == "" or self.noun == noun

    def set(self, noun):
        self.noun = noun
        return self

    def get(self):
        return self.noun
    
    def str(self):
        return self.get()

###############################################################################
## Test-cases vil løbende skal definere til eksperimentere med.              ##
###############################################################################

def test_once(label = "ADTonce", valid = True):
    ## Den enkeltstående test vi skal se effekt af igen og igen.
    ##  - label: Identifikation af det kørte test scenarie.
    ##  - valid: Flag for gældende status af test scenarie.

    ## Identificer det kørende test scenarie.
    if show_test(label + " start: ", valid):
    
        ## Lav kontrolleret, enkelt-stående test.
        pass

    ## Annoncer afslutning af test scenarie.
    return show_exit(label, valid)

def test_more(label = "ADTmore", valid = True):
    ## Det test-mønster vi skal se effekt af igen og igen.
    ##  - label: Identifikation af det kørte test scenarie.
    ##  - valid: Flag for gældende status af test scenarie.

    ## Identificer det kørende test scenarie.
    if show_test(label + " start: ", valid):

        ## Objekter: Instans af klasser
        hidden = Empty()
        ticket = Quale()
        entity = Quale()
        matter = entity

        ## Objekter: Hvordan ser de ud ?
        print("Hidden", type(hidden))
        print("Ticket", type(ticket))
        print("Entity", type(entity))
        print("Matter", type(matter))

        ## Lav nogle simple eksperimenter til sammenliging ...
        same_xy = is_same(ticket, entity, ("Ticket", "Entity", label))
        same_xz = is_same(ticket, matter, ("Ticket", "Matter", label))
        same_yz = is_same(entity, matter, ("Entity", "Matter", label))

        ## Objekter: Hvordan bruges de ?
        if entity.has("Quale") or matter.has():
            events = (entity.get(), entity.set("State").get(), matter.get())

            print("Bean events:", events[0], events[1], events[2])

        ## Spørgsmål: Er der nogle overraskelser her ... ?
        print(" ... også dette:", Quale.set(matter, "Topic").get())

        ## Lav nogle simple eksperimenter til sammenliging ...
        same_xy = is_same(ticket, entity, ("Ticket", "Entity", label))
        same_xz = is_same(ticket, matter, ("Ticket", "Matter", label))
        same_yz = is_same(entity, matter, ("Entity", "Matter", label))

    ## Annoncer afslutning af test scenarie.
    return show_exit(label, valid)

def test_case(label = "ADTtest", valid = True):
    ## Det test mønster vi skal se effekt af igen og igen. 
    ##  - label: Identifikation af det kørte test scenarie.
    ##  - valid: Flag for gældende status af test scenarie.

    ## Klasse variable: Tildeling af ny værdi
    Quale.noun = "Entry"
    
    ## Nogle varierende og demonstrative test-scenarier.
    ## return test_more(label, test_once(label, valid))
    valid = test_more(label, valid)

    ## Normal afslutning: Akkumuleret status a test-label.
    return valid

###############################################################################
## Vores hovedprogram (main loop).                                           ##
###############################################################################



my_once = test_once()
my_more = test_more()

my_case = test_case(label = "KKJtest")

#print(x)
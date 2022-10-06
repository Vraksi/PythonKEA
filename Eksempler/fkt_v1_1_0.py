        
###############################################################################
##                                                                           ##
## fkt_test.py: Demonstraktion af Simpel Abstraktion i Python sproget.       ##
##                                                                           ##
## Written by Keld Kondrup Jensen, Kondrup Invest ApS.                       ##
##                                                                           ##
## Time of creation: Fri Sep 23 21:45:02 2022 (by Keld Kondrup Jensen).      ##
##    Last modified: Fri Sep 23 21:45:02 2022 (by Keld Kondrup Jensen).      ##
##                                                                           ##
###############################################################################

###############################################################################
## Fælle funktioner til brug for Test af Simpel Python Abstraktion           ##
###############################################################################

from common import greetings

###############################################################################
## Test-cases vil løbende skal definere til eksperimentere med.              ##
###############################################################################

from common import show_test, show_exit

def test_once(label = "FKTonce", valid = True):
    ## Den enkeltstående test vi skal se effekt af igen og igen.
    ##  - label: Identifikation af det kørte test scenarie.
    ##  - valid: Flag for gældende status af test scenarie.

    ## Identificer det kørende test scenarie.
    init = show_test(label + " start: ", valid, str(greet_cnt))
    
    ## Lav kontrolleret, enkelt-stående test.
    show = greetings(show = init)

    ## Annoncer afslutning af test scenarie.
    exit = show_exit(label, show)
    
    ## Normal afslutning: Akkumuleret status a test-label.
    return exit

def test_more(label = "FKTmore", valid = True):
    ## Det test-mønster vi skal se effekt af igen og igen.
    ##  - label: Identifikation af det kørte test scenarie.
    ##  - valid: Flag for gældende status af test scenarie.

    ## Identificer det kørende test scenarie.
    valid = show_test(label + " start: ", valid, greet_cnt)

    ## Lav en sekvens af sammenhørende tests.
    if greetings("Hello", "world", show = valid):
        ## Flere varianter af funktionskald.
        valid = greetings("Bienvenu", "mes amis")
        valid = greetings("Hej", "venner")

        ## Mulig brug ved default parameter.
        if valid and greetings() and greetings("Scary"):
            valid = greetings(actor = "everybody")
        
    ## Demonstrer nu også brug af resultat fra kald ...
    count = cnt_greet("Goodbye", "I'm retiring", show = valid)
    valid = greetings(" ...", f"after {count} greets", "", count > 0)

    ## Annoncer afslutning af test scenarie.
    exit = show_exit(label, valid)
    
    ## Normal afslutning: Akkumuleret status a test-label.
    return exit

def test_case(label = "FKTtest", valid = True):
    ## Det test mønster vi skal se effekt af igen og igen. 
    ##  - label: Identifikation af det kørte test scenarie.
    ##  - exit: Flag for gældende status af test scenarie.

    ## Nogle varierende og demonstrative test-scenarier.
    return test_more(label, test_once(label, valid))

###############################################################################
## Vores hovedprogram (main loop).                                           ##
###############################################################################

my_test = test_once()
my_next = test_more()

my_case = test_case(label = "KKJtest")


###############################################################################
## Fælle funktioner til brug for Test af Simpel Python Abstraktion           ##
###############################################################################

## Global variable: Optæller Tæller  til brug for procedure ...
greet_cnt = 0

## Simpel Python funktion som udskriver en hilsen.
def prt_greet(greet = "Hello", actor = "world", valid = True):
    if valid:
        print(greet, actor)

    ## Annoncer succesfull udskrivning ...
    return valid

## Simpel Python procedurer som optæller hilsner.
def cnt_greet(greet = "Hello", actor = "world", valid = True):
    global greet_cnt            ## Brug global variabel nu i lokalt scope.

    ## Bemært brug af formattering og sammensætning af tekst ...
    if prt_greet(f"{greet_cnt + 1}. {greet}", actor, valid):
        greet_cnt += 1

    ## Annoncer antallet af udskrevne hilsner.
    return greet_cnt;

## Wrapper funktion til kontrol af test-case.
def greetings(greet = "Hello", actor = "world", pick = "", valid = True):
    ## Det interface vi løbende vi justere i udvikling af test scenarier.
    ##  - pick: Selektor til valg af ønsket funktionalitet.
    ##  - valid: Flag som skal være sat for at opnå hilsen.

    ## Kald target funktion (nu med valgmulighed)
    if pick == "func":
        exit = prt_greet(greet, actor, valid)

    elif pick == "proc":
        exit = greet_cnt < cnt_greet(greet, actor, valid)

    elif pick == "" and valid is True:
        exit = greetings(greet, actor, "proc")

    else:
        exit = greetings(f"Bad use ({pick}),", "you fool !")
    
    ## Normal afslutning: Giv status for realiseret hilsen.
    return exit

###############################################################################
## Test-cases vil løbende skal definere til eksperimentere med.              ##
###############################################################################

## Global beskrivelse af eventuel erkendt fejl.
error = "Unknown"

def show_test(case, init, qual = ""):
    return prt_greet(case, qual, init)

def show_exit(case, exit):
    if exit is True:
        print("...", case, "passed sucessfully\n")
    else:
        print("...", case, f"failed ({error})\n")

    return exit

def test_once(label = "FKTonce", valid = True):
    ## Den enkeltstående test vi skal se effekt af igen og igen.
    ##  - label: Identifikation af det kørte test scenarie.
    ##  - exit: Flag for gældende status af test scenarie.

    ## Identificer det kørende test scenarie.
    init = show_test(label + " start: ",  valid, greet_cnt)

    ## Lav kontrolleret, enkelt-stående test.
    show = greetings(init)

    ## Annoncer afslutning af test scenarie.
    exit = show_exit(label, show)
    
    ## Normal afslutning: Akkumuleret status a test-label.
    return exit

def test_more(label = "FKTmore", valid = True):
    ## Det test-mønster vi skal se effekt af igen og igen.
    ##  - label: Identifikation af det kørte test scenarie.
    ##  - exit: Flag for gældende status af test scenarie

    ## Identificer det kørende test scenarie.
    valid = show_test(label + " start: ", greet_cnt, valid)

    ## Lav en sekvens af sammenhørende tests.
    if greetings("Hello world", valid):		# Vis (og ret) effekt af syntax fejl.
        ## Flere varianter af funktionskald.
        valid = greetings("Bienvenu", "mes amis")
        valid = greetings("Hej", "venner")

        ## Mulig brug ved default parameter.
        if valid and greetings() and greetings("Scary"):
            valid = greetings(actor = "everybody")
        
    ## Demonstrer nu også brug af resultat fra kald ...
    count = cnt_greet("Goodbye", "I'm retiring", valid)
    valid = greetings(" ...", f"after {count} greets", "func", valid)

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

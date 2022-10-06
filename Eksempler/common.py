
###############################################################################
##                                                                           ##
## common.py: 
##                                                                           ##
## Written by Keld Kondrup Jensen, Kondrup Invest ApS.                       ##
##                                                                           ##
## Time of creation: Fri Sep 23 21:47:00 2022 (by Keld Kondrup Jensen).      ##
##    Last modified: Fri Sep 23 21:47:00 2022 (by Keld Kondrup Jensen).      ##
##                                                                           ##
###############################################################################

###############################################################################
## Simmple Python Abstractions validated by Test-scenaries ...               ##
###############################################################################

## Global variable: Optæller Tæller til brug for procedure ...
greet_cnt = 0

## Simpel Python funktion som udskriver en hilsen.
def prt_greet(greet = "Hello", actor = "world", show = True):
    if show is True:
        print(greet, actor)

    ## Annoncer succesfull udskrivning ...
    return show

## Simpel Python procedurer som optæller hilsner.
def cnt_greet(greet = "Hello", actor = "world", show = True):
    global greet_cnt            ## Brug global variabel nu i lokalt scope.

    ## Bemært brug af formattering og sammensætning af tekst ...
    if prt_greet(f"{greet_cnt + 1}. " + greet, actor, show):
        greet_cnt += 1

    ## Annoncer antallet af udskrevne hilsner.
    return greet_cnt;

## Wrapper funktion til kontrol af test-case.
def greetings(greet = "Hello", actor = "world", pick = "", show = True):
    ## Det interface vi løbende vi justere i udvikling af test scenarier.
    ##  - pick: Selektor til valg af ønsket funktionalitet.
    ##  - valid: Flag som skal være sat for at opnå hilsen.

    ## Kald target funktion (nu med valgmulighed)
    if pick == "func":
        exit = prt_greet(greet, actor, show)

    elif pick == "proc":
        exit = greet_cnt < cnt_greet(greet, actor, show)

    elif pick == "" and show is True:
        exit = greetings(greet, actor, "proc")

    else:
        ## pick = f"{pick}(greet = {greet}, actor = {actor}, show = {show})"
        exit = greetings(f"Bad use ({pick}),", "you fool !")
    
    ## Normal afslutning: Giv status for realiseret hilsen.
    return exit

###############################################################################
## Fælle funktioner til brug for Test af Simpel Python Abstraktion           ##
###############################################################################

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
## Simple Python Abstractions utilizing validated behaviour ...              ##
###############################################################################

## Global beskrivelse af eventuel erkendt fejl.
error = "Unknown"

def show_test(case, init = True, qual = ""):
    if init == True and qual == "":
        qual = str(greet_cnt)

    return greetings(case, qual, show = init)

def show_exit(case, exit):
    if exit is True:
        print("...", case, "passed sucessfully\n")
    else:
        print("...", case, f"failed ({error})\n")

    return exit

###############################################################################
##                                                                           ##
###############################################################################

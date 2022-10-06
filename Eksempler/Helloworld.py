x = 2
list = [1,2,3,4,5,9]
tuple = ("varm", "kold", "dk", "dk2", "dk")
set = {"bananer", "æbler", "ananas"}
dictionary = {
    "bananer": "gul",
    "pære": "grøn",
    "æbler": "rød"
}
list.append(584)
list.index(2)

def printlistandtuple():
    list.remove(5)
    for item in list:
        print(item)
    print(list.index(584))


    for item in tuple:
        print(item)
    print(tuple[-1])

    set.add("æblers")
    for item in set:
        print(item)
    #print(dictionary["pære"])

printlistandtuple()

class myclass:
    def __init__(self, age):
        self.age = age
    x = 2

pl = myclass(2992)
print(pl.x)
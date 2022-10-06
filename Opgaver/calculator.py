import re



class Analyse():

    def __init__(self):
        pass

    def SplitElements(self, math):
        regex = "([0-9]+)([+*-/])"


        print("my regex: " + regex)

        #math = "1+12-55*8+3+7/46"

        split = re.split(regex, math)

        while ('' in split):
            split.remove('')
            
        









        return(split)


class Calculator():
    def __init__(self):
        pass

    def Calculate(self, split):
        result = Calculator.Multiply(self, split)
        result = Calculator.Divide(self, result)
        result = Calculator.Subtract(self, result)
        temp = Calculator.Add(self, result)
        print(temp)
        return(temp)

    def Divide(self, split):
        count = 0
        for val in split:
            if(val == "/"):
                temp = int(int(split[count - 1]) / int(split[count + 1]))
                split[count - 1] = str(temp)
                list(split.pop(count))
                list(split.pop(count))
                Calculator.Divide(self, split)
                pass
            count = count + 1  
        return split  

    def Multiply(self, split):
        count = 0
        for val in split:
            if(val == "*"):
                split[count - 1] = str(int(split[count - 1]) * int(split[count + 1]))
                list(split.pop(count))
                list(split.pop(count))
                Calculator.Multiply(self, split)
                pass
            count = count + 1  
        return split  

    def Add(self, split):
        count = 0
        for val in split:
            if(val == "+"):
                split[count - 1] = int(split[count - 1]) + int(split[count + 1])
                list(split.pop(count))
                list(split.pop(count))
                Calculator.Add(self, split)
                pass
            count = count + 1  
        return split  

    def Subtract(self, split):
        count = 0
        for val in split:
            if(val == "-"):
                split[count - 1] = str(int(split[count - 1]) - int(split[count + 1]))
                list(split.pop(count))
                list(split.pop(count))
                Calculator.Subtract(self, split)
                pass
            count = count + 1  
        return split  


class WriteToFIle():
    
    def __init__(self):
        pass
    
    def writeout(self, x):
        file = open("udregninger.txt", "wbr")
        file.write(str("${x} \n").encode("utf8", "ignore"))
        file.close()
        print(file.read())
        pass


file = WriteToFIle()
Analisys = Analyse()
Calcu = Calculator()

math = "2-3*6+3+1+2/2+3+2"
file.writeout(math)


result = Analisys.SplitElements(math)
print(Calcu.Multiply(result))
Calcu.Calculate(result)
print("")




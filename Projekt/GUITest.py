from turtle import tilt
import easygui as gui


#gui.msgbox(msg="Hello", title="Im the title", ok_button="Click me")
colors = ["red", "yellow", "green"]

temp = gui.indexbox(
    msg="Hvad er din farve",
    title="Temp1",
    choices=(colors),
)

temp1 = gui.enterbox(
    msg="hva så",
    title="hvem så"
)

print(temp1)

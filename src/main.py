from src import *
from src.gui.gui import Gui


while True:
    event, values = Gui.window.read()# type: ignore
    print(event,values)

    if event in (sg.WIN_CLOSED,'Exit'):
        break

Gui.window.close()
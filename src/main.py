from src import *
from src.gui.gui import Gui
from src.vars.basic import about


while True:
    event, values = Gui.window.read()# type: ignore
    print(event,values)

    if event in (sg.WIN_CLOSED,'Exit'):
        break
    
    if event == 'About':
        sg.popup_ok(about,title='About')

Gui.window.close()
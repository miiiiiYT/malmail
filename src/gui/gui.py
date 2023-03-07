"""
    Script responsible for building the GUI.
"""

from src import *

sg.theme('BlueMono')
class Gui:
    with open('data/accounts.json') as f:
        accounts = json.load(f)
        f.close()

    menu = [['MalMail', ['About','Settings','Exit']],['Tools',['Spam',['1','2']]],['Accounts',['Add', 'Show']]]

    account_lay = [
        [sg.Text('Accounts')],
    ]
    for acc in accounts:
        i = 0
        account_lay.append(
            [sg.Radio(f"{acc}",'account',key=f'-ACC-{accounts[acc]["id"]}-',enable_events=True)]#type: ignore
        )
        i=i+1

    messages_lay = [
        sg.Listbox(values=['Listbox 1', 'Listbox 2', 'Listbox 3'])
    ]
    content_lay = [
        sg.Multiline('Content')
    ]
    tools_lay = [
        [
        sg.Text('Tools')
        ]
    ]

    layout = [
        [sg.Menu(menu)],
        [
            sg.Column(account_lay,expand_x=True,expand_y=True,),
            sg.VSeparator(),
            sg.Column([messages_lay,[sg.HSeparator()],content_lay],expand_x=True,expand_y=True,),
            sg.VSeparator(),
            sg.Column(tools_lay,expand_x=True,expand_y=True,),
        ]
    ]

    w,h = sg.Window.get_screen_size()
    w,h = math.floor(w/2),math.floor(h/2)
    window = sg.Window('MalMail 0.0.1', layout, resizable=True, finalize=True, size=(w,h))
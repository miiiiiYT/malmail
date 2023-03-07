from src import *

sg.theme('BlueMono')
class Gui:
    menu = [['MalMail', ['About','Settings','Exit']],['Tools',['Spam',['1','2']]]]

    account_lay = [
        [
            sg.Text('Accounts')
        ]
    ]
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

    window = sg.Window('MalMail 0.0.1', layout, resizable=True, finalize=True)
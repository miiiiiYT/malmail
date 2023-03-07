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

# while True:
#     event, values = window.read()# type: ignore
#     print(event,values)

#     if event in (sg.WIN_CLOSED,'Exit'):
#         break

# window.close()


# import PySimpleGUI as sg

# layout = [[sg.Text('Item 1', background_color='red'),
#             sg.VSep(),
#             sg.Column([[sg.Text('Item 2', background_color='yellow')],
#                 [sg.Text('Item 3', background_color='green')]], background_color='blue'),
#             sg.VSep(),sg.Text('Item 4', background_color='purple')]]

# window = sg.Window('Nested Layout', layout)
# event, values = window.read()
# window.close()

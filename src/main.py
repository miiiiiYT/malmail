from src import *
from src.gui.gui import Gui
from src.vars.basic import about
from src.functions.accounts import Account


while True:
    event, values = Gui.window.read()# type: ignore
    print(event,values)

    # Exit on exit
    if event in (sg.WIN_CLOSED,'Exit'):
        break
    
    # About page
    if event == 'About':
        sg.popup_ok(about,title='About')
    
    # Accout management
    if event.startswith('-ACC-'):
        pass

    if event == "Add":
            layout = [
                [sg.Text('Account Creation')],
                [sg.Text('Email: '),sg.Input(key='-ADD-EMAIL-')],
                [sg.Text('IMAP-Address: '),sg.Input(key='-ADD-IMAP-')],
                [sg.Text('IMAP-Port: '),sg.Input('993',key='-ADD-IMAP-PORT-')],
                [sg.Text('SMTP-Adress: '),sg.Input(key='-ADD-SMTP-')],
                [sg.Text('SMTP-Port: '),sg.Input('587',key='-ADD-SMTP-PORT-')],
                [sg.Text('Password: '),sg.Input(key='-ADD-PASSWORD-', password_char='\u2022')],
                [sg.Push(),sg.OK(),sg.Cancel()]
            ]
            acc_creator_event, acc_creator_values = sg.Window('Create Account - MalMail',layout,modal=True).read(close=True)#type: ignore
            if acc_creator_event == 'OK':
                Account(email=acc_creator_values['-ADD-EMAIL-'],imapaddr=acc_creator_values['-ADD-IMAP-'],smtpaddr=acc_creator_values['-ADD-SMTP-'],password=acc_creator_values['-ADD-PASSWORD-'],imapport=acc_creator_values['-ADD-IMAP-PORT-'],smtpport=acc_creator_values['-ADD-SMTP-PORT-']).create()

    if event == 'Add-Acc':
        print(event)

    if event == 'Add Account':
        print(event)

    if event == "List":
        pass

    print(event)

Gui.window.close()
from src import *

def get_all_accounts() -> dict:
    with open('data/accounts.json') as f:
        accounts = json.load(f)
        f.close()
    return accounts

def write_accounts(accounts:dict) -> None:
    with open('data/accounts.json','w') as f:
        json.dump(accounts,f)
        f.close()

def get_next_id() -> int:
    id = 0
    data = get_all_accounts()
    for item in data:
        if data[item]['id'] > id:
            id = data[item]['id']
    return id+1


class Account():
    def __init__(self,email:str,password="",imapaddr="",smtpaddr="",imapport:int=993,smtpport:int=587,):
        """
            Only provide email when trying to load from accounts.json, or provide everything in- or excluding the ports to create a new account
        """
        if email and not password or not imapaddr or not smtpaddr:
            data = get_all_accounts()
            if email in data:
                self.email = data[email]['email']
                self.imapaddr = data[email]['imap-addr']
                self.imapport = data[email]['imap-port']
                self.smtpaddr = data[email]['smtp-addr']
                self.smtpport = data[email]['smtp-port']
                self.password = data[email]['password']
            else:
                raise KeyError('The given email does not exist')
        elif email and password and imapaddr and smtpaddr:
            self.email = email
            self.imapaddr = imapaddr
            self.imapport = imapport
            self.smtpaddr = smtpaddr
            self.smtpport = smtpport
            self.password = password
        else:
            raise ValueError('Arguments were provided incorrectly.')
    
    def create(self):
        data = get_all_accounts()
        
        _account = self.export()
        _account['id'] = get_next_id()

        data[self.email] = _account

        write_accounts(data)

    def export(self) -> dict:
        return {
            'email':self.email,
            'imap-addr':self.imapaddr,
            'imap-port':self.imapport,
            'smtp-addr':self.smtpaddr,
            'smtp-port':self.smtpport,
            'password':self.password,
        }
    
    def delete(self):
        data = get_all_accounts()
        try:
            data.pop(self.email)
        except KeyError as e:
            raise KeyError('This email was not saved!').with_traceback(e.__traceback__)
        
        write_accounts(data)
        del self

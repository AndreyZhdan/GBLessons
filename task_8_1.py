import re

def email_parse(mail):
    try:
        dct = {}
        RE = re.compile('^([a-z0-9]+)@([a-z]+.[a-z]+$)', re.IGNORECASE)
        lst = list(RE.findall(mail)[0])
        dct.update({"username": lst[0], "domain": lst[1]})
        return dct
    except IndexError:
        print("not valid email")

str_mail = 'soMeone@geekbrains.ru'

print(email_parse(str_mail))
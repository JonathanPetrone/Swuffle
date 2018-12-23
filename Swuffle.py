class Textinputs:

    def __init__(self):
        self.textinput = textinput

    def textinput(): # funktionen för textinsamling av användaren
        usertext = input("Insert text here:")
        userlist = usertext.replace(';', ' ').replace(',', ' ').replace('.', ' ').replace(':', ' ').split()
        print(userlist)

    # spara insamlad text av användare i en ny textfil
    # se till att ord som väljs ur texten kan bli utbyttna mot rätt ord som använderen matar in (placeholder?)

Textinputs.textinput()

from tools.tools import Tool


class ToolsMenu:
    def __init__(self, title):
        self.title = title

    def creer(self):
        nom = input("Nom du nouvel outil: ")
        description = input("Description du nouvel outil")

        # créer un outils avec les infos recues
        new_tool = Tool(name=nom, description=description)
        new_tool.save()

        return self

    def quit(self):
        print("Good bye")

    def display(self):
        print("1. Créer un nouvel outil\n" "2. Quitter\n")
        reponse = input("Quel est votre choix ? ")
        if reponse == "1":
            return self.creer()
        elif reponse == "2":
            return self.quit()
        else:
            return self

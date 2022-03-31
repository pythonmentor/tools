from tools.menus.tools import ToolsMenu


class HomeMenu:
    def __init__(self, title):
        self.title = title

    def quit(self):
        print("Goodbye")

    def manage_tools(self):
        return ToolsMenu(title="Gestion des outils")

    def display(self):
        print("1. Gérer les outils\n" "2. Quitter\n\n")
        reponse = input("Quel est votre choix ? ")
        if reponse == "1":
            return self.manage_tools()
        elif reponse == "2":
            return self.quit()
        else:
            return self

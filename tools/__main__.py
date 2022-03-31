from tools.menus.home import HomeMenu


def main():
    menu = HomeMenu(title="Accueil")
    while menu is not None:
        menu = menu.display()

    print("C'est fini")


main()

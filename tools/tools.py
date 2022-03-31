from tools.database import db


class Tool:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def save(self):
        """Sauvegarde l'outils"""
        print(f"sauvegarde de {self.name}")
        db.insert({"name": self.name, "description": self.description})


class Delivery:
    ...


class User:
    def __init__(self, name, prenom, email):
        self.name = name
        self.prenom = prenom
        self.email = email

    def save(self):
        ...

    def search(self):
        ...

    def send_email(self, subject, message):
        ...


class Client:
    ...

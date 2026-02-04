import json
from datetime import datetime

class Figurine:
    """Classe représentant une figurine de collection"""
    
    def __init__(self, nom, serie, prix, date_acquisition=None, etat="En boîte"):
        self.nom = nom
        self.serie = serie
        self.prix = prix
        self.etat = etat
        
        # Gestion de la date : conversion si c'est une chaîne, sinon date actuelle
        if isinstance(date_acquisition, str):
            try:
                self.date_acquisition = datetime.strptime(date_acquisition, '%Y-%m-%d')
            except ValueError:
                self.date_acquisition = datetime.now()
        else:
            self.date_acquisition = date_acquisition or datetime.now()

    def changer_etat(self, nouvel_etat):
        """Met à jour l'état de la figurine"""
        self.etat = nouvel_etat
        print(f"✓ État de '{self.nom}' mis à jour : {self.etat}")

    def afficher_details(self):
        """Affiche les détails complets d'une figurine"""
        date_str = self.date_acquisition.strftime('%d-%m-%Y')
        print(f"[{self.nom}] - Série: {self.serie} | Prix: {self.prix}€ | État: {self.etat} | Acquis le: {date_str}")

class CollectionFigurines:
    """Classe pour gérer l'ensemble de la collection"""
    
    def __init__(self):
        self.liste_figurines = []

    def ajouter(self, figurine):
        self.liste_figurines.append(figurine)
        print(f"✓ Figurine '{figurine.nom}' ajoutée à la collection !")

    def supprimer(self, nom):
        initial_count = len(self.liste_figurines)
        self.liste_figurines = [f for f in self.liste_figurines if f.nom.lower() != nom.lower()]
        if len(self.liste_figurines) < initial_count:
            print(f"✓ Figurine '{nom}' retirée avec succès.")
        else:
            print(f"✗ Aucun objet nommé '{nom}' trouvé.")

    def rechercher(self, nom):
        """Recherche une figurine par son nom"""
        for f in self.liste_figurines:
            if f.nom.lower() == nom.lower():
                return f
        return None

    def afficher_tout(self):
        if not self.liste_figurines:
            print("\nLa collection est actuellement vide.")
            return
        
        print(f"\n{'='*60}")
        print(f"MA COLLECTION ({len(self.liste_figurines)} figurines)")
        print(f"{'='*60}")
        for i, f in enumerate(self.liste_figurines, 1):
            print(f"{i}. ", end="")
            f.afficher_details()

# --- Fonctions de l'Interface (Menu) ---

def menu_ajouter(collection):
    print("\n--- NOUVELLE FIGURINE ---")
    nom = input("Nom de la figurine : ")
    serie = input("Série / Franchise : ")
    while True:
        try:
            prix = float(input("Prix d'achat (€) : "))
            break
        except ValueError:
            print("Erreur : Veuillez entrer un nombre valide (ex: 25.50)")
    
    date_saisie = input("Date d'acquisition (AAAA-MM-JJ) [Entrée pour aujourd'hui] : ")
    nouvelle = Figurine(nom, serie, prix, date_saisie if date_saisie else None)
    collection.ajouter(nouvelle)

def menu_rechercher_modifier(collection):
    print("\n--- RECHERCHE & MODIFICATION ---")
    nom = input("Entrez le nom de la figurine : ")
    f = collection.rechercher(nom)
    
    if f:
        print("\nFigurine trouvée :")
        f.afficher_details()
        print("\nQue souhaitez-vous faire ?")
        print("1. Modifier l'état")
        print("2. Retour au menu")
        choix = input("Votre choix : ")
        
        if choix == "1":
            etats = ["En boîte", "Exposée", "Rangement (Stock)", "En réparation"]
            print("\nChoisissez le nouvel état :")
            for i, e in enumerate(etats, 1):
                print(f"{i}. {e}")
            try:
                idx = int(input("Numéro : ")) - 1
                if 0 <= idx < len(etats):
                    f.changer_etat(etats[idx])
                else:
                    print("Choix invalide.")
            except ValueError:
                print("Entrée invalide.")
    else:
        print(f"✗ La figurine '{nom}' n'existe pas dans la collection.")

def main():
    ma_collection = CollectionFigurines()
    
    # Quelques données initiales pour tester
    ma_collection.ajouter(Figurine("Goku Super Saiyan", "Dragon Ball Z", 35.99))
    ma_collection.ajouter(Figurine("Luffy Gear 5", "One Piece", 42.00))

    while True:
        print("\n" + "="*50)
        print(" GESTIONNAIRE DE COLLECTION ".center(50, "="))
        print("="*50)
        print("1. Ajouter une figurine")
        print("2. Supprimer une figurine")
        print("3. Afficher la collection")
        print("4. Rechercher / Modifier l'état")
        print("5. Quitter")
        
        choix = input("\nVotre choix : ")

        if choix == "1":
            menu_ajouter(ma_collection)
        elif choix == "2":
            nom_suppr = input("Nom de la figurine à supprimer : ")
            ma_collection.supprimer(nom_suppr)
        elif choix == "3":
            ma_collection.afficher_tout()
        elif choix == "4":
            menu_rechercher_modifier(ma_collection)
        elif choix == "5":
            print("\nFermeture du programme. Bonne collection !")
            break
        else:
            print("\nChoix non reconnu, réessayez.")

if __name__ == "__main__":
    main()
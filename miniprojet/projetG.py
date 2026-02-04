import os
import sys

# Fonction pour nettoyer la console (Windows ou Mac/Linux)
def nettoyer_ecran():
    os.system('cls' if os.name == 'nt' else 'clear')

try:
    # On importe la fonction main du fichier principal
    from gestor_figurinas import main
except ImportError:
    print("❌ Erreur : Impossible de trouver le fichier 'gestor_figurinas.py'.")
    print("Vérifiez que les deux fichiers sont dans le même dossier.")
    sys.exit()

def demarrer():
    nettoyer_ecran()
    print("="*50)
    print(" BIENVENUE DANS VOTRE GESTIONNAIRE ".center(50, " "))
    print("="*50)
    
    reponse = input("\nVoulez-vous lancer le gestionnaire maintenant ? (o/n) : ").lower()

    if reponse in ['o', 'oui', 'y', 'yes']:
        nettoyer_ecran()
        main()
    else:
        print("\n👋 À bientôt ! Votre collection reste précieusement gardée.")

if __name__ == "__main__":
    demarrer()

import tkinter
from tkinter import simpledialog
import generationFichierBiling
import generationFichierInfra
import generationFichierReseau
import generationFichierSecurity
import audit_NPS


def demandeActionExecuter() :
    root = tkinter.Tk()
    root.withdraw()
    try :
        choix = simpledialog.askinteger("Choix d'application",
        "Quelle action voulez-vous menez                ? :\n"
        "\n"
        "1 - Update Base Ressources \n"
        "\n"
        "2 - Update Base AMS \n"
        "\n"
        "3 - Update Infos Radius \n"
        "\n"
        "4 - Update Infos BSCS \n"
        "\n"
        "5 - Update Base Unifiée \n"
        "\n"
        "6 - Croisement Fichier Externe \n")
        
        if choix == 1 :
            print("Exécution de Update Base Ressources...")
            generationFichierInfra.createRessourcesLocalHost()
            print("Vos données sont prêtes")
        elif choix == 2 :
            print("Exécution de Update Base AMS...")
            generationFichierReseau.create_ams_database()
            print("Vos données sont prêtes")
        elif choix == 3 :
            print("Exécution de Infos Radius...")
            generationFichierSecurity.createRessourcesSecurity()
            print("Vos données sont prêtes")
        elif choix == 4 :
            print("Exécution de Infos BSCS...")
            generationFichierBiling.createRessourcesbiling
            print("Vos données sont prêtes")
        elif choix == 5 :
            print("Exécution de Base Unifiée...")
            createFichierDataUnified()
            print("Vos données sont prêtes")
        elif choix == 6 :
            print("Exécution de Fichier Externe...")
            audit_NPS.createConsolidedFile()
            print("Vos données sont prêtes")
    except ValueError :
        print("Erreur : Veuillez entrer un numéro valide.")

def createFichierDataUnified() :
    AMS = generationFichierReseau.create_ams_database()
    SI = generationFichierInfra.createRessourcesLocalHost()
    BSCS = generationFichierBiling.createRessourcesbiling()
    AAA = generationFichierSecurity.createRessourcesSecurity()
    EXT = audit_NPS.createConsolidedFile()
    
    UNI = AMS.merge(SI, how = 'left').merge(BSCS, how = 'left').merge(AAA, how = 'left')

if __name__ == "__main__":
   demandeActionExecuter()
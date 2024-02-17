import tkinter
from tkinter.simpledialog import SimpleDialog
import generationFichierBiling
import generationFichierInfra
import generationFichierReseau
import generationFichierSecurity
import fonctions_generiques

def demandeActionExecuter() :
    root = tkinter.Tk()
    root.withdraw()
    try :
        choix = SimpleDialog.askinteger("Choix d'application",
        "Quelle action voulez-vous menez                ? :\n"
        "\n"
        "1 - Update Infos Ressources \n"
        "\n"
        "2 - Update Infos AMS \n"
        "\n"
        "3 - Update Infos Radius \n"
        "\n"
        "4 - Update Infos BSCS \n"
        "\n"
        "5 - Update Base Unifiée \n"
        "\n"
        "6 - Croisement avec Fichier Externe \n")
        
        if choix == 1 :
            print("Exécution de Update Données AMS ...")
            generationFichierReseau.create_ams_database()g
            print("Vos données sont prêtes")
        elif choix == 2 :
            print("Exécution de Update Données Ressources ...")
            generationFichierInfra.createRessourcesLocalHost()
            print("Vos données sont prêtes")
        elif choix == 3 :
            print("Exécution de Données Radius ...")
            generationFichierSecurity.createRessourcesSecurity()
            print("Vos données sont prêtes")
        elif choix == 4 :
            print("Exécution de Données BSCS...")
            generationFichierBiling.createRessourcesbiling()
            print("Vos données sont prêtes")
        elif choix == 5 :
            print("Exécution de Données Unifiée...")
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
    
    UNI = AMS.merge(SI, how = 'left').merge(BSCS, how = 'left').merge(AAA, how = 'left')
    UNI.reset_index(inplace = True, drop = True)
    print ('Sauvegarde des données')
    fonctions_generiques.sauvegardeFichier(UNI,  saveFile+ 'UnitedDatabase.xlsx')
    
def createFichierDataAnalyst() :
    AMS = generationFichierReseau.create_ams_database()
    SI = generationFichierInfra.createRessourcesLocalHost()
    BSCS = generationFichierBiling.createRessourcesbiling()
    AAA = generationFichierSecurity.createRessourcesSecurity()
    EXT = audit_NPS.createConsolidedFile()
    
    UNI = AMS.merge(SI, how = 'left').merge(BSCS, how = 'left').merge(AAA, how = 'left')
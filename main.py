from pathlib import Path
import sys
import pandas
import fonctions_generiques
import traitement_fichiers

#print(dir(traitement_fichiersLocalHost))

def create_ams_database():
    dataBase_AMS = pandas.DataFrame()
    
    listePath = traitement_fichiers.checkMyOS()
    pathFile = listePath[0]
    saveFile = listePath[1]
    
    fileCustomer = fonctions_generiques.RechercherFichierByName(pathFile, 'Customer')
    fileONT = fonctions_generiques.RechercherFichierByName(pathFile, 'Port')
    fileShaper = fonctions_generiques.RechercherFichierByName(pathFile, 'Shaper')
    fileBandwith = fonctions_generiques.RechercherFichierByName(pathFile, 'Bandwith')
    fileOptique = fonctions_generiques.RechercherFichierByName(pathFile, 'Bilan')
    fileModule = fonctions_generiques.RechercherFichierByName(pathFile, 'SFP')
    customerId =  traitement_fichiers.traitementProfilsCustmerId(pathFile, saveFile, fileCustomer)
    portsOnt = traitement_fichiers.traitementProfilsPortsOnt(pathFile, saveFile, fileONT)
    profilsDebit = traitement_fichiers.traitementProfilsDebit(pathFile, saveFile, fileShaper, fileBandwith)
    profilsOptiques = traitement_fichiers.traitementProfilsOptiques(pathFile, saveFile, fileOptique)
    modulesSFP = traitement_fichiers.traitementProfilsModules(pathFile, saveFile, fileModule)
    
    dataBase_AMS = customerId.merge(portsOnt, how = 'left').merge(profilsDebit, how = 'left').merge(profilsOptiques, how = 'left')
    dataPortPon = dataBase_AMS['Port_OLT'].str.split('.', expand = True)
    traitement_fichiers.tronquerDonneesAlphabetiques(dataBase_AMS,dataPortPon)
    dataBase_AMS = dataBase_AMS.merge(modulesSFP, on = "PON")
    dataBase_AMS.pop("PON")
    traitement_fichiers.traitementFormattagePort(dataBase_AMS,dataPortPon)
    #print(dataBase_AMS.head(), dataBase_AMS.tail(5), dataBase_AMS.shape, sep = "\n")
    fonctions_generiques.sauvegardeFichier(dataBase_AMS, saveFile + 'dataBase_AMS.xlsx')


if __name__ == '__main__' :
    create_ams_database()
    #print(PROJECT_DIR,  sep = '\n')
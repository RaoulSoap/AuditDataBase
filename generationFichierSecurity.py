import pandas
import fonctions_generiques

def traitementFichiersDonneesSecurity (pathFile, saveFile, fileName) :
    usedColonnes =  []
    print ('Recuperation et Traitement des données : ' + fileName)
    donneesSecurity = fonctions_generiques.recupererDonneesXLSX(pathFile, fileName, usedColonnes, 0)
    fonctions_generiques.valeursNumeriques(donneesSecurity, 'ND')
    fonctions_generiques.tronquerValeurs(donneesSecurity, 'SN', 12)
    return donneesSecurity

def traitementFormattagePortPON(dataBase_AMS : pandas.DataFrame) :
    dataPortPon = dataBase_AMS['Port'].str.split('/', expand = True)
    nouvellesEntetes = ['OLT:Baie', 'Chassis', 'Carte', 'Pon', 'ONT', 'y']
    fonctions_generiques.renommerEntetes(dataPortPon, nouvellesEntetes)
    dataPortPon['OLT:Baie'] = dataPortPon['OLT:Baie'].replace([' eth '], [':'] , regex = True)
    dataPortPon[['OLT:Baie', 'Chassis', 'Carte', 'Pon']] = dataPortPon[['OLT:Baie', 'Chassis', 'Carte', 'Pon']].astype(str)
    dataPortPon.reset_index(inplace = True, drop = True)
    col = dataPortPon[['OLT:Baie', 'Chassis', 'Carte', 'Pon']].apply("-".join, axis = 1)
    dataBase_AMS.pop("Port")
    dataBase_AMS.insert(loc = 0, column = "Port", value = col)
    
def createRessourcesSecurity() : 
    securityDatabase = pandas.DataFrame()
    listFichiersZippes = []

    listePath = fonctions_generiques.checkMyOS()
    filePath = listePath[0] + 'AAA' + listePath[2]
    saveFile = listePath[1]
    
    print('Identification des fichiers sources ...')    
    securityInfo = fonctions_generiques.RechercherFichierByName(filePath, 'radius')
    securityDatabase = traitementFichiersDonneesSecurity(filePath, saveFile, securityInfo)
    traitementFormattagePortPON(securityDatabase)
    securityDatabase.dropna(inplace = True, axis = 0,)
    securityDatabase.reset_index(inplace = True, drop = True)
    #print(securityDatabase.head(), securityDatabase.tail(5), securityDatabase.shape, sep = "\n")
    print ('Sauvegarde des données')
    fonctions_generiques.sauvegardeFichier(securityDatabase, saveFile + 'securityDatabase.xlsx')
    return securityDatabase

if __name__ == '__main__' :
    createRessourcesSecurity()
    
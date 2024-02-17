import pandas
import fonctions_generiques

def traitementFichiersDonneesBiling (pathFile, saveFile, fileName) :
    usedColonnes =  ['PLAN_TARIFAIRE', 'CATEGORIE', 'IDENTITE', 'LOGIN', 'NUMERO_FIBRE', 'STATUT', 'DATE_STATUT', 'DEBIT']
    print ('Recuperation et Traitement des données : ' + fileName)
    donneesBiling = fonctions_generiques.recupererDonneesCSV(pathFile, fileName, ';', usedColonnes, 0)
    fonctions_generiques.valeursNumeriques(donneesBiling, 'NUMERO_FIBRE')
    donneesBiling['PLAN_TARIFAIRE'] = donneesBiling.apply(lambda x : 'PREPAYE' if x['PLAN_TARIFAIRE'][-3:] == 'Prep' else 'POSTPAYE', axis = 1)
    return donneesBiling
    
def createRessourcesbiling() : 
    bilingDatabase = pandas.DataFrame()
    listFichiersZippes = []

    listePath = fonctions_generiques.checkMyOS()
    filePath = listePath[0] + 'BSCS' + listePath[2]
    saveFile = listePath[1]
    
    nomFichier  = fonctions_generiques.RechercherFichierByName(filePath, 'PARC', 'zip')
    dossierParent  = fonctions_generiques.extraction_fichier(filePath, listFichiersZippes, nomFichier)
    if len(dossierParent) != 0 :
        filePath += dossierParent + listePath[2]
        
    print('Identification des fichiers sources ...')    
    bilingInfo = fonctions_generiques.RechercherFichierByName(filePath, 'PARC', 'csv')
    bilingDatabase = traitementFichiersDonneesBiling(filePath, saveFile, bilingInfo)
    bilingDatabase.dropna(inplace = True, axis = 0,)
    bilingDatabase.reset_index(inplace = True, drop = True)
    print ('Sauvegarde des données')
    fonctions_generiques.sauvegardeFichier(bilingDatabase, saveFile + 'bilingDatabase.xlsx')
    #print(bilingDatabase.head(), bilingDatabase.tail(5), bilingDatabase.shape, sep = "\n")
    fonctions_generiques.supprimerDossierByMame(filePath, 'PARC', 'csv')
    return bilingDatabase

if __name__ == '__main__' :
    createRessourcesbiling()
    
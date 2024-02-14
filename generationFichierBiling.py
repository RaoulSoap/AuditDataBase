import pandas
import fonctions_generiques

def traitementFichiersDonneesBiling (pathFile, saveFile, fileName1) :
    usedColonnes =  ['PLAN_TARIFAIRE', 'CATEGORIE', 'IDENTITE', 'LOGIN', 'NUMERO_FIBRE', 'STATUT', 'DATE_STATUT', 'DEBIT']
    donneesBiling = fonctions_generiques.recupererDonneesCSV(pathFile + fileName1, ';', usedColonnes, 0)
    fonctions_generiques.valeursNumeriques(donneesBiling, 'NUMERO_FIBRE')
    donneesBiling['PLAN_TARIFAIRE'] = donneesBiling.apply(lambda x : 'PREPAYE' if x['PLAN_TARIFAIRE'][-3:] == 'Prep' else 'POSTPAYE', axis = 1)
    #donneesBiling.loc[donneesBiling.PLAN_TARIFAIRE[-3:] != 'Prep','PLAN_TARIFAIRE'] = 'POSTPAYE'
    #donneesBiling.loc[donneesBiling.PLAN_TARIFAIRE[-3:] == 'Prep','PLAN_TARIFAIRE'] = 'PREPAYE'
    #fonctions_generiques.tronquerValeurs(donneesBiling, 'PLAN_TARIFAIRE', 4)
    return donneesBiling
    
def createRessourcesbiling() : 
    bilingDatabase = pandas.DataFrame()
    listFichiersZippes = []

    listePath = fonctions_generiques.checkMyOS()
    filePath = listePath[0]
    saveFile = listePath[1]
    
    nomFichier  = fonctions_generiques.RechercherFichierByName(filePath, 'PARC', 'zip')
    dossierParent  = fonctions_generiques.extraction_fichier(filePath, listFichiersZippes, nomFichier)
    if len(dossierParent) != 0 :
        filePath += dossierParent + listePath[2]
        
    bilingInfo = fonctions_generiques.RechercherFichierByName(filePath, 'PARC', 'csv')
    bilingDatabase = traitementFichiersDonneesBiling(filePath, saveFile, bilingInfo)
    bilingDatabase.dropna(inplace = True, axis = 0,)
    bilingDatabase.reset_index(inplace = True, drop = True)
    #fonctions_generiques.sauvegardeFichier(bilingDatabase, saveFile + '\\' + 'bilingsDatabase.xlsx')
    print(bilingDatabase.head(), bilingDatabase.tail(5), bilingDatabase.shape, sep = "\n")
    #fonctions_generiques.supprimerDossierByMame(filePath, 'PARC', '.csv')
    return bilingDatabase

if __name__ == '__main__' :
    createRessourcesbiling()
    
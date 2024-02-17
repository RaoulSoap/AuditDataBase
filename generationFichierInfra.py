import pandas
import fonctions_generiques

#print(dir(fonctions_generiques))

usedColonnes = []
nouvellesEntetes = ['port', 'tiroirTransport', 'transportPlot', 'sn', 'mac', 'nd', 'login', 'ip', 'typeClient', 'offreCode', 'distribution', 'distributionPlot', 'pb']

def traitementFichiersDonneesAwale (pathFile, saveFile, fileName1, fileName2) :
    usedColonnes =  ['port', 'typeTiroir', 'tiroirTransport', 'sn', 'mac', 'nd', 'login', 'ip', 'type_client', 'codeOffre']
    print ('Recuperation et Traitement des données : ' + fileName1)
    donneesAwaleTransport = fonctions_generiques.recupererDonneesXLSX(pathFile, fileName1, usedColonnes, 0)
    fonctions_generiques.valeursNumeriques(donneesAwaleTransport, 'nd')
    donneesAwaleTransport.dropna(subset = ['nd'], inplace = True, axis = 0)
    donneesAwaleTransport.reset_index(inplace = True, drop = True)
    usedColonnes = ['distribution', 'distributionplot', 'sro/pb', 'nd']
    print ('Recuperation et Traitement des données : ' + fileName2)
    donneesAwaleDistribution = fonctions_generiques.recupererDonneesXLSX(pathFile, fileName2, usedColonnes, 2)
    fonctions_generiques.valeursNumeriques(donneesAwaleDistribution, 'nd')
    donneesAwaleDistribution.dropna(subset = ['nd'], inplace = True, axis = 0)
    donneesAwaleDistribution.reset_index(inplace = True, drop = True)
    donneesAwale = donneesAwaleTransport.merge(donneesAwaleDistribution, on = 'nd')
    donneesAwale.dropna(inplace = True, axis = 0)
    donneesAwale.reset_index(inplace = True, drop = True)
    fonctions_generiques.renommerEntetes(donneesAwale, nouvellesEntetes)
    #print(donneesAwaleTransport.shape, donneesAwaleDistribution.shape, donneesAwale.shape, sep = "\n")
    #print ('Creation du fichier et sauvegarde des Donnees.')
    #fonctions_generiques.sauvegardeFichier(donneesAwaleTransport, saveFile + '\\' + "DonneesAwale.xlsx")
    return donneesAwale

def traitementFichiersDonneesLegacy (pathFile, saveFile, fileName1, fileName2) :
    usedColonnes =  ['port', 'tiroirTransport', 'transportPot', 'sn', 'mac', 'nd', 'login', 'ip', 'type_client', 'codeOffre']
    print ('Recuperation et Traitement des données : ' + fileName1)
    donneesLegacyTransport = fonctions_generiques.recupererDonneesXLSX(pathFile, fileName1, usedColonnes, 0)
    fonctions_generiques.valeursNumeriques(donneesLegacyTransport, 'nd')
    donneesLegacyTransport.dropna(subset = ['nd'], inplace = True, axis = 0)
    donneesLegacyTransport.reset_index(inplace = True, drop = True)
    usedColonnes = ['distribution', 'distributionplot', 'sro/pb', 'nd']
    print ('Recuperation et Traitement des données : ' + fileName2)
    donneesLegacyDistribution = fonctions_generiques.recupererDonneesXLSX(pathFile, fileName2, usedColonnes, 2)
    fonctions_generiques.valeursNumeriques(donneesLegacyDistribution, 'nd')
    donneesLegacyDistribution.dropna(subset = ['nd'], inplace = True, axis = 0)
    donneesLegacyDistribution.reset_index(inplace = True, drop = True)
    donneesLegacy = donneesLegacyTransport.merge(donneesLegacyDistribution, on = 'nd')
    donneesLegacy.dropna(inplace = True, axis = 0)
    donneesLegacy.reset_index(inplace = True, drop = True)
    fonctions_generiques.renommerEntetes(donneesLegacy, nouvellesEntetes)
    #print(donneesLegacyTransport.shape, donneesLegacyDistribution.shape, donneesLegacy.shape, sep = "\n")
    #print ('Creation du fichier et sauvegarde des Donnees.')
    #fonctions_generiques.sauvegardeFichier(donneesLegacyTransport, saveFile + '\\' + "donneesLegacy.xlsx")
    return donneesLegacy

def traitementFichiersDonneesDisruptive (pathFile, saveFile, fileName) :
    usedColonnes =  ['port', 'tiroirTransport', 'transportPlot', 'sn', 'mac', 'nd', 'login', 'ip', 'typeClient', 'offreCode', 'distribution', 'distributionPlot', 'pb', 'sro']
    print ('Recuperation et Traitement des données : ' + fileName)
    donneesDisruptive = fonctions_generiques.recupererDonneesXLSX(pathFile, fileName, usedColonnes, 0)
    fonctions_generiques.valeursNumeriques(donneesDisruptive, 'nd')
    donneesDisruptive['sro/pb'] = donneesDisruptive['sro'] + '/' + donneesDisruptive['pb']
    donneesDisruptive.pop("sro")
    donneesDisruptive.pop("pb")
    donneesDisruptive.dropna(subset = ['nd'], inplace = True, axis = 0)
    donneesDisruptive.reset_index(inplace = True, drop = True)
    fonctions_generiques.renommerEntetes(donneesDisruptive, nouvellesEntetes)
    #print(donneesDisruptive.shape, donneesLegacyDistribution.shape, donneesLegacy.shape, sep = "\n")
    #print ('Creation du fichier et sauvegarde des Donnees.')
    #fonctions_generiques.sauvegardeFichier(donneesDisruptive, saveFile + '\\' + "donneesDisruptive.xlsx")
    return donneesDisruptive

def traitementFichiersDonneesQuickOdn (pathFile, saveFile, fileName) :
    usedColonnes = ['port', 'tiroirTransport', 'transportPlot', 'sn', 'mac', 'nd', 'login', 'ip', 'typeClient', 'offreCode', 'distribution', 'distributionPlot', 'pb', 'sro']
    print ('Recuperation et Traitement des données : ' + fileName)
    donneesQuickOdn = fonctions_generiques.recupererDonneesXLSX(pathFile, fileName, usedColonnes, 0)
    fonctions_generiques.valeursNumeriques(donneesQuickOdn, 'nd')
    donneesQuickOdn['sro/pb'] = donneesQuickOdn['sro'] + '/' + donneesQuickOdn['pb']
    donneesQuickOdn.pop("sro")
    donneesQuickOdn.pop("pb")
    donneesQuickOdn.dropna(subset = ['nd'], inplace = True, axis = 0)
    donneesQuickOdn.reset_index(inplace = True, drop = True)
    fonctions_generiques.renommerEntetes(donneesQuickOdn, nouvellesEntetes)
    #print(donneesQuickOdn.shape, donneesLegacyDistribution.shape, donneesLegacy.shape, sep = "\n")
    #print ('Creation du fichier et sauvegarde des Donnees.')
    #fonctions_generiques.sauvegardeFichier(donneesQuickOdn, saveFile + '\\' + "donneesQuickOdn.xlsx")
    return donneesQuickOdn

def createRessourcesLocalHost() : 
    ressourcesDatabase = pandas.DataFrame()
    listFichiersZippes = ["Extraction Client Awale Transport.xlsx", "Extraction Client Awale Distribution.xlsx", "Extraction Client Disruptive.xlsx", "Extraction Client Disruptivev2.xlsx", "Extraction Client Legacy Transport.xlsx", "Extraction Client Legacy Distribution.xlsx"]

    listePath = fonctions_generiques.checkMyOS()
    pathFile = listePath[0] + 'SI' + listePath[2]
    saveFile = listePath[1]
    
    nomFichier  = fonctions_generiques.RechercherFichierByName(pathFile, 'extraction')
    dossierParent  = fonctions_generiques.extraction_fichier(pathFile, listFichiersZippes, nomFichier)
    if len(dossierParent) != 0 :
        filePath = pathFile +  dossierParent + listePath[2]
    
    print('Identification des fichiers sources ...') 
    awaletransport = fonctions_generiques.RechercherFichierByName(filePath, 'Awale Transport')
    awaleDistribution = fonctions_generiques.RechercherFichierByName(filePath, 'Awale Distribution')
    legacyTransport = fonctions_generiques.RechercherFichierByName(filePath, 'Legacy Transport')
    legacyDistribution = fonctions_generiques.RechercherFichierByName(filePath, 'Legacy Distribution')
    fileDisruptive = fonctions_generiques.RechercherFichierByName(filePath, 'Disruptive')
    fileQuickODN = fonctions_generiques.RechercherFichierByName(filePath, ' Disruptivev2')
    
    awaleData = traitementFichiersDonneesAwale(filePath, saveFile, awaletransport, awaleDistribution)
    legacyData = traitementFichiersDonneesLegacy(filePath, saveFile, legacyTransport, legacyDistribution)
    disruptiveData  = traitementFichiersDonneesDisruptive(filePath, saveFile, fileDisruptive)
    quickOdnData = traitementFichiersDonneesQuickOdn(filePath, saveFile, fileQuickODN)
    
    ressourcesDatabase = pandas.concat([awaleData, legacyData, disruptiveData, quickOdnData], ignore_index = True)
    ressourcesDatabase.reset_index(inplace = True, drop = True)
    print ('Sauvegarde des données')
    fonctions_generiques.sauvegardeFichier(ressourcesDatabase, saveFile + 'ressourcesDatabase.xlsx')
    fonctions_generiques.supprimerDossierByMame(pathFile, 'extraction')
    return ressourcesDatabase

if __name__ == '__main__' :
    createRessourcesLocalHost()
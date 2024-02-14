import pandas
import fonctions_generiques

#print(dir(fonctions_generiques))

def traitementProfilsCustmerId (pathFile, saveFile, fileName) :
    usedColonnes = ['Object Name', 'Customer ID']
    donneesCustomerId = fonctions_generiques.recupererDonneesCSV(pathFile  + fileName, ',', usedColonnes, 2)
    donneesAremplacer  = ['.C1.P1']
    donnéesDeremplacement = ['']
    fonctions_generiques.remplacerValeurs(donneesCustomerId, 'Object Name', donneesAremplacer, donnéesDeremplacement)
    fonctions_generiques.tronquerValeurs(donneesCustomerId, 'Customer ID', 10)
    fonctions_generiques.valeursNumeriques(donneesCustomerId, 'Customer ID')
    nouvellesEntetes = ['Port_OLT', 'Customer_ID']
    fonctions_generiques.renommerEntetes(donneesCustomerId, nouvellesEntetes)
    donneesCustomerId.dropna(inplace = True, axis = 0)
    donneesCustomerId.reset_index(inplace = True, drop = True)
    #print(donneesCustomerId.head(), donneesCustomerId.tail(5), donneesCustomerId.shape, sep = "\n")
    #fonctions_generiques.sauvegardeFichier(donneesCustomerId, saveFile + '\\' + "CustomerId.xlsx")
    return donneesCustomerId

def traitementProfilsDebit (pathFile, saveFile, fileName1, fileName2) :
    usedColonnes = ['Object Name',  'Shaper Profile']
    donneesProfilDebitDown = fonctions_generiques.recupererDonneesCSV(pathFile + fileName1, ',', usedColonnes, 2)
    usedColonnes = ['Object Name', 'Bandwidth Profile']
    donneesProfilDebitUp = fonctions_generiques.recupererDonneesCSV(pathFile + fileName2, ',', usedColonnes, 2)
    donneesProfilDebit = fonctions_generiques.jointureFichiers(donneesProfilDebitUp, donneesProfilDebitDown)
    donneesAremplacer  = ['.C1.P1.Q0', '.C1.P1.Q4', '.C1.P1.Q6', '.C14.P1.Q6', '.C1.P2.Q6', '.C1.P1.Q1']
    donnéesDeremplacement = ['', '', '', '', '', '']
    fonctions_generiques.remplacerValeurs(donneesProfilDebit, 'Object Name', donneesAremplacer, donnéesDeremplacement)
    fonctions_generiques.antiDoublons(donneesProfilDebit, 'Object Name')
    if (donneesProfilDebit.columns[1] == 'Bandwidth Profile' ):
        nouvellesEntetes = ['Port_OLT', 'Debit_UP', 'Debit_Down']
    else:
        nouvellesEntetes = ['Port_OLT', 'Debit_Down', 'Debit_Up']
    fonctions_generiques.renommerEntetes(donneesProfilDebit, nouvellesEntetes)
    donneesProfilDebit.dropna(inplace = True, axis = 0,)
    donneesProfilDebit.reset_index(inplace = True, drop = True)
    #print(donneesProfilDebit.head(), donneesProfilDebit.tail(5), donneesProfilDebit.shape, sep = "\n")
    #fonctions_generiques.sauvegardeFichier(donneesProfilDebit, saveFile + '\\' + "Debit.xlsx")
    return donneesProfilDebit

def traitementProfilsModules (pathFile, saveFile, fileName) :
    usedColonnes = ['Object Name', 'Basic SFP/SFP/XFP/CFP Type']
    donneesinfosSFP = fonctions_generiques.recupererDonneesCSV(pathFile + fileName, ',', usedColonnes, 2)
    donneesAremplacer = ['Base10G-LR', 'SFP Unknown', 'Base1000-BX10-D', 'Base10G-ER', 'Base1000-LX']
    donnéesDeremplacement = ['#N/A', '#N/A', '#N/A', '#N/A', '#N/A']
    fonctions_generiques.remplacerValeurs(donneesinfosSFP, 'Basic SFP/SFP/XFP/CFP Type', donneesAremplacer, donnéesDeremplacement)
    donneesAremplacer = ['.SFP']
    donnéesDeremplacement = ['.PON']
    fonctions_generiques.remplacerValeurs(donneesinfosSFP, 'Object Name', donneesAremplacer, donnéesDeremplacement)
    donneesinfosSFP = donneesinfosSFP.loc[donneesinfosSFP['Basic SFP/SFP/XFP/CFP Type'] != '#N/A']
    nouvellesEntetes = ['PON', 'Type_Module']
    fonctions_generiques.renommerEntetes(donneesinfosSFP, nouvellesEntetes)
    donneesinfosSFP.dropna(inplace = True, axis = 0,)
    donneesinfosSFP.reset_index(inplace = True, drop = True)
    #print(donneesinfosSFP.head(), donneesinfosSFP.tail(5), donneesinfosSFP.shape, sep = "\n")
    #fonctions_generiques.sauvegardeFichier(donneesinfosSFP, saveFile + '\\' + 'modulesSFP.xlsx')
    return donneesinfosSFP

def traitementProfilsOptiques (pathFile, saveFile, fileName) :
    usedColonnes = ['Object Name', 'Rx Optical Signal Level (dBm)', 'Tx Optical Signal Level (dBm)']
    donneesOptiques = fonctions_generiques.recupererDonneesCSV(pathFile + fileName, ',', usedColonnes, 2)
    fonctions_generiques.valeursNumeriques(donneesOptiques, 'Rx Optical Signal Level (dBm)')
    fonctions_generiques.valeursNumeriques(donneesOptiques, 'Tx Optical Signal Level (dBm)')
    nouvellesEntetes = ['Port_OLT', 'Rx_Signal', 'Tx_Signal']
    fonctions_generiques.renommerEntetes(donneesOptiques, nouvellesEntetes)
    donneesOptiques.dropna(inplace = True, axis = 0,)
    donneesOptiques.reset_index(inplace = True, drop = True)
    #print(donneesOptiques.head(), donneesOptiques.tail(5), donneesOptiques.shape, sep = "\n")
    #fonctions_generiques.sauvegardeFichier(donneesOptiques, saveFile + '\\' + 'bilanOptique.xlsx')
    return donneesOptiques

def traitementProfilsPortsOnt (pathFile, saveFile, fileName) :
    usedColonnes = ['Object Name', 'Serial Number (General-Identification)', 'Operational State', 'Active Software', 'Last Change Date']
    donneesPortsOnt = fonctions_generiques.recupererDonneesCSV(pathFile + fileName, ',', usedColonnes, 2)
    nouvellesEntetes = ['Port_OLT', 'Serial_Number', 'Statut_Port', 'Software_Version', 'Last Change Date']
    fonctions_generiques.renommerEntetes(donneesPortsOnt, nouvellesEntetes)
    donneesPortsOnt.dropna(inplace = True, axis = 0,)
    donneesPortsOnt.reset_index(inplace = True, drop = True)
    #print(donneesPortsOnt.head(), donneesPortsOnt.tail(5), donneesPortsOnt.shape, sep = "\n")
    #fonctions_generiques.sauvegardeFichier(donneesPortsOnt, saveFile + '\\' + 'StatutPortsOnt.xlsx')
    return donneesPortsOnt

def traitementProfilsParc (pathFile, saveFile, fileName) :
    usedColonnes = ['Object Name', 'Serial Number (General-Identification)', 'Operational State', 'Active Software', 'Last Change Date']
    donneesPortsOnt = fonctions_generiques.recupererDonneesCSV(pathFile + fileName, ',', usedColonnes, 2)
    nouvellesEntetes = ['Port_OLT', 'Serial_Number', 'Statut_Port', 'Software_Version', 'Last Change Date']
    fonctions_generiques.renommerEntetes(donneesPortsOnt, nouvellesEntetes)
    donneesPortsOnt.dropna(inplace = True, axis = 0,)
    donneesPortsOnt.reset_index(inplace = True, drop = True)
    #print(donneesPortsOnt.head(), donneesPortsOnt.tail(5), donneesPortsOnt.shape, sep = "\n")
    #fonctions_generiques.sauvegardeFichier(donneesPortsOnt, saveFile + '\\' + 'StatutPortsOnt.xlsx')
    return donneesPortsOnt

def traitementProfilsPortsOnt (pathFile, saveFile, fileName) :
    usedColonnes = ['Object Name', 'Serial Number (General-Identification)', 'Operational State', 'Active Software', 'Last Change Date']
    donneesPortsOnt = fonctions_generiques.recupererDonneesCSV(pathFile + fileName, ',', usedColonnes, 2)
    nouvellesEntetes = ['Port_OLT', 'Serial_Number', 'Statut_Port', 'Software_Version', 'Last Change Date']
    fonctions_generiques.renommerEntetes(donneesPortsOnt, nouvellesEntetes)
    donneesPortsOnt.dropna(inplace = True, axis = 0,)
    donneesPortsOnt.reset_index(inplace = True, drop = True)
    #print(donneesPortsOnt.head(), donneesPortsOnt.tail(5), donneesPortsOnt.shape, sep = "\n")
    #fonctions_generiques.sauvegardeFichier(donneesPortsOnt, saveFile + '\\' + 'StatutPortsOnt.xlsx')
    return donneesPortsOnt

def tronquerDonneesAlphabetiques (dataBase_AMS : pandas.DataFrame, dataPortPon : pandas.DataFrame) : 
    nouvellesEntetes = ['OLT:Baie', 'Chassis', 'Carte', 'Pon', 'ONT', 'y', 'z']
    fonctions_generiques.renommerEntetes(dataPortPon, nouvellesEntetes)
    dataBase_AMS["PON"] = dataPortPon[['OLT:Baie', 'Chassis', 'Carte', 'Pon']].apply(".".join, axis=1)

def traitementFormattagePort(dataBase_AMS : pandas.DataFrame, dataPortPon : pandas.DataFrame) :
    dataPortPon['OLT:Baie'] = dataPortPon['OLT:Baie'].replace([':R'], [':'] , regex = True)
    dataPortPon['Chassis'] = dataPortPon['Chassis'].replace(['S'], [''] , regex = True)
    dataPortPon['Carte'] = dataPortPon['Carte'].replace(['LT'], [''] , regex = True)
    dataPortPon['Pon'] = dataPortPon['Pon'].replace(['PON'], [''] , regex = True)
    dataPortPon['ONT'] = dataPortPon['ONT'].replace(['ONT'], [''] , regex = True)
    col = dataPortPon[['OLT:Baie', 'Chassis', 'Carte', 'Pon', 'ONT']].apply("-".join, axis=1)
    dataBase_AMS.pop("Port_OLT")
    dataBase_AMS.insert(loc = 0, column = "Port_OLT", value = col)
   
def create_ams_database():
    dataBase_AMS = pandas.DataFrame()
    
    listePath = fonctions_generiques.checkMyOS()
    pathFile = listePath[0]
    saveFile = listePath[1]
    
    fileCustomer = fonctions_generiques.RechercherFichierByName(pathFile, 'Customer')
    fileONT = fonctions_generiques.RechercherFichierByName(pathFile, 'Port')
    fileShaper = fonctions_generiques.RechercherFichierByName(pathFile, 'Shaper')
    fileBandwith = fonctions_generiques.RechercherFichierByName(pathFile, 'Bandwith')
    fileOptique = fonctions_generiques.RechercherFichierByName(pathFile, 'Bilan')
    fileModule = fonctions_generiques.RechercherFichierByName(pathFile, 'SFP')
    
    customerId =  traitementProfilsCustmerId(pathFile, saveFile, fileCustomer)
    portsOnt = traitementProfilsPortsOnt(pathFile, saveFile, fileONT)
    profilsDebit = traitementProfilsDebit(pathFile, saveFile, fileShaper, fileBandwith)
    profilsOptiques = traitementProfilsOptiques(pathFile, saveFile, fileOptique)
    modulesSFP = traitementProfilsModules(pathFile, saveFile, fileModule)
    
    dataBase_AMS = customerId.merge(portsOnt, how = 'left').merge(profilsDebit, how = 'left').merge(profilsOptiques, how = 'left')
    dataPortPon = dataBase_AMS['Port_OLT'].str.split('.', expand = True)
    tronquerDonneesAlphabetiques(dataBase_AMS,dataPortPon)
    dataBase_AMS = dataBase_AMS.merge(modulesSFP, on = "PON")
    dataBase_AMS.pop("PON")
    traitementFormattagePort(dataBase_AMS,dataPortPon)
    #print(dataBase_AMS.head(), dataBase_AMS.tail(5), dataBase_AMS.shape, sep = "\n")
    fonctions_generiques.sauvegardeFichier(dataBase_AMS, saveFile + 'dataBase_AMS.xlsx')
    return dataBase_AMS


if __name__ == '__main__' :
    create_ams_database()
    #print(PROJECT_DIR,  sep = '\n')
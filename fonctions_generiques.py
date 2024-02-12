import pandas
import os

def recupererDonneesCSV( pathfile , separateur, colonnesUtiles : list, nbfooter, sheetName = "", nbentete = 0) :
    if len(colonnesUtiles) != 0 :
        df = pandas.read_csv(pathfile, sep = separateur,  usecols = colonnesUtiles, skiprows = nbentete, skipfooter = nbfooter, engine='python')
    elif len(sheetName) != 0 :
        df = pandas.read_csv(pathfile, sep = separateur, sheet_name = sheetName, skiprows = nbentete, skipfooter = nbfooter, engine='python')
    elif len(colonnesUtiles) != 0 and len(sheetName) != 0 :
        df = pandas.read_csv(pathfile, sep = separateur,  usecols = colonnesUtiles, sheet_name = sheetName, skiprows = nbentete, skipfooter = nbfooter, engine='python')
    else :
        df = pandas.read_csv(pathfile, sep = separateur, skiprows = nbentete, skipfooter = nbfooter, engine='python')
    return df

def recupererDonneesXLSX(pathfile , colonnesUtiles : list, nbfooter, sheetName = "", nbentete = 0) :
    if len(colonnesUtiles) != 0 :
        df = pandas.read_excel(pathfile, usecols = colonnesUtiles, skiprows = nbentete, skipfooter = nbfooter)
    elif len(sheetName) != 0 :
        df = pandas.read_excel(pathfile, sheet_name = sheetName, skiprows = nbentete, skipfooter = nbfooter)
    elif len(colonnesUtiles) != 0 and len(sheetName) != 0 :
        df = pandas.read_excel(pathfile, usecols = colonnesUtiles, sheet_name = sheetName, skiprows = nbentete, skipfooter = nbfooter)
    else :
        df = pandas.read_excel(pathfile, skiprows = nbentete, skipfooter = nbfooter)
    return df

def renommerEntetes(df : pandas.DataFrame, listeEntetes : list) :
    df.columns = listeEntetes

def remplacerValeurs(df : pandas.DataFrame,  nomColonne, listeDonnesActuelles : list, listeDonnesCibles : list) :
    df[nomColonne] = df[nomColonne].replace(listeDonnesActuelles, listeDonnesCibles, regex = True) 

def tronquerValeurs(df : pandas.DataFrame,  nomColonne, n : int) :
    df[nomColonne] = df[nomColonne].str[-n:]

def valeursNumeriques(df : pandas.DataFrame, nomColonne) :
    df[nomColonne] = df[nomColonne].apply(pandas.to_numeric, errors = 'coerce')
    df = df[df[df.columns].notnull().all(axis = 1)]

def sauvegardeFichier(df : pandas.DataFrame, dossierDeSauvegarde) :
    df.to_excel(dossierDeSauvegarde, sheet_name="données_ams", index = False, engine = "openpyxl")

def antiDoublons(df : pandas.DataFrame,  nomColonne, ) :
    df.drop_duplicates(subset = nomColonne, keep = 'first', inplace=True)

def jointureFichiers(df : pandas.DataFrame,  df2 : pandas.DataFrame) :
    if (len(df) >= len(df2)):
        df_merge  = df.merge(df2, how= 'left')
    else:
       df_merge =  df2.merge(df, how= 'left')
    return df_merge

def RechercherFichierByName (pathFile, motifRecherche) :
    files_in_app = os.listdir(pathFile)
    for file in files_in_app:
        if (file.find(motifRecherche)) >= 0 :
            #print(file, sep = '\n')
            nomFichier  = file
    return nomFichier
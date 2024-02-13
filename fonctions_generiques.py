from pathlib import Path
import tkinter
import platform
import shutil
import sys
import zipfile
import pandas
import os

def recupererDonneesCSV( pathfile , separateur, colonnesUtiles : list, nbfooter, sheetName = "", nbentete = 0) :
    if len(colonnesUtiles) != 0 :
        df = pandas.read_csv(pathfile, sep = separateur,  usecols = colonnesUtiles, skiprows = nbentete, skipfooter = nbfooter, engine = 'python', encoding = 'latin-1')
    elif len(sheetName) != 0 :
        df = pandas.read_csv(pathfile, sep = separateur, sheet_name = sheetName, skiprows = nbentete, skipfooter = nbfooter, engine = 'python', encoding = 'latin-1')
    elif len(colonnesUtiles) != 0 and len(sheetName) != 0 :
        df = pandas.read_csv(pathfile, sep = separateur,  usecols = colonnesUtiles, sheet_name = sheetName, skiprows = nbentete, skipfooter = nbfooter, engine = 'python', encoding = 'latin-1')
    else :
        df = pandas.read_csv(pathfile, sep = separateur, skiprows = nbentete, skipfooter = nbfooter, engine = 'python', encoding = 'latin-1')
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

def checkMyOS() : 
    my_os = platform.system()
    PROJECT_DIR = str(Path(sys.argv[0]).resolve().parent)
    if my_os == 'Linux' or my_os == 'Mac' :
        pathFile = PROJECT_DIR + '/sourcesfiles/'
        saveFile = PROJECT_DIR  + '/resultFiles/'
        listePath = [pathFile, saveFile, '/']
    elif  my_os == 'Windows' :
        pathFile = PROJECT_DIR + '\\sourcesfiles\\'
        saveFile = PROJECT_DIR + '\\resultFiles\\'
        listePath = [pathFile, saveFile, '\\']
    else :
        print('', sep = '\n')
    return listePath 

def extraction_fichier(pathfile, listFichiersZippes : list, nameFile) :
    if zipfile.is_zipfile(pathfile + nameFile) == True : 
        zfile = zipfile.ZipFile(pathfile + nameFile, "r")
        fichiersZippes = zfile.namelist()
        if len(listFichiersZippes) != 0 :
            if fichiersZippes[0].endswith('/'):
                #print("ParentFichiers : Dossier ", sep = '\n')
                dossierParent  = fichiersZippes[0][0 : len(fichiersZippes[0]) - 1]
                for zinfo in fichiersZippes :
                    test = zinfo.split('/')
                    for i in range(0, len(listFichiersZippes)) :
                        if (test[len(test)-1] == listFichiersZippes[i]) :
                            zfile.extract(zinfo, pathfile)
            else :
                #print("ParentFichiers : ArchiveZip  ", sep = '\n')
                dossierParent = ""
                for zinfo in fichiersZippes :
                    if (zinfo == listFichiersZippes[i]) :
                            zfile.extract(zinfo, pathfile)
        else :
            dossierParent = ""
            for zinfo in fichiersZippes :
                zfile.extract(zinfo, pathfile)
        zfile.close()
        #print(dossierParent, sep = '\n')
    return dossierParent

def supprimerDossierByMame(pathFile, motifRecherche, finWord = ""):
    dossiers = os.listdir(pathFile)
    if len(finWord) == 0 :
        for dossier in dossiers :
            if dossier.find(motifRecherche) >= 0 and os.path.isdir(dossier) == True :
                chemin_dossier = os.path.join(pathFile, dossier)
                shutil.rmtree(chemin_dossier)
                #print(chemin_dossier)
            elif dossier.find(motifRecherche) >= 0 and os.path.isfile(dossier) == True :
                os.remove(dossier)
                #print(dossier)
            else : 
              print(dossier + " : Pas de bol", sep = '\n')  
    else : 
        for dossier in dossiers :
            if dossier.find(motifRecherche) >= 0 and dossier[-3:] == finWord :
                print(pathFile + dossier)
                os.remove(pathFile + dossier)
            else : 
                print(pathFile + dossier + " Pas de bol", sep = '\n')

def RechercherFichierByName (pathFile, motifRecherche, finWord = "") :
    files_in_app = os.listdir(pathFile)
    if len(finWord) == 0 : 
        for file in files_in_app:
            if file.find(motifRecherche) >= 0 :
                print(file, sep = '\n')
                nomFichier  = file
                break
    else :
        for file in files_in_app:
            if file.find(motifRecherche) >= 0 and file[-3:] == finWord : 
                print(file, sep = '\n')
                nomFichier  = file
                break
    return nomFichier
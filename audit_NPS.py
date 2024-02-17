import fonctions_generiques

def createConsolidedFile() :
    pathFileNPS = 'C:\\Users\\FWKT5376\\Documents\\projetsPython\\Audit_base_AMS\\src\\sourcesFiles\\Données sondage NPS fibre T45.xlsx'
    pathFileAMS = 'C:\\Users\\FWKT5376\\Documents\\projetsPython\\Audit_base_AMS\\src\\resultFiles\\dataBase_AMS.xlsx'
    saveFile = 'C:\\Users\\FWKT5376\\Documents\\projetsPython\\Audit_base_AMS\\src\\resultFiles\\'
    usedcolumn = []
    dataNPS = fonctions_generiques.recupererDonneesXLSX(pathFileNPS, 'Feuil4', usedcolumn, 0)
    dataAMS = fonctions_generiques.recupererDonneesXLSX(pathFileAMS, 'données_ams', usedcolumn, 0)
    
    dataNPS = dataNPS.merge(dataAMS, how = 'left', left_on = 'ND', right_on = 'Customer_ID' )
    
    fonctions_generiques.sauvegardeFichier(dataNPS, saveFile + 'dataBase_NPS.xlsx')
    return dataNPS
    

if __name__ == '__main__' :
    createConsolidedFile()
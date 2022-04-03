import pymiere,time,os,sys
from pathlib import Path
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication


class Ventana_principal(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("./GUI/main_window.ui",self)
        #self.Iniciar_Shell.clicked.connect(lambda: test_function())




# ----- Read Config File-----------------------
f = open("./config.conf", "r")
file=f.readlines()
path_dir=(file[0].split('='))[1].replace("\n","")
formats_list=((file[1].split("="))[1]).replace("\n","").split(",")
list_Importeds=file[2].split("=")[1]

#---------------------- Functions ---------------

def ImportMedia(media_path):
    project = pymiere.objects.app.project
    success = project.importFiles([media_path],suppressUI=True,targetBin=project.getInsertionBin(),importAsNumberedStills=False)
    sendImportedMediaToFile(media_path)

def sendImportedMediaToFile(media_path):
    if FileInListImporteds(media_path):
        return 0
    f = open(list_Importeds, "a")
    f.write(media_path+"\n")

def FileInListImporteds(media_path):
    try:
        f = open(list_Importeds, "r")
    except FileNotFoundError:
        file = open(list_Importeds, "w")
        file.close()
        f = open(list_Importeds, "r") 
    if (media_path+"\n" in f.readlines()):
        return True
    else:
        return False


def ScanDirectoryAndImport(directory):
    try:
        scan = os.listdir(directory)
    except FileNotFoundError:
        os.system("cls")
        print("The path ("+(directory)+") is not a valid path")
        os.system("pause")
        os.system("exit")
    for i in scan:
        if (i[-3:] in formats_list):
            if (FileInListImporteds(directory+i) == False):
                print("Importing ("+i+") ...")
                ImportMedia(directory+i)



#---------------------- Main ---------------------------
if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = Ventana_principal()
    GUI.show()
    sys.exit(app.exec_())

    try:
        if (pymiere.objects.app.isDocumentOpen()):
            print("Waiting for videos of: "+path_dir+" ...")
            while True:
                time.sleep(1)
                ScanDirectoryAndImport(path_dir)
        else:
            print("You need to open a project first")
            os.system("pause")
            os.system("exit")
    except ValueError:
        print("Premiere is not runing")
        os.system("pause")
        os.system("exit")
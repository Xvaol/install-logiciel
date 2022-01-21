#####################################################################
#				Intallation logiciels basique V1					#
#					   Dylan FAUCHOT								#
#					   Novembre 2021								#
#				   #!/usr/bin/env python3							#
#####################################################################
#Fonction de manipulation de fichiers
import os.path
#Contrôleur de navigateur
import webbrowser
#interface système d'exploitation
import os
#Protocole http
import requests
#Gestion des ZIP
import zipfile
#Les opérations sur les fichiers
import shutil
#Accès au temps et conversions
import time
#Génère des fichiers et répertoires temporaires
import tempfile
#test
#Permet de trouver le nom d'utilisateur
name = os.getlogin()

#Variable url > lien aws vers le zip des logiciels (pas de restriction sur le fichier)
url = 'https://s3.eu-west-3.amazonaws.com/logiciels.projet6/logiciel.zip'
#chemin cible
logiciel = 'Logiciels.zip'

print("Fichier ZIP Telecharger depuis AWS")
#construction de l'objet requests pour récupérer les resources sur le serveur aws (url)
resource = requests.get(url, stream=True)
#Extration du fichier ZIP
fichier = open(logiciel, "wb")
for section in resource.iter_content(chunk_size=512):
	#flitre les morceaux
	if section:
		fichier.write(section)
fichier.close()

with zipfile.ZipFile("Logiciels.zip", "r") as zip_ref:
	zip_ref.extractall("logiciel")

print("Extration fichier ZIP terminer")

# fonction pour savoir si le logiciel est présent sur la machine et si l'installation s'effectue
def install_firefox():
	#méthode pour changer le répertoire de travail actuel
	os.chdir(r"C:\Program Files")
	# test avec "os.path" et "exists" si dans la liste1, à l'argument "0", Firefox existe
	if(os.path.exists(liste1[0])):
		print("Firefox existe déjà")
	else:
		print("Installation de Firefox en cours")
		#le programme doit être placer dans c:\Projet pour fonctionner
		os.chdir(r"C:\Projet\logiciel")
		#intéraction avec L'OS
		os.system("Firefox.exe /S")
		print("Firefox installé")

def install_notepad():
	os.chdir(r"C:\Program Files")
	if(os.path.exists(liste1[1])):
		print("Notepad ++ existe déjà")
	else:
		print("Installation de Notepad ++")
		os.chdir(r"C:\Projet\logiciel")
		os.system("Notepad.exe /S")
		print ("Notepad ++ installé")

def install_gotomeeting():
	os.chdir(r"C:\Program Files (x86)")
	if(os.path.exists(liste1[2])):
		print("GoToMeeting existe déjà")
	else:
		print("Installation de GoToMeeting")
		os.chdir(r"C:\Projet\logiciel")
		os.system("GoToMeeting.exe /S")
		print ("GoToMeeting installé")

def install_vlc():
	os.chdir(r"C:\Program Files")
	if(os.path.exists(liste1[3])):
		print("VLC existe déjà")
	else:
		print("Installation de VLC")
		os.chdir(r"C:\Projet\logiciel")
		os.system("VLC /S")
		print ("VLC installé")

def install_zoom():
	os.chdir(r"C:\\Users\\"+name+"\\AppData\\Roaming")
	if(os.path.exists(liste1[4])):
		print("ZOOM existe déjà")
	else:
		print("Installation de ZOOM")
		os.chdir(r"C:\Projet\logiciel")
		os.system("Zoom /S")
		print ("ZOOM installé")

def install_teams():
	os.chdir(r"C:\\Users\\"+name+"\\AppData\\Roaming")
	if(os.path.exists(liste1[5])):
		print("Teams existe déjà")
	else:
		print("Installation de Teams")
		os.chdir(r"C:\Projet\logiciel")
		os.system("Teams /S")
		print ("Teams installé")

def install_adobe():
	os.chdir(r"C:\Program Files (x86)")
	if(os.path.exists(liste1[6])):
		print("Adobe existe déjà")
	else:
		print("Installation de Adobe")
		os.chdir(r"C:\Projet\logiciel")
		os.system("Adobe /S")
		print ("Adobe installé")

def install_filezilla():
	os.chdir(r"C:\Program Files")
	if(os.path.exists(liste1[7])):
		print("FileZilla existe déjà")
	else:
		print("Installation de FileZilla")
		os.chdir(r"C:\Projet\logiciel")
		os.system("FileZilla /S")
		print ("FileZilla installé")

def install_teamviewer():
	os.chdir(r"C:\Program Files (x86)")
	if(os.path.exists(liste1[8])):
		print("TeamViewer existe déjà")
	else:
		print("Installation de TeamViewer")
		os.chdir(r"C:\Projet\logiciel")
		os.system("TeamViewer /S")
		print ("TeamViewer installé")								
								



print("Installation Logiciels de base")

liste1 = ["Mozilla Firefox","Notepad++","GoToMeeting","VideoLAN","Zoom","Teams","Adobe",
"FileZilla FTP Client","TeamViewer"]

#Appel de la fonction définie plus haut
install_firefox()
install_notepad()
install_gotomeeting()
install_vlc()
install_zoom()
install_teams()
install_adobe()
install_filezilla()
install_teamviewer()



print("Installation Logiciels terminée")

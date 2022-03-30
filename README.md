# Premiere-Auto-Import-Tool
[[English](https://github.com/BrianGoldYT/Premiere-Auto-Import-Tool)] - [[Spanish](https://github.com/BrianGoldYT/Premiere-Auto-Import-Tool/blob/main/README-es.md)]

This program allows you to automatically import all the files that are added to a folder, it only imports them once, convenient for when you are downloading many videos from the internet.

To be able to use this program in premiere we first have to install the Pymere Link extension, [this script](https://raw.githubusercontent.com/BrianGoldYT/Premiere-Auto-Import-Tool/main/Install_Pymiere_Link.bat) will install the extension automatically

Once the script is executed, we can check if it is installed if it appears in Premiere > Window > Extensions > Pymiere Link
Una vez Pymere Link este funcionando podemos descargar [Import-Videos.exe](https://github.com/BrianGoldYT/Premiere-Auto-Import-Tool/releases/download/0.0.1/Import-Videos.exe) y [config.conf](https://github.com/BrianGoldYT/Premiere-Auto-Import-Tool/releases/download/0.0.1/config.conf), Estos archivos necesitan estar juntos en una misma carpeta para funcionar
To set our folder we must edit the config.conf file using a text editor and change the following line:

    Directory=C:\Users\User\Downloads\

and add the folder from which the videos will be imported.

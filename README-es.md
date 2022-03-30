# Herramienta de importación automática de Premiere
[[Inglés](https://github.com/BrianGoldYT/Premiere-Auto-Import-Tool/blob/main/README.md)] - [[Español](https://github.com/BrianGoldYT/Premiere-Auto-Import-tool/blob/main/README-es.md)]

Este programa le permite importar automáticamente todos los archivos que se agregan a una carpeta, solo los importa una vez, conveniente para cuando está descargando muchos videos de Internet.

Para poder usar este programa en estreno primero tenemos que instalar la extensión Pymere Link, [este script](https://raw.githubusercontent.com/BrianGoldYT/Premiere-Auto-Import-Tool/main/Install_Pymiere_Link.bat) instalará la extensión automáticamente

Una vez ejecutado el script podemos comprobar si está instalado si aparece en Premiere > Ventana > Extensiones > Pymiere Link
Una vez Pymere Link este funcionando podemos descargar [Import-Videos.exe](https://github.com/BrianGoldYT/Premiere-Auto-Import-Tool/releases/download/0.0.1/Import-Videos.exe) y [ config.conf](https://github.com/BrianGoldYT/Premiere-Auto-Import-Tool/releases/download/0.0.1/config.conf), Estos archivos necesitan estar juntos en una misma carpeta para funcionar
Para configurar nuestra carpeta debemos editar el archivo config.conf usando un editor de texto y cambiar la siguiente línea:

    Directorio=C:\Usuarios\Usuario\Descargas\

y agregue la carpeta desde la cual se importarán los videos.

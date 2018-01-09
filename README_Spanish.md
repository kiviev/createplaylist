
# Generador automático de playlist con ***Python***


Este script sirve para generar playlist simples de forma automática con Python en formato ***.m3u***.  

Se pueden generar al ejecutar el script o bien añadirlo a una tarea cron y así mantener las playlist al día.

## Requerimientos
Es necesario tener instalado Python >= v3.*

## Cómo se usa

### Archivo mySearch.py
#### Array para generar las búsquedas
Existe en el repositorio un archivo llamado Sample_mySearch.py.   Este archivo se puede utilizar a modo de ejemplo, tan sólo hay que eliminar de su nombre la parte "**Sample_**" y obtendremos un archivo llamado mySearch.py.

En este arhivo añadiremos un array con todos los tipos de listas que queramos generar y los nombres de las búsquedas por ejemplo:
```python
AllArray = {
	"rock" : ["Led Zeppelin","Iron Maiden","Metallica"],
	"acction" :["Rambo","Rambo 2","Rambo 3"],
	"travel" : ["Hawai","Roma","Paris","Australia"],
	"all" : ['']
}
```
Por ejemplo, con el Array "rock" generaremos de una vez playlist para la búsqueda de Led Zeppelin, Iron Maiden y Metallica, que luego más adelante podremos decidir donde buscar y donde crear el fichero de la playlist, incluso el nombre que queremos que tenga el fichero generado.

El último (**"all"**) haría una búsqueda de todos los archivos que encontrara según el tipo (que añadiremos más adelante)

#### Ejecución de las búsquedas
En este archivo ejecutaremos la función **_createPlayListSingle()_**
Esta función se le pasan varios parámetros:

- _lista_ [***requerido***] -> Es la lista desde la que se sacan los nombres de búsqueda.
- _directorio_ [***requerido***]  -> Es la ruta (**relativa**) donde hacer la búsqueda desde el directorio donde se creará la playlist.
- _tipo_ [***requerido***]  -> Es el tipo de búsqueda, las opciones son ***"video", "audio" o "image"***.
- _path_ [requerido] -> Ruta donde se generará el archivo de la playlist.
- _filename_ [***opcional***]  -> El nombre del archivo de la playlist, si no se añade, el nombre será el nombre de la búsqueda, es decir, el texto que aparece en el Array AllArray, por ejemplo, si ejecutamos para "rock",  si no ponemos este parámetro uno de los nombres de ficheros con la playlist sería **Led Zeppelin.m3u** .

``` python
createPlayListSingle(AllArray['rock'] ,'../../../' , 'audio', '/home/pack/playlist/music/')
```

## Uso
Una vez configurado lo anteriór, tan sólo hay que ejecutarlo desde la terminal cambiado al directorio donde esté el archivo ***AllPlaylist.py*** y ejecutarlo:
```bash
cd ~/createplaylist/
python3 AllPlaylist.py
```

## Automatización mediante tarea cron

Si lo deseas se pueden tener todas tus listas actualizadas, aunque añadas nuevos archivos.

Esto es posible mediante ***CRON***.  

Si añades la ejecución de este script a una tarea cron, podrás hacer que se ejecute cada X tiempo y se crearán todas las playlist de nuevo, incluyendo los nuevos archivos que hayas descargado.

Ejemplo:
```bash
crontab -e
```
Una vez abierto con tu editor favorito, añadir la siguiente línea:

```txt
1 * * * * python3.5 /home/pack/Automatizaciones/python/createplaylist/AllPlaylist.py
```
Esto significa que se ejecutará en el minuto 1 de cada hora este script.  Para saber más sobre cron visite la  [Documentación de crontab](http://man7.org/linux/man-pages/man5/crontab.5.html)
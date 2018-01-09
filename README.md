
# Automatic playlist generator with ***Python***


This script serves to generate simple playlist automatically with Python in format ***.m3u***.  

Can be generated when executing the script or add it to a cron task and thus keep the playlist up to date.

## Requirements

It is necessary to have installedPython >= v3.*

## How to use

### File mySearch.py
#### 
Array to generate searches There is a file in the repository called Sample_mySearch.py. This file can be used as an example, you just have to delete the part of your name"**Sample_**"and we'll get a file called mySearch.py.


In this file we will add an array with all the types of lists that we want to generate and the names of the searches, for example:
```python
AllArray = {
	"rock" : ["Led Zeppelin","Iron Maiden","Metallica"],
	"acction" :["Rambo","Rambo 2","Rambo 3"],
	"travel" : ["Hawai","Roma","Paris","Australia"],
	"all" : ['']
}
```
For example, with the Array "rock" we will generate once a playlist for the search of Led Zeppelin, Iron Maiden and Metallica, which later on we can decide where to look and where to create the playlist file, even the name we want it to have the generated file.

The last one (**"all"**) would do a search of all the files that it will find according to the type (that we will add later)


#### Execution of searches
In this file we will execute the function **_createPlayListSingle()_**
This function will pass several parameters

- _list_ [***required***] -> It is the list from which the search names are taken.
- _dir_ [***required***]  -> Is the path (**relativa**)  where to search from the directory where the playlist will be created.
- _type_ [***required***]  -> It's the type of search, the options are***"video", "audio" o "image"***.
- _path_ [requerido] -> Path where the playlist file will be generated.
- _filename_ [***optional***]  -> The name of the playlist file, if it is not added, the name will be the name of the search, that is, the text that appears in the Array AllArray, for example, if we execute for "rock", if we do not put this parameter one of the names of files with the playlist would be **Led Zeppelin.m3u** .

``` python
createPlayListSingle(AllArray['rock'] ,'../../../' , 'audio', '/home/pack/playlist/music/')
```

## Use
Once configured the above, you just have to execute it from the terminal changed to the directory where the file is ***AllPlaylist.py*** and execute it:
```bash
cd ~/createplaylist/
python3 AllPlaylist.py
```

## Automation through cron task

If you wish you can have all your lists updated, even if you add new files.

This is possible through ***CRON***.  

If you add the execution of this script to a cron task, you can make it run every X time and all the playlists will be created again, including the new files that you have downloaded.

Example:
```bash
crontab -e
```
Once opened with your favorite editor, add the following line:

```txt
1 * * * * python3.5 /home/pack/Automatizaciones/python/createplaylist/AllPlaylist.py
```
This means that this script will be executed in the minute 1 of each hour. To know more about cron visit the [Documentation of crontab](http://man7.org/linux/man-pages/man5/crontab.5.html)
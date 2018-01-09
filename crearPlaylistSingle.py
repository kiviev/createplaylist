#!/usr/bin/env python3

import  os ,argparse
from functions import *
from config import *

# comienza ejecucion


files = []
search = args.search
pathOutputPlaylist = args.path
dirs = [args.dir]
extensiones = extensions[args.type]

if args.filename:
	newFilename = args.filename
else :
	newFilename = search

print(search)

# cambiamos al directorio
create_or_change_path_output(pathOutputPlaylist)
# hacemos la busqueda
find_files(files , dirs , extensiones , search)
# creamos el archivo en el path indicado
create_file( strFile(files , True), newFilename  , 'm3u', pathOutputPlaylist )


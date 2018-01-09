#!/usr/bin/env python3

import  os 

def find_files(files, dirs=[], extensions=[] , search = ''):
	new_dirs = []
	search = search.lower()
	repace_underscore = search.replace("_" , " ")
	replace_blank = search.replace(" " , "_")
	for d in dirs:
		try:
			new_dirs += [ os.path.join(d, f) for f in os.listdir(d) ]
		except OSError:
			pathName = os.path.splitext(d)[0].lower()
			exten = os.path.splitext(d)[1].lower()

			if (pathName.find(search) != -1 or pathName.find(repace_underscore) != -1 or pathName.find(replace_blank) != -1) and exten in extensions:
				files.append(d)

	if new_dirs:
		find_files(files, new_dirs, extensions , search )
	else:
		return

def create_file(content , name , ext = '' , path = './'):
	if name == '':
		name = "Todo_playlist"

	f = open(path + name + "." + ext, 'w')
	f.write(content)
	f.close()

def get_filenames(files , string = False , sort = False):
	filenames = []
	for i in range(0,len(files)):
		filepath = files[i] 
		path = filepath.split('/')
		filename = path[len(path) -1]
		filenames.append(filename)
		if sort :
			filenames.sort()

	return (filenames , "\n".join(filenames))[string]

def strFile(files , sort = False):
	if sort:
		files.sort()
	return  "\n".join(files)

def create_or_change_path_output(pathOutput):
	if not os.path.exists(pathOutput):
		os.makedirs(pathOutput)

	os.chdir(pathOutput)







def createPlayListSingle(lista , directorio , tipo , path , filename = ''):
	for i in lista:
		command = 'python3.5 ./crearPlaylistSingle.py -s "' + i  + '" -d ' + directorio  + ' -t ' + tipo + ' -p ' + path
		if filename != '':
			command += ' -f ' + filename 
		os.system(command)
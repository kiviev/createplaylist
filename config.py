#!/usr/bin/env python3

import  os ,argparse

parser = argparse.ArgumentParser(description='Process some integers.')

parser.add_argument("-f", "--file", dest="filename",
                  help="Nombre de salida del archivo FILE", metavar="FILE")
parser.add_argument("-p", "--path", dest="path",
                  help="Path del archivo de salida", metavar="PATH" , default="./")
parser.add_argument("-s", "--search", dest="search",
                  help="Expresion a buscar", metavar="SEARCH", default="")
parser.add_argument("-d", "--dir", dest="dir" , required=True,
                  help="Ruta relativa al archivo de salida donde buscar", metavar="DIR")
parser.add_argument("-t", "--type", dest="type",required=True ,
                  help="Tipos de archivos para buscar [audio,video,image]", metavar="TYPE")

parser.add_argument("-q", "--quiet",
                  action="store_false", dest="verbose", default=True,
                  help="don't print status messages to stdout")

args = parser.parse_args()


# print(args.search)
extensions = {
				"video" : ['.mp4' , '.avi' , '.flv' ,'.wmv' ,'.mkv' , '.mpg' , '.mpeg'] , 
				"audio" : ['.mp3','.ogg' , '.wab' , '.wma' , '.webm'],
				"image" : [ '.gif' , '.jpg' , '.jpeg' , '.png' , ' .bmp' ]
			}

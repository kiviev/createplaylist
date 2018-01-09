#!/usr/bin/env python3


##########

# remove from this file part of the name "Sample_" and with it you can work

##########


from functions import createPlayListSingle

AllArray = {
	"rock" : ["Led Zeppelin","Iron Maiden","Metallica"],

	"acction" :["Rambo","Rambo 2","Rambo 3"],

	"travel" : ["Hawai","Roma","Paris","Australia"],

	"all" : ['']
}

# with this path, search the entire personal folder
createPlayListSingle(AllArray['rock'] ,'../../../' , 'audio', '/home/pack/playlist/music/')

createPlayListSingle(AllArray['action'] ,'../../../../' , 'video', '/home/pack/playlist/video/films/action/')

createPlayListSingle(AllArray['travel'] ,'../../../' , 'image', '/home/pack/playlist/photo/travels/')

createPlayListSingle(AllArray['all'] ,'../../../' , 'video', '/home/pack/playlist/video/' , 'All Videos')
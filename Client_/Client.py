import Ice
import app
import sys
import os

with Ice.initialize(sys.argv) as communicator:
    # Create a proxy to the remote Printer object
    obj = communicator.stringToProxy("StreamApplication:tcp -h 127.0.0.1 -p 10000")

    # Downcast obj to Printer proxy
    managerApp = app.StreamApplicationPrx.checkedCast(obj)

   

    s1=app.Song("song 1", "path 1","artist 1", "album1", "genre1", "year1")
    s2=app.Song("song 2", "path 2","artist 2", "album2", "genre2", "year2")
    s3=app.Song("song 3", "path 3","artist 3", "album3", "genre3", "year3")

    managerApp.ajoutMusic(s1)
    managerApp.ajoutMusic(s2)
    managerApp.ajoutMusic(s3)

    print "Menu:"
  
    print "choisir une option :"
    print "1.enregistrer une musique  "
    print "2.supprimer une musique "
    print "3.rechercher "
    print "4.afficher la liste des musiques"
    choice = raw_input()

    if choice =='1':
       print " entrez le titre"
       titre = raw_input()
       print " entrez le chanteur"
       chanteur = raw_input()
       print " entrez le genre"
       genre = raw_input()
       print " entrez le album"
       album = raw_input()
       print " entrez l'annee"
       annee = raw_input()
       print " entrez chemin"
       chemin = raw_input()
       music1 = app.Song(titre, chemin,chanteur, album, genre, annee)
       if( managerApp.ajoutMusic(music1)):
       	print "chanson ajoute"
  
    if choice=='2':
    	print "Donnez le nom : "
   	choix=raw_input()
   	if managerApp.suppMusic(choix):
   	   	print "chanson supprime"
   	else:
   	  	print "chanson n'existe pas"
    if choice=='4':
    	result = managerApp.getAll()
    	for v in result:
        	
         	print ( v.name ,  v.artist,v.genre, v.year, v.album)

 
         	
    if choice=='3':
        print "vous voulez chercher par: "
        print "1.titre"
        print "2.chanteur"
        print "3.genre"
        print "4.l'annee"
        nbr = raw_input()
        if nbr=='1' :
           print " entrez le titre"
           titre = raw_input()
           result = managerApp.findByName(titre)
           #print result
           if not result:
             print " aucun resultat"
           for v in result:
              print "music ",":"
    	      print ( v.name ,  v.artist,v.genre, v.year, v.album)
    	if nbr=='2' :
           print " entrez le chanteur"
           chanteur = raw_input()
           result = managerApp.findByArtist(chanteur)
           if not result:
             print " aucun resultat"
           for v in result:
              print "music ",":"
    	      print ( v.name ,  v.artist,v.genre, v.year, v.album)
    	if nbr=='3' :
           print " entrez le genre"
           genre = raw_input()
           result = managerApp.findByGenre(genre)
           if not result:
             print " aucun resultat"
           for v in result:
              print "music ",":"
    	      print ( v.name ,  v.artist,v.genre, v.year, v.album)
    	if nbr=='4' :
           print " entrez l'annee"
           annee = raw_input()
           result = managerApp.findByYear(annee)
           if not result:
             print " aucun resultat"
           for v in result:
              print "music ",":"
    	      print ( v.name ,  v.artist,v.genre, v.year, v.album)

	
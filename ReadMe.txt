| Compte Rendu (TP) Middlware|
| M1-ILSEN		     |
| Nom : KHELAFI Abdelhamid   |
|____________________________|

1. Prérequis:

- Version de ice: 3.7
- Version python: 2.7 ou ultérieur.
- Version JAVA : 8
- Environnement de travail linux (linux mint ou ubuntu à prioris).
- Il faut avoir Maven installé pour compiler.

2. Comment lancer l’application:
	Dans mon rendu y’a 2 dossiers:
		- Celui du client Python :
			Pour le lancer il suffit d’executer la commande suivante :
			python Client.py
		- Celui du Serveur: c’est un projet Maven (Java) et pour le compiler il
			faut executer la commande suivante :
				mvn clean package
				Pour lancer le serveur :
				mvn exec:java -Dexec.mainClass="com.streamapplication.Server"
				Ou juste faire Make dans une ligne de commande.

3. Propositions d’interfaces pour le partage entre plusieurs
	utilisateurs:
		Pour le partage entre plusieurs utilisateurs il faut créer pour chacun
		des utilisateurs un projet différent s’il s’agit de langage de programmation
		différente. Quand à l’interface slice​ , on aura la même interface pour chacundes utilisateurs (client) et pour celle du serveur afin qu’il puisse
		communiquer.

4. Fonctionnement et contenu de l’application
		a. Contenu:
				i. Une interface StreamApplication qui contient les différentes
					méthodes pour la gestion des musiques.
				ii. Une séquence qui permet de renvoyer une liste de musique à partir
					d’une recherche.
				iii. Une classe qui représente les informations d’un morceaux de son
					(nom, artist ..).
		b. Fonctionnement
			i. Pour cette partie j’ai choisi de faire l'implémentation avec le langage
				Java. Qui me servira côté serveur pour l’ajout d’un son à partager, à
				supprimer et encore plus pour la recherche d’un son déjà partagé par
				d’autre personne par plusieurs critères.
				1. Le nom de la musique;
				2. Le chanteur;
				3. L’album;
				4. Le genre;
				5. L’année;
			iii. Pour la recherche il faut choisir aussi quel type de critère vous
				voulez utiliser et donner l’information.
			iv. Pour la supression je n’ai défini qu’un seul critère : par le titre de la
			musique.
5. Les difficultés rencontrées:
			Comprendre le fonctionnement de ice, il n’y a pas assez de
		documentation en ligne, moins de communauté utilisateur. J’ai rencontré
		une erreur lors de la compilation en java, alors j’ai décidé d’utilisé un projet
		maven qui gère les dépendances automatiquement.6. Ce qui pourrait être fait pour améliorer l'outils:
		Faire une structuration plus avancer pour la gestion des fichier
		audio. On peut aussi utiliser des bibliothéque de streaming pour diffuser les
		flux audio au différents client et créer des client avec des interface
		graphiques et des lecteur audio pour lire les flux.

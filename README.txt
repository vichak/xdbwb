----------------------------------------------------------------------------
"THE BEER-WARE LICENSE" (Revision 42):
<vichak-at-hakoun-dot-fr> wrote this file. As long as you retain this notice you
can do whatever you want with this stuff. If we meet some day, and you think
this stuff is worth it, you can buy me a beer in return vichak
----------------------------------------------------------------------------

   _  __ ____  ____ _       ______ 
  | |/ // __ \/ __ ) |     / / __ )
  |   // / / / __  | | /| / / __  |
 /   |/ /_/ / /_/ /| |/ |/ / /_/ / 
/_/|_/_____/_____/ |__/|__/_____/  Xbmc Data Base Web Browser

 
(ascii generator slant
http://www.network-science.de/ascii/ )

Xdbwb is a personal project. Feell free to contribute to it.

Xdbwb is a simple website that browse xbmc databse.


This project is built with Ptyhon(2.7.3), django web framework(1.4.1) and jquery mobile framework(1.3.0).
It uses your populated XBMC database (specified in setting.py).
Developpement and deployement is done on GNU/Linux host.
model.py generated with django script :
https://docs.djangoproject.com/en/dev/howto/legacy-databases/
(a few modifications were applied)

1. Generate your secret key on http://www.miniwebtool.com/django-secret-key-generator/
Edit SECRET_KEY variable in xdbwb/settings.py

2. Clone the git repo - `git clone https://github.com/commadelimited/jQuery-Mobile-Icon-Pack.git` - or [download it](https://github.com/commadelimited/jQuery-Mobile-Icon-Pack/zipball/master)
In static directory

3. Create the xdbwb database:
$ python manage.py syncdb

4. Define wbmc database location:
use django syntax https://docs.djangoproject.com/en/dev/ref/databases/
expample of mysql xbmc database in xdbwb/settings.py 

5. Download poster; run Python script download_poster.py. Xbmc database is used.
$ python download_poster.py -d static/img/

6. Run development server
$ python manage.py runserver

//TODO describe depoiement
apache + lighttpd

//TODO

	####BUG########
	1. multiple film in stack:///chemin/film/cd1 . /chemin/film/cd2
	###############
	utf-8
	improve pagination
	Writers/Actors
	Streamdetails
	Series
	comments on a film
	note a film
	signal a problem with a movie
	write tests
	search form
	internationalization
	#####admin########
	improve admin section //now olnly auth Movies
	#####display######
	apple-touch-icon optimize android and choose a new one
	film detail => improve display
	#####auth#########
	user information // next accounts/profile
	####project mgmt##
	security https
	

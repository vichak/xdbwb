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

([ascii generator](http://www.network-science.de/ascii/) slant )

# Description

xdbwb is a personal project. Feel free to contribute to it.

xdbwb is a simple website that browse xbmc database.

This project is built with Python(2.7.3), django web framework(1.4.1) and jquery mobile framework(1.3.0).
It uses your populated xbmc database (specified in xdbwb/settings.py).

Development and deployement is done on GNU/Linux host.

xdbwb/lib/models.py is generated with [this django script](https://docs.djangoproject.com/en/dev/howto/legacy-databases/), a few modifications were applied.

# Needed packages
```sh
sudo apt-get install git python-pip python-dev libmysqlclient-dev
sudo pip install Django==1.4.1 MySQL-python
```

# Setup development environment
1. Get working dir
  ```sh
mkdir ~/working_dir
cd working_dir
git clone https://github.com/vichak/xdbwb.git
cd xdbwb
  ```

2. Generate your secret key on http://www.miniwebtool.com/django-secret-key-generator/

  Edit SECRET_KEY variable in xdbwb/settings.py

  Commit your change

  ```sh
git add xdbwb/settings.py
git commit -m "Set SECRET_KEY value"
  ```

3. Clone the git repo of JQuery-Mobile-Icon-Pack in static directory or [download it](https://github.com/commadelimited/jQuery-Mobile-Icon-Pack/zipball/master)
  ```sh
cd static
git clone https://github.com/commadelimited/jQuery-Mobile-Icon-Pack.git
cd ..
  ```

4. Create xdbwb's database:
  ```sh
python manage.py syncdb
  ```
  Save superuser login/password

5. Define xbmc database location:

  Use django syntax https://docs.djangoproject.com/en/dev/ref/databases/
example of mysql xbmc database in xdbwb/settings.py

6. Download poster via Python script download_poster.py. xbmc database is used.
  ```sh
mkdir -p static/img
python download_poster.py -d static/img/
  ```

7. Run development server
  ```sh
python manage.py runserver
  ```

# Setup production environment

Apache2 + mod_wsgi for django website and lighttpd for serve static files (imgs/js/css).

1. Get xdbwb in /var/www
  ```sh
sudo mkdir -p /var/www
cd /var/www
sudo git clone /home/vichak/working_dir/xdbwb
  ```

2. Set production variables in /var/www/xdbwb/xdbwb/settings.py
  ```
DEBUG = FALSE
PROJECT_PATH = '/var/www/xdbwb/'
  ```

3. Get database from development environment
  ```sh
sudo cp /home/vichak/working_dir/xdbwb/xdbwb.db /var/www/xdbwb
  ```

4. Install apache2 + mod_wsgi
  ```sh
sudo apt-get install apache2 libapache2-mod-wsgi
  ```

5. Configure xdbwb in apache2
  ```sh
sudo chown -R www-data. /var/www
sudo chmod u+x /var/www/xdbwb/conf/xdbwb.wsgi
sudo cp /var/www/xdbwb/conf/xdbwb /etc/apache2/sites-available
sudo a2dissite default
sudo a2ensite xdbwb
  ```

6. Install static lighttpd server
  ```sh
sudo apt-get install lighttpd
  ```

7. Collect static files from development environment
  ```sh
cd /home/vichak/working_dir/xdbwb/
python manage.py collectstatic
sudo cp -R /home/vichak/working_dir/xdbwb/static_for_prod /var/www/xdbwb_static
  ```

8. Configure lighttpd
  ```sh
sudo cp /var/www/xdbwb/conf/lighttpd.conf /etc/lighttd/
  ```

9. Configure production xdbwb

  Edit /var/www/xdbwb/settings.py
  ```
STATIC_URL = 'http://<IP_ADDRESS>:81/'
  ```
  Commit your change
  ```sh
git add xdbwb/settings.py
git commit -m "Set settings for production"
  ```
10. Restart apache2 and lighttpd

  ```sh
sudo service apache2 restart
sudo service lighttpd restart
  ```

#TODO

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

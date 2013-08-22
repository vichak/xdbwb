import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'xdbwb.settings'

from PIL import Image
from lib.models import Movie
import os.path
import urllib
import argparse

def script_interface():
    """Script interface command like Unix
    """
    parser = argparse.ArgumentParser(description="Generate poster for xdbwb")
    parser.add_argument('-d',
                dest="DIR",
                required=True,
                help="Destination directory")
    args = parser.parse_args() 
    if not os.path.isdir(args.DIR):
        parser.error("path does not exist or is not a directory")
    return args

if __name__ == "__main__":
    args = script_interface()
    DIR = os.path.abspath(args.DIR)
    movies = []
    for movie in Movie.objects.all():
        if len(movie.thumbnails.split('>')) > 1 :
            t = movie.thumbnails.split('>')[1].rsplit('</thumb')[0]
            movies.append((movie.idmovie, t))
    os.chdir(DIR)
    size = 93, 140
    size2 = 225, 300
    for t in movies :
	id = t[0]
	title = Movie.objects.get(pk=id).title.encode("utf-8")
        print title
        filename = '%d_poster.jpg' % id
        filename2 = '%d_93x140_thumbnail.jpg' % id
        filename3 = '%d_225x300_thumbnail.jpg' % id
        if not os.path.isfile(filename):
            urllib.urlretrieve(t[1], filename=filename)
        try:
            im = Image.open(os.path.join(DIR , filename))
            im.thumbnail(size, Image.ANTIALIAS)
            im.save(os.path.join(DIR, filename2), "JPEG")
            im2 = Image.open(os.path.join(DIR , filename))
            im2.thumbnail(size2, Image.ANTIALIAS)
            im2.save(os.path.join(DIR, filename3), "JPEG")            
        except IOError:
            print "cannot create thumbnail for '%s'" % filename2

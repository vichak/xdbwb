# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
import os

from django.db import models
from os.path import basename

class Actorlinkepisode(models.Model):
    idactor = models.IntegerField(null=True, db_column=u'idActor', blank=True) # Field name made lowercase.
    idepisode = models.IntegerField(null=True, db_column=u'idEpisode', blank=True) # Field name made lowercase.
    strrole = models.TextField(db_column=u'strRole', blank=True) # Field name made lowercase.
    iorder = models.IntegerField(null=True, db_column=u'iOrder', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'actorlinkepisode'

class Actorlinkmovie(models.Model):
    idactor = models.IntegerField(null=True, db_column=u'idActor', blank=True) # Field name made lowercase.
    idmovie = models.IntegerField(null=True, db_column=u'idMovie', blank=True) # Field name made lowercase.
    strrole = models.TextField(db_column=u'strRole', blank=True) # Field name made lowercase.
    iorder = models.IntegerField(null=True, db_column=u'iOrder', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'actorlinkmovie'

class Actorlinktvshow(models.Model):
    idactor = models.IntegerField(null=True, db_column=u'idActor', blank=True) # Field name made lowercase.
    idshow = models.IntegerField(null=True, db_column=u'idShow', blank=True) # Field name made lowercase.
    strrole = models.TextField(db_column=u'strRole', blank=True) # Field name made lowercase.
    iorder = models.IntegerField(null=True, db_column=u'iOrder', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'actorlinktvshow'

class Actors(models.Model):
    idactor = models.IntegerField(primary_key=True, db_column=u'idActor', blank=True) # Field name made lowercase.
    stractor = models.TextField(db_column=u'strActor', blank=True) # Field name made lowercase.
    strthumb = models.TextField(db_column=u'strThumb', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'actors'
    
    def __unicode__(self):
        return u'%s' % (self.stractor)

class Artistlinkmusicvideo(models.Model):
    idartist = models.IntegerField(null=True, db_column=u'idArtist', blank=True) # Field name made lowercase.
    idmvideo = models.IntegerField(null=True, db_column=u'idMVideo', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'artistlinkmusicvideo'

class Bookmark(models.Model):
    idbookmark = models.IntegerField(primary_key=True, db_column=u'idBookmark', blank=True) # Field name made lowercase.
    idfile = models.IntegerField(null=True, db_column=u'idFile', blank=True) # Field name made lowercase.
    timeinseconds = models.TextField(db_column=u'timeInSeconds', blank=True) # Field name made lowercase. This field type is a guess.
    totaltimeinseconds = models.TextField(db_column=u'totalTimeInSeconds', blank=True) # Field name made lowercase. This field type is a guess.
    thumbnailimage = models.TextField(db_column=u'thumbNailImage', blank=True) # Field name made lowercase.
    player = models.TextField(blank=True)
    playerstate = models.TextField(db_column=u'playerState', blank=True) # Field name made lowercase.
    type = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'bookmark'

class Country(models.Model):
    idcountry = models.IntegerField(primary_key=True, db_column=u'idCountry', blank=True) # Field name made lowercase.
    strcountry = models.TextField(db_column=u'strCountry', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'country'

class Countrylinkmovie(models.Model):
    idcountry = models.IntegerField(null=True, db_column=u'idCountry', blank=True) # Field name made lowercase.
    idmovie = models.IntegerField(null=True, db_column=u'idMovie', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'countrylinkmovie'

class Directorlinkepisode(models.Model):
    iddirector = models.IntegerField(null=True, db_column=u'idDirector', blank=True) # Field name made lowercase.
    idepisode = models.IntegerField(null=True, db_column=u'idEpisode', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'directorlinkepisode'

class Directorlinkmovie(models.Model):
    iddirector = models.IntegerField(null=True, db_column=u'idDirector', blank=True) # Field name made lowercase.
    idmovie = models.IntegerField(null=True, db_column=u'idMovie', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'directorlinkmovie'

class Directorlinkmusicvideo(models.Model):
    iddirector = models.IntegerField(null=True, db_column=u'idDirector', blank=True) # Field name made lowercase.
    idmvideo = models.IntegerField(null=True, db_column=u'idMVideo', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'directorlinkmusicvideo'

class Directorlinktvshow(models.Model):
    iddirector = models.IntegerField(null=True, db_column=u'idDirector', blank=True) # Field name made lowercase.
    idshow = models.IntegerField(null=True, db_column=u'idShow', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'directorlinktvshow'

class Episode(models.Model):
    idepisode = models.IntegerField(primary_key=True, db_column=u'idEpisode', blank=True) # Field name made lowercase.
    idfile = models.IntegerField(null=True, db_column=u'idFile', blank=True) # Field name made lowercase.
    c00 = models.TextField(blank=True)
    c01 = models.TextField(blank=True)
    c02 = models.TextField(blank=True)
    c03 = models.TextField(blank=True)
    c04 = models.TextField(blank=True)
    c05 = models.TextField(blank=True)
    c06 = models.TextField(blank=True)
    c07 = models.TextField(blank=True)
    c08 = models.TextField(blank=True)
    c09 = models.TextField(blank=True)
    c10 = models.TextField(blank=True)
    c11 = models.TextField(blank=True)
    c12 = models.CharField(max_length=24, blank=True)
    c13 = models.CharField(max_length=24, blank=True)
    c14 = models.TextField(blank=True)
    c15 = models.TextField(blank=True)
    c16 = models.TextField(blank=True)
    c17 = models.CharField(max_length=24, blank=True)
    c18 = models.TextField(blank=True)
    c19 = models.TextField(blank=True)
    c20 = models.TextField(blank=True)
    c21 = models.TextField(blank=True)
    c22 = models.TextField(blank=True)
    c23 = models.TextField(blank=True)
    class Meta:
        db_table = u'episode'

class Files(models.Model):
    idfile = models.IntegerField(primary_key=True, db_column=u'idFile', blank=True) # Field name made lowercase.
    idpath = models.IntegerField(null=True, db_column=u'idPath', blank=True) # Field name made lowercase.
    strfilename = models.TextField(db_column=u'strFilename', blank=True) # Field name made lowercase.
    playcount = models.IntegerField(null=True, db_column=u'playCount', blank=True) # Field name made lowercase.
    lastplayed = models.TextField(db_column=u'lastPlayed', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'files'

class Genre(models.Model):
    idgenre = models.IntegerField(primary_key=True, db_column=u'idGenre', blank=True) # Field name made lowercase.
    strgenre = models.TextField(db_column=u'strGenre', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'genre'
        
    def __unicode__(self):
        return u'%s' % (self.strgenre)

class Genrelinkmovie(models.Model):
    idgenre = models.IntegerField(null=True, db_column=u'idGenre', blank=True) # Field name made lowercase.
    idmovie = models.IntegerField(null=True, db_column=u'idMovie', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'genrelinkmovie'

class Genrelinkmusicvideo(models.Model):
    idgenre = models.IntegerField(null=True, db_column=u'idGenre', blank=True) # Field name made lowercase.
    idmvideo = models.IntegerField(null=True, db_column=u'idMVideo', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'genrelinkmusicvideo'

class Genrelinktvshow(models.Model):
    idgenre = models.IntegerField(null=True, db_column=u'idGenre', blank=True) # Field name made lowercase.
    idshow = models.IntegerField(null=True, db_column=u'idShow', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'genrelinktvshow'

class Movie(models.Model):
    idmovie = models.IntegerField(primary_key=True, db_column=u'idMovie', blank=True) # Field name made lowercase.
    idfile = models.IntegerField(null=True, db_column=u'idFile', blank=True) # Field name made lowercase.
    title = models.TextField(blank=True, db_column=u'c00')
    movieplot = models.TextField(blank=True, db_column=u'c01')
    movielotoutline = models.TextField(blank=True, db_column=u'c02')
    movietagline = models.TextField(blank=True, db_column=u'c03')
    ratingvotes = models.TextField(blank=True, db_column=u'c04')
    rating = models.TextField(blank=True, db_column=u'c05')
    writers = models.TextField(blank=True, db_column=u'c06')
    yearreleased = models.TextField(blank=True, db_column=u'c07')
    thumbnails = models.TextField(blank=True, db_column=u'c08')
    idimbd = models.TextField(blank=True, db_column=u'c09')
    p = models.TextField(blank=True, db_column=u'c10')
    runtime = models.TextField(blank=True, db_column=u'c11')
    p1 = models.TextField(blank=True, db_column=u'c12')
    p2 = models.TextField(blank=True, db_column=u'c13')
    genre = models.TextField(blank=True, db_column=u'c14')
    director = models.TextField(blank=True, db_column=u'c15')
    originalmovietitle = models.TextField(blank=True, db_column=u'c16')
    p3 = models.TextField(blank=True, db_column=u'c17')
    studio = models.TextField(blank=True, db_column=u'c18')
    trailerurl = models.TextField(blank=True, db_column=u'c19')
    fanarturls = models.TextField(blank=True, db_column=u'c20')
    country = models.TextField(blank=True, db_column=u'c21')
    filepath = models.TextField(blank=True, db_column=u'c22')
    p4 = models.TextField(blank=True, db_column=u'c23')
    class Meta:
        db_table = u'movie'
    
    def get_trailer_url(self):
        url = self.trailerurl
        #plugin://plugin.video.youtube/?action=play_video&videoid=qYsyABPvtU0
        video_id = url.split("=")[-1] 
        utube_url = "http://www.youtube.com/watch?v=%s" % video_id
        return utube_url

class Movielinktvshow(models.Model):
    idmovie = models.IntegerField(null=True, db_column=u'idMovie', blank=True) # Field name made lowercase.
    idshow = models.IntegerField(null=True, db_column=u'IdShow', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'movielinktvshow'

class Musicvideo(models.Model):
    idmvideo = models.IntegerField(primary_key=True, db_column=u'idMVideo', blank=True) # Field name made lowercase.
    idfile = models.IntegerField(null=True, db_column=u'idFile', blank=True) # Field name made lowercase.
    c00 = models.TextField(blank=True)
    c01 = models.TextField(blank=True)
    c02 = models.TextField(blank=True)
    c03 = models.TextField(blank=True)
    c04 = models.TextField(blank=True)
    c05 = models.TextField(blank=True)
    c06 = models.TextField(blank=True)
    c07 = models.TextField(blank=True)
    c08 = models.TextField(blank=True)
    c09 = models.TextField(blank=True)
    c10 = models.TextField(blank=True)
    c11 = models.TextField(blank=True)
    c12 = models.TextField(blank=True)
    c13 = models.TextField(blank=True)
    c14 = models.TextField(blank=True)
    c15 = models.TextField(blank=True)
    c16 = models.TextField(blank=True)
    c17 = models.TextField(blank=True)
    c18 = models.TextField(blank=True)
    c19 = models.TextField(blank=True)
    c20 = models.TextField(blank=True)
    c21 = models.TextField(blank=True)
    c22 = models.TextField(blank=True)
    c23 = models.TextField(blank=True)
    class Meta:
        db_table = u'musicvideo'

class Path(models.Model):
    idpath = models.IntegerField(primary_key=True, db_column=u'idPath', blank=True) # Field name made lowercase.
    strpath = models.TextField(unique=True, db_column=u'strPath', blank=True) # Field name made lowercase.
    strcontent = models.TextField(db_column=u'strContent', blank=True) # Field name made lowercase.
    strscraper = models.TextField(db_column=u'strScraper', blank=True) # Field name made lowercase.
    strhash = models.TextField(db_column=u'strHash', blank=True) # Field name made lowercase.
    scanrecursive = models.IntegerField(null=True, db_column=u'scanRecursive', blank=True) # Field name made lowercase.
    usefoldernames = models.BooleanField(db_column=u'useFolderNames', blank=True) # Field name made lowercase.
    strsettings = models.TextField(db_column=u'strSettings', blank=True) # Field name made lowercase.
    noupdate = models.BooleanField(db_column=u'noUpdate', blank=True) # Field name made lowercase.
    exclude = models.BooleanField(blank=True)
    class Meta:
        db_table = u'path'

class Setlinkmovie(models.Model):
    idset = models.IntegerField(null=True, db_column=u'idSet', blank=True) # Field name made lowercase.
    idmovie = models.IntegerField(null=True, db_column=u'idMovie', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'setlinkmovie'

class Sets(models.Model):
    idset = models.IntegerField(primary_key=True, db_column=u'idSet', blank=True) # Field name made lowercase.
    strset = models.TextField(db_column=u'strSet', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'sets'

class Settings(models.Model):
    idfile = models.IntegerField(unique=True, null=True, db_column=u'idFile', blank=True) # Field name made lowercase.
    deinterlace = models.BooleanField(db_column=u'Deinterlace', blank=True) # Field name made lowercase.
    viewmode = models.IntegerField(null=True, db_column=u'ViewMode', blank=True) # Field name made lowercase.
    zoomamount = models.TextField(db_column=u'ZoomAmount', blank=True) # Field name made lowercase. This field type is a guess.
    pixelratio = models.TextField(db_column=u'PixelRatio', blank=True) # Field name made lowercase. This field type is a guess.
    verticalshift = models.TextField(db_column=u'VerticalShift', blank=True) # Field name made lowercase. This field type is a guess.
    audiostream = models.IntegerField(null=True, db_column=u'AudioStream', blank=True) # Field name made lowercase.
    subtitlestream = models.IntegerField(null=True, db_column=u'SubtitleStream', blank=True) # Field name made lowercase.
    subtitledelay = models.TextField(db_column=u'SubtitleDelay', blank=True) # Field name made lowercase. This field type is a guess.
    subtitleson = models.BooleanField(db_column=u'SubtitlesOn', blank=True) # Field name made lowercase.
    brightness = models.TextField(db_column=u'Brightness', blank=True) # Field name made lowercase. This field type is a guess.
    contrast = models.TextField(db_column=u'Contrast', blank=True) # Field name made lowercase. This field type is a guess.
    gamma = models.TextField(db_column=u'Gamma', blank=True) # Field name made lowercase. This field type is a guess.
    volumeamplification = models.TextField(db_column=u'VolumeAmplification', blank=True) # Field name made lowercase. This field type is a guess.
    audiodelay = models.TextField(db_column=u'AudioDelay', blank=True) # Field name made lowercase. This field type is a guess.
    outputtoallspeakers = models.BooleanField(db_column=u'OutputToAllSpeakers', blank=True) # Field name made lowercase.
    resumetime = models.IntegerField(null=True, db_column=u'ResumeTime', blank=True) # Field name made lowercase.
    crop = models.BooleanField(db_column=u'Crop', blank=True) # Field name made lowercase.
    cropleft = models.IntegerField(null=True, db_column=u'CropLeft', blank=True) # Field name made lowercase.
    cropright = models.IntegerField(null=True, db_column=u'CropRight', blank=True) # Field name made lowercase.
    croptop = models.IntegerField(null=True, db_column=u'CropTop', blank=True) # Field name made lowercase.
    cropbottom = models.IntegerField(null=True, db_column=u'CropBottom', blank=True) # Field name made lowercase.
    sharpness = models.TextField(db_column=u'Sharpness', blank=True) # Field name made lowercase. This field type is a guess.
    noisereduction = models.TextField(db_column=u'NoiseReduction', blank=True) # Field name made lowercase. This field type is a guess.
    nonlinstretch = models.BooleanField(db_column=u'NonLinStretch', blank=True) # Field name made lowercase.
    postprocess = models.BooleanField(db_column=u'PostProcess', blank=True) # Field name made lowercase.
    scalingmethod = models.IntegerField(null=True, db_column=u'ScalingMethod', blank=True) # Field name made lowercase.
    deinterlacemode = models.IntegerField(null=True, db_column=u'DeinterlaceMode', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'settings'

class Stacktimes(models.Model):
    idfile = models.IntegerField(unique=True, null=True, db_column=u'idFile', blank=True) # Field name made lowercase.
    times = models.TextField(blank=True)
    class Meta:
        db_table = u'stacktimes'

class Streamdetails(models.Model):
    idfile = models.IntegerField(null=True, db_column=u'idFile', blank=True) # Field name made lowercase.
    istreamtype = models.IntegerField(null=True, db_column=u'iStreamType', blank=True)  # Field name made lowercase.
    strvideocodec = models.TextField(db_column=u'strVideoCodec', blank=True) # Field name made lowercase.
    fvideoaspect = models.TextField(db_column=u'fVideoAspect', blank=True) # Field name made lowercase. This field type is a guess.
    ivideowidth = models.IntegerField(null=True, db_column=u'iVideoWidth', blank=True) # Field name made lowercase.
    ivideoheight = models.IntegerField(null=True, db_column=u'iVideoHeight', blank=True) # Field name made lowercase.
    straudiocodec = models.TextField(db_column=u'strAudioCodec', blank=True) # Field name made lowercase.
    iaudiochannels = models.IntegerField(null=True, db_column=u'iAudioChannels', blank=True) # Field name made lowercase.
    straudiolanguage = models.TextField(db_column=u'strAudioLanguage', blank=True) # Field name made lowercase.
    strsubtitlelanguage = models.TextField(db_column=u'strSubtitleLanguage', blank=True) # Field name made lowercase.
    ivideoduration = models.IntegerField(null=True, db_column=u'iVideoDuration', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'streamdetails'

class Studio(models.Model):
    idstudio = models.IntegerField(primary_key=True, db_column=u'idStudio', blank=True) # Field name made lowercase.
    strstudio = models.TextField(db_column=u'strStudio', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'studio'

class Studiolinkmovie(models.Model):
    idstudio = models.ForeignKey(Studio, db_column=u'idStudio')
    idmovie = models.ForeignKey(Movie, db_column=u'idMovie')
#    idstudio = models.IntegerField(null=True, db_column=u'idStudio', blank=True) # Field name made lowercase.
#    idmovie = models.IntegerField(null=True, db_column=u'idMovie', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'studiolinkmovie'

class Studiolinkmusicvideo(models.Model):
    idstudio = models.IntegerField(null=True, db_column=u'idStudio', blank=True) # Field name made lowercase.
    idmvideo = models.IntegerField(null=True, db_column=u'idMVideo', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'studiolinkmusicvideo'

class Studiolinktvshow(models.Model):
    idstudio = models.IntegerField(null=True, db_column=u'idStudio', blank=True) # Field name made lowercase.
    idshow = models.IntegerField(null=True, db_column=u'idShow', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'studiolinktvshow'

class Tvshow(models.Model):
    idshow = models.IntegerField(primary_key=True, db_column=u'idShow', blank=True) # Field name made lowercase.
    c00 = models.TextField(blank=True)
    c01 = models.TextField(blank=True)
    c02 = models.TextField(blank=True)
    c03 = models.TextField(blank=True)
    c04 = models.TextField(blank=True)
    c05 = models.TextField(blank=True)
    c06 = models.TextField(blank=True)
    c07 = models.TextField(blank=True)
    c08 = models.TextField(blank=True)
    c09 = models.TextField(blank=True)
    c10 = models.TextField(blank=True)
    c11 = models.TextField(blank=True)
    c12 = models.TextField(blank=True)
    c13 = models.TextField(blank=True)
    c14 = models.TextField(blank=True)
    c15 = models.TextField(blank=True)
    c16 = models.TextField(blank=True)
    c17 = models.TextField(blank=True)
    c18 = models.TextField(blank=True)
    c19 = models.TextField(blank=True)
    c20 = models.TextField(blank=True)
    c21 = models.TextField(blank=True)
    c22 = models.TextField(blank=True)
    c23 = models.TextField(blank=True)
    class Meta:
        db_table = u'tvshow'

class Tvshowlinkepisode(models.Model):
    idshow = models.IntegerField(null=True, db_column=u'idShow', blank=True) # Field name made lowercase.
    idepisode = models.IntegerField(null=True, db_column=u'idEpisode', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'tvshowlinkepisode'

class Tvshowlinkpath(models.Model):
    idshow = models.IntegerField(null=True, db_column=u'idShow', blank=True) # Field name made lowercase.
    idpath = models.IntegerField(null=True, db_column=u'idPath', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'tvshowlinkpath'

class Version(models.Model):
    idversion = models.IntegerField(null=True, db_column=u'idVersion', blank=True) # Field name made lowercase.
    icompresscount = models.IntegerField(null=True, db_column=u'iCompressCount', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'version'

class Writerlinkepisode(models.Model):
    idwriter = models.IntegerField(null=True, db_column=u'idWriter', blank=True) # Field name made lowercase.
    idepisode = models.IntegerField(null=True, db_column=u'idEpisode', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'writerlinkepisode'

class Writerlinkmovie(models.Model):
    idwriter = models.ForeignKey(Actors, db_column=u'idWriter')
    idmovie = models.ForeignKey(Movie, db_column=u'idMovie')
#    idwriter = models.IntegerField(null=True, db_column=u'idWriter', blank=True) # Field name made lowercase.
#    idmovie = models.IntegerField(null=True, db_column=u'idMovie', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'writerlinkmovie'


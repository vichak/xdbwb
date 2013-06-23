from django.db.models.base import ModelBase
from django.contrib import admin

from lib.models import Movie
from lib.models import models as xdbwb_models

admin.site.register(Movie)

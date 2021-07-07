from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Actors)
admin.site.register(Plays)
admin.site.register(Amplua)
admin.site.register(Staging)
admin.site.register(Tickets)
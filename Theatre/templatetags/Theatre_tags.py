from django import template
from Theatre.models import *

register = template.Library()

@register.simple_tag()
def get_actors():
    return Actors.objects.all()

@register.simple_tag()
def get_plays():
    return Plays.objects.all()

@register.simple_tag()
def get_roles():
    return Amplua.objects.all()



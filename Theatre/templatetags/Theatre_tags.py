from django import template
from Theatre.models import *

register = template.Library()

@register.simple_tag()
def get_actors():
    return Actors.objects.all()
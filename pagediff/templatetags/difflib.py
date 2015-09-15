import difflib 
from django import template

register = template.Library()

@register.filter(name='isjunk')
def isjunk(value):
    """ According to difflib, is line junk? """
    return difflib.IS_LINE_JUNK(value)
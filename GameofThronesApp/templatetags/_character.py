from django import template

register = template.Library()

@register.filter
def _character(value,arg):
	print("Here")
	return value.replace(arg,'_')
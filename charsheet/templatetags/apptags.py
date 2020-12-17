from django import template

register = template.Library()

@register.filter
def percentage(value):
	try:
		return "{:.0%}".format(value)
	except (ValueError):
		return ""
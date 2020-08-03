from django import template


register = template.Library()

@register.filter
def inc(a, b):
	return int(a) + int(b)

@register.simple_tag
def division(a, b, to_int = False):
	otvet = int(a) / int(b)
	if to_int:
		return int(otvet)
	else:
		return otvet


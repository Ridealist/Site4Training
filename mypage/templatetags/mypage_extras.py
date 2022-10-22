from django import template

register = template.Library()

@register.filter
def addstr(arg1, arg2):
    return str(arg1)+str(arg2)

@register.filter
def divide(arg1, arg2):
    return arg1//arg2

@register.filter
def multi(arg1, arg2):
    return arg1*arg2

# @register.filter
# def url_split(arg1):
#     if str(arg1)[-1] == '/':
#         url = str(arg1)[:-1]
#     else:
#         url = str(arg1)
#     ind = url.rfind('/')
#     if ind > 40:
#         result = url[:ind]
#     else:
#         result = url
#     return result

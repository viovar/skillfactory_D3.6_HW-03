from datetime import datetime

from django import template


register = template.Library()

# @register.filter()
# def currency(value):
#     """
#     value:
#     :param value:
#     :return:
#     """
#     return F'{value} P'


@register.simple_tag()
def current_time(format_string='%b %d %Y'):
   return datetime.utcnow().strftime(format_string)


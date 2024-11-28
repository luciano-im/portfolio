from django import template
import readtime

register = template.Library()


@register.simple_tag
def get_reading_time(content):
    return readtime.of_markdown(content)
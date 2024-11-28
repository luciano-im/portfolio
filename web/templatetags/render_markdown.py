from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe
import markdown

register = template.Library()


@register.filter
@stringfilter
def render_markdown(content):
    md = markdown.markdown(content, extensions=["fenced_code", "codehilite"])
    return mark_safe(md)

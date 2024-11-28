from django import template
import markdown

register = template.Library()


@register.simple_tag
def get_html_from_markdown(content):
    return markdown.markdown(content)
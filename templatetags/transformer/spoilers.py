from django import template

register = template.Library()


@register.inclusion_tag('transformer/spoiler.html')
def object_list(todo: dict):
    # {operation: [cols]}
    return todo

from django import template
from utils import get_model_by_appname

register = template.Library()


@register.inclusion_tag('base/object_list.html')
def object_list(qset):
    context = {'qset': qset}
    return context


@register.inclusion_tag('base/like_save.html')
def like_save_tag(user, app_name: str, post):
    model = get_model_by_appname(app_name)
    if not model:
        raise ValueError
    likeds = eval(f"user.liked_{app_name}.all()")
    saveds = eval(f"user.treasure.{app_name}.all()")
    context = {'likeds': likeds, 'saveds': saveds, 'post': post}
    return context


@register.inclusion_tag('base/support_save.html')
def support_save_tag(user, app_name: str, post):
    model = get_model_by_appname(app_name)
    if not model:
        raise ValueError(f"incorrect app name: {app_name}")

    if app_name == 'answer':
        supporteds = eval(f"user.supported_{app_name}.all()")
        context = {'supporteds': supporteds, 'post': post, 'is_answer': True}
        return context

    else:
        supporteds = eval(f"user.supported_{app_name}.all()")
        saveds = eval(f"user.treasure.{app_name}.all()")
        context = {'supporteds': supporteds, 'saveds': saveds, 'post': post}
        return context

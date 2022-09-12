from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect

from apps.blog.models import Blog
from apps.forum.models import Question, Answer


def get_model_by_appname(app_name: str):
    app_list = ['blog', 'question', 'answer']
    if app_name not in app_list:
        return None
    if app_name == 'blog':
        return Blog
    elif app_name == 'question':
        return Question
    elif app_name == 'answer':
        return Answer


def get_top_n(n: int = 5):
    """
    returns a dict of top n posts from all apps

    """
    qsets = {}
    qsets['blogs'] = Blog.objects.all().order_by('-date_created')[:n]
    qsets['questions'] = Question.objects.all().order_by('-date_created')[:n]

    return qsets


def get_object_or_none(model, pk):
    try:
        obj = model.objects.get(pk=pk)
        return obj
    except:
        return None


def search_in_apps(text: str, in_content=False):
    """
    takes string for searching and searchs in all app's
    models. Returns dict of querysets, where each of keys are
    name of app and walues are the querysets.
    in_content makes including contents of posts also to
    searching.

    """

    def search_in(model):
        if not in_content:
            posts = model.objects.filter(title__icontains=text).order_by("-date_created")
        else:
            posts = model.objects.filter(Q(title__icontains=text) | Q(content__icontains=text)).order_by(
                "-date_created")
        return posts

    apps = {'blogs': Blog, 'questions': Question}
    qsets = {}
    for app_name in apps.keys():
        app_name = str(app_name)
        posts = search_in(apps[app_name])
        if posts:
            qsets[app_name] = posts

    return qsets


def search_by_upi(code_str: str):
    """"
        Takes code string as '<app><id_num>'
        and returns post with 'id_num' id of
        'app' application's model.

        Abbrivations for apps:
        {'b':blog, 'e':events, 'fq': forum-question,'n': news, 'v': vacancy}

    """

    app_list = ['b', 'fa', 'fq']
    try:
        app = code_str[:code_str.index(':')]
        ID = code_str[code_str.index(':') + 1:]
        if app not in app_list:
            post = None
        elif app == 'b':
            from apps.blog.models import Blog
            post = get_object_or_none(Blog, pk=ID)

        if app == 'fq':
            from apps.forum.models import Question
            post = get_object_or_none(Question, pk=ID)

    except ValueError:
        post = None

    return post

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import FileUploadForm

import json

from .ds.load_table import read_csv_return_html, get_basic_stats
from .ds.transforming import restore_user_file, load_hdf_to, select_dtypes, apply_todo


class Transformer(View, LoginRequiredMixin):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('login')
        template_name = "transformer/t.html"
        form = FileUploadForm()
        context = {'file_form': form}
        return render(request, template_name, context=context)

    def post(self, request):
        if not request.user.is_authenticated:
            return redirect('login')

        delimiter = request.POST['delimiter']
        template_name = "transformer/t.html"
        file = request.FILES['file']
        n_rows = 10
        r = read_csv_return_html(file, n_rows,username=request.user.user_name, html=True,
                                 html_index=False, stat_table_to_html=True)
        return JsonResponse(r)


class Transforming(View, LoginRequiredMixin):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('login')

        data = restore_user_file(request.user.user_name)
        stat = get_basic_stats(data, to_html=True)
        dtypes = select_dtypes(data)
        r = load_hdf_to(username=request.user.user_name, to_html=True, index=False)
        template_name = "transformer/ting.html"
        context = {'table': r, 'numerics': dtypes['numerics'], 'categorics': dtypes['categorics'],
                   'row_col': stat['row_col'], 'null_dtype': stat['stat_table']}
        return render(request, template_name, context)

    def post(self, request):
        if not request.user.is_authenticated:
            return redirect('login')
        data = dict(json.loads(request.body))
        todo = data['todo']
        todo = {k: v for k, v in todo.items() if v}
        tables = apply_todo(request.user.user_name, todo)
        return JsonResponse(tables)


class Analysing(View, LoginRequiredMixin):
    def get(self, request):
        data = restore_user_file(request.user.user_name)
        template_name = "transformer/aing.html"
        return render(request, template_name)

    def post(self, request):
        pass

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import FileUploadForm

import json

from .ds.load_table import read_csv_return_html, get_basic_stats
from .ds.transforming import _restore_file, load_hdf_to, select_dtypes, apply_todo


class Transformer(View, LoginRequiredMixin):
    def get(self, request):
        template_name = "transformer/t.html"
        form = FileUploadForm()
        context = {'file_form': form}
        return render(request, template_name, context=context)

    def post(self, request):
        delimeter = request.POST['delimeter']
        template_name = "transformer/t.html"
        file = request.FILES['file']
        r = read_csv_return_html(file, 20, html=True, html_index=False, stat_table_to_html=True)
        print(r)
        return JsonResponse(r)


class Transforming(View, LoginRequiredMixin):
    def get(self, request):
        data = _restore_file()
        stat = get_basic_stats(data, to_html=True)
        dtypes = select_dtypes(data)
        r = load_hdf_to(to_html=True, index=False)
        template_name = "transformer/ting.html"
        context = {'table': r, 'numerics': dtypes['numerics'], 'categorics': dtypes['categorics'],
                   'row_col': stat['row_col'], 'null_dtype': stat['stat_table']}
        return render(request, template_name, context)

    def post(self, request):
        data = dict(json.loads(request.body))
        todo = data['todo']
        todo = {k: v for k, v in todo.items() if v}
        tables = apply_todo(todo)
        print(tables)
        return JsonResponse(tables)


class Analising(View, LoginRequiredMixin):
    def get(self, request):
        data = _restore_file()
        template_name = "transformer/aing.html"
        return render(request, template_name)

    def post(self, request):
        pass

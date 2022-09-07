from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic import View

from .forms import FileUploadForm

from .ds.load_table import read_csv_return_html
from .ds.transforming import _restore_file


class Transformer(View):
    def get(self, request):
        template_name = "transformer/t.html"
        form = FileUploadForm()
        context = {'file_form':form}
        return render(request, template_name, context = context)

    def post(self, request):
        delimeter = request.POST['delimeter']
        template_name = "transformer/t.html"
        file = request.FILES['file']
        r = read_csv_return_html(file, 20, html = True)
        # print(r)
        return JsonResponse(r)

class Transforming(View):
    def get(self, request):
        data = _restore_file()
        template_name = "transformer/ting.html"
        return render(request,template_name)

    def post(self, request):
        pass


class Analising(View):
    def get(self, request):
        data = _restore_file()
        template_name = "transformer/aing.html"
        return render(request,template_name)

    def post(self, request):
        pass
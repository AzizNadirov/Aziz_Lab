from django.shortcuts import render
from django.views.generic import View, ListView, DetailView

from .forms import FileUploadForm

from DS_side.transformer.funcs import read_csv_return_json

class Transformer(View):
    def get(self, request):
        template_name = "transformer/t.html"
        form = FileUploadForm()
        context = {'file_form':form}
        return render(request, template_name, context = context)

    def post(self, request):
        template_name = "transformer/t.html"
        form = FileUploadForm(data = request.POST, files = request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            print(read_csv_return_json(file, 3))
            return render(request, template_name)

        else:
            context = {'file_form':form}
            return render(request, template_name, context = context)
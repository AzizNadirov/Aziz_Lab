from django.shortcuts import render
from django.views.generic import View, ListView, DetailView

class Transformer(View):
    def get(self, request):
        template_name = "transformer/t.html"
        return render(request, template_name)
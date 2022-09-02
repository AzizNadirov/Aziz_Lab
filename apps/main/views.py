from django.shortcuts import render, reverse
from django.views.generic import View, ListView, DetailView


class HomePageView(View):
    def get(self,request):
        template_name = "main/home_page.html"
        return render(request, template_name)
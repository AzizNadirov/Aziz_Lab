from django.shortcuts import render
from django.views.generic import View


class LoadFileView(View):
    def post(self, request):
        
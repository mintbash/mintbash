# Imports
from django.views.generic import View
from django.shortcuts import render, redirect


# Views
class HomeView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, "crypto/home.html", context=context)

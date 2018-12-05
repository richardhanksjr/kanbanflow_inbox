from django.shortcuts import render
from django.views import View

# Create your views here.
class InboxItem(View):
    def get(self, request, *args, **kwargs):
        pass

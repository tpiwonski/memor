from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'main/home.html'

    def __init__(self):
        pass

    def get_context_data(self, **kwargs):
        return dict(hello_message="Welcome", current_date="never")

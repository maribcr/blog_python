# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
from django.conf import settings
from django.core.urlresolvers import reverse_lazy
from pip.utils import logging
from .models import Cadastro, Carro
from django.views.generic import CreateView, ListView
from django.http import HttpResponse


# def cadastro_list(request):
#     cadastro = Cadastro.objects.all()
#     context = {
#         'cadastro_list': cadastro
#     }
#
#     return render(request, 'cadastro/template/lista.html', context)


class FrontendCadastroView(CreateView):
    def get(self, request, *args, **kwargs):
        try:
            with open(os.path.join(settings.REACT_APP_DIR, 'build', 'home.html')) as f:
                return HttpResponse(f.read())
        except FileNotFoundError:
            logging.exception()
            return HttpResponse(
                """
                This URL is only used when you have built the production
                version of the app. Visit http://localhost:3000/ instead, or
                run `yarn run build` to test the production version.
                """,
                status=501,
            )


class Cadastro(CreateView):
    template_name = 'cadastro.html'
    model = Cadastro
    success_url = reverse_lazy('lista')


class Lista(ListView):
    template_name = 'lista.html'
    model = Carro
    context_object = 'nome'

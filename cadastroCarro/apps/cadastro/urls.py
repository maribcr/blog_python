from django.conf.urls import url
from apps.cadastro import views
from apps.cadastro.views import Cadastro

urlpatterns = [
    url('^$', views.FrontendCadastroView.as_view(), name='home'),
    url('^cadastro/$', Cadastro.as_view(), name='cadastro'),
]


from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^json/$', views.gerajson, name='gerajson'),
    url(r'^sobre/$', views.sobre, name='sobre')

]
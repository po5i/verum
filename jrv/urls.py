from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^voluntario/$', views.voluntario, name='voluntario'),
    url(r'^faq/$', views.faq, name='faq'),
    url(r'^resultados/$', views.resultados, name='resultados'),
    url(r'^opendata/$', views.opendata, name='opendata'),
    url(r'^register/$', views.register, name='register'),
    url(r'^acta/(?P<acta_id>[0-9]+)/$', views.acta, name='acta'),
    url(r'^reportar/(?P<acta_id>[0-9]+)/$', views.reportar, name='reportar'),
]

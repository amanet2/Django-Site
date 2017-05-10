from django.conf.urls import url

from . import views

app_name='scenebuilder'
urlpatterns = [
    # ex: /scenebuilder/
    url(r'^$', views.index, name='index'),
]
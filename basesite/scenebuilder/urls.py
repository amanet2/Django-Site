from django.conf.urls import url

from . import views

app_name='scenebuilder'
urlpatterns = [
    # ex: /scenebuilder/
    # url(r'^$', views.index, name='index'),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^templates/$', views.TemplateView.as_view(), name='templates'),
    url(r'^dictionary/$', views.DictionaryView.as_view(), name='dictionary'),
    url(r'^objects/$', views.CodesView.as_view(), name='objects')
]
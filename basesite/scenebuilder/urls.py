from django.conf.urls import url

from . import views

app_name='scenebuilder'
urlpatterns = [
    # ex: /scenebuilder/
    # url(r'^$', views.index, name='index'),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^dictionary/$', views.DictionaryView.as_view(), name='dictionary'),
    url(r'^objects/$', views.CodesView.as_view(), name='objects'),
    url(r'^buildyourown/$', views.BuildYourOwnView.as_view(), name='buildyourown'),
    url(r'^maps/$', views.AllMapsView.as_view(), name='allmaps'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<map_id>[0-9]+)/download/$', views.download, name='download')
]
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.utils import timezone
from .custom import template
from .models import Map
import os
from django.conf import settings
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'scenebuilder/index.html')



def download(request, map_id):
    map = get_object_or_404(Map, pk=map_id)

    file_path = os.path.join(settings.MEDIA_ROOT, f'downloadable_maps/{map_id}.map')
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    return HttpResponse

class AllMapsView(generic.ListView):
    template_name = 'scenebuilder/allmaps.html'
    context_object_name = 'all_maps_list'

    def get_queryset(self):
        return Map.objects.all()

class DetailView(generic.DetailView):
    model = Map
    template_name = 'scenebuilder/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Map.objects.filter(map_date__lte=timezone.now())

class IndexView(generic.ListView):
    returnlist = []
    mapname = template.MapDoc.new_map.source

    for scene in template.MapDoc.new_map.scenes:
        returnlist.append(f'Scene {mapname}/{scene.name}')

    template_name = 'scenebuilder/index.html'
    context_object_name = 'scene_template'

    def get_queryset(self):
        return self.returnlist

class DictionaryView(generic.ListView):
    returnlist = []
    scene_dict = template.MapDoc.new_map.obj_defs
    for key in scene_dict:
        returnlist.append(f'{key}: {scene_dict[key]}')

    template_name = 'scenebuilder/dictionary.html'
    context_object_name = 'scene_template'

    def get_queryset(self):
        return self.returnlist

class CodesView(generic.ListView):
    returnlist = []
    code_dict = template.MapDoc.new_map.obj_codes
    for key in code_dict:
        returnlist.append(f'{key}: {code_dict[key]}')

    template_name = 'scenebuilder/objects.html'
    context_object_name = 'scene_template'

    def get_queryset(self):
        return self.returnlist

class BuildYourOwnView(generic.ListView):
    returnlist = []
    obj_map = template.MapDoc.new_map.obj_defs
    for var in obj_map:
        returnlist.append(f'{var}-{obj_map[var]}')

    template_name = 'scenebuilder/buildyourown.html'
    context_object_name = 'scene_template'

    def get_queryset(self):
        return self.returnlist
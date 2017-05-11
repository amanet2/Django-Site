from django.shortcuts import render
from django.views import generic
from .custom import template

# Create your views here.
def index(request):
    return render(request,'scenebuilder/index.html')

class TemplateView(generic.ListView):
    returnlist = []

    returnlist.append(template.MapDoc.scene_grid0)
    returnlist.append(template.MapDoc.scene_grid1)
    returnlist.append(template.MapDoc.scene_grid2)

    scene_dict = template.MapDoc.new_map.obj_codes
    for key in scene_dict:
        returnlist.append(f'{key}: {scene_dict[key]}')

    template_name = 'scenebuilder/templates.html'
    context_object_name = 'scene_template'

    def get_queryset(self):
        return self.returnlist

class IndexView(generic.ListView):
    returnlist = []
    scene_dict = template.MapDoc.new_map.obj_defs
    for key in scene_dict:
        returnlist.append(f'{key}: {scene_dict[key]}')

    template_name = 'scenebuilder/index.html'
    context_object_name = 'scene_template'
    print(returnlist)
    def get_queryset(self):
        return self.returnlist

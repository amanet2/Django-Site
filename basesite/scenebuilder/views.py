from django.shortcuts import render
from django.views import generic
from .custom import template

# Create your views here.
def index(request):
    return render(request,'scenebuilder/index.html')

class IndexView(generic.ListView):
    returnlist = []
    mapname = template.MapDoc.new_map.source

    for scene in template.MapDoc.new_map.scenes:
        returnlist.append(f'Scene {mapname}/{scene.name}')

    template_name = 'scenebuilder/index.html'
    context_object_name = 'scene_template'

    def get_queryset(self):
        return self.returnlist

class TemplateView(generic.ListView):
    returnlist = []
    scene_grids = [
        template.MapDoc.scene_grid0,
        template.MapDoc.scene_grid1,
        template.MapDoc.scene_grid2
    ]
    i=0
    for scene in template.MapDoc.new_map.scenes:
        returnlist.append(scene.name)
        returnlist.append(scene_grids[i])
        i+=1

    template_name = 'scenebuilder/templates.html'
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
    returnlist = [template.MapDoc.scene_grid0]

    template_name = 'scenebuilder/buildyourown.html'
    context_object_name = 'scene_template'

    def get_queryset(self):
        return self.returnlist
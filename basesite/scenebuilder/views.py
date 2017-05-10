from django.shortcuts import render
from django.views import generic
from .custom import template

# Create your views here.
def index(request):
    return render(request,'scenebuilder/index.html')

class IndexView(generic.ListView):
    model = template.MapDoc.scene_grid0
    model1 = template.MapDoc.scene_grid1
    model2 = template.MapDoc.scene_grid2
    scene_dict = template.MapDoc.new_map.obj_codes

    template_name = 'scenebuilder/index.html'
    context_object_name = 'scene_template'

    def get_queryset(self):
        return [self.scene_dict,self.model,self.model1,self.model2]

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

    i = 0
    for line in model:
        if i != 0 and i%30 == 0:
            line += '\n'
            print('yes')

    template_name = 'scenebuilder/index.html'
    context_object_name = 'scene_template'

    def get_queryset(self):
        return [self.model,self.model1,self.model2]

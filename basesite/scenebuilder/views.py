from django.shortcuts import render
from django.views import generic
from .custom import template

# Create your views here.
def index(request):
    return render(request,'scenebuilder/index.html')

class IndexView(generic.DetailView):
    model = template.MapDoc.scene_grid0
    template_name = 'scenebuilder/index.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())
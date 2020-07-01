from django.http import HttpResponse, Http404
from django.shortcuts import render

from .models import Story
# Create your views here.
def home_view(request, *args, **kwargs):
    return HttpResponse("<h1>This is the Microfiction Site<h1>")

def story_detail_view(request, story_id,  *args, **kwargs):
    try:
        obj = Story.objects.get(id=story_id)
    except:
        raise Http404
    return HttpResponse(f"<h1>Hello {story_id} - {obj.content}<h1>")
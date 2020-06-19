from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    print(args, kwargs)
    return HttpResponse("<h1>Microfiction Site<h1>")

def story_detail_view(request, story_id,  *args, **kwargs):
    print(args, kwargs)
    return HttpResponse(f"<h1>Hello {story_id}<h1>")
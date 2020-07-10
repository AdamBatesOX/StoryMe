import random
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render

from .models import Story

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "pages/home.html", context={}, status=200)



def story_list_view(request,*args, **kwargs):
    """
    REST API VIEW
    Consume by JavaScript or Swift/Java/iOS/Android
    return json data
    """
    qs = Story.objects.all()
    stories_list = [{"id": x.id, "content": x.content, "likes": random.randint(0, 500)} for x in qs]
    data = {
        "isUser": False,
        "response": stories_list
    }
    return JsonResponse(data)



def story_detail_view(request, story_id,  *args, **kwargs):
    """
    REST API VIEW
    Consume by JavaScript or Swift/Java/iOS/Android
    return json data
    """
    data = {
        "id": story_id,
    }
    status = 200
    try:
        obj = Story.objects.get(id=story_id)
        data['content'] = obj.content
    except:
        data['message'] - "Not found"
        status = 404
    return JsonResponse(data, status=status) # json.dumps content_type='application/json'python3 
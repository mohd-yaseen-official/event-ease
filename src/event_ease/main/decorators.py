import json

from django.shortcuts import render
from django.http import HttpResponse

from events.models import Event


def allow_self(function):
    def wrapper(request, *args, **kwargs):

        id = kwargs["id"]

        if not Event.objects.filter(id=id, customer__user=request.user).exists():
            
            if request.headers.get("x-requested-with") == "XMLHttpsRequest":
                
                response_data = {
                    "message": "You are not authorized to make changes in this event",
                    "title": "Unauthorized",
                    "status": "error",
                    "redirect": False,
                    "redirect_url": "",
                }

                return HttpResponse(json.dumps(response_data), content_type="application/json")

            else:
                return render(request, 'authentication/authentication-failed.html')
            
        return function(request, *args, **kwargs)
    
    return wrapper
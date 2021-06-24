"""Estas son las vistas de juanjoGram"""
from django.http import HttpResponse
#utilities
from datetime import datetime



def greating(request):
    
    now= datetime.now().strftime('%b %dth %Y -%H:%M hrs')
    return HttpResponse('Hello World the actual time is  :  {now}'.format(now=now))

def hi(request,name,age):
    if age<18:
     message='Sorry {} you are not allowed '.format(name)   
   
    else:
     message='Hello {} Welcome to JuanJoGram'.format(name)

    return HttpResponse(message)
   
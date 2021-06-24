""" Posts views"""
#Django imports
from django.shortcuts import render
#utilities
from datetime import datetime
#Creo Diccionario de Posts

posts=[{
    'title': 'Fiesta Loca',
    'user':{ 
        'name':'jjestrada',
        'picture':'https://www.pexels.com/photo/black-and-white-cat-in-front-of-black-and-white-front-load-washing-machine-4975907/'
        },
        'timestamp': datetime.now(),
        'photo':'https://www.pexels.com/photo/animal-big-fur-zoo-4468189/' 

    },
    {
    'title': 'Viaje a NY',
    'user':{ 
        'name':'Cvanjercito',
        'picture':'https://www.pexels.com/photo/topless-man-with-black-eyes-7519434/'

        },
    'timestamp': datetime.now(),
    'picture':'https://images.unsplash.com/photo-1624215824600-ed3118b76873?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=750&q=80'
    

    },
    {
    'title': 'Primer dia de clases',
    'user':{ 
        'name':'jpcuervo',
        'picture':'https://images.pexels.com/photos/4550259/pexels-photo-4550259.jpeg?cs=srgb&dl=pexels-salus-natura-suprema-lex-esto-4550259.jpg&fm=jpg'

        },
    'timestamp': datetime.now(),
    'picture':'https://images.pexels.com/photos/4436390/pexels-photo-4436390.jpeg?cs=srgb&dl=pexels-el%C3%ADas-manuel-4436390.jpg&fm=jpg'
    

    },
    ]
 
def list_posts(request):
    return render(request,'feed.html',{'posts':posts})
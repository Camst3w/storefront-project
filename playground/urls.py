from django.urls import path
from . import views # . is current folder

# URLConfb
urlpatterns = [
    path("hello/", views.say_hello) # not calling function, just passing a reference (not views.say_hello())
]
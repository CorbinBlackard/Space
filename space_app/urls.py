from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('planet/<int:id>', views.planet),
    path('measure/<int:item_id>/<int:planet_id>', views.measure),
    path('create', views.create),
    path('add', views.add),
    path('update/<int:id>', views.update),
    path('updatePlanet/<int:id>', views.updatePlanet)
]
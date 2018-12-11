# accounts/urls.py
from django.urls import path
from .views import objectApprove
from .views import eventsView
from django.conf.urls import url

urlpatterns = [
    #url('events', views.EventsView, name='events'),
    path('', eventsView, name='events'),
    #path('events/', include('events.urls'))
    #url(r'^(?P<object_id>[0-9]+)/delete/$', views.objectDelete, name='delete_object')
    path('approve/<int:pk>',objectApprove, name="approve"),
]


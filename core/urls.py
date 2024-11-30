from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),

    path('', views.index, name='index'),
    path('add-venue/', views.add_venue, name='add_venue'),
    path('venues/', views.venue_list, name='venue-list'),
    path('add-wedding/', views.add_event, name='add-wedding'),
    path('<int:wedding_id>/add-guest/', views.add_guest, name='add-guest'),
    path('events/', views.user_events, name='user-events'),
    path('events/<int:event_id>/delete/', views.delete_event, name='delete-event'),
    path('guests/<int:guest_id>/delete/', views.delete_guest, name='delete-guest'),
    path('update-guest/<int:guest_id>/', views.update_guest, name='update-guest'),
    path('<int:event_id>/', views.event_detail, name='event-detail'),

    
    path('my-weddings/', views.user_events, name='user-events'),
]
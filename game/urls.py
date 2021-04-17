from django.urls import path
from game import views

urlpatterns = [
    path('list/', views.UserGameListView.as_view(), name='game_list'),
    path('detail/<uuid:game_id>/', views.GameDetailView.as_view(), name='game_details'),
    path('new/', views.NewGame.as_view(), name='new_game'),
    path('detail/<uuid:game_id>/choose/<int:char_id>/', views.select_character, name='select-character'),
]

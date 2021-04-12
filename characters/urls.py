from django.urls import path
from characters import views

urlpatterns = [
    path(
        'create/',
        views.NewCharacterView.as_view(),
        name='new-character'
    ),
    path(
        'view/',
        views.CharacterDetailView.as_view(),
        name='view_characters'
    ),
]

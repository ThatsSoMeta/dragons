from django.urls import path
from characters import views

urlpatterns = [
    path(
        'create/',
        views.NewCharacterView.as_view(),
        name='new-character'
    ),
]

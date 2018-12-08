from django.urls import path

from .views import CommentView, RatingView, ThankView


urlpatterns = [
    path('', RatingView.as_view(), name='ratings'),
    path('<str:rating>/', CommentView.as_view(), name='comments'),
    path('thanks', ThankView.as_view(), name='thanks')
]

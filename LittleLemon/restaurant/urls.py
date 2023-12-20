#define URL route for index() view
from django.urls import path
from . import views
from .views import *
from django.urls import path, include






urlpatterns = [
    path('booking/', bookingView.as_view()),
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
]

from django.urls import path

from .views import ApplicationUserListView, ApplicationUserDetail

urlpatterns = [
    path('user/', ApplicationUserListView.as_view()),
    path('user/<int:pk>', ApplicationUserDetail.as_view()),
]

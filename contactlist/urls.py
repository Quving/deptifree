from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from contactlist import views

urlpatterns = [
    path('contactlist', views.ContactListList.as_view()),
    path('contactlist/<int:pk>', views.ContactListDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from dept import views

urlpatterns = [
    path('simpledept', views.SimpleDeptList.as_view()),
    path('simpledept/<int:pk>', views.SimpleDeptDetail.as_view()),
    # path('complexdept', views.OneToManyDeptList.as_view()),
    # path('complexdept/<int:pk>', views.OneToManyDeptDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

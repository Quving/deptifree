from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from dept import views

urlpatterns = [
	path('onetoonedept', views.OneToOneDeptList.as_view()),
	path('onetoonedept/<int:pk>', views.OneToOneDeptDetail.as_view()),
	path('onetomanydept', views.OneToManyDeptList.as_view()),
	path('onetomanydept/<int:pk>', views.OneToManyDeptDetail.as_view()),
	path('users/', views.UserList.as_view()),
	path('users/<int:pk>/', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

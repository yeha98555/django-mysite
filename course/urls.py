from django.urls import path
from django.views.generic import TemplateView
from .views import CourseListView, CourseCreateView, CourseDeleteView, CourseDetailView

app_name = 'course'

urlpatterns = [
    path('', TemplateView.as_view(template_name='course/home.html')),
    path('course-list/', CourseListView.as_view(), name='course_list'), 
    path('course-create/', CourseCreateView.as_view(), name='course_create'), 
    path('course-delete/<int:pk>/', CourseDeleteView.as_view(), name='course_delete'),
    path('course-detail/<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
]

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import CustomLoginView

pp_name = 'prints'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('add_material/', views.add_material, name='add_material'),
    path('add_print_job/', views.add_print_job, name='add_print_job'),
    path('all/', views.all_print_jobs, name='all_print_jobs'),
    path('update_print_job/<int:pk>/', views.update_print_job, name='update_print_job'),
    path('remove_print_job/<int:pk>/', views.remove_print_job, name='remove_print_job'),
    path('add_print_error/', views.add_print_error, name='add_print_error'),
    path('all_print_errors/', views.all_print_errors, name='all_print_errors'),
    path('upload_stl/', views.upload_stl, name='upload_stl'),
    path('stream-page/', views.streaming_page, name='streaming_page'),
    path('stream/', views.stream_video, name='stream_video'),
    path('materials/edit/<int:material_id>/', views.edit_material, name='edit_material'),
    path('materials/', views.all_materials, name='all_materials'),
    path('materials/remove/<int:material_id>/', views.remove_material, name='remove_material'),
    path('stl_files/', views.stl_files, name='stl_files'),
    path('remove_stl/<int:stl_id>/', views.remove_stl, name='remove_stl'),
    path('remove_print_error/<int:error_id>/', views.remove_print_error, name='remove_print_error'),
    path('print_errors/', views.add_print_error, name='add_print_error'),
    path('print_errors/change_status/<int:error_id>/', views.change_print_error_status, name='change_status'),
    path('print_errors/list/', views.all_print_errors, name='all_print_errors'),
    path('update_print_error_status/<int:error_id>/', views.update_print_error_status, name='update_print_error_status'),
    path('remove_print_error/<int:error_id>/', views.remove_print_error, name='remove_print_error'),
]
from django.urls import path

# logout
from django.contrib.auth.views import LogoutView

from . import views


urlpatterns = [
    path('login/', views.LoginPage.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page='login'), name="logout"),
    path('', views.TaskList.as_view(), name="tasks"),
    path('task/<int:pk>/', views.TaskDetail.as_view(), name="task"),
    path('create-task/', views.TaskCreate.as_view(), name="task-create"),
    path('task-update/<int:pk>/', views.TaskUpdate.as_view(), name="task-update"),
    path('task-delete/<int:pk>/', views.TaskDelete.as_view(), name="task-delete"),
]


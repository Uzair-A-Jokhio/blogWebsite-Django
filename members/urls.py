from django.urls import path
from . import views
from .views import UserEditView

urlpatterns = [
    path('login_user/', views.login_user, name='login'),
    path('logout_user/', views.logout_user, name='logout'),
    path('signup/', views.signup_user, name='signup'),
    path('edit_profile/', UserEditView.as_view() , name='edit_profile'),
]
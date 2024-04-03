from django.urls import path
from . import views
from .views import AddCategoryview


urlpatterns = [
    # path('/home', views.home, name='home'),
    path('', views.product_list, name='product_list'),
    path('contact/', views.contact_page, name='contact_page'),
    path('blog/<int:pk>/', views.product_detail, name='product_detail'),
    path('blog/<int:pk>/edit/', views.edit_product, name='edit_product'),
    path('blog/<int:pk>/delete/', views.delete_product, name='delete_product'),
    path('about/', views.about_page, name='about_page'),
    path('search/', views.search_bar, name="search_bar"),
    # path('add_post/',AddPostBlog.as_view() , name='add_post'),
    path('add_post/', views.post_blog, name='add_post'),
    path('add_category/', AddCategoryview.as_view(),name='add_category' )
]
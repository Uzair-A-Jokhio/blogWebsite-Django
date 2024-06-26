from django.urls import path
from . import views
from .views import AddCategoryview, HomeView, ArticalDetailView


urlpatterns = [
    # path('/home', views.home, name='home'),
    path('', HomeView.as_view(), name='product_list'),
    path('blog/<int:pk>/', ArticalDetailView.as_view(), name='product_detail'),
    path('contact/', views.contact_page, name='contact_page'),
    path('blog/<int:pk>/edit/', views.edit_product, name='edit_product'),
    path('blog/<int:pk>/delete/', views.delete_product, name='delete_product'),
    path('about/', views.about_page, name='about_page'),
    path('search/', views.search_bar, name="search_bar"),
    # path('add_post/',AddPostBlog.as_view() , name='add_post'),
    path('add_post/', views.post_blog, name='add_post'),
    path('add_category/', AddCategoryview.as_view(),name='add_category' ),
    path("category/<str:cats>/", views.cateogry_views, name='category'),
    path('category-list/', views.category_list_view, name='category-list' ),
    path('like/<int:pk>', views.LikeView, name='like_post'),
]
from . import views
from django.urls import path, include

app_name = 'home'
bucket_urls =[
    path('', views.BucketHome.as_view(), name='bucket'),
    path('delete_obj/<str:key>/', views.DeleteBucketObject.as_view(), name='delete_obj_bucket'),
    path('download_obj/<str:key>/', views.DownloadBucketObject.as_view(), name='download_obj_bucket'),
]
urlpatterns = [
    path('',views.HomeView.as_view(),name='home'),
    path('category/<slug:category_slug>/', views.HomeView.as_view(), name='category_filter'),

    path('all-category/', views.GetAllCategoriesView.as_view(), name='all_categories'),
    path('all-category/<slug:slug>/', views.GetAllCategoriesView.as_view(), name='all_categories'),

    path('bucket/', include(bucket_urls)),
    path('product/<int:product_id>/<slug:slug>/', views.ProductDetailView.as_view(), name= 'product_detail'),
    path('contact-us/', views.ContactUsView.as_view(), name='contact_us'),


]
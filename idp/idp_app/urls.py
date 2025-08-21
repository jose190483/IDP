from django.urls import path
from . import views
urlpatterns = [
    path('search_keywords', views.search_keywords, name='search_keywords'),
    path('manage_pdfs/', views.manage_pdfs, name='manage_pdfs'),
    path('export_csv/', views.export_csv, name='export_csv'),
    path('pdf_compare/', views.pdf_compare_view, name='pdf_compare'),
    path('home_page', views.home_view, name='home_page'),

]
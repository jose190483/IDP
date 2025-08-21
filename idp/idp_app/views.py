from django.shortcuts import render

from .sub_views.search_keywords import search_keywords
from .sub_views.manage_pdfs import manage_pdfs
from .sub_views.export_csv import export_csv
from .sub_views.compare_pdfs import pdf_compare_view
from .sub_views.home_view import home_view
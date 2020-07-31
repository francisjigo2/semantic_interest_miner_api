from django.urls import path

from . import views

urlpatterns = [
    path('interest-extraction/', views.PublicInterestExtractionView.as_view()),
    path('semantic-similarity/', views.PublicKeywordSimilarityView.as_view()),
    path('wiki-categories/', views.PublicKeywordCategoriesView.as_view()),
]

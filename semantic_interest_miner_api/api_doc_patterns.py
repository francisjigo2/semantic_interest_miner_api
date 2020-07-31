from django.urls import path

from interests import views

doc_patterns = [
    path(
        'api/interests/interest-extraction/',
        views.PublicInterestExtractionView.as_view(),
    ),
    path('api/interests/semantic-similarity/', views.PublicKeywordSimilarityView.as_view()),
    path('api/interests/wiki-categories/', views.PublicKeywordCategoriesView.as_view()),

]

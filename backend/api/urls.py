from django.urls import path

from .views import PlantsAPIView, DeletePlant, BestMatch, Matches, MatchMaker, MyPlants

urlpatterns = [
    path('plants/', PlantsAPIView.as_view()),
    path('bestmatch/', BestMatch.as_view()),
    path('matches/', Matches.as_view()),
    path('matchmaker/', MatchMaker.as_view()),
    path('plants/delete/', DeletePlant.as_view()),
    path('myplants/', MyPlants.as_view())
]
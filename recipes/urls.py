from django.urls import path
from recipes import views as api_views

urlpatterns = [
   path('recipes/',api_views.RecipeListCreateAPIView.as_view({'get': 'get'}), name='recipe-list' ),
   path('recipess/',api_views.RecipeListCreateAPIViewasd.as_view({'get': 'list'}), name='recipe-lists' ),
   path('recipes/<int:pk>', api_views.RecipeDetailAPIView.as_view(), name='recipe-detail'),

]
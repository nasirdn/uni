from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import QuestionViewSet, global_statistics, chart_image

router = DefaultRouter()
router.register(r'questions', QuestionViewSet, basename='questions')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/global-statistics/', global_statistics, name='global-statistics'),
    path('api/questions/<int:pk>/chart-image/', chart_image, name='chart-image'),
]
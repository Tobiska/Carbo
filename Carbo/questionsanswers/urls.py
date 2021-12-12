from django.urls import include, path
from rest_framework.routers import SimpleRouter

from questionsanswers import views

question_router = SimpleRouter()
question_router.register('', views.QuestionsViewSet, basename='Question')

answer_router = SimpleRouter()
answer_router.register('', views.AnswersViewSet, basename='Answer')

urlpatterns = [
    path('questions/', include(question_router.urls)),
    path('answers/', include(answer_router.urls)),
]

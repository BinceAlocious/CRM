from django.urls import path
from dsp import views
app_name='dsp'
urlpatterns = [
    path("create/<str:pk>",views.DailyReport,name='report'),
    path("details/<int:pk>",views.Detail.as_view(),name='details'),
]

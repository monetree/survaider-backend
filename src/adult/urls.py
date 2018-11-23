from django.urls import path
from .views import table_data, graph_data


urlpatterns = [
    path('graph_data/', graph_data),
    path('table_data/', table_data),
]

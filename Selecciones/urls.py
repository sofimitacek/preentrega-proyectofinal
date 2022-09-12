from django.urls import path

from Selecciones import views

urlpatterns =[
    path('Players/', views.PlayersListView.as_view(), name="Players"),
    path('crear-Players/', views.PlayersCreateView.as_view(), name="crear_Players"),
    path('editar-Players/<int:pk>/', views.PlayersUpdateView.as_view(), name="editar_Players"),
    path('eliminar-Players/<int:pk>/', views.PlayersDeleteView.as_view(), name="eliminar_Players"),
]

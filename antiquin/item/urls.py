from django.urls import path
from . import views

app_name = "item"

urlpatterns = [
    path("detail/<int:pk>/", views.detail, name="detail"),
    path("search/", views.searchProduct, name="search"),
    path("new/", views.add_items, name="new"),
    path("edit/<int:pk>/", views.edit, name="edit"),
    path("delete/<int:pk>", views.delete, name="delete"),
    path("categories/", views.show_categories, name="category"),
    path("add-category", views.add_category, name="add_category"),
    path("delete-category/<int:pk>", views.delete_category, name="delete_category"),
]

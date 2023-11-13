from django.urls import path

from product import views

urlpatterns = [
    path("latest-products/", views.LatestProductsList.as_view()),
    path("products/search", views.Search),
    path(
        "products/<slug:category_slug>/<slug:product_slug>/",
        views.ProductDetail.as_view(),
    ),
    path("categories/<slug:category_slug>/", views.CategoryDetail.as_view()),
]

from django.urls import path
from .views import SimpleLoginView, CategoryListCreateView, SubCategoryListCreateView, FieldNameListCreateView,FieldPhotoUploadView

urlpatterns = [
    path("login/", SimpleLoginView.as_view(), name="simple-login"),
    path("categories/", CategoryListCreateView.as_view(), name="category-list-create"),
    path("categories/<int:category_id>/subcategories/", SubCategoryListCreateView.as_view(), name="subcategory-list-create"),
    path("subcategories/<int:subcategory_id>/fields/", FieldNameListCreateView.as_view(), name="field-list-create"),
    path("fields/<int:field_id>/upload-photo/", FieldPhotoUploadView.as_view(), name="field-photo-upload"),

]

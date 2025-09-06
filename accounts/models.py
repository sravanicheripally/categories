from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    category = models.ForeignKey(Category, related_name="subcategories", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    class Meta:
        unique_together = ('category', 'name')

    def __str__(self):
        return f"{self.category.name} -> {self.name}"


class FieldName(models.Model):
    subcategory = models.ForeignKey(SubCategory, related_name="fields", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    class Meta:
        unique_together = ('subcategory', 'name')

    def __str__(self):
        return f"{self.subcategory.category.name} -> {self.subcategory.name} -> {self.name}"


class FieldPhoto(models.Model):
    field = models.ForeignKey(FieldName, related_name="photos", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="field_photos/")  # will store in MEDIA folder
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Photo for {self.field}"
from django.db import models


# About Project Model
class AboutProject(models.Model):
    name = models.TextField()
    short_description = models.TextField(max_length=500)
    preview = models.TextField(max_length=150, default="none")
    technology = models.CharField(max_length=200)
    image = models.ImageField(upload_to="img/")

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return "Project"


# About me Model
class About_me(models.Model):
    name = models.TextField(default="none")
    email = models.CharField(max_length=50, default="none")
    telephone = models.CharField(max_length=20, default="none")
    age = models.TextField(max_length=20, default="none")
    preferences = models.TextField(max_length=500, default="none")
    certifications = models.TextField(max_length=200, default="none")
    intro = models.TextField(default="none")

    class Meta:
        verbose_name = "About_me"
        verbose_name_plural = "About_me"

    def __str__(self):
        return "About_me"

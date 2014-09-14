from django.db import models


class HomepageSpotlightLink(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField()
    image = models.ImageField(upload_to="homepage_spotlight_links")
    url = models.CharField(max_length=100)
    sort_order = models.FloatField(default=0)


class HomepageLearnMoreLink(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField()
    icon_image = models.ImageField(upload_to="homepage_learn_more_links")
    url = models.CharField(max_length=100)
    sort_order = models.FloatField(default=0)
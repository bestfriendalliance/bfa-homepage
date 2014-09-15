from django.db import models


class EditableItemManager(models.Manager):

    def published(self):
        return self.filter(show=True).order_by("sort_order")


class EditableItemModel(models.Model):
    sort_order = models.FloatField(default=0)
    show = models.BooleanField(default=False)

    objects = EditableItemManager()

    class Meta:
        abstract = True


class HomepageSpotlightLink(EditableItemModel):
    title = models.CharField(max_length=60)
    description = models.TextField()
    image = models.ImageField(upload_to="homepage_spotlight_links")
    url = models.CharField(max_length=100)


class HomepageLearnMoreLink(EditableItemModel):
    title = models.CharField(max_length=40)
    description = models.TextField()
    icon_image = models.ImageField(upload_to="homepage_learn_more_links")
    url = models.CharField(max_length=100)


class HomepageTestimonial(EditableItemModel):
    text = models.TextField()
    author = models.CharField(max_length=80)

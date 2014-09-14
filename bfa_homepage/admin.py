from django.contrib import admin

from .models import *

class HomepageSpotlightLinkAdmin(admin.ModelAdmin):
    class Meta:
        model = HomepageSpotlightLink
admin.site.register(HomepageSpotlightLink, HomepageSpotlightLinkAdmin)

class HomepageLearnMoreLinkAdmin(admin.ModelAdmin):
    class Meta:
        model = HomepageLearnMoreLink
admin.site.register(HomepageLearnMoreLink, HomepageLearnMoreLinkAdmin)
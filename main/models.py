from django.db import models


class Link(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=500)
    pub_date = models.DateField(null=True, blank=True)
    text = models.TextField()
    scrapped = models.BooleanField(default=False)
    created_at = models.DateField(auto_now=True)
    is_keyword = models.BooleanField(default=False)
# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Asset_Catalog_Type(models.Model):

    #__Asset_Catalog_Type_FIELDS__
    name = models.TextField(max_length=255, null=True, blank=True)
    created_ts = models.DateTimeField(blank=True, null=True, default=timezone.now)
    updated_ts = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Asset_Catalog_Type_FIELDS__END

    class Meta:
        verbose_name        = _("Asset_Catalog_Type")
        verbose_name_plural = _("Asset_Catalog_Type")


class Asset_Catalog_Kind(models.Model):

    #__Asset_Catalog_Kind_FIELDS__
    name = models.TextField(max_length=255, null=True, blank=True)
    created_ts = models.DateTimeField(blank=True, null=True, default=timezone.now)
    updated_ts = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Asset_Catalog_Kind_FIELDS__END

    class Meta:
        verbose_name        = _("Asset_Catalog_Kind")
        verbose_name_plural = _("Asset_Catalog_Kind")


class Asset_Catalog(models.Model):

    #__Asset_Catalog_FIELDS__
    kind = models.ForeignKey(asset_catalog_kind, on_delete=models.CASCADE)
    type = models.ForeignKey(asset_catalog_type, on_delete=models.CASCADE)
    created_ts = models.DateTimeField(blank=True, null=True, default=timezone.now)
    updated_ts = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Asset_Catalog_FIELDS__END

    class Meta:
        verbose_name        = _("Asset_Catalog")
        verbose_name_plural = _("Asset_Catalog")



#__MODELS__END

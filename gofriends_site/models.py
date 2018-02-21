from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from ckeditor_uploader.fields import RichTextUploadingField
from django.core.validators import RegexValidator


class CommonInfo(models.Model):

    class Meta:
        abstract = True
        ordering = ['-created']

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class CaseStudies(CommonInfo):

    class Meta(CommonInfo.Meta):
        verbose_name = "Case Study"
        verbose_name_plural = "1. Case Studies"

    title = models.CharField(max_length=256)
    title_image = models.ImageField(blank=True, null=True, upload_to='images', verbose_name='title image')
    short_description = models.CharField(blank=True, null=True, max_length=256)
    description = RichTextUploadingField(blank=True, null=True, verbose_name='description')
    url_field = models.URLField(blank=True, null=True, verbose_name='URL')

    def __str__(self):
        return "{}".format(self.title)


class Services(CommonInfo):

    class Meta(CommonInfo.Meta):
        verbose_name = "Service"
        verbose_name_plural = "2. Services"

    title = models.CharField(max_length=256)
    title_image = models.ImageField(blank=True, null=True, upload_to='images', verbose_name='title image')
    short_description = models.CharField(blank=True, null=True, max_length=256)
    description = RichTextUploadingField(blank=True, null=True, verbose_name='description')

    def __str__(self):
        return "{}".format(self.title)


class Industries(CommonInfo):

    class Meta(CommonInfo.Meta):
        verbose_name = "Industry"
        verbose_name_plural = "3. Industries"

    title = models.CharField(max_length=256)
    title_image = models.ImageField(blank=True, null=True, upload_to='images', verbose_name='title image')
    short_description = models.CharField(blank=True, null=True, max_length=256)
    description = RichTextUploadingField(blank=True, null=True, verbose_name='description')

    def __str__(self):
        return "{}".format(self.title)


class Technologies(CommonInfo):

    class Meta(CommonInfo.Meta):
        verbose_name = "Technology"
        verbose_name_plural = "4. Technologies"

    title = models.CharField(max_length=256)
    title_image = models.ImageField(blank=True, null=True, upload_to='images', verbose_name='title image')
    short_description = models.CharField(blank=True, null=True, max_length=256)
    description = RichTextUploadingField(blank=True, null=True, verbose_name='description')

    def __str__(self):
        return "{}".format(self.title)


class About(models.Model):

    class Meta:
        verbose_name = "About us"
        verbose_name_plural = "5. About us"

    name = models.CharField(max_length=256)
    position = models.CharField(max_length=256)
    photo = models.ImageField(upload_to='team/photos')
    description = RichTextUploadingField(blank=True, null=True)

    def __str__(self):
        return "{}".format(self.name)


class Contacts(models.Model):

    class Meta:
        verbose_name = "Contacts"
        verbose_name_plural = "6. Contacts"

    phone = models.CharField(max_length=256)
    mail = models.EmailField()
    address = models.CharField(max_length=256)


class Customers(CommonInfo):

    class Meta(CommonInfo.Meta):
        verbose_name = "Customer"
        verbose_name_plural = "Customers"

    phone_regex = RegexValidator(regex=r'^\+?\d{9,12}$',
                                 message="Phone number must be entered in the format: "
                                         "'+380441234567'. Up to 12 digits allowed.")

    name = models.CharField(max_length=256)
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True, null=True)
    mail = models.EmailField(verbose_name='e-mail')

    def __str__(self):
        return "{}".format(self.name)


class MetaTags(models.Model):

    class Meta:
        verbose_name = "Meta tag"
        verbose_name_plural = "Meta tags"

    page = models.CharField(max_length=256)
    title = models.CharField(max_length=256)
    description = models.CharField(max_length=256, blank=True, null=True)
    keywords = models.TextField(blank=True, null=True)

    def __str__(self):
        return "{}".format(self.page)

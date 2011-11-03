from django.db import models
from django.core.urlresolvers import reverse


class Contact(models.Model):
    name = models.CharField(max_length=255,
                            verbose_name='Name')
    email = models.EmailField(blank=True,
                              null=True)
    phone = models.CharField(max_length=255,
                             blank=True,
                             null=True)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('contact_list:contact_form', args=(self.pk,))

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

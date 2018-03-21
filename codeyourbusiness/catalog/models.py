from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel

# Create your models here.


class Home(Page):
    hero_text = models.TextField(blank=True)


    content_panels = Page.content_panels + [
        FieldPanel('hero_text', classname="full"),
    ]


class OpenSource(Page):
    pass


class About(Page):
    pass


class Contact(Page):
    pass


class Learn(Page):
    pass

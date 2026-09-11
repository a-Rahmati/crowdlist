from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.models import Page
from wagtail.fields import RichTextField


class HomePage(Page):
    hero = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("hero"),
        FieldPanel("body", classname="full"),
    ]

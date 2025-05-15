from django.db import models


class BlockType(models.TextChoices):
    SLIDER = 'slider', 'Slider'
    TEXT = 'text', 'Text'
    GALLERY = 'gallery', 'Gallery'
    MEDIA = 'media', 'Media'
    NEWS = 'news', 'News'
    EVENTS = 'events', 'Events'
    CONTACTS = 'contacts', 'Contacts'
    MAP = 'map', 'Map'
    FORM = 'form', 'Form'


class ContentType(models.TextChoices):
    TEXT = 'text', 'Text'
    SLIDER = 'slider', 'Slider'
    NEWS = 'news', 'News'
    EVENTS = 'events', 'Events'
    MEDIA = 'media', 'Media'
    FORM = 'form', 'Form'
    CONTACTS = 'contacts', 'Contacts'
    CALENDAR = 'calendar', 'Calendar'
    MAP = 'map', 'Map'


class ContentStatus(models.TextChoices):
    draft = 'draft', 'Draft'
    pending = 'pending', 'Pending'
    approved = 'Approved', 'Approved'
    rejected = 'Rejected', 'Rejected'


class ModerationStatus(models.TextChoices):
    PENDING = 'pending', 'Pending'
    APPROVED = 'Approved', 'Approved'
    REJECTED = 'Rejected', 'Rejected'

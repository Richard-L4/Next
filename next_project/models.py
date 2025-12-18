from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} | {self.email} | {self.phone} | {self.address}"

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contact"


class Register(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    address = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} | {self.email}"

    class Meta:
        verbose_name = "Register"
        verbose_name_plural = "Register"


class CardText(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    image_name = models.CharField(
        max_length=100,
        help_text="Enter the image filename (eg 'An image of...)",
        default='default.jpg',
        blank=True
    )

    def __str__(self):
        return self.title or f"Card for {self.image_name}"


class CardTextTranslation(models.Model):
    LANGUAGE_CHOICES = [
        ('en', 'English'),
        ('es', 'Spanish'),
    ]

    card = models.ForeignKey(
        CardText,
        related_name='translations',
        on_delete=models.CASCADE
    )
    language = models.CharField(max_length=5, choices=LANGUAGE_CHOICES)
    content = models.TextField()

    def __str__(self):
        return f"{self.card.title} ({self.language})"


class Comment(models.Model):
    CardText = models.ForeignKey(CardText, on_delete=models.CASCADE,
                                 related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.text[:20]}"

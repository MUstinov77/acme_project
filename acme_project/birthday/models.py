from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

from .validators import real_age_validator


User = get_user_model()

class Birthday(models.Model):
    first_name = models.CharField('Имя', max_length=20)
    last_name = models.CharField(
        'Фамилия',
        blank=True,
        help_text='Необязательное поле',
        max_length=20,
    )
    birthday = models.DateField(
        'Дата рождения',
        validators=[real_age_validator]
    )
    image = models.ImageField(
        'Фото',
        blank=True,
        upload_to='birthday_images',
    )
    author = models.ForeignKey(
        User,
        verbose_name='Автор',
        on_delete=models.CASCADE,
        null=True,
    )

    class Meta:
        constraints = (
            models.UniqueConstraint(
                fields=('first_name', 'last_name', 'birthday'),
                name='Unique person constraint',
            ),
        )
    def get_absolute_url(self):
        return reverse('birthday:detail', kwargs={'pk': self.pk})
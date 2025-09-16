import os

from django.core.validators import URLValidator, ValidationError
from django.db import models


class Factory(models.Model):
    name = models.CharField(max_length=255, verbose_name='производитель')
    country = models.CharField(max_length=100, verbose_name='страна')
    website = models.URLField(blank=True, verbose_name='вебсайт')
    image = models.ImageField(upload_to='factory_images/', null=True, verbose_name='изображение')

    class Meta:
        ordering = ['name']
        verbose_name = 'производителя'
        verbose_name_plural = 'Производители'

    def __str__(self):
        return self.name

    # Функция комплексной нормализации и валидации URL
    def clean(self):
        validator = URLValidator()
        try:
            validator(self.website)
        except ValidationError:
            self.website = f'https://{self.website}'
            validator(self.website)


class Bike(models.Model):
    factory = models.ForeignKey(Factory, on_delete=models.CASCADE, verbose_name='бренд')
    model_name = models.CharField(max_length=255, verbose_name='модель')
    engine_volume = models.IntegerField(null=True, blank=True, verbose_name='двигатель')
    year = models.IntegerField(default=20, verbose_name='год выпуска')
    file = models.FileField(upload_to='uploads/', verbose_name='файл')
    file_preview = models.ImageField(upload_to='previews/', blank=True, null=True, verbose_name='превью')

    class Meta:
        ordering = ['factory']
        verbose_name = 'Модель'
        verbose_name_plural = 'Модели'

    def __str__(self):
        return self.model_name

    # Функция вывода человекочитаемого названия файла в шаблонах и админке
    def get_readable_filename(self):
        # Удаляем путь и заменяем подчеркивания на пробелы
        filename = os.path.basename(self.file.name)
        return filename.replace('_', ' ')

    # def __str__(self):
    #     return f'{self.model_name} ({self.year})'

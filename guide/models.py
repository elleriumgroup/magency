from django.db import models

class Sex(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    class Meta:
        verbose_name = 'Пол'
        verbose_name_plural = 'Пол'
    def __str__(self):
        return self.name

class Education(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    class Meta:
        verbose_name = 'Образование'
        verbose_name_plural = 'Образования'
    def __str__(self):
        return self.name


class Specialty(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    class Meta:
        verbose_name = 'Специальность'
        verbose_name_plural = 'Специальности'
    def __str__(self):
        return self.name


class MaterialStatus(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    class Meta:
        verbose_name = 'Материальное положение'
        verbose_name_plural = 'Материальные положения'
    def __str__(self):
        return self.name


class MaritalStatus(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    class Meta:
        verbose_name = 'Семейное положение'
        verbose_name_plural = 'Семейные положения'
    def __str__(self):
        return self.name

class HousingConditions(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    class Meta:
        verbose_name = 'Жилищные условия'
        verbose_name_plural = 'Жилищные условия'
    def __str__(self):
        return self.name


class AttitudeToAlcohol(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    class Meta:
        verbose_name = 'Отношение к алкоголю'
        verbose_name_plural = 'Отношения к алкоголю'
    def __str__(self):
        return self.name

class AttitudeToSmoking(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    class Meta:
        verbose_name = 'Отношение к курению'
        verbose_name_plural = 'Отношения к курению'
    def __str__(self):
        return self.name

class BodyType(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    class Meta:
        verbose_name = 'Телосложение'
        verbose_name_plural = 'Телосложения'
    def __str__(self):
        return self.name

class EyeColor(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    class Meta:
        verbose_name = 'Цвет глаз'
        verbose_name_plural = 'Цвета глаз'
    def __str__(self):
        return self.name


class HairColor(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    class Meta:
        verbose_name = 'Цвет волос'
        verbose_name_plural = 'Цвета волос'
    def __str__(self):
        return self.name

class Religion(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    class Meta:
        verbose_name = 'Вероисповедание'
        verbose_name_plural = 'Вероисповедания'
    def __str__(self):
        return self.name

class Nationality(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    class Meta:
        verbose_name = 'Национальность'
        verbose_name_plural = 'Национальности'
    def __str__(self):
        return self.name

class CharacterTraits(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    class Meta:
        verbose_name = 'Черта характера'
        verbose_name_plural = 'Черты характера'
    def __str__(self):
        return self.name

class PlaceOfResidence(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    class Meta:
        verbose_name = 'Место проживания'
        verbose_name_plural = 'Места проживания'
    def __str__(self):
        return self.name

class AvailabilityOfHousing(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    class Meta:
        verbose_name = 'Наличие собственного жилья'
        verbose_name_plural = 'Наличие собственного жилья'
    def __str__(self):
        return self.name

class Elements(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    class Meta:
        verbose_name = 'Элемент стихии'
        verbose_name_plural = 'Элементы стихий'
    def __str__(self):
        return self.name

class CharacteristicsOfZodiac(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    class Meta:
        verbose_name = 'Характеристика (Знака зодиака)'
        verbose_name_plural = 'Характеристика (Знака зодиака)'
    def __str__(self):
        return self.name

class QualityOfZodiac(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    class Meta:
        verbose_name = 'Качество (Знака зодиака)'
        verbose_name_plural = 'Качества (Знака зодиака)'
    def __str__(self):
        return self.name

class ControlOfPlanet(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    class Meta:
        verbose_name = 'Контролирующая планета (Знака зодиака)'
        verbose_name_plural = 'Контролирующие планеты (Знака зодиака)'
    def __str__(self):
        return self.name

class ManagingHome(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    class Meta:
        verbose_name = 'Управляющий дом (Знака зодиака)'
        verbose_name_plural = 'Управляющие дома (Знака зодиака)'
    def __str__(self):
        return self.name

class TarotCard(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    class Meta:
        verbose_name = 'Карта Таро (Знака зодиака)'
        verbose_name_plural = 'Карты Таро (Знака зодиака)'
    def __str__(self):
        return self.name

class ColoursOfZodiac(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    class Meta:
        verbose_name = 'Цвет (Знака зодиака)'
        verbose_name_plural = 'Цвета (Знака зодиака)'
    def __str__(self):
        return self.name

class StoneFortuneOfZodiac(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    class Meta:
        verbose_name = 'Камень удачи (Знака зодиака)'
        verbose_name_plural = 'Камни удачи (Знака зодиака)'
    def __str__(self):
        return self.name

class FlowersOfZodiac(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    class Meta:
        verbose_name = 'Цветок (Знака зодиака)'
        verbose_name_plural = 'Цветы (Знака зодиака)'
    def __str__(self):
        return self.name

class ZodiacSign(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название знака зодиака')
    characteristics = models.ManyToManyField(CharacteristicsOfZodiac, verbose_name='Характеристики знака')
    element = models.ForeignKey(Elements, on_delete=models.CASCADE, verbose_name='Элемент знака')
    quality = models.ForeignKey(QualityOfZodiac, on_delete=models.CASCADE, verbose_name='Качество знака')
    planets = models.ManyToManyField(ControlOfPlanet, verbose_name='Управляющие планеты')
    manhome = models.ForeignKey(ManagingHome, on_delete=models.CASCADE, verbose_name='Управляющий дом')
    tarot = models.ForeignKey(TarotCard, on_delete=models.CASCADE, verbose_name='Карта Таро')
    color = models.ForeignKey(ColoursOfZodiac, on_delete=models.CASCADE, verbose_name='Цвет знака')
    stones = models.ManyToManyField(StoneFortuneOfZodiac, verbose_name='Камни удачи')
    flowers = models.ManyToManyField(FlowersOfZodiac, verbose_name='Цветы')
    compatibil = models.ManyToManyField('self', verbose_name='Лучшая совместимость')
    class Meta:
        verbose_name = 'Знак зодиака'
        verbose_name_plural = 'Знаки зодиака'
    def __str__(self):
        return self.name
    # https://horoscopes.rambler.ru/znaki-zodiaka/
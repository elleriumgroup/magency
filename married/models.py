from django.db import models
from guide.models import Sex
from guide.models import ZodiacSign
from guide.models import Education
from guide.models import Specialty
from guide.models import MaterialStatus
from guide.models import MaritalStatus
from guide.models import HousingConditions
from guide.models import AttitudeToAlcohol
from guide.models import AttitudeToSmoking
from guide.models import BodyType
from guide.models import EyeColor
from guide.models import HairColor
from guide.models import Religion
from guide.models import Nationality
from guide.models import CharacterTraits
from guide.models import PlaceOfResidence
from guide.models import AvailabilityOfHousing


class MarriedAnkets(models.Model):
    # Общая часть анкеты
    family = models.CharField(max_length=50, verbose_name='Фамилия')
    name = models.CharField(max_length=50, verbose_name='Имя')
    surname = models.CharField(max_length=50, verbose_name='Отчество')
    sex = models.ForeignKey(Sex, on_delete=models.CASCADE, verbose_name='Пол')
    birthday = models.DateField()
    zodiacsign = models.ForeignKey(ZodiacSign, on_delete=models.CASCADE, verbose_name='Знак зодиака')
    fullyears = models.IntegerField(verbose_name='Полных лет')
    education = models.ForeignKey(Education, on_delete=models.CASCADE, verbose_name='Образование')
    speciality = models.ForeignKey(Specialty, on_delete=models.CASCADE, verbose_name='Специальность')
    place_of_work = models.TextField(max_length=200, verbose_name='Место работы')
    position = models.TextField(max_length=100, verbose_name='Должность')
    material_status = models.ForeignKey(MaterialStatus, on_delete=models.CASCADE, verbose_name='Материальное положение')
    marital_status = models.ForeignKey(MaritalStatus, on_delete=models.CASCADE, verbose_name='Семейное положение')
    children = models.BooleanField(default=False, verbose_name='Наличие детей')
    children_locations = models.TextField(max_length=200, verbose_name='При наличии детей: место их проживания')
    housing_conditions = models.ForeignKey(HousingConditions, on_delete=models.CASCADE, verbose_name='Жилищные условия')
    car = models.BooleanField(default=False, verbose_name='Наличие личного автомобиля')
    attitude_to_alcohol = models.ForeignKey(AttitudeToAlcohol, on_delete=models.CASCADE, verbose_name='Отношение к алкоголю')
    height = models.IntegerField(verbose_name='Рост')
    weight = models.IntegerField(verbose_name='Вес')
    body_type = models.ForeignKey(BodyType, on_delete=models.CASCADE, verbose_name='Телосложение')
    eye_color = models.ForeignKey(EyeColor, on_delete=models.CASCADE, verbose_name='Цвет глаз')
    hair_color = models.ForeignKey(HairColor, on_delete=models.CASCADE, verbose_name='Цвет волос')
    religion = models.ForeignKey(Religion, on_delete=models.CASCADE, verbose_name='Вероисповедение')
    nationality = models.ForeignKey(Nationality, on_delete=models.CASCADE, verbose_name='Национальность')
    hobby = models.TextField(max_length=1000, verbose_name='Интересы/хобби, какими видами спорта занимаетесь, как и где проводите свободное время')
    character_traits = models.ManyToManyField(CharacterTraits, verbose_name='Присущие черты характера')
    life_priorities = models.TextField(max_length=1000, verbose_name='Жизненные ценности, приоритеты')
    life_credo = models.TextField(max_length=200, verbose_name='Жизненное кредо/девиз')
    phone = models.CharField(max_length=11, verbose_name='Номер телефона для связи')
    email = models.EmailField(verbose_name='Электронная почта')
    time_contact = models.CharField(max_length=50, verbose_name='Удобное время для связи')
    # Конфиденциальная часть
    address = models.TextField(max_length=1000, verbose_name='Адрес проживания')
    condition_dispensary = models.TextField(max_length=200, verbose_name='Состоит ли клиент в диспансере')
    criminal_record = models.TextField(max_length=500, verbose_name='Бал ли судим, если Да по каким квалификациям')
    childfree = models.BooleanField(default=True, verbose_name='Планируете ли детей в браке?')
    clienttime = models.CharField(max_length=100, verbose_name='На какое время планирует быть нашим клиентом')
    class Meta:
        verbose_name = 'Анкета клиента'
        verbose_name_plural = 'Анкеты клиентов'
    def __str__(self):
        return self.family + ' ' + self.name + ' ' + self.surname + ' ' + str(self.birthday)

class ClientRequirements(models.Model):
    client = models.ForeignKey(MarriedAnkets, on_delete=models.CASCADE, verbose_name='Клиент')
    age_in = models.PositiveIntegerField(verbose_name='Возраст от')
    age_out = models.PositiveIntegerField(verbose_name='Возраст до')
    zodiacsign = models.ManyToManyField(ZodiacSign, verbose_name='Знак зодиака')
    height = models.IntegerField(verbose_name='Рост')
    weight = models.IntegerField(verbose_name='Вес')
    body_type = models.ForeignKey(BodyType, on_delete=models.CASCADE, verbose_name='Телосложение')
    eye_color = models.ForeignKey(EyeColor, on_delete=models.CASCADE, verbose_name='Цвет глаз')
    hair_color = models.ForeignKey(HairColor, on_delete=models.CASCADE, verbose_name='Цвет волос')
    religion = models.ForeignKey(Religion, on_delete=models.CASCADE, verbose_name='Вероисповедение')
    nationality = models.ForeignKey(Nationality, on_delete=models.CASCADE, verbose_name='Национальность')
    education = models.ForeignKey(Education, on_delete=models.CASCADE, verbose_name='Образование')
    speciality = models.ForeignKey(Specialty, on_delete=models.CASCADE, verbose_name='Специальность')
    place_of_residence = models.ForeignKey(PlaceOfResidence, on_delete=models.CASCADE, verbose_name='Место проживания')
    presence_of_children = models.BooleanField(default=False, verbose_name='Наличие детей у партнера')
    availability_of_housing = models.ForeignKey(AvailabilityOfHousing,on_delete=models.CASCADE, verbose_name='Наличие жилья у партнера')
    attitude_to_alcohol = models.ForeignKey(AttitudeToAlcohol, on_delete=models.CASCADE, verbose_name='Отношение к алкоголю')
    attitude_to_smoking = models.ForeignKey(AttitudeToSmoking, on_delete=models.CASCADE, verbose_name='Отношение к курению')
    character_traits = models.ManyToManyField(CharacterTraits, verbose_name='Важные качества характера партнера')
    not_needed = models.TextField(max_length=1000, verbose_name='Какой партнер не нужен')
    remm = models.TextField(max_length=2000, verbose_name='Дополнительная информация')
    date_create = models.DateField(verbose_name='Дата создания анкеты')
    class Meta:
        verbose_name = 'Требования клиентов'
        verbose_name_plural = 'Требования клиентов'
import email
from msilib.schema import RadioButton
from django.db import models
from django.forms import RadioSelect, widgets
from json import JSONEncoder


# model of subects

# model of teacher
class Tutor(models.Model):
    first_name = models.CharField(max_length=200, help_text='Имя', blank=True)
    last_name = models.CharField(
        max_length=200, help_text='Имя', blank=True)
    phone_num = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    date_of_birth = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


# model of Kurators
class Kurator(models.Model):
    first_name = models.CharField(max_length=200, help_text='Имя', blank=True)
    last_name = models.CharField(
        max_length=200, help_text='Фамилия', blank=True)
    birth_date = models.DateTimeField(auto_now_add=True)
    tel_numb = models.CharField(
        max_length=150, help_text='Номер телефона', blank=True)
    adress = models.CharField(max_length=200, help_text='Адресс')
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

# model of tarbiyewi


class Vospitatel(models.Model):
    vospitatel_full_name = models.CharField(max_length=200)
    birth_date = models.DateTimeField(auto_now_add=True)
    tel_numb = models.CharField(max_length=100)
    adress = models.CharField(max_length=200, help_text='Адресс')
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.vospitatel_full_name


# model of student
class Category_class(models.Model):
    name = models.CharField(max_length=128, verbose_name="Выберите класс")

    def __str__(self):
        return self.name


class Student(models.Model):
    STATUS_SEX = (
        ('female', 'Женский'),
        ('male', 'Мужской'),
    )

    STATUS_FAMILY = (
        ('полный', 'Полный'),
        ('неполный', 'Неполный'),
    )
    QUANTITY_CHILDS = (
        ('да', 'ДА'),
        ('нет', 'НЕТ'),
    )
    DISABILITY_CHOICES = (
        ('да', 'Да'),
        ('нет', 'Нет'),

    )
    CHOICES_LANG = (
        ('казахский', 'казахский'),
        ('русский', 'русский'),
    )

    category_class = models.ForeignKey(
        Category_class, on_delete=models.CASCADE, verbose_name="Выберите класс")
    full_name = models.CharField(max_length=250, verbose_name='ФИО')
   
    learning_lang = models.CharField(
        max_length=10, choices=CHOICES_LANG, default='каазахский', verbose_name='Язык обучение')
    
    IIN = models.CharField(max_length=15, verbose_name='ИИН')
    disability = models.CharField(
        max_length=20, choices=DISABILITY_CHOICES, default='нет', verbose_name='Инвалидность')
    category_fam = models.CharField(
        max_length=10, choices=STATUS_FAMILY, default='Полный', verbose_name='Тип семьи')
    father_full_name = models.CharField(max_length=200, blank=True, verbose_name='ФИО отца')
    father_educ = models.CharField(max_length=200, blank=True, verbose_name='Образования')
    father_pos = models.CharField(max_length=200, blank=True, verbose_name='Позиция на работе')
    father_org = models.CharField(max_length=250, blank=True, verbose_name='Место работы')
    father_tel = models.CharField(max_length=100, null=True, blank=True, verbose_name='Контактные данные отца')
    mother_full_name = models.CharField(max_length=200, blank=True, verbose_name='ФИО матери')
    mother_educ = models.CharField(max_length=200, blank=True, verbose_name='Образование')
    mother_pos = models.CharField(max_length=200, blank=True, verbose_name='Позиция на работе')
    mother_org = models.CharField(max_length=250, blank=True, verbose_name='Место работы')
    mother_tel = models.CharField(max_length=100, null=True, blank=True, verbose_name='Контактные данные матери')
    large_family = models.CharField(
        max_length=10, choices=QUANTITY_CHILDS, default='нет', verbose_name='Большая семья')
    childs_in_family = models.CharField(
        max_length=10, verbose_name='Количество детей', blank=True)
    adress = models.CharField(max_length=200, verbose_name='Адресс')
    kurator = models.ForeignKey(Kurator, on_delete=models.CASCADE, null=True, verbose_name='Выберите куратора')
    vospitatel = models.ForeignKey(
        Vospitatel, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Выберите воспитателя')

    stud_tutor = models.ForeignKey(
        Tutor, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Выберите тьютора')
    stud_photo = models.ImageField(upload_to='media/', blank=True, verbose_name='Фото')
    stud_nationality = models.CharField(max_length=100, verbose_name='Национальность')
    stud_date_of_birth = models.DateField(verbose_name='Дата рождения')
    stud_age = models.CharField(max_length=200, verbose_name='Возраст ученика')
    stud_gender = models.CharField(
        max_length=10, choices=STATUS_SEX, default='none', verbose_name='Пол')

    stud_email = models.EmailField(null=True, blank=True, verbose_name='Почта')
    stud_tel = models.CharField(max_length=20, null=True, blank=True, verbose_name='Номер телефона')
    

    def __str__(self):
        return self.full_name

    


class AppealCurators(models.Model):
    CHOOSE_TYPE_APPEAL = (
        ('вопросы внешнего суммативного оценивания',
         'вопросы внешнего суммативного оценивания'),
        ('вопросы выбора профессии', 'вопросы выбора профессии'),
        ('вопросы интелектуального развития учащихся (олимпиады, проекты)',
         'вопросы интелектуального развития учащихся (олимпиады, проекты)'),
        ('вопросы к психологической службе', 'вопросы к психологической службе'),
        ('вопросы общей успеваемости', 'вопросы общей успеваемости'),
        ('вопросы опеспечения безопастности', 'вопросы опеспечения безопастности'),
        ('вопросы по изучения второго иностранного языка',
         'вопросы по изучения второго иностранного языка'),
        ('вопросы по содержанию программы и оценивания',
         'вопросы по содержанию программы и оценивания'),
        ('вопросы поведения', 'вопросы поведения'),
        ('личные вопросы', 'личные вопросы'),
        ('не соблюдение внутренних правил школы',
         'не соблюдение внутренних правил школы'),
        ('опаздания на урок', 'опаздания на урок'),
        ('по вызову мед. Работников', 'по вызову мед. Работников'),
        ('по тестированию IELTS', 'по тестированию IELTS'),
        ('по тестированию SAT ', 'по тестированию SAT '),
        ('Разное', 'Разное'),
        ('рекомендации по улучшению работы школы',
         'рекомендации по улучшению работы школы'),

    )
    parent = models.CharField(max_length=200, verbose_name="Родители")
    category_class = models.ForeignKey(Category_class, on_delete=models.CASCADE)
    student = models.ForeignKey( Student, on_delete=models.CASCADE,
     verbose_name="Ученик")
    visited = models.BooleanField(default=False, verbose_name="Посетил")
    by_telephone = models.BooleanField(
        default=False, verbose_name="По телефону")
    by_writing = models.BooleanField(default=False, verbose_name="Письменно")
    date_of_appeal = models.DateField(verbose_name="Время создания")
    type_appeal = models.CharField(
        max_length=200, choices=CHOOSE_TYPE_APPEAL, default='Разное', verbose_name="Выберите тип обращение")
    question = models.TextField(verbose_name="Вопрос")

    



class Participant(models.Model):
    CHOOSE_TYPE = (
        ('ОЛИМПИАДА', 'ОЛИМПИАДА'),
        ('НАУЧНЫЙ ПРОЕКТ', 'НАУЧНЫЙ ПРОЕКТ'),
        ('КРУЖОК', 'КРУЖОК'),
    )
    category_class = models.ForeignKey(
        Category_class, on_delete=models.CASCADE, verbose_name="Выберите класс")
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, verbose_name="Ученик")
    title = models.CharField(max_length=250, verbose_name="Название")
    category = models.CharField(
        max_length=250, choices=CHOOSE_TYPE, verbose_name='Выберите тип деятельности')
    date_of_participant = models.DateField(verbose_name='Дата участие')
    result = models.FileField(
        upload_to="pdf/%Y/%m/%d/", verbose_name='Результат')

from tkinter import Widget
from .models import AppealCurators, Student, Participant, Category_class
import json
from django import forms
from crispy_forms.layout import Layout, Field
from django.contrib.admin.widgets import AdminDateWidget


class DateInput(forms.DateInput):
    input_type = 'date'


# class ApealForm(forms.Form):

#     CHOOSE_TYPE_APPEAL = (
#         ('вопросы внешнего суммативного оценивания',
#          'вопросы внешнего суммативного оценивания'),
#         ('вопросы выбора профессии', 'вопросы выбора профессии'),
#         ('вопросы интелектуального развития учащихся (олимпиады, проекты)',
#          'вопросы интелектуального развития учащихся (олимпиады, проекты)'),
#         ('вопросы к психологической службе', 'вопросы к психологической службе'),
#         ('вопросы общей успеваемости', 'вопросы общей успеваемости'),
#         ('вопросы опеспечения безопастности', 'вопросы опеспечения безопастности'),
#         ('вопросы по изучения второго иностранного языка',
#          'вопросы по изучения второго иностранного языка'),
#         ('вопросы по содержанию программы и оценивания',
#          'вопросы по содержанию программы и оценивания'),
#         ('вопросы поведения', 'вопросы поведения'),
#         ('личные вопросы', 'личные вопросы'),
#         ('не соблюдение внутренних правил школы',
#          'не соблюдение внутренних правил школы'),
#         ('опаздания на урок', 'опаздания на урок'),
#         ('по вызову мед. Работников', 'по вызову мед. Работников'),
#         ('по тестированию IELTS', 'по тестированию IELTS'),
#         ('по тестированию SAT ', 'по тестированию SAT '),
#         ('Разное', 'Разное'),
#         ('рекомендации по улучшению работы школы',
#          'рекомендации по улучшению работы школы'),

#     )
#     parent = forms.CharField(max_length=200)
#     klass = forms.ModelChoiceField(Category_class.objects.all())
#     student = forms.ModelChoiceField(Student.objects.all())
#     visited = forms.BooleanField()
#     by_telephone = forms.BooleanField()
#     by_writing = forms.BooleanField()
#     date_of_appeal = forms.DateField()
#     type_appeal = forms.ChoiceField(
#         max_length=200, choices=CHOOSE_TYPE_APPEAL, default='Разное')
#     question = forms.TextField()


class AppealForms(forms.ModelForm):
    class Meta:
        model = AppealCurators
        fields = '__all__'
        widgets = {
            'date_of_appeal': DateInput(),
            'question': forms.Textarea(attrs={'rows': 4}),
        }
        labels = {
            "parent": "Родители",
            "category_class": "Выберите класс",
            "student": "Выберите ученика",
            "visited": "Посетил",
            "date_of_appeal": "Дата обращение",
            "type_appeal": "Выберите тип обращение",
            "question": "Вопрос обращение"
            }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['student'].queryset = Student.objects.none()

        if 'category_class' in self.data:
            try:
                category_class_id = int(self.data.get('category_class'))
                self.fields['student'].queryset = Student.objects.filter(category_class_id=category_class_id).order_by('name')
            except (ValueError, TypeError):
                pass # invalid input from the client;ignore and fallback to empty student queryset
        elif self.instance.pk:
            self.fields['student'].queryset = self.instance.category_class.student_set.order_by('name')


class ParticipantForm(forms.ModelForm):

    class Meta:
        model = Participant
        fields = '__all__'
        widgets = {
            'date_of_participant': DateInput(),
        }

    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['student'].queryset = Student.objects.none()

        if 'category_class' in self.data:
            try:
                category_class_id = int(self.data.get('category_class'))
                self.fields['student'].queryset = Student.objects.filter(category_class_id=category_class_id).order_by('name')
            except (ValueError, TypeError):
                pass # invalid input from the client;ignore and fallback to empty student queryset
        elif self.instance.pk:
            self.fields['student'].queryset = self.instance.category_class.student_set.order_by('name')


class AddStudent(forms.ModelForm):
    class Meta:
        model = Student

        fields = '__all__'
        widgets = {
            'stud_date_of_birth':DateInput(),

        }
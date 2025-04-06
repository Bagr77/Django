from django.db import models
from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.shortcuts import render
from django.utils.deconstruct import deconstructible

# Create your models here.

class Auto(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField()
    price = models.IntegerField(default=0, blank=True)
    distance = models.IntegerField(default=0, blank=True)
    is_exists = models.BooleanField(default=True)

    def __str__(self):
        return self.title



cars = [
    dict(name="BMW X6", model="BMW", price=6000111),
    dict(name="Toyota Corolla", model="Toyota", distance=72000),
    dict(name="Haval 7", model="Haval", price=3500222)
]

for m in cars:
    Auto.objects.create(**m)

autos = Auto.objects.all()[:2]

# username: текстовое поле; максимальная длина 100 символов, обязательное;
# email: поле ввода адреса электронной почты; обязательное;
# agree: поле типа CheckBox; обязательное;
# content: поле ввода полноценного многострочного текста; обязательное.

class CommentForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    agree = forms.BooleanField()
    content = forms.CharField(widget=forms.Textarea)



# fio: текстовое поле; максимальная длина 200 символов, обязательное, название "Владелец";
# email: поле ввода адреса электронной почты; обязательное, название "E-mail";
# vin: текстовое поле; максимальная длина 20 символов, обязательное, название "VIN";
# model: текстовое поле; максимальная длина 100 символов, обязательное, название "Модель";
# stag: числовое поле; необязательное, название "Стаж".

class OsagoForm(forms.Form):
    fio = forms.CharField(max_length=200, label='Владелец')
    email = forms.EmailField(label='E-mail')
    vin = forms.CharField(max_length=20, label='VIN')
    model = forms.CharField(max_length=100, label='Модель')
    stag = forms.IntegerField(required=False, label='Стаж')


# Подвиг 4. Объявите класс формы с именем LoginForm, не связанной с моделью, со следующими полями:
# username: текстовое поле; максимальная длина 50 символов, минимальная длина 5 символов, обязательное, название "Логин";
# password: поле ввода пароля; минимальная длина 6 символов, обязательное, название "Пароль".
# Атрибуты класса должны иметь те же названия и порядок, что и в описании.
# Для полей формы через параметр widget укажите стили оформления: attrs={'class': 'form-login-input'}
# Для проверки корректности поля password объявите в классе LoginForm метод с именем:
# clean_<название поля>
# В этом методе реализовать проверку значения поля password по следующим критериям:
# допустимые символы: буквы латинского алфавита (малые и большие), цифры и символы "-?!$#@_";
# минимальная длина пароля 6 символов.
# Если эти проверки не проходят, то генерировать исключение:
#raise ValidationError("Некорректно введенный пароль.")



class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, min_length=5, label='Логин',
                               widget=forms.TextInput(attrs={'class': 'form-login-input'}))
    password = forms.CharField(min_length=6, label='Пароль',
                               widget=forms.PasswordInput(attrs={'class': 'form-login-input'}))


    def clean_password(self, ):
        password = self.cleaned_data['password']
        valid_string = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-?!$#@_")

        if set(password) <= set(valid_string) or len(password) < 6:
            raise ValidationError("Некорректно введенный пароль.")

        return  password


#  Объявите класс формы с именем RegisterForm, не связанной с моделью, со следующими полями
# username: текстовое поле; максимальная длина 50 символов, минимальная длина 5 символов, обязательное, название "Логин";
# email: поле ввода адреса электронной почты; минимальная длина 5 символов, необязательное, название "E-mail";
# first_name: текстовое поле; максимальная длина 50 символов, необязательное, название "Имя";
# last_name: текстовое поле; максимальная длина 50 символов, необязательное, название "Фамилия";
# password1: поле ввода пароля; минимальная длина 6 символов, обязательное, название "Пароль";
# password2: поле ввода пароля; минимальная длина 6 символов, обязательное, название "Повтор пароля".
# Атрибуты класса должны иметь те же названия и порядок, что и в описании.
# Для полей формы через параметр widget укажите стили оформления: attrs={'class': 'form-register-input'}
# Для проверки корректности полей password1 и password2 объявите в классе RegisterForm метод clean следующим образом:
# def clean(self):
#     cleaned_data = super().clean()
#     # продолжение метода
# В этом методе реализуйте проверку значений полей password1 и password2 по следующим критериям:
# а) допустимые символы: буквы латинского алфавита (малые и большие), цифры и символы "-?!$#@_";
# б) минимальная длина пароля 6 символов;
# в) пароли password1 и password2 должны совпадать.
# Если эти проверки не проходят, то генерировать исключения:
# а) raise ValidationError("Некорректно введенный пароль.")
# б) raise ValidationError("Слишком короткий пароль.")
# в) raise ValidationError("Пароли не совпадают.")
# P.S. На экран ничего выводить не нужно.

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50, min_length=5, label='Логин',
                               widget=forms.TextInput(attrs={'class': 'form-register-input'}))
    email = forms.EmailField(min_length=5, label='E-mail',
                             widget=forms.EmailInput(attrs={'class': 'form-register-input'}))
    first_name = forms.CharField(max_length=50, required=False, label='Имя',
                                 widget=forms.TextInput(attrs={'class': 'form-register-input'}))
    last_name = forms.CharField(max_length=50, required=False, label='Фамилия',
                                widget=forms.TextInput(attrs={'class': 'form-register-input'}))
    password1 = forms.CharField(min_length=6, label='Пароль',
                                widget=forms.TextInput(attrs={'class': 'form-register-input'}))
    password2 = forms.CharField(min_length=6, label='Повтор пароля',
                                widget=forms.TextInput(attrs={'class': 'form-register-input'}))

    def clean(self):
        cleaned_data = super().clean()
        p1 = cleaned_data['password1']
        p2 = cleaned_data['password2']
        valid_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-?!$#@_")

        if p1 != p2:
            raise ValidationError("Пароли не совпадают.")
        if not (set(p1) <= set(valid_chars)):
            raise ValidationError("Некорректно введенный пароль.")
        if len(p1) < 6:
            raise ValidationError("Слишком короткий пароль.")

# Объявите класс формы PersonForm, связанной с моделью Person и следующими свойствами, прописанными во вложенном классе Meta:
#
# отображаемые поля (с сохранением порядка): full_name, salary, job;
# поля full_name и job должны иметь CSS-стили attrs={'class': 'form-input'};
# названия полей в HTML-форме: full_name -> "Полное имя"; salary -> "Зарплата"; job -> "Профессия".


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['full_name', 'salary', 'job']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-input'}),
            'job': forms.TextInput(attrs={'class': 'form-input'})
        }
        labels = {
            'full_name': "Полное имя",
            'salary': "Зарплата",
            'job': "Профессия",
        }


# Объявите класс формы SubjectForm, связанной с моделью Subject и следующими свойствами:
#
# отображаемые поля (с сохранением порядка): title, slug, descr, cat; прописывается во вложенном классе Meta;
# поля title и slug должны иметь CSS-стили attrs={'class': 'form-input'}; прописывается во вложенном классе Meta;
# поле descr должно иметь CSS-стили attrs={'cols': 50, 'rows': 5} и быть необязательным; прописывается в форме SubjectForm, как объект класса соответствующего поля;
# поле cat должно наполняться всеми записями из модели Category; не выбранный пункт должен называться "Выберите категорию"; прописывается в форме SubjectForm, как объект класса соответствующего поля.
# P.S. На экран ничего выводить не нужно.

class SubjectForm(forms.ModelForm):
    descr = forms.CharField(required=False, widget=forms.Textarea(attrs={'cols': 50, 'rows': 5}))
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label='Выберите категорию')

    class Meta:
        fields = ['title', 'slug', 'descr', 'cat']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'slug': forms.TextInput(attrs={'class': 'form-input'})
        }

# для метода передачи данных GET представление должно создавать пустую форму CategoryForm и
# с помощью функции render формируется HTML-документ по шаблону 'subject/addcategory.html'
# с передачей в него объекта формы CategoryForm через переменную (ключ) form;
# при получении POST-запроса создать заполненную форму CategoryForm (из принятых данных),
# проверить корректность заполнения формы стандартным методом формы и для корректных данных выполнить сохранение данных формы в БД
# (с помощью соответствующего метода формы); после сохранения данных возвратить объект формы.


def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return form
    else:
        form = CategoryForm()
        return render(request, 'subject/addcategory.html', {'form': form})


# Объявите класс формы AddPersonForm, связанной с моделью Person со следующими свойствами, прописанными во вложенном классе Meta:
#
# отображаемые поля (с сохранением порядка): full_name, age, job;
# поля full_name, age и job должны иметь CSS-стили attrs={'class': 'form-input'}.
# Добавить в класс AddPersonForm метод с именем:
#
# clean_<проверяемое поле>
#
# для проверки, что введенный возраст age меньше 65. Если проверка не проходит, то генерировать исключение:
#
# raise ValidationError("Слишком большой возраст.")
# Иначе, метод должен возвращать значение age.

class AddPersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['full_name', 'age', 'job']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-input'}),
            'age': forms.TextInput(attrs={'class': 'form-input'}),
            'job': forms.TextInput(attrs={'class': 'form-input'}),
        }

    def clean_age(self):
        age = self.cleaned_data['age']
        if age > 64:
            raise ValidationError("Слишком большой возраст.")

        return age

# Необходимо в файле (разделе) forms.py объявить класс формы UploadImageFile, не связанной с моделью для выбора файлов. Этот класс должен содержать одно поле:
#
# upload_image: класс ImageField, обязательное, название "Выберите изображение".
#
# Затем, в файле (разделе) views.py объявить функцию представления upload_image_file со следующим функционалом:
#
# при GET-запросе должна создаваться пустая форма UploadImageFile и с помощью функции render формироваться HTML-документ по шаблону
# 'studio/upload_file.html' с передачей в него объекта формы UploadImageFile через переменную (ключ) form;
# при POST-запросе должна формироваться заполненная форма UploadImageFile, затем, выполняться проверка корректности переданных данных методом is_valid
# и при успешной проверке сохраняться файл путем вызова метода handle_uploaded_image(form.cleaned_data['upload_image']);
# функция upload_image_file и для GET и для POST запросов должна с помощью функции render возвращать HTML-документ по шаблону 'studio/upload_file.html'
# с передачей в него сформированного объекта формы UploadImageFile через переменную (ключ) form.

class UploadImageFile(forms.Form):
    upload_image = forms.ImageField(labels='Выберите изображение')

def upload_image_file(request):
    if request.method == 'POST':
        form = UploadImageFile(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(form.cleaned_data['upload_image'])
            return render(request, 'studio/upload_file.html', {'form': form})
    else:
        form = UploadImageFile()
        return render(request, 'studio/upload_file.html', {'form': form})


from django.db import models
from .models import Subject, District, CityGPT, Street, House, Flat
from django.forms import ModelForm, NumberInput, TextInput, SelectMultiple, Select, ChoiceField

class SubjectForm(ModelForm):
        class Meta:
            model = Subject
            
            #Изменяю заголовки формы
            labels = {
                'name': ('Наименование*'),
                'sorc': ('Тип*'),
                'code': ('Код*'),
                'octd': ('ОКАТО*'),
                'gnimb': ('Код ИФНС*'),
            }        

            #Подставляю нужные мне атрибуты
            widgets = {
                'name': TextInput( attrs = { 'placeholder': 'Омск', 'class':'form-control', 'style': 'text-transform: capitalize;' } ),
                'sorc': Select(attrs = { 'class': 'form-control' }),
                'code': NumberInput( attrs = { 'type': 'number', 'class':'form-control', 'maxlength': 13, 'minlength': 13 } ),
                'octd': NumberInput( attrs = { 'type': 'number', 'class':'form-control', 'maxlength': 11, 'minlength': 11 } ),
                'gnimb': NumberInput( attrs = { 'type': 'number', 'class':'form-control', 'maxlength': 4, 'minlength': 4 } ),
            }


            fields = ['name', 'sorc', 'code', 'octd', 'gnimb']

class DistrictForm(ModelForm):
        class Meta:
            model = District

            labels = {
                'subject' : ('К какому субъекты относится*'),
                'name': ('Наименование*'),
                'sorc': ('Тип*'),
                'code': ('Код*'),
                'octd': ('ОКАТО*'),
                'gnimb': ('Код ИФНС*'),
                'uno': ('Код территориального участка ИФНС*'),
            }        

            widgets = {
                'subject': Select( attrs = { 'class': 'form-control' }),
                'name': TextInput( attrs = { 'placeholder': 'Омск', 'class':'form-control', 'style': 'text-transform: capitalize;' } ),
                'sorc': Select(attrs = { 'class': 'form-control' }),
                'code': NumberInput( attrs = { 'type': 'number', 'class':'form-control', 'maxlength': 13, 'minlength': 13 } ),
                'octd': NumberInput( attrs = { 'type': 'number', 'class':'form-control', 'maxlength': 11, 'minlength': 11 } ),
                'gnimb': NumberInput( attrs = { 'type': 'number', 'class':'form-control', 'maxlength': 4, 'minlength': 4 } ),
                'uno': NumberInput( attrs = { 'type': 'number', 'class':'form-control', 'maxlength': 4, 'minlength': 4 } ),
                
            }


            fields = ['subject', 'name', 'sorc', 'code', 'octd', 'gnimb', 'uno']

class CityGPTForm(ModelForm):
        class Meta:
            model = CityGPT

            labels = {

                'name': ('Наименование*'),
                'sorc': ('Тип*'),
                'code': ('Код*'),
                'octd': ('ОКАТО*'),
                'gnimb': ('Код ИФНС*'),
                'uno': ('Код территориального участка ИФНС*'),
                'district': ('К какому админ. району относится*'),
            }        

            widgets = {
                'name': TextInput( attrs = { 'placeholder': 'Омск', 'class':'form-control', 'style': 'text-transform: capitalize;' } ),
                'sorc': Select(attrs = { 'class': 'form-control' }),
                'code': NumberInput( attrs = { 'type': 'number', 'class':'form-control', 'maxlength': 13, 'minlength': 13 } ),
                'octd': NumberInput( attrs = { 'type': 'number', 'class':'form-control', 'maxlength': 11, 'minlength': 11 } ),
                'gnimb': NumberInput( attrs = { 'type': 'number', 'class':'form-control', 'maxlength': 4, 'minlength': 4 } ),
                'uno': NumberInput( attrs = { 'type': 'number', 'class':'form-control', 'maxlength': 4, 'minlength': 4 } ),
                'district': Select( attrs = { 'class': 'form-control' }),
            }


            fields = ['name', 'sorc', 'code', 'octd', 'gnimb', 'uno', 'district']


class StreetForm(ModelForm):
        class Meta:
            model = Street

            labels = {

                'name': ('Наименование*'),
                'sorc': ('Тип*'),
                'code': ('Код*'),
                'octd': ('ОКАТО*'),
                'gnimb': ('Код ИФНС*'),
                'index': ('Почтовый индекс*'),
                'citygpt': ('К какому городу, населённому пункту относится*')
            }        

            widgets = {
                'name': TextInput( attrs = { 'placeholder': 'Омск', 'class':'form-control', 'style': 'text-transform: capitalize;' } ),
                'sorc': Select(attrs = { 'class': 'form-control' }),
                'code': NumberInput( attrs = { 'type': 'number', 'class':'form-control', 'maxlength': 13, 'minlength': 13 } ),
                'octd': NumberInput( attrs = { 'type': 'number', 'class':'form-control', 'maxlength': 11, 'minlength': 11 } ),
                'gnimb': NumberInput( attrs = { 'type': 'number', 'class':'form-control', 'maxlength': 4, 'minlength': 4 } ),
                'index': NumberInput( attrs = { 'type': 'number', 'class':'form-control', 'maxlength': 6, 'minlength': 6 } ),
                'citygpt': Select( attrs = { 'class': 'form-control' }),
            }


            fields = ['name', 'sorc', 'code', 'octd', 'gnimb', 'index', 'citygpt']

class HouseForm(ModelForm):
        class Meta:
            model = House

            labels = {

                'name': ('Наименование*'),
                'sorc': ('Тип*'),
                'code': ('Код*'),
                'octd': ('ОКАТО*'),
                'gnimb': ('Код ИФНС*'),
                'index': ('Почтовый индекс*'),
                'street': ('К какой улице относится**'),
            }        

            widgets = {
                'name': TextInput( attrs = { 'placeholder': 'Омск', 'class':'form-control', 'style': 'text-transform: capitalize;' } ),
                'sorc': Select(attrs = { 'class': 'form-control' }),
                'code': NumberInput( attrs = { 'type': 'number', 'class':'form-control', 'maxlength': 13, 'minlength': 13 } ),
                'octd': NumberInput( attrs = { 'type': 'number', 'class':'form-control', 'maxlength': 11, 'minlength': 11 } ),
                'gnimb': NumberInput( attrs = { 'type': 'number', 'class':'form-control', 'maxlength': 4, 'minlength': 4 } ),
                'index': NumberInput( attrs = { 'type': 'number', 'class':'form-control', 'maxlength': 6, 'minlength': 6 } ),
                'street': Select( attrs = { 'class': 'form-control' }),
            }


            fields = ['name', 'sorc', 'code', 'octd', 'gnimb', 'index', 'street']

class FlatForm(ModelForm):
        class Meta:
            model = Flat

            labels = {
                'name': ('Номер квартиры*'),
                'floor': ('Этаж*'),
                'house': ('К какому дому относится'),
            }        

            widgets = {
                'name': NumberInput( attrs = { 'type': 'number', 'class':'form-control', 'maxlength': 1, 'minlength': 13 } ),
                'floor': NumberInput( attrs = { 'type': 'number', 'class':'form-control', 'maxlength': 1, 'minlength': 13 } ),
                'house': Select( attrs = { 'class': 'form-control' }),
            }


            fields = ['name', 'floor', 'house']
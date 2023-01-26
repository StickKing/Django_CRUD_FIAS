import re
from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.views.generic import View

from .models import Subject, District, CityGPT, Street, House, Flat
from .forms import SubjectForm, DistrictForm, CityGPTForm, StreetForm, HouseForm, FlatForm

#<<<<<<<<<<<< Субъекты РФ >>>>>>>>>>
def main_page(request):

    try:
        form = SubjectForm(request.POST, request.FILES)
        #использую стандартный метод save для сохранения данныъ в базу данных
        new_person = form.save()
    except Exception as e:
        pass
    
    subjects = Subject.objects.all;

    return render(request, 'fias/list/main.html', { 'subjects': subjects } )

def add_subject_page(request):
    #Создаю переменную класса формы, указываю что она может быть не заполненой 
    subject_form = SubjectForm(request.POST or None)
    #Указываем какой шаблон применить и передаю с ним форму для отображения на странице
    return render(request, 'fias/list/add_subject.html', { 'subject_form': subject_form } )

def update_subject_page(request, id):
    item = Subject.objects.get(id = id)
    #Создаю переменную класса формы, указываю что она может быть не заполненой 
    subject_form = SubjectForm(request.POST or None, instance=item)
    #Указываем какой шаблон применить и передаю с ним форму для отображения на странице
    return render(request, 'fias/list/update_subject.html', { 'subject_form': subject_form, 'id': id } )

def updated_subject_page(request, id):
    updated_item = Subject.objects.get(id=id)
    try:
        form = SubjectForm(request.POST, instance=updated_item)
        #использую стандартный метод save для сохранения данныъ в базу данных
        new_person = form.save()
    except Exception as e:
        pass

    #Указываем какой шаблон применить и передаю с ним форму для отображения на странице
    return render(request, 'fias/list/updated.html' )

def delete_subject(request, id):
    try:
        subject = Subject.objects.get(id=id)
        subject.delete()
        return HttpResponseRedirect("/")
    except Subject.DoesNotExist:
        return HttpResponseNotFound("<h2>Субъект не найден</h2>")

#<<<<<<<<<<<< Административные районы >>>>>>>>>>
def district_page(request):
    try:
        form = DistrictForm(request.POST, request.FILES)
        #использую стандартный метод save для сохранения данныъ в базу данных
        new_form = form.save()
    except Exception as e:
        pass

    subjects = District.objects.all;

    return render(request, 'fias/list/district.html', { 'subjects': subjects } )

def add_district_page(request):
    #Создаю переменную класса формы, указываю что она может быть не заполненой 
    added_form = DistrictForm(request.POST or None)
    #Указываем какой шаблон применить и передаю с ним форму для отображения на странице
    return render(request, 'fias/list/add_district.html', { 'added_form': added_form } )

def update_district_page(request, id):
    item = District.objects.get(id = id)
    #Создаю переменную класса формы, указываю что она может быть не заполненой 
    added_form = DistrictForm(request.POST or None, instance=item )
    #Указываем какой шаблон применить и передаю с ним форму для отображения на странице
    return render(request, 'fias/list/update_district.html', { 'added_form': added_form, 'id': id } )

def updated_district_page(request, id):
    updated_item = District.objects.get(id=id)
    try:
        form = DistrictForm(request.POST, instance=updated_item)
        #использую стандартный метод save для сохранения данныъ в базу данных
        new_form = form.save()
    except Exception as e:
        pass
    updated_item.save()
    #Указываем какой шаблон применить и передаю с ним форму для отображения на странице
    return render(request, 'fias/list/updated.html' )

def delete_district(request, id):
    try:
        subject = District.objects.get(id=id)
        subject.delete()
        return HttpResponseRedirect("/District/")
    except Subject.DoesNotExist:
        return HttpResponseNotFound("<h2>Субъект не найден</h2>")




#<<<<<<<<<<<< Город населённый пункт посёлки >>>>>>>>>>
def city_gpt_page(request):

    try:
        form = CityGPTForm(request.POST, request.FILES)
        #использую стандартный метод save для сохранения данныъ в базу данных
        new_form = form.save()
    except Exception as e:
        pass
    subjects = CityGPT.objects.all;

    return render(request, 'fias/list/city_gpt.html', { 'subjects': subjects } )

def add_city_gpt_page(request):
    #Создаю переменную класса формы, указываю что она может быть не заполненой 
    added_form = CityGPTForm(request.POST or None)
    #Указываем какой шаблон применить и передаю с ним форму для отображения на странице
    return render(request, 'fias/list/add_city_gpt.html', { 'added_form': added_form } )

def update_city_gpt_page(request, id):
    item = CityGPT.objects.get(id = id)
    #Создаю переменную класса формы, указываю что она может быть не заполненой 
    added_form = CityGPTForm(request.POST or None, instance=item)
    #Указываем какой шаблон применить и передаю с ним форму для отображения на странице
    return render(request, 'fias/list/update_city_gpt.html', { 'added_form': added_form, 'id': id } )

def updated_city_gpt_page(request, id):
    updated_item = CityGPT.objects.get(id=id)
    #Создаю переменную класса формы, указываю что она может быть не заполненой 
    try:
        form = CityGPTForm(request.POST, instance=updated_item)
        #использую стандартный метод save для сохранения данныъ в базу данных
        new_form = form.save()
    except Exception as e:
        pass


    #Указываем какой шаблон применить и передаю с ним форму для отображения на странице
    return render(request, 'fias/list/updated.html' )

def delete_city_gpt(request, id):
    try:
        subject = CityGPT.objects.get(id=id)
        subject.delete()
        return HttpResponseRedirect("/CityGPT/")
    except Subject.DoesNotExist:
        return HttpResponseNotFound("<h2>Субъект не найден</h2>")







#<<<<<<<<<<<< Улицы >>>>>>>>>>
def street_page(request):

    try:
        form = StreetForm(request.POST, request.FILES)
        #использую стандартный метод save для сохранения данныъ в базу данных
        new_form = form.save()
    except Exception as e:
        pass
    subjects = Street.objects.all;

    return render(request, 'fias/list/street.html', { 'subjects': subjects } )

def add_street_page(request):
    #Создаю переменную класса формы, указываю что она может быть не заполненой 
    added_form = StreetForm(request.POST or None)
    #Указываем какой шаблон применить и передаю с ним форму для отображения на странице
    return render(request, 'fias/list/add_street.html', { 'added_form': added_form } )

def update_street_page(request, id):
    item = Street.objects.get(id = id)
    #Создаю переменную класса формы, указываю что она может быть не заполненой 
    added_form = StreetForm(request.POST or None, instance=item)
    #Указываем какой шаблон применить и передаю с ним форму для отображения на странице
    return render(request, 'fias/list/update_street.html', { 'added_form': added_form, 'id': id } )

def updated_street_page(request, id):
    updated_item = Street.objects.get(id=id)
    #Создаю переменную класса формы, указываю что она может быть не заполненой 
    try:
        form = StreetForm(request.POST, instance=updated_item)
        #использую стандартный метод save для сохранения данныъ в базу данных
        new_form = form.save()
    except Exception as e:
        pass
    #Указываем какой шаблон применить и передаю с ним форму для отображения на странице
    return render(request, 'fias/list/updated.html' )

def delete_street(request, id):
    try:
        subject = Street.objects.get(id=id)
        subject.delete()
        return HttpResponseRedirect("/Street/")
    except Subject.DoesNotExist:
        return HttpResponseNotFound("<h2>Субъект не найден</h2>")


#<<<<<<<<<<<< Дома >>>>>>>>>>
def house_page(request):
    try:
        form = HouseForm(request.POST, request.FILES)
        #использую стандартный метод save для сохранения данныъ в базу данных
        new_form = form.save()
    except Exception as e:
        pass
    subjects = House.objects.all;

    return render(request, 'fias/list/house.html', { 'subjects': subjects } )

def add_house_page(request):
    #Создаю переменную класса формы, указываю что она может быть не заполненой 
    added_form = HouseForm(request.POST or None)
    #Указываем какой шаблон применить и передаю с ним форму для отображения на странице
    return render(request, 'fias/list/add_house.html', { 'added_form': added_form } )

def update_house_page(request, id):
    item = House.objects.get(id = id)
    #Создаю переменную класса формы, указываю что она может быть не заполненой 
    added_form = HouseForm(request.POST or None, instance=item)
    #Указываем какой шаблон применить и передаю с ним форму для отображения на странице
    return render(request, 'fias/list/update_house.html', { 'added_form': added_form, 'id': id } )

def updated_house_page(request, id):
    updated_item = House.objects.get(id=id)
    #Создаю переменную класса формы, указываю что она может быть не заполненой 
    try:
        form = HouseForm(request.POST, instance=updated_item)
        #использую стандартный метод save для сохранения данныъ в базу данных
        new_form = form.save()
    except Exception as e:
        pass
    #Указываем какой шаблон применить и передаю с ним форму для отображения на странице
    return render(request, 'fias/list/updated.html' )

def delete_house(request, id):
    try:
        subject = House.objects.get(id=id)
        subject.delete()
        return HttpResponseRedirect("/House/")
    except Subject.DoesNotExist:
        return HttpResponseNotFound("<h2>Субъект не найден</h2>")



class FlatCreate(View):    
    def get(self, request):
        added_form = FlatForm(request.POST or None)
        #Указываем какой шаблон применить и передаю с ним форму для отображения на странице
        return render(request, 'fias/list/add_flat.html', { 'added_form': added_form } )


def flat_page(request):
    try:
        form = FlatForm(request.POST, request.FILES)
        #использую стандартный метод save для сохранения данныъ в базу данных
        new_form = form.save()
    except Exception as e:
        pass
    subjects = Flat.objects.all;

    return render(request, 'fias/list/flat.html', { 'subjects': subjects } )

def update_flat_page(request, id):
    item = Flat.objects.get(id = id)
    #Создаю переменную класса формы, указываю что она может быть не заполненой 
    added_form = FlatForm(request.POST or None, instance=item)
    #Указываем какой шаблон применить и передаю с ним форму для отображения на странице
    return render(request, 'fias/list/update_flat.html', { 'added_form': added_form, 'id': id } )

def updated_flat_page(request, id):
    updated_item = Flat.objects.get(id=id)
    #Создаю переменную класса формы, указываю что она может быть не заполненой 
    try:
        form = FlatForm(request.POST, instance=updated_item)
        #использую стандартный метод save для сохранения данныъ в базу данных
        new_form = form.save()
    except Exception as e:
        pass
    #Указываем какой шаблон применить и передаю с ним форму для отображения на странице
    return render(request, 'fias/list/updated.html' )

def delete_flat(request, id):
    try:
        subject = Flat.objects.get(id=id)
        subject.delete()
        return HttpResponseRedirect("/Flat/")
    except Subject.DoesNotExist:
        return HttpResponseNotFound("<h2>Субъект не найден</h2>")
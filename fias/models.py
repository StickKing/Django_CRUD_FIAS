from django.db import models

#Таблица сокращений
class SorcName(models.Model):

    #Наименование типа адресного объекта
    name = models.CharField(max_length=100, null=False)
    #Уровень адресного объекта
    level = models.SmallIntegerField(null=True, default = 1, blank = True)
    #Сокращённое наименование типа адресного объекта
    sorc = models.CharField(max_length=100, null=False)
    
    #Метод возвращающий строки соответствующие определённому уровню
    def SorcToTuple(level = 1):
        #Списочным выражением создаю список нужных объектов
        sorc_tuple = [ (i.sorc, i.name) for i in SorcName.objects.filter(level = level) ]
        #Возвращаю кортёж с данными
        return tuple(sorc_tuple)
    
    #Изменяю встроенный метод __str__
    def __str__(self):
        return f'{self.name} {self.sorc}'


#Таблица субъектов РФ
class Subject(models.Model):

    #Наименование субъекта РФ
    name = models.CharField(max_length=100, null=False)
    #Сокращённое наименование типа адресного объекта
    sorc = models.CharField(choices = SorcName.SorcToTuple(), max_length = 100 )
    #Классификационный код адресного объекта
    code = models.CharField(max_length=100, null=False)
    #Код ОКАТО
    octd = models.CharField(max_length=100, null=True)
    #Код ИФНС
    gnimb = models.CharField(max_length=100, null=True)
    
    #Изменяю встроенный метод __str__
    def __str__(self):
        return self.name + ' ' + self.code

#Таблица административных районов
class District(models.Model):

    #Создание связи один ко многим с субъектами РФ
    subject = models.ForeignKey(Subject, on_delete = models.CASCADE)

    #Наименование административного района
    name = models.CharField(max_length=100, null=False)
    #Сокращённое наименование типа адресного объекта
    sorc = models.CharField(choices = SorcName.SorcToTuple(2), max_length = 100 )
    #Классификационный код адресного объекта
    code = models.CharField(max_length=100, null=False)
    #Код ОКАТО
    octd = models.CharField(max_length=100, null=True)
    #Код ИФНС
    gnimb = models.CharField(max_length=100, null=True)
    #Код территориального участка ИФНС
    uno = models.CharField(max_length=100, null=True)
    
    #Изменяю встроенный метод __str__
    def __str__(self):
        return self.name + ' ' + self.code

#Таблица населённых пунктов
class CityGPT(models.Model):

    #Создание связи один ко многим с админ. районами
    district = models.ForeignKey(District, on_delete = models.CASCADE)

    #Наименование населённого пункта
    name = models.CharField(max_length=100, null=False)
    #Сокращённое наименование типа адресного объекта
    sorc = models.CharField(choices = SorcName.SorcToTuple(3), max_length = 100 )
    #Классификационный код адресного объекта
    code = models.CharField(max_length=100, null=False)
    #Код ОКАТО
    octd = models.CharField(max_length=100, null=True)
    #Код ИФНС
    gnimb = models.CharField(max_length=100, null=True)
    #Код территориального участка ИФНС
    uno = models.CharField(max_length=100, null=True)
    
    #Изменяю встроенный метод __str__
    def __str__(self):
        return self.name + ' ' + self.code

#Таблица улиц
class Street(models.Model):

    #Создание связи один ко многим с населёнными пунктами
    citygpt = models.ForeignKey(CityGPT, on_delete = models.CASCADE)

    #Наименование улицы
    name = models.CharField(max_length=100, null=False)
    #Сокращённое наименование типа адресного объекта
    sorc = models.CharField(choices = SorcName.SorcToTuple(4), max_length = 100 )
    #Классификационный код адресного объекта
    code = models.CharField(max_length=100, null=False)
    #Код ОКАТО
    octd = models.CharField(max_length=100, null=False)
    #Код ИФНС
    gnimb = models.CharField(max_length=100, null=True)
    #Почтовый индекс
    index = models.CharField(max_length=100, null=True)
    
    #Изменяю встроенный метод __str__
    def __str__(self):
        return self.name + ' ' + self.code

#Таблица домов
class House(models.Model):

    #Создание связи один ко многим с улицами
    street = models.ForeignKey(Street, on_delete = models.CASCADE)

    #Номер дома
    name = models.CharField(max_length=100, null=False)
    #Сокращённое наименование типа адресного объекта
    sorc = models.CharField(choices = SorcName.SorcToTuple(5), max_length = 100 )
    #Классификационный код адресного объекта
    code = models.CharField(max_length=100, null=False)
    #Код ОКАТО
    octd = models.CharField(max_length=100, null=True)
    #Код ИФНС
    gnimb = models.CharField(max_length=100, null=True)
    #Почтовый индекс
    index = models.CharField(max_length=100, null=True)
    
    #Изменяю встроенный метод __str__
    def __str__(self):
        return self.name + ' ' + self.code

#Таблица квартир
class Flat(models.Model):

    #Создание связи один ко многим с домами 
    house = models.ForeignKey(House, on_delete = models.CASCADE)

    #Номер квартиры
    name = models.SmallIntegerField(null = False, blank = False)
    #Этаж
    floor = models.SmallIntegerField(null = False, blank = False)
    
    #Изменяю встроенный метод __str__
    def __str__(self):
        return self.name + ' ' + self.floor
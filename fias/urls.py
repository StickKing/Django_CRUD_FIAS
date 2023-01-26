from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    #Субъекты РФ
    path('', views.main_page, name = 'main_page'),
    path('addSubject/', views.add_subject_page, name = 'add_subject_page'),
    path('Subject/Update/<int:id>', views.update_subject_page, name = 'update_subject_page'),
    path('Subject/Updated/<int:id>', views.updated_subject_page, name = 'updated_subject_page'),
    path('Subject/Delete/<int:id>', views.delete_subject, name = 'delete_subject'),

    #Адмиснитративные раоны
    path('District/', views.district_page, name = 'district_page'),
    path('addDistrict/', views.add_district_page, name = 'add_district_page'),
    path('District/Update/<int:id>', views.update_district_page, name = 'update_district_page'),
    path('District/Updated/<int:id>', views.updated_district_page, name = 'updated_district_page'),
    path('District/Delete/<int:id>', views.delete_district, name = 'delete_district'),

    #Населённые пункты
    path('CityGPT/', views.city_gpt_page, name = 'city_gpt_page'),
    path('addCityGPT/', views.add_city_gpt_page, name = 'add_city_gpt_page'),
    path('CityGPT/Update/<int:id>', views.update_city_gpt_page, name = 'update_city_gpt_page'),
    path('CityGPT/Updated/<int:id>', views.updated_city_gpt_page, name = 'updated_city_gpt_page'),
    path('CityGPT/Delete/<int:id>', views.delete_city_gpt, name = 'delete_city_gpt'),

    #Улицы
    path('Street/', views.street_page, name = 'street_page'),
    path('addStreet/', views.add_street_page, name = 'add_street_page'),
    path('Street/Update/<int:id>', views.update_street_page, name = 'update_street_page'),
    path('Street/Updated/<int:id>', views.updated_street_page, name = 'updated_street_page'),
    path('Street/Delete/<int:id>', views.delete_street, name = 'delete_street'),

    #Дома
    path('House/', views.house_page, name = 'house_page'),
    path('addHouse/', views.add_house_page, name = 'add_house_page'),
    path('House/Update/<int:id>', views.update_house_page, name = 'update_house_page'),
    path('House/Updated/<int:id>', views.updated_house_page, name = 'updated_house_page'),
    path('House/Delete/<int:id>', views.delete_house, name = 'delete_house'),

    #Квартиры
    path('addFlat/', views.FlatCreate.as_view(), name = 'add_flat_page'),
    path('Flat/', views.flat_page, name = 'flat_page'),
    path('Flat/Update/<int:id>', views.update_flat_page, name = 'update_flat_page'),
    path('Flat/Updated/<int:id>', views.updated_flat_page, name = 'updated_flat_page'),
    path('Flat/Delete/<int:id>', views.delete_flat, name = 'delete_flat'),

]
#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
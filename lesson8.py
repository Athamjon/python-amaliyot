# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 15:02:48 2022

@author: ASUS
"""
#dad = {
   #    'ism':'baxtiyor maxmudov',
   #    'yosh':45,
    #   'kasb':'fermer',
   #   'yil':1977
   #    }
#print(f"Mening dadam {dad['ism'].title()},\
 #     {dad['yil']}-yilda tug'ilgan,\
 #     kasbi {dad['kasb'].title()},\
   #   yoshi {dad['yosh']} da") 
   
   
   
""" household = {
             'dad':'osh',
             'mum':'Mastava',
             'sister':'chuchvara',
             'I':'qozon kabob'
     } 
print(f"Dadamning sevimli ovqati {household['dad'].upper()}")
print(f"Mening sevimli ovqatim {household['I'].title()}")
print(f"Oyimning sevimli ovqati {household['mum'].lower()}") """


"""python = {
          'string':'matn',
          'integer':'butun son',
          'float':'kasr son',
          'if':'shart operatori agar degani',
          'elif':'shart operatori aks holda degani',
          'else':'shart operatori aks holda degani bu',
          'list':'ro\'yxat',
          'typle':'o\'zgarmas ro\'yxat',
          'for':'takrorlanish operatori'
    }
word = input("Biror so'z kiriting: \n").lower()
if word in python:
    print(python.get(word))
else:
    print("This is word not available")
#print(python.get(word, "this is word not available"))"""

"""python = {
          'string':'matn',
          'integer':'butun son',
          'float':'kasr son',
          'if':'shart operatori agar degani',
          'elif':'shart operatori aks holda degani',
          'else':'shart operatori aks holda degani bu',
          'list':'ro\'yxat',
          'typle':'o\'zgarmas ro\'yxat',
          'for':'takrorlanish operatori'
    }

for k, q in sorted(python.items()):
    print(f"{k.title()}-{q}")                   """
    
"""countries = {
             'AQSH':'Vashington',
             'Angliya':'London',
             'Fransiya':'Parij',
             'Uzbekistan':'Toshkent',
             'Yaponiya':'Tokio',
             'BAA':'Abu Dabi'
    }
print("Countries of the world:\n")
for k in sorted(countries.keys()):
    print(f"{k.upper()}")

print("Capital of the countries:\n")
for q in sorted(countries.values()):
    print(q.upper())"""

"""countries = {
             'aqsh':'vashington',
             'angliya':'london',
             'fransiya':'parij',
             'uzbekistan':'toshkent',
             'yaponiya':'tokio',
             'baa':'abu aabi'
    }

print("Biror davlatni poytaxtini bilishni istaysizmi?\n")
word = input("Biror davlatni kiriting:\n").lower()
capital = countries.get(word)
if word in countries:
    print(f"{word.title()} ning poytaxti {capital.title()}")
else:
    print("I do not have about this information")"""

"""menu = {
        'osh':30000,
        'kabob':12000,
        'chuchvara':13000,
        'dimlama':20000,
        'bishteks':25000,
        'norin':23000,
        'sho\'rva':28000,
        'mastava':14000,
        'qo\'g\'irma':30000,
        'girl':45000
     }
print("Istalgan 3 ta taom kiriting:\n")
buyurtmalar = []
for n in range(3):
   buyurtmalar.append(input(f"{n+1}-taom:\n").lower())
   
for buyurtma in buyurtmalar:
    if buyurtma in menu:
        print(f"{buyurtma.title()}ning narxi {menu[buyurtma]} so'm")
    else:
        print(f"This is {buyurtma.title()} not available in menu")"""


    
"""person = {
          'ism':'alisher navoiy',
          'yil':1441,
          'joy':'hirot',
          'asar':['layli & majnun', 'sabbayi sayyor']
    }

person1 = {
           'ism':'amir temur',
           'yil':1336,
           'joy':'kesh',
           'asar':['temur tuzuklari', 'kuch birlikda']
    }

person2 = {
           'ism':'islom karimov',
           'yil':1938,
           'joy':'samarqand',
           'asar':['tinchlik', 'prezident']
    }

persons = [person, person1, person2]

for shaxs in persons:
  #  print(f"{shaxs['ism'].title()} {shaxs['yil']}-yilda {shaxs['joy'].title()} da tug'ilgan")
    print(f"{shaxs['ism'].title()}ning mashxur asarlari:\n"
          f"{shaxs['asar'] [0].title()} \n" 
          f"{shaxs['asar'] [1].title()}") """



"""friend = {
             'shoxrux':['terminator', 'forsaj', 'scorpion' ],
             'bahrom':['muhabbat oyatlari', 'umar ibn hattob', 'abdulhamidxon'],
             'ozod':['merlin', 'sevgi afsonasi', 'uyda yolg\'iz']
    }

for ism, kinolar in friend.items():
    print(f"{ism.title()}ning sevimli kinolari: ")
    for kino in kinolar:
        print(f"{kino.title()}")"""
        
davlatlar = {
             
             'uzbekiston':{
                           'poytaxt':'toshkent',
                           'maydoni':338.8,
                           'aholi':36000000,
                           'pul':'so\'m'
                 },
             'aqsh':{
                           'poytaxt':'vashington',
                           'maydoni':986.8,
                           'aholi':156000000,
                           'pul':'dollar'
                 },
             'turkiya':{
                           'poytaxt':'anqara',
                           'maydoni':497.8,
                           'aholi':98000000,
                           'pul':'lira'
                 },
 
    }

davlat = input("Davlat nomini kiriting:\n").lower()
if davlat in davlatlar:
    info = davlatlar[davlat]
    print(f"\n {davlat.capitalize()}ning poytaxti: {info['poytaxt'].title()}"
       f"\n Maydoni: {info['maydoni']} kv.km"
       f"\n Aholisi: {info['aholi']}"
       f"\n Pul birligi: {info['pul'].title()}")
else:
    print(f"We do not have this information about {davlat.capitalize()}")

























   
"""countries = ['uzbekiston', 'aqsh', 'turkiya']    
print("Birorta davlat haqida ma'lumot bilishni istaysizmi?\n")
information = input("Unda davlatni kiriting:\n").lower()        
for davlat, info in davlatlar.items():
    if davlat.lower() == 'aqsh':
        davlat= davlat.upper()
    else:
        davlat = davlat.capitalize()
    if information in countries:
       print(f"\n {davlat}ning poytaxti: {info['poytaxt'].title()}"
          f"\n Maydoni: {info['maydoni']}"
          f"\n Aholisi: {info['aholi']}"
          f"\n Pul birligi: {info['pul'].title()}")
    else:
        print("We do not have this information!")"""






































































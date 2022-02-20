# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 21:44:58 2022

@autho"""

"""print("Yoqtirgan kitoblarizni chiqaruvchi dastur:\n")
kitob = "Yoqtirgan kitoblarizni kiriting!\n"
kitob+= "Dasturni to'xtatish uchun 'stop' deb yozing\n"
qiymat = ''
while qiymat != 'stop':
    qiymat = input(kitob.capitalize())
    if qiymat != 'stop':
        print(kitob.capitalize())
print("Dastur tugadi!")"""        


"""ism = input("Ismingizni kiriting!\n")
yosh = input(f" Salom {ism.title()}. Yoshingiz nechida ?\n")
#yosh = input(yosh)
while True:
    qiymat = input(yosh)
    if qiymat == 'exit' or qiymat == 'quit':
        break
    yosh = int(yosh)
    if yosh<7:
        price = 2000
    elif 7<=yosh<=18:
        price = 3000
    elif 18<yosh<65:
        price = 10000
    else:
        price = 0
    if price == 0:
        print(f"Sizga chipta bepul!\n")
    else:
        print(f"Sizga chipta {price} so'm")"""



"""savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    
    if qiymat=='exit':
        break
    elif float(qiymat)<0:
        continue
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")"""










"""savol ="Yaxshi ko'rgan kitoblarizni kiriting!\n"

while True:
    qiymat = input(savol)
    if qiymat == 'exit':
        break
    else:
        print(qiymat.title())
print("Dastur tugadi")   """



"""ism = input("Ismingizni kiriting!\n")
yosh = input(f"Salom {ism.title()}. Yoshingiz nechchida?\n")
#yosh = input(yosh)
ishora = True
while ishora:
    qiymat = input(yosh)
    if qiymat == 'exit' or qiymat == 'quit':
        ishora = False
    else:
         yosh = int(yosh)
    if yosh<7:
        price = 2000
    elif 7<=yosh<18:
        price = 3000
    elif 18<=yosh<65:
        price = 10000
    else:
        price = 0
    if price == 0:
        print("Sizga chipta bepul")
    else:
        print(f"Sizga chipta {price} so'm")
print("Dastur tugadi!")"""






buyurtmalar = []
ism = input("Ismingizni kiriting!\n")
print(f"Salom {ism.title()}. Biror nima buyurtma bering!\n")

while True:
    savol = input("Buyurtma berishiz mumkin!\n")
   # buyurtma = input(savol)
    buyurtmalar.append(savol)
    
    javob = input("Dasturni davom ettirasizmi ha/yoq\n")
    if javob == 'ha':
        continue
    else:
        break
    
#print(buyurtmalar)
print("Sizning buyurtmalaringiz:\n")
for zakaz in buyurtmalar:
    print(f"{zakaz.title()}")
     




































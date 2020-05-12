def generator(list):
    for index in range(0,12):
        yield print(list[index])


list = ['Styczen','Luty','Marzec','Kwiecien','Maj',"Czerwiec","lipiec",
    "sierpień","Wrzesień","Październik","listopad","grudzień"]


x = generator(list)

for i in range(0,12):
    next(x)


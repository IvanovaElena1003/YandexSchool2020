import pandas as pd
import numpy as np


# метод для парсинга даты в целое число секунд
def hms_to_seconds(t):
    ty = t.split(' ')
    time = ty[2]
    h, m, s = [int(i) for i in time.split(':')]
    return 86400*int(ty[0]) + 3600*h + 60*m + s

#Считываем данные из файлов
purchases = pd.read_csv('purchases.csv', delimiter=',')
visits = pd.read_csv('t1.csv', delimiter=',')

#Приведём дату в удобный вид и формат
visits['start_dt'] = pd.to_datetime(visits['start_dt'], errors="coerce") .dt.strftime("%Y-%m-%d %H:%M:%S")
visits['start_dt'] = pd.to_datetime(visits['start_dt'], errors="coerce")
visits['end_ts'] = pd.to_datetime(visits['end_ts'], errors="coerce").dt.strftime("%Y-%m-%d %H:%M:%S")
visits['end_ts'] = pd.to_datetime(visits['end_ts'], errors="coerce")
#Посчитаем время визита
visits['time'] = visits['end_ts'] - visits['start_dt']

#Теперь необходимо преобразовать данное время в число секунд.
time = []
for index, row in visits.iterrows():
    time.append(hms_to_seconds(str(row['time'])))
visits['time_v'] = pd.Series(time, index=visits.index)

#####################
# 1.	Определение когорт.
# Для определение когорт, необходимо посчитать количество уникальных значений по двум столбцам
a = visits[['device', 'source_id']]
u = np.unique(a.apply(tuple, axis=1))
# уникальные когорты
print(u)
print('\n')

#####################
# 2.	Распределение Users по когортам.
# Находим первые вхождения уникальных юзеров
b = visits[['uid']]
uid, index = np.unique(b, return_index=True)
# отбираем строки соответствующие первых вхождениям клиентов
uuid = visits.loc[index]

# сюда будем записывать id кагорты
t = []
# на место каждого элемента массива, будет накопленное значение по кагорте
# 4.	Revenue по когорте.
price_k = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# 5.	Lifetime по когорте.
time_k1 = []
time_k2 = []
time_k3 = []
time_k4 = []
time_k5 = []
time_k6 = []
time_k7 = []
time_k8 = []
time_k9 = []
time_k10 = []
time_k11 = []
time_k12 = []
time_k13 = []
time_k14 = []
time_k15 = []
time_k16 = []
time_k17 = []
time_k18 = []

for index, row in uuid.iterrows():
    for i in range(0, len(u)): # пробегаемся по всем когортам
        if row['device'] == u[i][0] and row['source_id'] == u[i][1]: # Смотрим к какой относится клиент
            t.append(i) # фиксируем когорту для клиента
            id_price = purchases.query('uid ==' + str(row['uid'])) # Ищем все покупки клиента
            id_time = visits.query('uid ==' + str(row['uid'])) # Ищем все визиты клиента
            price_k[i] = price_k[i] + id_price['revenue'].sum() #Считаем сумму и суммируем с суммой когорты.
            #Считаем медиану и ложим в когорту.
            if i == 0:
                time_k1.append(id_time['time_v'].median())
            if i == 1:
                time_k2.append(id_time['time_v'].median())
            if i == 2:
                time_k3.append(id_time['time_v'].median())
            if i == 3:
                time_k4.append(id_time['time_v'].median())
            if i == 4:
                time_k5.append(id_time['time_v'].median())
            if i == 5:
                time_k6.append(id_time['time_v'].median())
            if i == 6:
                time_k7.append(id_time['time_v'].median())
            if i == 7:
                time_k8.append(id_time['time_v'].median())
            if i == 8:
                time_k9.append(id_time['time_v'].median())
            if i == 9:
                time_k10.append(id_time['time_v'].median())
            if i == 10:
                time_k11.append(id_time['time_v'].median())
            if i == 11:
                time_k12.append(id_time['time_v'].median())
            if i == 12:
                time_k13.append(id_time['time_v'].median())
            if i == 13:
                time_k14.append(id_time['time_v'].median())
            if i == 14:
                time_k15.append(id_time['time_v'].median())
            if i == 15:
                time_k16.append(id_time['time_v'].median())
            if i == 16:
                time_k17.append(id_time['time_v'].median())
            if i == 17:
                time_k18.append(id_time['time_v'].median())


# каждый клиент в своей когорте
uuid['cohort'] = pd.Series(t[:len(uuid['uid'])], index=uuid.index)
print(uuid)


# 3. Количество Users по когорте.
cohort, count = np.unique(uuid['cohort'], return_counts=True)
for i in range(0, len(cohort)):
    print('In ' + str(u[cohort[i]]) + ' - ' + str(count[i]) + ' Users')

print('\n')
##############
# 4.	Revenue по когорте.
for i in range(0, len(u)):
    print('In ' + str(u[i]) + ' - ' + str(price_k[i]) + ' revenue')

print('\n')
##############
# 5.	Lifetime по когорте.
for i in range(0, len(u)):
    if i == 0:
        print('In ' + str(u[i]) + ' - ' + str(np.median(time_k1)) + ' median time (second)')
    if i == 1:
        print('In ' + str(u[i]) + ' - ' + str(np.median(time_k2)) + ' median time (second)')
    if i == 2:
        print('In ' + str(u[i]) + ' - ' + str(np.median(time_k3)) + ' median time (second)')
    if i == 3:
        print('In ' + str(u[i]) + ' - ' + str(np.median(time_k4)) + ' median time (second)')
    if i == 4:
        print('In ' + str(u[i]) + ' - ' + str(np.median(time_k5)) + ' median time (second)')
    if i == 5:
        print('In ' + str(u[i]) + ' - ' + str(np.median(time_k6)) + ' median time (second)')
    if i == 6:
        print('In ' + str(u[i]) + ' - ' + str(np.median(time_k7)) + ' median time (second)')
    if i == 7:
        print('In ' + str(u[i]) + ' - ' + str(np.median(time_k8)) + ' median time (second)')
    if i == 8:
        print('In ' + str(u[i]) + ' - ' + str(np.median(time_k9)) + ' median time (second)')
    if i == 9:
        print('In ' + str(u[i]) + ' - ' + str(np.median(time_k10)) + ' median time (second)')
    if i == 10:
        print('In ' + str(u[i]) + ' - ' + str(np.median(time_k11)) + ' median time (second)')
    if i == 11:
        print('In ' + str(u[i]) + ' - ' + str(np.median(time_k12)) + ' median time (second)')
    if i == 12:
        print('In ' + str(u[i]) + ' - ' + str(np.median(time_k13)) + ' median time (second)')
    if i == 13:
        print('In ' + str(u[i]) + ' - ' + str(np.median(time_k14)) + ' median time (second)')
    if i == 14:
        print('In ' + str(u[i]) + ' - ' + str(np.median(time_k15)) + ' median time (second)')
    if i == 15:
        print('In ' + str(u[i]) + ' - ' + str(np.median(time_k16)) + ' median time (second)')
    if i == 16:
        print('In ' + str(u[i]) + ' - ' + str(np.median(time_k17)) + ' median time (second)')
    if i == 17:
        print('In ' + str(u[i]) + ' - ' + str(np.median(time_k18)) + ' median time (second)')

print('\n')

##############
# 6.Для каждой когорты посчитать LTV.

for i in range(0, len(u)):
    print('LTV' + str(i) + ' = ' + str(price_k[i] / count[i]))
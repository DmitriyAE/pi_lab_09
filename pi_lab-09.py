# 7. Найти средний возраст пассажиров по каждому классу обслуживания (поле Pclass, указав количество
# братьев, сестер... (столбец SibSp): [0, ..., 8])
import matplotlib.pyplot as plt
import streamlit as st

# Функция, которая вычисляет средний возраст пассажиров каждого класса на основе данных из файла
def calculate_average_age(filename, consider_family_size=False, family_size=None):
    class1_total_age = 0
    class1_passenger_count = 0
    class2_total_age = 0
    class2_passenger_count = 0
    class3_total_age = 0
    class3_passenger_count = 0

    with open(filename) as file:
        for line in file:
            data = line.strip().split(',')
            if data[6] == 'Age' or data[6] == '' or data[2] == 'Pclass' or data[2] == '':
                continue
            if not consider_family_size or (consider_family_size and data[7] == str(family_size)):
                if data[2] == '1':
                    class1_total_age += float(data[6])
                    class1_passenger_count += 1
                elif data[2] == '2':
                    class2_total_age += float(data[6])
                    class2_passenger_count += 1
                elif data[2] == '3':
                    class3_total_age += float(data[6])
                    class3_passenger_count += 1

        class1_average_age = 0
    if class1_passenger_count > 0:
        class1_average_age = class1_total_age / class1_passenger_count

    class2_average_age = 0
    if class2_passenger_count > 0:
        class2_average_age = class2_total_age / class2_passenger_count

    class3_average_age = 0
    if class3_passenger_count > 0:
        class3_average_age = class3_total_age / class3_passenger_count

    return class1_average_age, class2_average_age, class3_average_age

# Визуализируем решение
st.image('titaniс.jpg')
st.subheader('Средний возраст пассажиров парохода «Титаник» по каждому классу обслуживания в зависимости от количества родственников (братьев, сестер, сводных братьев, сводных сестер, супругов на борту).')
family_size_options = ['Без учета родственников', '0', '1', '2', '3', '4', '5', '6', '7', '8']
class_service = ['1 класс', '2 класс', '3 класс']
selected_family_size = st.selectbox('Для просмотра данных выберите значение поля SibSp:', family_size_options)

# Заполняем таблицу в зависимости от выбора selected_family_size
if selected_family_size == 'Без учета родственников':
    class1_avg, class2_avg, class3_avg = calculate_average_age('data.csv')
    st.table({'Класс обслуживания': class_service, 'Средний возраст': [class1_avg, class2_avg, class3_avg]})
else:
    family_size = int(selected_family_size)
    class1_avg, class2_avg, class3_avg = calculate_average_age('data.csv', consider_family_size=True, family_size=family_size)
    st.table({'Класс обслуживания': class_service, 'Средний возраст': [class1_avg, class2_avg, class3_avg]})

# Строим столбчатую диаграмму в зависимости от выбора selected_family_size
plt.figure(figsize=(8, 4))
if selected_family_size == 'Без учета родственников':
    plt.bar(class_service, [class1_avg, class2_avg, class3_avg])
    plt.xlabel('Класс пассажира (Pclass)')
    plt.ylabel('Средний возраст')
    plt.title(f'Средний возраст пассажиров по классам обслуживания')
    st.pyplot(plt)
else:
    plt.bar(class_service, [class1_avg, class2_avg, class3_avg])
    plt.xlabel('Класс пассажира (Pclass)')
    plt.ylabel('Средний возраст')
    if selected_family_size == '1':
        plt.title(f'Средний возраст пассажиров по классам обслуживания для {selected_family_size} родственника')
    else:
        plt.title(f'Средний возраст пассажиров по классам обслуживания для {selected_family_size} родственников')
    st.pyplot(plt)

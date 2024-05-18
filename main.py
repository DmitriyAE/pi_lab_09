# 7. Найти средний возраст пассажиров по каждому классу обслуживания (поле Pclass, указав количество
# братьев, сестер... (столбец SibSp): [0, ..., 8])
import matplotlib.pyplot as plt
import streamlit as st


# Функция, которая вычисляет средний возраст пассажиров каждого класса на основе данных из файла
def calculate_average_age(lines, consider_family_size=False, family_size=None):
    class1_total_age = 0
    class1_passenger_count = 0
    class2_total_age = 0
    class2_passenger_count = 0
    class3_total_age = 0
    class3_passenger_count = 0

    for line in lines:
        data = line.strip().split(',')
        try:
            age = float(data[6])
            pclass = data[2]
            sibsp = data[7]
        except (ValueError, IndexError):
            continue

        if not consider_family_size or (consider_family_size and sibsp == str(family_size)):
            if pclass == '1':
                class1_total_age += age
                class1_passenger_count += 1
            elif pclass == '2':
                class2_total_age += age
                class2_passenger_count += 1
            elif pclass == '3':
                class3_total_age += age
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


with open('data.csv') as file:
    lines = file.readlines()

# Визуализируем решение
st.image('titaniс.jpg')
st.subheader('Средний возраст пассажиров парохода «Титаник» по каждому классу обслуживания в зависимости от количества родственников (братьев, сестер, сводных братьев, сводных сестер, супругов на борту).')
class_service = ['1 класс', '2 класс', '3 класс']
selected_family_size = st.number_input('Для просмотра данных выберите значение поля SibSp:', 0, 8)
family_size_options = st.checkbox('Без учета родственников')

# Заполняем таблицу и строим график в зависимости от выбора family_size_options
if family_size_options:
    class1_avg, class2_avg, class3_avg = calculate_average_age(lines)
    st.table({'Класс обслуживания': class_service, 'Средний возраст': [class1_avg, class2_avg, class3_avg]})
    plt.figure(figsize=(8, 4))
    plt.bar(class_service, [class1_avg, class2_avg, class3_avg])
    plt.xlabel('Класс пассажира (Pclass)')
    plt.ylabel('Средний возраст')
    plt.title('Средний возраст пассажиров по классам обслуживания')
    st.pyplot(plt)
else:
    if selected_family_size == 'Без учета родственников':
        class1_avg, class2_avg, class3_avg = calculate_average_age(lines)
        st.table({'Класс обслуживания': class_service, 'Средний возраст': [class1_avg, class2_avg, class3_avg]})
    else:
        family_size = int(selected_family_size)
        class1_avg, class2_avg, class3_avg = calculate_average_age(lines, consider_family_size=True, family_size=family_size)
        st.table({'Класс обслуживания': class_service, 'Средний возраст': [class1_avg, class2_avg, class3_avg]})

    plt.figure(figsize=(8, 4))
    plt.bar(class_service, [class1_avg, class2_avg, class3_avg])
    plt.xlabel('Класс пассажира (Pclass)')
    plt.ylabel('Средний возраст')
    if selected_family_size == '1':
        plt.title(f'Средний возраст пассажиров по классам обслуживания для {selected_family_size} родственника')
    else:
        plt.title(f'Средний возраст пассажиров по классам обслуживания для {selected_family_size} родственников')
    st.pyplot(plt)

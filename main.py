# Вариант 5
# База данных медицинской фирмы
# База данных используется в работе медицинской фирмы.
# Необходимо хранить информацию обо всех врачах с указанием их Ф.И.О.,
# адреса, телефона , специализации (терапевт, лор и др.), режима работы и номера кабинета.
# Кроме того, необходимо хранить информацию об образовании врача, курсах повышения квалификации,
# научных степенях.
# Для каждого пациента, который обращается в фирму, заводится персональная карточка,
# где фиксируются Ф.И.О. пациента, дата рождения, домашний адрес, контактные телефоны,
# хронические и перенесенные заболевания. Всякий раз, когда врач осматривает больного,
# фиксируются дата проведения осмотра, симптомы, диагноз, предписания больному и информация о враче,
# проводившем осмотр. Если врач прописывает больному ка-кое-либо лекарство,
# в таблицу заносятся название лекарства, способ его приема, словесные описания
# предполагаемого действия и возможных побочных эффектов.
import sqlite3

conn = sqlite3.connect("MedCenter.db")
cursor = conn.cursor()

zap_doctor = "create table IF NOT EXISTS table_doctors (" \
             "id INTEGER PRIMARY KEY autoincrement," \
             "full_name_doctor text," \
             "home_address_doctor text," \
             "phone_number_doctor bigint unsigned," \
             "specialization text," \
             "work_schedule text," \
             "office_number int," \
             "education text," \
             "courses text," \
             "degrees text);"
cursor.execute(zap_doctor)
conn.commit()


zap_patient = "create table IF NOT EXISTS table_patients (" \
              "id INTEGER PRIMARY KEY autoincrement," \
              "full_name_patient text," \
              "date_of_birth_patient date," \
              "home_address_patient text," \
              "phone_number_patient bigint unsigned," \
              "chronic_diseases text," \
              "previous_diseases text," \
              "date_examination date," \
              "doctor_name text," \
              "symptoms text," \
              "diagnosis text," \
              "prescription text," \
              "medication text," \
              "method_of_taking text," \
              "main_effect text," \
              "side_effect text);"

cursor.execute(zap_patient)
conn.commit()



zap_1_doc = "insert into table_doctors (" \
            "full_name_doctor, " \
            "home_address_doctor, " \
            "phone_number_doctor, " \
            "specialization, " \
            "work_schedule, " \
            "office_number, " \
            "education, " \
            "courses, " \
            "degrees) VALUES (" \
            "'Петров Пётр Петрович'," \
            "'г. Минск, ул. Сердича, д. 8, кв. 22'," \
            "'80296543322', " \
            "'хирург', " \
            "'пн-пт с 8 до 14', " \
            "'23', " \
            "'Белорусский Государственный Медицинский Университет', " \
            "'Интенсивная терапия неотложных состояний', " \
            "'Кандидат медицинских наук');"
cursor.execute(zap_1_doc)
conn.commit()

zap_select_doc = "select * from table_doctors;"
cursor.execute(zap_select_doc)
d = cursor.fetchall()
print(d)

zap_1_pat = "insert into table_patients (" \
            "full_name_patient," \
            "date_of_birth_patient," \
            "home_address_patient," \
            "phone_number_patient," \
            "chronic_diseases," \
            "previous_diseases," \
            "date_examination," \
            "doctor_name," \
            "symptoms," \
            "diagnosis," \
            "prescription," \
            "medication," \
            "method_of_taking," \
            "main_effect," \
            "side_effect) VALUES (" \
            "'Пипкин Сократ Фернандович'," \
            "'1965-12-12'," \
            "'г. Минск, ул. Немига, д. 23, кв. 55'," \
            "'80299998877'," \
            "'Артериальная гипертензия'," \
            "'Аппендицит'," \
            "'2022-09-25'," \
            "'Петров Пётр Петрович'," \
            "'резкая боль в области правого голеностопного сустава'," \
            "'тендовагинит голеностопного сустава'," \
            "'покой, физиопроцедуры'," \
            "'ибупрофен 400 мг'," \
            "'перорально, по 1 таблетке 2-3 раза в день, 5-7 дней'," \
            "'противовоспалительное, анальгезирующее и жаропонижающее действие'," \
            "'аллергия, тошнота, головная боль');"
cursor.execute(zap_1_pat)
conn.commit()

zap_select_pat = "select * from table_patients;"
cursor.execute(zap_select_pat)
p = cursor.fetchall()
print(p)


cursor.close()
conn.close()

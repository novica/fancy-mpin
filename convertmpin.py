#Convert MPIN csv file to useful html report
import sys
import csv, itertools
from jinja2 import Environment, FileSystemLoader, select_autoescape
env = Environment(
    loader=FileSystemLoader('templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

personal_report = env.get_template('personal_report.html')

mpin_dict = {'3.0': 'Реден број',
 '3.1': 'ЕМБГ',
 '3.10': 'Износ на надоместок',
 '3.12': 'Година од која е определен паричен надоместок во случај на невработеност',
 '3.13': 'Нето плата',
 '3.14': 'Плата во вкупен износ',
 '3.15': 'Придонес за задолжително ПИО од 3.14',
 '3.16': 'Доплата на придонес до најниска основица',
 '3.17': 'Шифра за вид на стаж на осигурување',
 '3.17б': 'Шифра за ослободување од плаќање придонеси и персонален данок',
 '3.18': 'Степен на зголемување за стаж со зголемено траење',
 '3.19а': 'Од ден',
 '3.19б': 'До ден',
 '3.2': 'Презиме',
 '3.20': 'Вкупно денови',
 '3.21': 'Основица за стаж со зголемено траење (бенефициран стаж)',
 '3.22': 'Износ на придонес за стаж со зголемено траење (бенефициран стаж)',
 '3.22б': 'Доплата до најниска основица за стаж со зголемено траење (бенефициран стаж)',
 '3.23': 'Ознака на надлежен органна државна управа обврзник за пресметка и уплата',
 '3.24': 'Часови за кои плаќа надлежен орган',
 '3.25': 'Основица за пресметка на придонеској го плаќа надлежен орган на дежавна управа',
 '3.26': 'Даночен број на обврзнокот каде е пријавен обврзникот за плаќање',
 '3.27': 'Дата на засновање на работен однос',
 '3.28': 'Дата на престанок на работен однос',
 '3.29': 'Шифра за промена на засновање / престанок на работен однос',
 '3.3': 'Име',
 '3.30': 'Број на пријава / одјава од задолжително социјално осигурување',
 '3.31': 'Ефективна нето плата',
 '3.32': 'Број на трансакциска сметка',
 '3.4': 'Број на деловна единица',
 '3.40': 'Придонес за задолжително здравствено осигурување',
 '3.41': 'Дополата на придонес до најниска основица',
 '3.42': 'Дополнителен придонес за задолжително здравствено осигурување за случај на повреда на работа и професионално заболување',
 '3.43': 'Доплата на придонес до најниска основица',
 '3.44': 'Придонес за осигурување во случај на невработеност',
 '3.45': 'Доплата на придонес до најниска основица',
 '3.46': 'Персонален данок на доход од плата',
 '3.4б': 'Ознака на подрачна единица за издавање на потврди за платен придонес за здравствено осигурување',
 '3.4ц': 'Ознака на општината на обврзникот за плаќање на придонеси и персонален данок',
 '3.5': 'Траење на стаж во денови',
 '3.6': 'Ефективна работа Часови',
 '3.6б': 'Прекувремени часови',
 '3.6ц': 'Неплатени часови',
 '3.7': 'Износ на ефективна работа',
 '3.8': 'Часови за надоместок',
 '3.9': 'Вид на надоместок'}

keys_list = ['3.0', '3.1', '3.2', '3.3', '3.4', '3.4б', '3.4ц', '3.5', '3.6', '3.6б', '3.6ц', '3.7', '3.8', '3.9', '3.10',
 '3.12', '3.14', '3.15', '3.16', '3.40', '3.41', '3.42', '3.43', '3.44', '3.45', '3.46', '3.17', '3.17б', '3.18',
 '3.19а', '3.19б', '3.20', '3.21', '3.22', '3.22б', '3.23', '3.24', '3.25', '3.26', '3.27', '3.28', '3.29', '3.30',
 '3.13', '3.31', '3.32']

values_list = ['Реден број',
 'ЕМБГ',
 'Презиме',
 'Име',
 'Број на деловна единица',
 'Ознака на подрачна единица за издавање на потврди за платен придонес за здравствено осигурување',
 'Ознака на општината на обврзникот за плаќање на придонеси и персонален данок',
 'Траење на стаж во денови',
 'Ефективна работа Часови',
 'Прекувремени часови',
 'Неплатени часови',
 'Износ на ефективна работа',
 'Часови за надоместок',
 'Вид на надоместок',
 'Износ на надоместок',
 'Година од која е определен паричен надоместок во случај на невработеност',
 'Плата во вкупен износ',
 'Придонес за задолжително ПИО од 3.14',
 'Доплата на придонес до најниска основица',
 'Придонес за задолжително здравствено осигурување',
 'Дополата на придонес до најниска основица',
 'Дополнителен придонес за задолжително здравствено осигурување за случај на повреда на работа и професионално заболување',
 'Доплата на придонес до најниска основица',
 'Придонес за осигурување во случај на невработеност',
 'Доплата на придонес до најниска основица',
 'Персонален данок на доход од плата',
 'Шифра за вид на стаж на осигурување',
 'Шифра за ослободување од плаќање придонеси и персонален данок',
 'Степен на зголемување за стаж со зголемено траење',
 'Од ден',
 'До ден',
 'Вкупно денови',
 'Основица за стаж со зголемено траење (бенефициран стаж)',
 'Износ на придонес за стаж со зголемено траење (бенефициран стаж)',
 'Доплата до најниска основица за стаж со зголемено траење (бенефициран стаж)',
 'Ознака на надлежен органна државна управа обврзник за пресметка и уплата',
 'Часови за кои плаќа надлежен орган',
 'Основица за пресметка на придонес кој го плаќа надлежен орган на дежавна управа',
 'Даночен број на обврзнокот каде е пријавен обврзникот за плаќање',
 'Дата на засновање на работен однос',
 'Дата на престанок на работен однос',
 'Шифра за промена на засновање / престанок на работен однос',
 'Број на пријава / одјава од задолжително социјално осигурување',
 'Нето плата',
 'Ефективна нето плата',
 'Број на трансакциска сметка']



def tax_free(employee_record, general_information):
    if general_information["Часови во месецот"] == employee_record["3.6"]:
        return general_information["Даночно ослободување"]
    else:
        return (float(employee_record["3.13"]) + float(employee_record["3.46"])) - float(employee_record["3.46"]/0.1)

def tax_base(employee_record):
    return (float(employee_record["3.13"]) + float(employee_record["3.46"]) )

def penalties(employee_record):
    if (float(employee_record["3.13"]) - float(employee_record["3.31"])) != 0:
        return (float(employee_record["3.13"]) - float(employee_record["3.31"]))
    else:
        return("Нема")


with open('dummy-data.txt', newline='\r\n') as csvfile: #don't forget encoding='cp1251'
    csvreader = csv.reader(csvfile, delimiter=';')

    #first three lines contain some genereal info that we need only parts of it
    gen_info={}

    row = next(csvreader)
    gen_info["Даночно ослободување"] = row[1]
    gen_info["Часови во месецот"] = row[3]

    row = next(csvreader)
    gen_info["Месец"] = row[0]
    gen_info["Година"] = row[1]

    row = next(csvreader)
    gen_info["ЕДБ"] = row[0]
    gen_info["ЕМБС"] = row[1]
    gen_info["Компанија"] = row[2]

    #print(gen_info)

    #now get the rest of the lines, but not the last four lines
    #person_list = []

    while True:
        row = next(csvreader)
        if not len(row) == 1: # len(['***********************************']) == 1
            person_dict = dict(zip(keys_list, row))
            print(personal_report.render(person_dict=person_dict, gen_info=gen_info, mpin_dict=mpin_dict, tax_free=tax_free, tax_base=tax_base, penalties=penalties))
            #person_list.append(person_dict)
        else:
            break

    #print(person_list)
    #print(personal_report.render(person_dict=person_dict, gen_info=gen_info, mpin_dict=mpin_dict, tax_free=tax_free, tax_base=tax_base, penalties=penalties))

from send_email import *

import xlrd
import csv
import os


def create_error_csv(i):
    error_file = open('src/data/{}/error.csv'.format(str(i)), 'w')
    wr = csv.writer(error_file, quoting=csv.QUOTE_ALL)
    f = open("src/data/"+str(i)+'/queue.csv', 'r')
    reader = csv.reader(f)
    index = 0
    for row in reader:
        for column in row:
            print(str(index) + " - " + column)
            index = index +1
        wr.writerow(row)
        break
    error_file.close()
    name_column = input("digite o numero da coluna de nomes: ")
    email_column = input("digite o numero da coluna de emails: ")
    age_column = input("digite o numero da coluna de idades: ")
    f.close()
    return [int(name_column),int(email_column),int(age_column) ,int(i)]

def csv_from_excel(arq_name):
    i = 0
    created = False
    while(not created):
        try:
            os.mkdir("src/data/{}".format(str(i)))
            created = True
        except:
            i = i +1
    wb = xlrd.open_workbook("src/{}.xlsx".format(arq_name))
    sh = wb.sheet_by_name('Plan1')
    queue_file = open('src/data/{}/queue.csv'.format(str(i)), 'w')
    wr = csv.writer(queue_file, quoting=csv.QUOTE_ALL)

    for rownum in range(sh.nrows):
        wr.writerow(sh.row_values(rownum))
    queue_file.close()
    return create_error_csv(i)
    
def read_queue_data(name_column,email_column,age_column,age_filter,i):
    
    #Tenho que fazer ler do ultimo ao primeiro e ir removendo as linhas

    filtered =0
    sent =0
    failed =0
    f = open("src/data/"+str(i)+'/queue.csv', 'r')
    reader = csv.reader(f)
    for row in reader:
        if(row != []):
            try:
                name = str(row[name_column])
                email = str(row[email_column])
                age = row[age_column].split('.')[0]
                int(age)
                print("nome: " + name + " / email: "+ email+ " / idade: "+ age)

                '''
                    Retorno:
                    0 = Não passou no filtro
                    1 = passou no filtro e foi enviado
                    2 = passou no filtro e não foi enviado
                '''
                response = check_valid_email(name,email, int(age), age_filter)
                if(response == 1):
                    sent = sent+1
                    filtered=filtered+1
                if(response==2):
                    filtered=filtered+1
                    failed=failed+1
                    add_failed_list(row,i)
                    
            except ValueError:
                print("Arquivo aberto")
            print("")
    f.close()
    return [filtered,sent,failed]

def check_valid_email(name,email,age,age_filter):
    if age<age_filter:
        print("Muito novo para receber o email")
        return 0
    else:
        return mail(name,email)

def add_failed_list(row,i):
    error_file = open('src/data/{}/error.csv'.format(str(i)), 'r')
    data = []
    rd = csv.reader(error_file)
    for rw in rd:
        data.append(rw)
    data.append(row)
    error_file.close()

    error_file = open('src/data/{}/error.csv'.format(str(i)), 'w')
    wr = csv.writer(error_file, quoting=csv.QUOTE_ALL)
    for rw in data:
        if(rw!=[]):
            wr.writerow(rw)
    error_file.close()
    
        
    


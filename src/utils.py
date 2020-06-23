from send_email import *
from text_responses import *
import xlrd
import csv
import os

#armazena os dados de onde estão as colunas dos dados selecionados
def set_data_storage(name_column, email_column, age_column,age_filter,i):
    data_file = open('src/data/{}/data.csv'.format(str(i)), 'w')
    wr = csv.writer(data_file, quoting=csv.QUOTE_ALL)
    wr.writerow([name_column, email_column, age_column,age_filter])
    data_file.close()

#le os dados selecionados previamente
def read_data_storage(i):
    log_reading_data(i)
    data_file = open('src/data/{}/data.csv'.format(str(i)), 'r')
    reader = csv.reader(data_file)
    data = []
    for row in reader:
        for column in row:
            data.append(int(column))
        return data

#cria uma tabela para armazenar os envios que deram errados
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

#le o xlsx e transforma numa fila em csv para poder trabalhar no python
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
    
#le a lista de itens que faltam ser enviados
#envia o email e e remove a linha da lista
#caso não consiga enviar o email, remove da lista e manda adicionar na tabela error
def read_queue_data(name_column,email_column,age_column,age_filter,i):    
    filtered =0
    sent =0
    failed =0
    f = open("src/data/"+str(i)+'/queue.csv', 'r')
    reader = csv.reader(f)
    
    data = []
    for r in reader:
        data.append(r)
    f.close()
    update_data = data
    for rw in range(len(data)-1,-1,-1):
        
        row = data[rw]
        if(row != []):
            try:
                name = str(row[name_column])
                email = str(row[email_column])
                age = row[age_column].split('.')[0]
                int(age)
                print("nome: " + name + " / email: "+ email+ " / idade: "+ age)

                
                    #Retorno:
                    #0 = Não passou no filtro
                    #1 = passou no filtro e foi enviado
                    #2 = passou no filtro e não foi enviado
                
                response = check_valid_email(name,email, int(age), age_filter)
                if(response==0):
                    update_data = update_queue(i,update_data,row)
                if(response == 1):
                    sent = sent+1
                    filtered=filtered+1
                    update_data = update_queue(i,update_data,row)
                            
                if(response==2):
                    filtered=filtered+1
                    failed=failed+1
                    update_data = update_queue(i,update_data,row)
                    add_failed_list(row,i)
                
            except ValueError:
                print("Lido!")
            print("")
    
    
    return [filtered,sent,failed]

#atualiza a fila de espera removendo a linha que foi trabalhada no momento
def update_queue(i,data,row):
    print("Removendo item da fila...")
    file = open("src/data/"+str(i)+'/queue.csv', 'w')
    wr = csv.writer(file, quoting=csv.QUOTE_ALL)
    for line in data:
        if(line !=row) and line !=[]:
            data = list(filter(lambda item: item!=row,data))
            wr.writerow(line)
    file.close()
    return data

#faz o filtro e se passar manda para enviar o email
def check_valid_email(name,email,age,age_filter):

    #a idade vai vir por data, tem que trabalhar esse dado
    if age<age_filter:
        print("Muito novo para receber o email")
        return 0
    else:
        return mail(name,email)

#adiciona o item enviado na tabela de erro
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
    
        
    


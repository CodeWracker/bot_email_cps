from send_email import *
from text_responses import *
import pandas as pd
import csv
import os
import datetime

#armazena os dados de onde estão as colunas dos dados selecionados
def set_data_storage(name_column, email_column,i):
    data_file = open('data/{}/data.csv'.format(str(i)), 'w')
    wr = csv.writer(data_file, quoting=csv.QUOTE_ALL)
    wr.writerow([name_column, email_column])
    data_file.close()

#le os dados selecionados previamente
def read_data_storage(i):
    log_reading_data(i)
    data_file = open('data/{}/data.csv'.format(str(i)), 'r')
    reader = csv.reader(data_file)
    data = []
    for row in reader:
        for column in row:
            data.append(int(column))
        return data

#cria uma tabela para armazenar os envios que deram errados
def create_error_csv(i):
    #os.mkdir("data/{}/error.csv".format(str(i)))
    error_file = open("data/{}/".format(str(i))+"error.csv", "w")
    wr = csv.writer(error_file, quoting=csv.QUOTE_ALL)
    f = open("data/"+str(i)+'/queue.csv', 'r')
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
    f.close()
    return [int(name_column),int(email_column) ,int(i)]

#le o xlsx e transforma numa fila em csv para poder trabalhar no python
def csv_from_excel(arq_name,new_name):
    i = 0
    created = False
    while(not created):
        try:
            os.mkdir("data/{}".format(str(i)))
            created = True
        except:
            i = i +1
    #os.mkdir("data/{}/queue.csv".format(str(i)))
    read_file = pd.read_excel ("{}.xlsx".format(arq_name))
    read_file.to_csv ("data/{}/".format(str(i))+new_name+".csv", index = None, header=True)
    return create_error_csv(i)

def blocked_csv(arq_name,i):
    read_file = pd.read_excel ("{}.xlsx".format(arq_name))
    read_file.to_csv ("data/{}/".format(str(i))+"block.csv", index = None, header=True)
    f = open("data/"+str(i)+'/block.csv', 'r', encoding='utf-8')
    reader = csv.reader(f)
    index = 0
    for row in reader:
        for column in row:
            print(str(index) + " - " + column)
            index = index +1
        break
    email_column = input("digite o numero da coluna de emails: ")
    f.close()
    
    return [int(email_column)]



#le a lista de itens que faltam ser enviados
#envia o email e e remove a linha da lista
#caso não consiga enviar o email, remove da lista e manda adicionar na tabela error
def read_queue_data(name_column,email_column,i):    
    filtered =0
    sent =0
    failed =0
    f = open("data/"+str(i)+'/queue.csv', 'r')
    reader = csv.reader(f)
    
    data = []
    for r in reader:
        data.append(r)
    f.close()
    update_data = data
    for rw in range(len(data)-1,0,-1):
        
        row = data[rw]
        if(row != []):
            try:
                name = str(row[name_column])
                email = str(row[email_column])
                #age = row[age_column].split('-')[0]
                
                #int(age)
                print("nome: " + name + " / email: "+ email) 
                # / nascimento: "+ age)

                
                    #Retorno:
                    #0 = Não passou no filtro
                    #1 = passou no filtro e foi enviado
                    #2 = passou no filtro e não foi enviado
                
                response = check_valid_email(name,email,i)
                #response = mail(name,email)
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
    file = open("data/"+str(i)+'/queue.csv', 'w')
    wr = csv.writer(file, quoting=csv.QUOTE_ALL)
    for line in data:
        if(line !=row) and line !=[]:
            data = list(filter(lambda item: item!=row,data))
            wr.writerow(line)
    file.close()
    return data

#faz o filtro e se passar manda para enviar o email
def check_valid_email(name,email,i):
    print('verificando se o email é valido')
    try:
        fi = open("data/"+str(i)+'/block.csv', 'r',encoding='utf-8')
        reader = csv.reader(fi)
        data = []
        for r in reader:
            data.append(r)
        fi.close()
        achou = False
        for rw in range(1,len(data),1):
        
            row = data[rw]
            print(row[1])
            if(str(row[1])==str(email)):
                achou = True

        if achou:
            print("email bloqueado")
            return 0
        else:
            print('ok')
            return mail(name,email)
    
    except:
        print('ok, sem lista de bloqueados')
        return mail(name,email)
    


#adiciona o item enviado na tabela de erro
def add_failed_list(row,i):
    print("adicionando na lista de erros")
    print(row)
    error_file = open('data/{}/error.csv'.format(str(i)), 'r')
    data = []
    rd = csv.reader(error_file)
    for rw in rd:
        data.append(rw)
    data.append(row)
    error_file.close()

    error_file = open('data/{}/error.csv'.format(str(i)), 'w')
    wr = csv.writer(error_file, quoting=csv.QUOTE_ALL)
    for rw in data:
        if(rw!=[]):
            wr.writerow(rw)
    error_file.close()
    
        
    


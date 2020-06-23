from utils import *
from text_responses import *

log_start_configuration()
caso = int(input("digite 1 para criar m caso novo e 2 para tentar um anterior: "))
if(caso==1):
    file_name = input("Digite o nome do arquivo excel(sem o .xlsx): ")
    [name_column, email_column, age_column,run_number] = csv_from_excel(file_name)
    age_filter = int(input("Digite a idade minima do filtro (<): "))
    set_data_storage(name_column, email_column, age_column,age_filter,run_number)
else:
    #tenho que fazer isso ser automatico
    
    run_number = int(input("digite o numero da pasta que deseja utilizar: "))
    [name_column, email_column, age_column,age_filter] = read_data_storage(run_number)
log_line()
log_start_reading_queue()
[filtered,sent,failed] = read_queue_data(name_column, email_column, age_column,age_filter,run_number)
log_line()
log_results(filtered,sent,failed)
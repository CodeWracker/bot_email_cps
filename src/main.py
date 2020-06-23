from utils import *
from text_responses import *

log_start_configuration()
file_name = input("Digite o nome do arquivo excel(sem o .xlsx): ")
[name_column, email_column, age_column,run_number] = csv_from_excel(file_name)
age_filter = int(input("Digite a idade minima do filtro (<): "))
log_line()
log_start_reading_queue()
[filtered,sent,failed] = read_queue_data(name_column, email_column, age_column,age_filter,run_number)
log_line()
log_results(filtered,sent,failed)
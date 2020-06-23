def log_start_configuration():
    log_line()
    print("iniciando configuracoes")

def log_line():
    print("___________________________")

def log_start_reading_queue():
    print("Iniciando Leitura da lista de emails agendados")
    print("")
def log_results(filtered,sent,failed):
    print("Passaram no filtro: "+ str(filtered))
    print("Enviados: "+ str(sent))
    print("Erro ao enviar: "+str(failed))
    print("Os eventuais erros, por enquanto, devem ser tratados manualmente")
    log_line()

def log_reading_data(run_number):
    print("")
    print("Lendo dados da execucao numero "+str(run_number))
    print("")
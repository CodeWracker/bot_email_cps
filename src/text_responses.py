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
    log_line()
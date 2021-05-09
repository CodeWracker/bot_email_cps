# Sobre

Um bot para enviar os emails para os membros do CPS
Um programa feito em python para enviar emails elaborados em HTML+CSS simples para uma lista predeterminada de emails, salva em um arquivo .xlsx

## Documentação

### Diagrama do funcionamento Básico

![alt text](https://raw.githubusercontent.com/CodeWracker/bot_email_cps/master/Documenta%C3%A7%C3%A3o/diagramas/flow3.png)

### Funcionamento

Ao iniciar o programa ele pergunta se deseja começar um novo caso ou tentar um antigo que não pode ser concluído.
Isso acontece, pois ao criar um caso novo é feito na pasta src/data uma nova pasta com o número do caso, e lá são gerados 3 arquivos .csv: queue.csv, data.csv e error.csv
No data.csv está gravado as informações sobre a tabela crua, como o indice das colunas de relevancia e o ano filtro.
No queue.csv é guardada a lista de espera de emails para serem analisados no filtro e enviados.
No error.csv é onde guarda os dados dos emails que retornaram erros na hora de enviar, para serem tratados posteriormente.

#### Por que uma queue?

A lista de espera é gerada pegando as informações das colunas de referencia do arquivo cru e ao tentar enviar um email é lido a ultima linha do queue.csv, para que caso hajam muitos emails e por algum motivo o envio tenha que ser interrompido, possa-se voltar ao envio de onde parou, apenas iniciando o processo com a queue.csv, ja que sempre se remove a ultima linha ao se passar por ela.

#### Prints de execução

![alt text](https://raw.githubusercontent.com/CodeWracker/bot_email_cps/master/Documenta%C3%A7%C3%A3o/printTudo.png)
![alt text](https://raw.githubusercontent.com/CodeWracker/bot_email_cps/master/Documenta%C3%A7%C3%A3o/printConfig.png)
![alt text](https://raw.githubusercontent.com/CodeWracker/bot_email_cps/master/Documenta%C3%A7%C3%A3o/printEnvios.png)
![alt text](https://raw.githubusercontent.com/CodeWracker/bot_email_cps/master/Documenta%C3%A7%C3%A3o/printResultados.png)

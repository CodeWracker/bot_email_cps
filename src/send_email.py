import smtplib
import config
import message
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
def send(to, msg):
    subject ="Minha Pesquisa de Mestrado"
    the_msg = MIMEMultipart("alternative")
    the_msg["Subject"] = subject
    the_msg['From'] = config.EMAIL_ADDRESS
    the_msg["To"] = to
    print('1')
    part_msg = MIMEText(msg, 'html')
    the_msg.attach(part_msg)
    print('2')
    server = smtplib.SMTP(f'{config.SMTP}:{config.PORT}')
    print('3')
    server.ehlo()
    print('4')
    server.starttls()
    print('5')
    server.login(config.EMAIL_ADDRESS, config.PASSWORD)
    print('6')
    server.sendmail(config.EMAIL_ADDRESS, to, the_msg.as_string())
    server.quit()



def mail(name, email):
    html = """\
                <html>
                    <head>
                        <style>
                            {}
                        </style>
                        <style>
                            {}
                        </style>
                    </head>
                    <body>
                        <div class="container">
                            <div class="col-md-8>
                                <div class="myCard" >
                                    <img src="https://img.freepik.com/fotos-gratis/dia-mundial-do-livro-fundo-do-livro_73944-11711.jpg?size=626&ext=jpg" style="max-width:100%;
                                    height:auto; self-align:justify"  alt="..." >
                                    <div class="card-body">
                                        <h5 class="card-title">Prezado(a) {}.</h5>
                                        <div class="row">
                                                <p style="text-align: justify;" >
                                                Meu nome é Rosemeire de Fátima Ferraz, sou docente locada na
                                                Etec de Poá, atualmente desenvolvendo a função de
                                                Coordenadora de Projetos na Cetec Capacitações –
                                                Administração Central.
                                            </br> Estou fazendo meus estudos de
                                                Mestrado em Psicogerontologia e meu tema de estudo é
                                                <b>ENVELHECIMENTO E TRABALHO DOCENTE: Motivos para
                                                permanecer no trabalho mesmo após a aposentadoria</b> Para está pesquisa preciso que professores em idade
                                                madura (acima de 45 anos) e aposentados que estejam ainda na
                                                atividade docente, seja em sala de aula ou desenvolvendo
                                                outras funções, participem respondendo a pesquisa.
                                            </br>Sua contribuição é muito valiosa para que seja possível identificar situações que proporcionem uma melhoria da qualidade de vida docente e, assim futuramente, propor para a nossa instituição, projetos que auxiliem na preparação da aposentadoria.
                                            </br>Você precisará de apenas 10
                                                minutos para responder a 2 questionários: Sociodemográfico e
                                                a Escala de Motivação Docente.</br> Conto com sua participação!</br>
                                                Desde já agradeço sua atenção e contribuição!
                                            </p>
                                        </div>
                                        <div class="row">
                                    
                                            <a
                                                href="https://google.com"
                                                class="myButton"
                                                >Ir para o questionário</a
                                            >
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                            
                            
                        
                    </body>
                    </html>
                                    """.format(message.BOOTSTRAP,message.MY_STYLE,name)
    try:
        print("enviando email para: " + email)
        send(email, html)
        print("enviado")
        return 1
    except:
        print("Falha ao enviar email")
        return 2

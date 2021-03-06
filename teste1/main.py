import smtplib
import config
import message
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
def send_email(to, subject, msg):
    try:
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
        return True

    except Exception as e:
        print(e)
        return False


html = """\
                <html>
<style type="text/css">
    {}
</style>

<body>


    </div>
    <div>
        <div class="myheader">
            <h2>Convite Para Pesquisa</h2>
        </div>
        <div class="corpo">
            <div class="img"><img src="https://image.freepik.com/fotos-gratis/papel-de-caderno-em-branco-lapis-e-oculos-no-local-de-trabalho_151013-11254.jpg"
                 alt="..."></div>
            <p class="fontcod">Olá Caro(a) colega! </p>
            <p class="fontnormal">
            Meu nome é Rosemeire de Fátima Ferraz, sou docente do Centro Paula Souza,  lotada na Etec de Poá, atualmente desenvolvendo a função de coordenadora de Projetos na Cetec Capacitações. </br>
            Iniciei meus estudos de mestrado profissional em janeiro/2019 com o título de pesquisa <b>ENVELHECIMENTO E TRABALHO DOCENTE: Motivos para permanecer no trabalho mesmo após a aposentadoria</b>,  entretanto, em 13/11/2019 foi publicado uma emenda constitucional 103, em que o servidor que requerer a aposentadoria junto ao INSS, a partir desta data e quando a aposentadoria for concedida terá que romper o vínculo empregatício. Mesmo assim, sendo de grande importância os estudos em desenvolvimento, preciso do apoio dos colegas para concluir minha pesquisa e finalizar meus estudos. 
            Portanto, estou lhe convidando a acessar o link abaixo, se desejar, para que possa ler o Termo de Consentimento Livre e Esclarecido e 2 questionários:  Sociodemográfico e a Escala de Motivação Docente. 
            Conto com sua participação!
            Desde já agradeço sua atenção e contribuição!
            <div class="button"><a href='https://forms.gle/cg5hkuFYFFibMz6y5'>Acessar link</a></div>
            </p>
        </div>
</body>

</html>
                """.format(message.MY_STYLE)
email_request = send_email("rosemeire.ferraz@cps.sp.gov.br", 'Convite para minha Pesquisade Mestrado', html)
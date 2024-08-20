from abc import ABC, abstractmethod

class Notificacao(ABC):
    def __init__(self, mensagem):
        self.mensagem = mensagem

    @abstractmethod
    def enviar(self) -> bool:
        ...

class NotificacaoEmail(Notificacao):
    
    def enviar(self):
        print('E-mail enviando: ', self.mensagem)
        return True


class NotificacaoSms(Notificacao):
    
    def enviar(self):
        print('SMS enviando: ', self.mensagem)
        return False

def enviar(notificacao: Notificacao):
    notificacaoEnviada = notificacao.enviar()

    if notificacaoEnviada:
        print('Notificação enviada')
    else:
        print('Notificação não enviada')



n = NotificacaoEmail('Bom dia!!')
s = NotificacaoSms('Tchau!!')
enviar(s)

        
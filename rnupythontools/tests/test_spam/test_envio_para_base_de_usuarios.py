import pytest
from rnupythontools.spam.enviador_de_email import Enviador
from rnupythontools.spam.main import EnviadordeSpam
from rnupythontools.spam.modelos import Usuario


@pytest.mark.parametrize("usuarios", [
    Usuario(nome='Rodrigo', email='rousuy@gmail.com'),
    Usuario(nome='Ellen', email='foo@bar.com')], [Usuario(nome='Ellen', email='foo@bar.com')])
def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadordeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'rousuy@gmail.com',
        'Curso de Python',
        'Confira os módulos fantásticos'
    )
    assert len(usuarios) == enviador.qtd_email_enviados


class EnviadorMock(Enviador):
    def __init__(self):
        self.qtd_email_enviados = 0
        self.parametros_de_envio = None

    def enviar(self, remetente, destinatario, assunto, corpo):
        self.parametros_de_envio = (remetente, destinatario, assunto, corpo)
        self.qtd_email_enviados += 1

    def test_parametros_de_spam(sessao):
        Usuario(nome='Rodrigo', email='rousuy@gmail.com')
        sessao.salvar(usuario)
        enviador = EnviadorMock()
        enviador_de_spam = EnviadordeSpam(sessao, enviador)
        enviador_de_spam.enviar_emails(
            'foo@bar.com.br',
            'Curso de Python',
            'Confira os módulos fantásticos'
        )
        assert enviador.parametros_de_envio == (
            'foo@bar.com.br',
            'rousuy@gmail.com',
            'Curso de Python',
            'Confira os módulos fantásticos'
        )

    def salvar(self, usuario):
        pass

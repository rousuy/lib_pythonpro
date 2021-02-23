import pytest

from rnupythontools.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize('destinatario', ['foo@bar.com.br', 'rousuy@gmail.com'])
def test_remetente(destinatario):
    enviador = Enviador()
    resultado = enviador.enviar(destinatario,
                                'teste@teste.com',
                                'Curso Python Pro',
                                'Primeira Turma Guido Von Rossum')

    assert destinatario in resultado


@pytest.mark.parametrize('destinatario', ['', 'rousuy'])
def test_remetente(destinatario):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(destinatario,
                        'teste@teste.com',
                        'Curso Python Pro',
                        'Primeira Turma Guido Von Rossum')

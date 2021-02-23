from unittest.mock import Mock

import pytest
from rnupythontools.spam.main import EnviadordeSpam
from rnupythontools.spam.modelos import Usuario


@pytest.mark.parametrize("usuarios", [
    Usuario(nome='Rodrigo', email='rousuy@gmail.com'),
    Usuario(nome='Ellen', email='foo@bar.com')], [Usuario(nome='Ellen', email='foo@bar.com')])
def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadordeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'rousuy@gmail.com',
        'Curso de Python',
        'Confira os módulos fantásticos'
    )
    assert len(usuarios) == enviador.enviar.call_count

<<<<<<< HEAD
=======

def test_parametros_de_spam(sessao):
    Usuario(nome='Rodrigo', email='rousuy@gmail.com')
    sessao.salvar(usuarios)
    enviador = Mock()
    enviador_de_spam = EnviadordeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'foo@bar.com.br',
        'Curso de Python',
        'Confira os módulos fantásticos'
    )
    assert enviador.enviar.assert_called_once_with == (
        'foo@bar.com.br',
        'rousuy@gmail.com',
        'Curso de Python',
        'Confira os módulos fantásticos'
    )
>>>>>>> 44ef1139a57c7712bce1579dfe5e8e707b068a1d

def test_parametros_de_spam(sessao):
    Usuario(nome='Rodrigo', email='rousuy@gmail.com')
    sessao.salvar(usuarios)
    enviador = Mock()
    enviador_de_spam = EnviadordeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'foo@bar.com.br',
        'Curso de Python',
        'Confira os módulos fantásticos'
    )
    assert enviador.enviar.assert_called_once_with == (
        'foo@bar.com.br',
        'rousuy@gmail.com',
        'Curso de Python',
        'Confira os módulos fantásticos'
    )

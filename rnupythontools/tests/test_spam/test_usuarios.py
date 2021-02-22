from rnupythontools.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Rodrigo', email='rousuy@gmail.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(sessao):
    usuarios = [Usuario(nome='Rodrigo', email='rousuy@gmail.com'), Usuario(nome='Ellen', email='foo@bar.com')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()

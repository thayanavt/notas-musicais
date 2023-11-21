from pytest import mark
from typer.testing import CliRunner

from notas_musicais.cli import app

runner = CliRunner()


def test_escala_retorna_0():
    result = runner.invoke(app)
    assert result.exit_code == 0


@mark.parametrize('tonica', ['C', 'D', 'E', 'F', 'G', 'A', 'B'])
def test_cli_retorna_notas(tonica):
    result = runner.invoke(app)
    assert tonica in result.stdout


import pytest

from notas_musicais.escalas import escala

# AAA - Arange - Act - Assets
# AAG - Arrumar - Agir - Garantir


def test_escala_tonica_minusculas():
    # Arange - Arrumar
    tonica = 'c'
    tonalidade = 'maior'
    # Act - Agir
    result = escala(tonica, tonalidade)
    # Assert - Garantir
    assert result


def test_escala_tonica_inexistente():
    # Arange - Arrumar
    tonica = 'Z'
    tonalidade = 'maior'
    # Act - Agir
    result = escala(tonica, tonalidade)
    # Assert - Garantir
    assert result


def test_escala_tonalidade_inexistente():
    # Arange - Arrumar
    tonica = 'C'
    tonalidade = 'tonalidade'
    # Act - Agir
    result = escala(tonica, tonalidade)
    # Assert - Garantir
    assert result


@pytest.mark.parametrize(
    'tonica, esperado',
    [
        ('C', ['C', 'D', 'E', 'F', 'G', 'A', 'B']),
        ('C#', ['C#', 'D#', 'F', 'F#', 'G#', 'A#', 'C']),
    ],
)
def test_escala_tonicas_corretas(tonica, esperado):
    # Act - Agir
    result = escala(tonica, 'maior')
    # Assert - Garantir
    assert result['notas'] == esperado

def test_escala_graus_corretos():
    # Arange - Arrumar
    tonica = 'C'
    tonalidade = 'maior'
    graus = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']
    # Act - Agir
    result = escala(tonica, tonalidade)
    # Assert - Garantir
    assert result['graus'] == graus
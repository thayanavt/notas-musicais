NOTAS = 'C C# D D# E F F# G G# A A# B'.split()
ESCALAS = {'maior': (0, 2, 4, 5, 7, 9, 11)}


def escala(tonica, tonalidade):
    """Gera uma escala a partir de uma nota escolhida (tônica) e uma
    tonalidade, seguindo os intervalos 0, 2, 4, 5, 7, 9, 11.

    Args:
        tonica (str): nota que será a primeira da escala.
        tonalidade (str): tonalidade da escala.

    Examples:
        >>> escala('C', 'maior')
        {'notas': ['C', 'D', 'E', 'F', 'G', 'A', 'B'], 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}

        >>> escala('a', 'maior')
        {'notas': ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#'], 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}

    Returns:
        dict: escala contendo as notas e graus.

    Raises:
        ValueError: caso a nota tônica não seja uma nota válida.
        KeyError: caso a tonalidade não seja válida.
    """
    tonica = tonica.upper()
    try:
        intervalos = ESCALAS[tonalidade]
        tonica_index = NOTAS.index(tonica)
    except KeyError:
        raise KeyError(f'A tonalidade {tonalidade} não é válida.')
    except ValueError:
        raise ValueError(f'Essa nota não existe, tente uma dessas {NOTAS}.')

    temp = []

    for intervalo in intervalos:
        nota_index = (tonica_index + intervalo) % 12
        temp.append(NOTAS[nota_index])

    return {
        'notas': temp,
        'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII'],
    }

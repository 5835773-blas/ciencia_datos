from datetime import date

from ejercicio import parse_fecha, separar_nombre_id


def test_parse_fecha():
    """Convierte correctamente una fecha válida."""
    assert parse_fecha("10/12/2026") == date(2026, 10, 12)


def test_separar_nombre_id_sin_id():
    """Caso borde: texto sin identificador numérico."""
    assert separar_nombre_id("Jennifer Thomas") == ("Jennifer Thomas", None)

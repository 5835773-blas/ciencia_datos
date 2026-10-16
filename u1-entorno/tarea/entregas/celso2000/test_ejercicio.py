from ejercicio import comision_esperada, separar_nombre_id


def test_comision_esperada_caso_normal():
    assert comision_esperada(1000, 0.1) == 100.0


def test_separar_nombre_id_sin_id_caso_borde():
    assert separar_nombre_id("  Jennifer Thomas  ") == ("Jennifer Thomas", None)
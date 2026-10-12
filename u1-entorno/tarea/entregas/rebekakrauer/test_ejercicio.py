from ejercicio import (
    comision_esperada,
    descripcion_venta,
    separar_nombre_id,
)


def test_separar_nombre_id_sin_id_caso_borde():
    assert separar_nombre_id("Jennifer Thomas") == ("Jennifer Thomas", None)


def test_comision_esperada_redondea_a_dos_decimales():
    assert comision_esperada(1000, 0.0333) == 33.3


def test_descripcion_venta_con_precio_invalido_usa_cero():
    venta = {"car_make": "Ford", "car_model": "Focus", "sale_price": "abc"}
    assert descripcion_venta(venta) == "Venta registrada: Ford Focus por $0"

def calcular_iva(base_imponible, porcentaje_iva=21):
    return base_imponible * porcentaje_iva / 100


def aplicar_descuento(importe, porcentaje_descuento=10):
    return importe - (importe * porcentaje_descuento / 100)

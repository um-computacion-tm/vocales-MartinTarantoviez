import unittest

def contar_vocales(palabra):
    vocales = ("a", "e", "i", "o", "u")
    resultado = {}
    for letra in palabra:
        letra_lower = letra.lower()  # Convertir letra a minúscula
        if letra_lower in vocales:
            # La letra es vocal
            if letra_lower in resultado.keys():
                # Sumar valor a diccionario ya existente
                resultado[letra_lower] += 1
            else:
                # Agregar letra por primera vez
                resultado[letra_lower] = 1
    return resultado

class TestContarVocales(unittest.TestCase):
    def test_sin_vocales(self):
        palabra = "tryhgf"
        resultado = contar_vocales(palabra)
        self.assertEqual(resultado, {})

    def test_con_vocal_o(self):
        palabra = "sol"
        resultado = contar_vocales(palabra)
        self.assertEqual(resultado, {"o": 1})

    def test_con_vocal_doble_o(self):
        palabra = "solo"
        resultado = contar_vocales(palabra)
        self.assertEqual(resultado, {"o": 2})

    def test_con_dos_vocales(self):
        palabra = "sola"
        resultado = contar_vocales(palabra)
        self.assertEqual(resultado, {"o": 1, "a": 1})

    def test_con_todas_las_vocales(self):
        palabra = "solamente quiero que gane Boca"
        resultado = contar_vocales(palabra)
        self.assertEqual(
            resultado,
            {"a": 3, "e": 5, "i": 1, "o": 3, "u": 2},
        )

    def test_con_vocales_en_mayuscula(self):
        palabra = "SOlAmente quIerO"
        resultado = contar_vocales(palabra)
        self.assertEqual(
            resultado,
            {"a": 1, "e": 3, "i": 1, "o": 2, "u": 1},
        )

unittest.main()
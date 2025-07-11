import unittest
from src.check_message import can_form_message

"""Este módulo contiene pruebas unitarias para la función `can_form_message`.
Prueba varios escenarios incluyendo casos básicos, insensibilidad a mayúsculas,
ignorando espacios, y casos con caracteres especiales y números."""

class TestCanFormMessage(unittest.TestCase):
    """Clase de pruebas unitarias para la función can_form_message."""
    def test_basic_cases(self):
        self.assertTrue(can_form_message("SOS", "PELIGROSOS")[0])
        self.assertTrue(can_form_message("HELP", "HELICOPTER")[0])
        self.assertFalse(can_form_message("RESCUE", "RSCU")[0])
        self.assertFalse(can_form_message("AAAB", "AAB")[0])
        self.assertTrue(can_form_message("AAB", "AAAB")[0])
        self.assertTrue(can_form_message("PYTHON", "PYTHON")[0])
    
    def test_case_insensitivity(self):
        self.assertTrue(can_form_message("sos", "PELIGROSOS")[0])
        self.assertTrue(can_form_message("Help", "HELICOPTER")[0])
        self.assertFalse(can_form_message("rescue", "RSCU")[0])

    def test_ignore_spaces(self):
        self.assertTrue(can_form_message("S O S", "PELIGROSOS")[0])
        self.assertTrue(can_form_message(" H E L P ", "HELICOPTER")[0])
        self.assertFalse(can_form_message("R E S C U E", "RSCU")[0])
        self.assertFalse(can_form_message("a a A B", "AAB")[0])
        self.assertTrue(can_form_message("A a B", "AAAB")[0])

    def test_unicode_and_symbols(self):
        self.assertTrue(can_form_message("Café", "Caféeéé")[0])
        self.assertTrue(can_form_message("mañana!", "mañanaa!")[0])
        self.assertFalse(can_form_message("mañana!", "mañanaa")[0])
        result = can_form_message("ñandú", "nandu")
        self.assertFalse(result[0])
        self.assertIn("ñ", result[1])
        self.assertIn("ú", result[1])
    
    def test_numerical_characters(self):
        self.assertTrue(can_form_message("112", "112A")[0])
        result = can_form_message("1123", "112")
        self.assertFalse(result[0])
        self.assertIn("3(1)", result[1])

    def test_empty_cases(self):
        self.assertEqual(can_form_message("", ""), (True, "Mensaje vacío: no requiere caracteres para formarse."))
        self.assertEqual(can_form_message("", "ANYTHING"), (True, "Mensaje vacío: no requiere caracteres para formarse."))
        self.assertEqual(can_form_message("A", ""), (False, "El cofre no contiene caracteres válidos."))
    
    def test_long_inputs(self):
        msg = "NEVER GONNA GIVE YOU UP NEVER GONNA LET YOU DOWN " * 5
        chest = "NEVERGONNAGIVEYOUUPNEVERGONNALETYOUDOWN" * 5
        self.assertEqual(can_form_message(msg, chest)[0], True)
 
if __name__ == '__main__':
    unittest.main()
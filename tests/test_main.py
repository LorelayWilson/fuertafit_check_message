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
 
if __name__ == '__main__':
    unittest.main()
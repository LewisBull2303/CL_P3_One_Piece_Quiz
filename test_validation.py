import unittest
import validation as val

class TestEmailValidation(unittest.TestCase):
    """
    This class will verify the users email
    """

    def test_validate_email(self):
        self.assertTrue(val.validate_email("correct_email@gmail.com"), True)

    def test_validate_wrong_email(self):
        self.assertEqual(val.validate_email("correct_email@gmail"), None)
        self.assertEqual(val.validate_email("correct_emailgmail.com"), None)

    
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

class TestUserLogin(unittest.TestCase):
    """
    Verification of the inputs for the user login
    """

    def test_log_in(self):
        self.assertTrue(val.player_login([val.name, val.email]), True)
        self.assertEqual(val.player_login(1), None)
    
class TestUserRegistration(unittest.TestCase):
    """
    Verification of the inputs for the user registration
    """
    def test_register_user(self):
        self.assertTrue(val.register_user[val.name, val.email], True)
        self.assertEqual(val.register_user(1), None)
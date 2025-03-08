import unittest
import validation as val
from email_validator import EmailSyntaxError


class TestEmailValidation(unittest.TestCase):
    """
    This class will verify the user's email
    """
    def test_validate_email(self):
        self.assertTrue(val.validate_email("correct_email@gmail.com"))

    def test_validate_wrong_email(self):
        self.assertFalse(val.validate_email("correct_email@gmail"))
        self.assertFalse(val.validate_email("correct_emailgmail.com"))


class TestUserLogin(unittest.TestCase):
    """
    Verification of the inputs for the user login
    """
    def test_log_in(self):
        self.assertTrue(val.player_login("user@gmail.com"))
        self.assertFalse(val.player_login(""))


class TestUserRegistration(unittest.TestCase):
    """
    Verification of the inputs for the user registration
    """
    def test_register_user(self):
        self.assertTrue(val.register_user("new_user", "email@gmail.com"))
        self.assertFalse(val.register_user("", ""))


if __name__ == "__main__":
    unittest.main()

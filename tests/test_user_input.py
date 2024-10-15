import unittest
from unittest.mock import patch
from mlna.user_input import get_entities, select_nodes, user_dict


class TestGetEntities(unittest.TestCase):

    @patch('builtins.input', side_effect=['PERSON', 'ORG', 'DONE'])
    def test_valid_choices(self, mock_input):
        """
        Test when the user enters valid entity choices followed by 'DONE'.
        """
        expected_entities = ['PERSON', 'ORG']
        result = get_entities()
        self.assertEqual(result, expected_entities)

    @patch('builtins.input', side_effect=['INVALID', 'PERSON', 'NORP', 'DONE'])
    def test_invalid_and_valid_choices(self, mock_input):
        """
        Test when the user enters an invalid choice first, then valid choices followed by 'DONE'.
        """
        expected_entities = ['PERSON', 'NORP']
        result = get_entities()
        self.assertEqual(result, expected_entities)

    @patch('builtins.input', side_effect=['DONE'])
    def test_no_choices(self, mock_input):
        """
        Test when the user enters 'DONE' immediately, expecting an empty list.
        """
        expected_entities = []
        result = get_entities()
        self.assertEqual(result, expected_entities)

if __name__ == '__main__':
    unittest.main()

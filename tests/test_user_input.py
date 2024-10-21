import pandas as pd
import unittest
from unittest.mock import patch
# import sys
# import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../MLNA/mlna')))
from mlna.user_input import get_entities, select_nodes, make_user_dict


text_df= pd.read_pickle('test_data/test_df.pickle')
user_dict= pd.read_pickle('test_data/test_dict.pickle')
entity_tags=['PERSON', 'GPE']
user_ents=['telegraph']


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



class TestSelectNodes(unittest.TestCase):

    @patch ('builtins.input', side_effect=['nasser-al-din shah', 'iran', 'telegraph', 'done'])
    def test_valid_nodes(self, mock_input):
        """
        Test when the user enters valid node names followed by 'done'.
        """
        result = select_nodes(text_df, entity_tags, user_ents, user_dict)
        expected_nodes = ['nasser-al-din shah', 'iran', 'telegraph']
        self.assertEqual(result, expected_nodes)

    @patch('builtins.input', side_effect=['InvalidNode', 'Iran', 'done'])
    def test_invalid_then_valid_nodes(self, mock_input):
        """
        Test when the user enters an invalid node name first, then valid node names.
        """
        result = select_nodes(text_df, entity_tags, user_ents, user_dict)
        expected_nodes = ['Iran']
        self.assertEqual(result, expected_nodes)

    @patch('builtins.input', side_effect=['done'])
    def test_no_nodes(self, mock_input):
        """
        Test when the user enters 'done' immediately, expecting an empty list.
        """
        result = select_nodes(text_df, entity_tags, user_ents, user_dict)
        expected_nodes = []
        self.assertEqual(result, expected_nodes)


if __name__ == '__main__':
    unittest.main()

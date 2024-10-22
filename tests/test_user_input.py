import pandas as pd
import unittest
import pickle
from unittest.mock import patch, mock_open, MagicMock
from mlna.user_input import get_entities, select_nodes, make_user_dict


text_df= pd.read_pickle('test_data/test_df.pickle')
user_dict= pd.read_pickle('test_data/test_dict.pickle')
entity_tags=['PERSON', 'GPE']
user_ents=['telegraph']


class TestGetEntities(unittest.TestCase):

    @patch('builtins.input', side_effect=['PERSON', 'ORG', 'DONE'])
    def test_valid_choices(self, mock_input):
        expected_entities = ['PERSON', 'ORG']
        result = get_entities()
        self.assertEqual(result, expected_entities)

    @patch('builtins.input', side_effect=['INVALID', 'PERSON', 'NORP', 'DONE'])
    def test_invalid_and_valid_choices(self, mock_input):
        expected_entities = ['PERSON', 'NORP']
        result = get_entities()
        self.assertEqual(result, expected_entities)

    @patch('builtins.input', side_effect=['DONE'])
    def test_no_choices(self, mock_input):
        expected_entities = []
        result = get_entities()
        self.assertEqual(result, expected_entities)



class TestSelectNodes(unittest.TestCase):

    @patch ('builtins.input', side_effect=['nasser-al-din shah', 'iran', 'telegraph', 'done'])
    def test_valid_nodes(self, mock_input):
        result = select_nodes(text_df, entity_tags, user_ents, user_dict)
        expected_nodes = ['nasser-al-din shah', 'iran', 'telegraph']
        self.assertEqual(result, expected_nodes)

    @patch('builtins.input', side_effect=['InvalidNode', 'Iran', 'done'])
    def test_invalid_then_valid_nodes(self, mock_input):
        result = select_nodes(text_df, entity_tags, user_ents, user_dict)
        expected_nodes = ['Iran']
        self.assertEqual(result, expected_nodes)

    @patch('builtins.input', side_effect=['done'])
    def test_no_nodes(self, mock_input):
        result = select_nodes(text_df, entity_tags, user_ents, user_dict)
        expected_nodes = []
        self.assertEqual(result, expected_nodes)



class TestMakeUserDict(unittest.TestCase):

    @patch('builtins.input', side_effect=['n', 'John Doe', 'Jon Do', 'done'])
    @patch('builtins.open', new_callable=mock_open)
    def test_manual_entity_spelling(self, mock_open, mock_input):
        empty_text_df = None
        entity_tags = None
        result = make_user_dict(empty_text_df, entity_tags, dict_path=None)
        expected_dict = {'Jon Do': 'John Doe'}
        self.assertEqual(result, expected_dict)
        mock_open.assert_called_once_with('user_dict.pickle', 'wb')
        mock_open().write.assert_called_once()
        pickled_data = pickle.dumps(expected_dict)
        mock_open().write.assert_called_once_with(pickled_data)

    @patch('builtins.input', side_effect=['y', 'Britta', 'done'])
    @patch('builtins.open', new_callable=mock_open)
    #@patch('mlna.preproc.group_similar_ents', return_value=[['Berita', 'Brita']])
    def test_fuzzy_entity_matching(self, mock_open, mock_input):

        test_dict={"text_id": ["123"],
                   "full_text": ["Berita was here. Brita was there."]}
        new_text_df = pd.DataFrame.from_dict(test_dict)
        #entity_tags = None
        result = make_user_dict(new_text_df, entity_tags, dict_path=None, threshold=80)
        expected_dict = {'Berita': 'Britta', 'Brita': 'Britta'}
        self.assertEqual(result, expected_dict)
        mock_open.assert_called_once_with('user_dict.pickle', 'wb')
        mock_open().write.assert_called_once()
        pickled_data = pickle.dumps(expected_dict)
        mock_open().write.assert_called_once_with(pickled_data)
        #mock_group_similar_ents.assert_called_once_with(new_text_df, entity_tags, None, {}, 80)

    @patch('builtins.input', side_effect=['y', 's', 'done'])
    @patch('builtins.open', new_callable=mock_open)
    #@patch('mlna.preproc.group_similar_ents', return_value=[['John Doe', 'Jon Do']])
    def test_skip_fuzzy_matching_group(self, mock_open, mock_input):

        # test_dict={"text_id": ["123"],
        #     "full_text": ["John Doe was here. Jon Do was there."]}
        # text_df= pd.DataFrame.from_dict(test_dict)

        result = make_user_dict(text_df, entity_tags, dict_path=None, threshold=80)
        expected_dict = {}
        self.assertEqual(result, expected_dict)
        mock_open.assert_called_once_with('user_dict.pickle', 'wb')
        mock_open().write.assert_called_once()
        pickled_data = pickle.dumps(expected_dict)
        mock_open().write.assert_called_once_with(pickled_data)
        #mock_group_similar_ents.assert_called_once_with(text_df, entity_tags, None, {}, 80)

    @patch('builtins.input', side_effect=['n', 'John Doe', 'Jon Do', 'done'])
    @patch('builtins.open', new_callable=mock_open)
    def test_existing_dict_load_and_update(self, mock_open, mock_input):
        existing_dict = user_dict
        mock_open.return_value.read = pickle.dumps(existing_dict)

        with patch('pickle.load', return_value=existing_dict):
            result = make_user_dict(text_df, entity_tags, dict_path='existing_dict.pickle')
            expected_dict=user_dict
            result['Jon Do']= 'John Doe'
            expected_dict['Jon Do']= 'John Doe'
            self.assertEqual(result, expected_dict)
            mock_open.assert_called_with('existing_dict.pickle', 'wb')
            mock_open().write.assert_called_once()
            pickled_data = pickle.dumps(expected_dict)
            mock_open().write.assert_called_once_with(pickled_data)



if __name__ == '__main__':
    unittest.main()

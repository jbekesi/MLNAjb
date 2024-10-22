import pandas as pd
import pandas.testing as pdt
import unittest
from unittest.mock import patch, MagicMock
from mlna.network import update_weights, get_network_data, detect_community, visualize_network, filter_network_data

data= {
    "source": ['ali', 'qoli', 'iran', 'qoli', 'qoli', 'ali'],
    "target": ['shiraz', 'naqi', 'tehran', 'naqi', 'naqi', 'shiraz']
}
df=pd.DataFrame(data)

entity_tags=['PERSON', 'GPE']
user_ents= ['telegraph']
text_df= pd.read_pickle('test_data/test_df.pickle')
user_dict= pd.read_pickle('test_data/test_dict.pickle')
network_df= pd.read_pickle('test_data/network_df.pickle')


class TestUpdateWeights(unittest.TestCase):

    def test_apply_user_dict(self):
        expected_df = pd.read_pickle("test_data/updated_weights.pickle")
        result= update_weights(df)
        pdt.assert_frame_equal(result, expected_df)



class TestGetNetworkData(unittest.TestCase):

    def test_get_network_data (self):
        expected_df= network_df
        result= get_network_data (text_df, entity_tags=entity_tags, user_ents=user_ents, user_dict=user_dict)
        pdt.assert_frame_equal(result, expected_df)



class TestDetectCommunity(unittest.TestCase):

    @patch('builtins.print')
    def test_detect_community(self, mock_print):
        title = 'test_community'
        detect_community(text_df, entity_tags=entity_tags, user_ents=user_ents, user_dict=user_dict, title=title)
        mock_print.assert_called_with(f"The community graph was successfully saved to the current file's location as '{title}.html'.")



class TestVisualizeNetwork(unittest.TestCase):

    @patch('builtins.print')
    def test_visualize_network(self, mock_print):
        title = 'test_network'
        visualize_network(text_df, entity_tags=entity_tags, user_ents=user_ents, user_dict=user_dict, select_nodes=None, sources=None, title=title)
        mock_print.assert_called_with(f"The network graph was successfully saved to the current file's location as '{title}.html'.")



class TestFilterNetworkData(unittest.TestCase):

    def test_filter_network_data_or (self):
        select_nodes= ['Nasser-al-Din Shah', 'Iran', 'telegraph']
        result= filter_network_data (text_df, select_nodes=select_nodes, entity_tags=entity_tags, user_ents=user_ents, user_dict=user_dict, operator='OR')
        expected_df= pd.read_pickle('test_data/filtered_df_or.pickle')
        pdt.assert_frame_equal(result, expected_df)

    def test_filter_network_data_and(self):
        select_nodes= ['Nasser-al-Din Shah', 'Iran']
        result= filter_network_data (text_df, select_nodes=select_nodes, entity_tags=entity_tags, user_ents=user_ents, user_dict=user_dict, operator='AND')
        expected_df= pd.read_pickle('test_data/filtered_df_and.pickle')
        pdt.assert_frame_equal(result, expected_df)


if __name__ == '__main__':
    unittest.main()

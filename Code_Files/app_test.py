from utils import *
import unittest
from unittest.mock import patch
import pytest
class Testutils(unittest.TestCase):                                 # As the actual DB is not being used for testing, a mock DB is created. 
                                                                    # The testing checks if the functions being tested are called only once.
    @patch("utils.DBOperations.connect_to_db")
    def test_insert_data(self,mock_connect_to_db):
        table='Products'
        products_dict={'Name':'Mango Juice','Price':2,'Stock':200}
        db_obj=DBOperations()
        db_obj.insert_data(table,products_dict)
        mock_connect_to_db.assert_called_once_with()
        
    @patch("utils.DBOperations.connect_to_db")
    def test_retrieve_data(self,mock_connect_to_db):
        table='Products'
        db_obj=DBOperations()
        db_obj.retrieve_data(table)
        mock_connect_to_db.assert_called_once_with()
        
    @patch("utils.DBOperations.connect_to_db")
    def test_update_table(self,mock_connect_to_db):
        table='Couriers'
        db_obj=DBOperations()
        db_obj.retrieve_data_conditional(table,'4')
        mock_connect_to_db.assert_called_once_with()

    @patch("utils.DBOperations.connect_to_db")
    def test_retrieve_data_conditional(self,mock_connect_to_db):
        table='Orders'
        db_obj=DBOperations()
        
        db_obj.retrieve_data_conditional(table,'Price','4')
        mock_connect_to_db.assert_called_once_with()

    @patch("utils.DBOperations.connect_to_db")
    def test_update_table(self,mock_connect_to_db):
        table='Products'
        column='Name'
        update_value='Pizza'
        ID='5'
        db_obj=DBOperations()
        
        db_obj.update_table(table,column,update_value,ID)
        mock_connect_to_db.assert_called_once_with()
        
        
    @patch("utils.DBOperations.connect_to_db")
    def test_delete_records(self,mock_connect_to_db):
        table='Couriers'
        ID='5'
        db_obj=DBOperations()
        db_obj.delete_records(table,ID)
        mock_connect_to_db.assert_called_once_with()
    
    @patch("utils.DBOperations.connect_to_db")
    def test_search(self,mock_connect_to_db):
            table='Products'
            search_text='Aroma'
            db_obj=DBOperations()
            db_obj.search(search_text,table)
            mock_connect_to_db.assert_called_once_with()

    @patch("utils.DBOperations.connect_to_db")
    def test_update_orders(self,mock_connect_to_db):
            ID='5'
            column='Name'
            table='Products'
            update_value='Jane Doe'
            db_obj=DBOperations()
            db_obj.update_orders(ID,column,update_value)
            mock_connect_to_db.assert_called_once_with()
    
    @patch("utils.DBOperations.connect_to_db")
    def test_retrieve_orders_data(self,mock_connect_to_db):
            
            db_obj=DBOperations()
            db_obj.retrieve_orders_data()
            mock_connect_to_db.assert_called_once_with()
    
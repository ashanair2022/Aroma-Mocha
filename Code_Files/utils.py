import tabulate
import csv
import pymysql
import os
from dotenv import load_dotenv

#Create a class to carry out operations with the DB
class DBOperations:
    
    def __init__(self):
        pass
        
    
    def connect_to_db(self):            #Create a method to connect to DB
        try:
            
        # Load environment variables from .env file
            load_dotenv()
            self.host = os.environ.get("mysql_host")
            self.user = os.environ.get("mysql_user")
            self.password = os.environ.get("mysql_pass")
            self.db_name = os.environ.get("mysql_db")
            
            connection = pymysql.connect(
            host = self.host,
            user = self.user,
            password =self.password,
            database = self.db_name,
            port=3336,charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor
            )
            return connection
        except Exception as e:
            print(e)
  
    def insert_data(self,table,dict):     
        try:
              
            connection=self.connect_to_db()
            cur=connection.cursor()
            table_header=','.join(dict.keys())
            table_values=','.join(str(v) for v in dict.values()).replace(",","','")
            query="INSERT into "+table+'('+table_header+') '+'VALUES ('+"'"+table_values+"'"+')'
            query=query.replace('%',',')
            # print(query)
            cur.execute(query)
            connection.commit()
            cur.close()
            connection.close() 
            
        except Exception as e:
            print(e)   
        
    def retrieve_data(self,table):
        try:
            
            connection=self.connect_to_db()
            cur=connection.cursor()
            query="SELECT * FROM "+table
            #print(query)
            cur.execute(query)
            results=cur.fetchall()
            cur.close()
            connection.close()
            return results
        except Exception as e:
            print(e)        
    
    def retrieve_orders_data(self):
        
        try:
            
            connection=self.connect_to_db()
            cur=connection.cursor()
            query="SELECT O.ID,O.Order_Name AS Order_Name,O.Customer_Name AS Customer_Name, \
                O.Customer_Address AS Customer_Address, O.Customer_Phone AS Customer_Phone,\
                C.Name AS Courier_Name,Ord.Name AS Order_Status,prd.Name AS Product_Name \
                FROM Orders O \
                INNER JOIN Couriers C \
                ON O.COURIER_ID=C.ID \
                INNER JOIN Order_Status Ord \
                ON Ord.ID=O.Order_Status \
                INNER JOIN Products prd \
                ON prd.ID=O.Items \
                ORDER BY O.ID"
            #print(query)
            cur.execute(query)
            results=cur.fetchall()
            cur.close()
            connection.close()
            return results
        
        except Exception as e:
            print(e)        
    
    
    def retrieve_data_conditional(self,table,column,value):
        try:
        
            connection=self.connect_to_db()
            cur=connection.cursor()
            query="SELECT * FROM "+table+'WHERE' + column+'='+value
            cur.execute(query)
            results=cur.fetchone() 
            cur.close()
            connection.close()
            return results
        
        except Exception as e:
            print(e)
    
    def update_table(self,table,column,update_value,ID):
        
        try:
            
            connection=self.connect_to_db()
            cur=connection.cursor()
            query="UPDATE "+table+" SET "+column+"="+"'"+update_value+"' "+" WHERE ID =" +ID
            #print(query)
            cur.execute(query)
            connection.commit()
            cur.close()
            connection.close()
        
        except Exception as e:
            print(e)        
    
    def update_orders(self,ID,column,update_value):
        
        try: 
            
            connection=self.connect_to_db()
            cur=connection.cursor()
            fetch_name="SELECT Order_Name FROM Orders WHERE ID= "+ID
            cur.execute(fetch_name)
            order_name=cur.fetchone()
            #print(order_name)
            query="UPDATE Orders SET "+column+'= '+"'"+update_value+"'"+ ' WHERE Order_Name ='+"'"+order_name['Order_Name']+"'"
            #print(query)
            cur.execute(query)
            connection.commit()
            cur.close()
            connection.close()
        
        except Exception as e:
            print(e)        
    
    
    def delete_records(self,table,ID):
        
        try:
        
            connection=self.connect_to_db()
            cur=connection.cursor()
            query="DELETE FROM "+table+" WHERE ID= "+ID
            cur.execute(query)
            connection.commit()
            cur.close()
            connection.close()
            
        except Exception as e:
            print(e)
        
    def search(self,search_text,table):
        
        try:
            
            connection=self.connect_to_db()
            cur=connection.cursor()
            query="Select * FROM "+table+" WHERE Name LIKE '%"+search_text+"%'"
            cur.execute(query)
            results=cur.fetchall()
            cur.close()
            connection.close()
            return results
            
        except Exception as e:
            print(e)

db_ob=DBOperations()

class Utility:
    
    def __init__(self):
        pass
    
    def tabulate_results(self,list):
        try:   
            print('\n')
            rows=[x.values() for x in list]
            header=list[0].keys()
            print(tabulate.tabulate(rows,header),'\n')
        
        except Exception as e:
            print(e)
        
    def export_csv(self,file_name,list):
        
        try:
            keys = list[0].keys()
            with open('F:\\Generation-Mini Project\\Aroma-Mocha\\am_venv\source\\'+file_name+'.csv', 'w', newline='') as output_file:
                                dict_writer = csv.DictWriter(output_file, keys)
                                dict_writer.writeheader()
                                dict_writer.writerows(list) 
        except Exception as e:
            print(e)
       
    
    def csv_reader(self,csv_file):
        try:
            
            with open('F:\\Generation-Mini Project\\Aroma-Mocha\\am_venv\\source\\'+csv_file) as f:
                    lst= [{k: v for k, v in row.items()}
                    for row in csv.DictReader(f, skipinitialspace=True)] 
            return lst
        
        except Exception as e:
            print(e)
        
    def csv_writer(self,csv_file,lst):
        try:
           
            keys = lst[0].keys()
            with open('F:\\Generation-Mini Project\\Aroma-Mocha\\MIni_Project\\source\\'+csv_file, 'w', newline='') as output_file:
                                    dict_writer = csv.DictWriter(output_file, keys)
                                    dict_writer.writeheader()
                                    dict_writer.writerows(lst) 
            return lst
       
        except Exception as e:
            print(e)       
    
# Print Dictionary
    def print_dict(self,dict):
        
        try:
            
            print('\n')
            print( "{:<15} {:<15}".format('Index','Menu'),'\n')
            for key, value in dict.items():
                print(key,' ',value,'\n')

        except Exception as e:
            print(e)

 
def main_menu():
    
    try:
        
        main_menu_options={
                        0: 'exit',
                        1: 'Products_Menu',
                        2: 'Couriers Menu',
                        3: 'Orders Menu'
                                            }
        return main_menu_options
    
    except Exception as e:
            print(e)

    

![image](https://user-images.githubusercontent.com/104994723/169697258-f5c16135-13f7-4895-adbf-0cba4dd945bc.png)








# Aroma-Mocha

- Problem Statement:  

Aroma Mocha is a coffee shop established in 2021. Due to it's excellent customer service, unique and delicious product ranges, the shop has started recieving larger number of orders from customers. The shop does online deliveries through it's tie ups with large food order and delivery platforms. Aroma Mocha, being a start-up decided to approach a Software Developer to build an application for them that can help them track their inventory and orders. 

** Requirements:**
- Track Product Inventory
   - Ability to view existing product inventory, create new products, update and delete products from the inventory as necessary   
- Track Couriers
  - Ability to view existing courrier providers, their phone numbers, create, update and delete couriers from the data
- Track Orders
  - Ability to view existing orders, create new orders that includes adding customer information, order information and status, update, delete orders. 

- Ability to export data to a csv file. 

The application has been developed using Python Programming Language and MySQL Database at the backend. 

- Python Version- 3.10.4
   - Please set up a virtual environment using virtualenv, instructions here https://towardsdatascience.com/create-virtual-environment-using-virtualenv-and-add-it-to-jupyter-notebook-6e1bf4e03415
   - Please specify the Python version, instructions here : https://stackoverflow.com/questions/1534210/use-different-python-version-with-virtualenv
- Code_Files/requirements.txt to be run meet system requirements
- Code_Files/utils.py - All helper classes and methods are written in this file.  
- Code_Files/app.py- The main file that has  the application code.
- Code_Files/app_test.py - The testing file used to test the functions in the application.   
- Code_Files/shop_name.py - Contains the logo of Aroma Mocha  
- Code_Files/docker-compose+Code_Files/.env to get docker up and running to connect to Mysql
- MySQL scripts to create Database,tables and add data to them
- All csv files as samples of the data in the database in Code_Files
- Please specify the path where the csv should be saved in the export_csv() method of Utility class in utils file. 

Please find a sample Aroma-Mocha Dashboard here that summarises the Orders: https://datastudio.google.com/reporting/4c6e8c67-4f54-45f3-996a-4b2202b42771


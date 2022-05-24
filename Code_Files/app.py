#@Author: Asha Nair

#import required libraries

from sys import exit
from shop_name import logo
import utils
from utils import Utility,DBOperations


print(logo+'\n')                            # Print the Organisation Logo
print('**Welcome to Aroma Mocha! Enjoy your day!!**\n')
print("--------------------------------------------\n")
print("                 MAIN MENU             ")
print("-------------------------------------------\n")

#Create Products,Courier which inherits the properties of Class Utility,DBOperations and 
# an Orders class which inherits both Products and Courier classes 

#1. Create the Products Class
class Products(DBOperations,Utility):
    def __init__(self):
        super().__init__()
    
        #Retrieve Products data from DB and save in Products list
        self.products_list=self.retrieve_data('Products')   
        
        self.product_menu={
                    0: 'Return to main menu',               #Create the product_menu 
                    1: 'View Products',
                    2: 'Create Product',
                    3: 'Update Product',
                    4: 'Delete Product',
                    5: 'Export Products list'
                                        }


#2. Create Courier Class
class Courier(DBOperations,Utility):
    
        def __init__(self):
            super().__init__()
            
           #Retrieve Couriers data from DB and save in Couriers list        
            self.couriers_list=self.retrieve_data('Couriers')          
            self.couriers_menu={
                    0: 'Return to main menu',
                    1: 'View Courier',
                    2: 'Create Courier',                #Create the couriers menu 
                    3: 'Update Courier',
                    4: 'Delete Courier',
                    5: 'Export Couriers list'
                                        }
            
#Create Orders class which will inherit from Products and Courier.
class Orders(Products,Courier):
        def __init__(self):
            super().__init__()
            
           #Retrieve Orders data from DB and save in Orders list
            self.orders_list=self.retrieve_orders_data()    
            
            self.orders_menu={
                        0:'Return to main menu',
                        1:'View Orders',
                        2:'Create Order',                           #Create the Orders menu
                        3:'Update Order Status',
                        4:'Update Order',
                        5:'Delete Order',
                        6: 'Export Orders list'

                                }
            self.order_status=self.retrieve_data('Order_Status')
                            
            
#Code execution starts here
#Introducing classes and objects to the code allows maintaining the state of the products,couriers and orders list
def main():
    try:
        
        prd_obj=Products()            #Instantiate object of Products class
        cr_obj=Courier()              #Instantiate object of Courier class
        ord_obj=Orders()              # Instantiate object of the Orders class
        
        while 1==1:
            
            prd_obj.print_dict(utils.main_menu())                       #Print the main menu
            main_option=int(input(' Please choose an option:'))         #Prompt the user to choose an option from the main menu
        
            
            match main_option:                                          #match the option chosen by the user from the main menu to the cases 0,1,2,3
                case 0:
                    exit_option=input('Are you sure you want to exit? Y/N:')        
                    if exit_option=='Y':
                            exit()
                    else:
                        main()
                case 1:
                    show_product_options(prd_obj)
                case 2:
                    show_courier_options(cr_obj)
                case 3:
                    show_order_options(ord_obj,cr_obj,prd_obj)
                    
    except Exception as e:
        print(e)

def show_product_options(prd_obj): 
        print('\n------------------PRODUCT MENU----------------')                           #Create product menu 
        prd_obj.print_dict(prd_obj.product_menu)                                            # Print Product Menu
        product_option=int(input("Please select one of the product menu's options:"))       #User chooses what they want to do with the products table
        prd_obj=Product_Management(product_option,prd_obj)                                  #Call the Product Management Function to carry out the chosen operation    
        user_menu_choice=input('Would you like to go back to the Product menu? Y/N: ')      # Once the operation is completed, the user may go back to the Product Menu
        if user_menu_choice=='Y':                                                           # If they go back, show product menu options again                                          
            show_product_options(prd_obj)                                                   
        else:
            print("--------------------------------------------\n")
            print("                 MAIN MENU             ")
            print("-------------------------------------------\n")
            main()                                                                          # Else, exit the Product Menu to return to Main Menu
        
        
def show_courier_options(cr_obj):                                                        #Create Courier Menu
        print('\n------------------COURIER MENU----------------')
        cr_obj.print_dict(cr_obj.couriers_menu)
        # pp.pprint(cr_obj.couriers_menu)
        courier_option=int(input("Please select one of the courier menu's options:"))  
        cr_obj=Courier_Management(courier_option,cr_obj)                                    #Call the Courier Management Function to carry out Courier Menu operations
        user_menu_choice=input('Would you like to go back to the Couriers menu? Y/N: ')
        if user_menu_choice=='Y':
            show_courier_options(cr_obj)
        else:
            print("--------------------------------------------\n")
            print("                 MAIN MENU             ")
            print("-------------------------------------------\n")
            main()

def show_order_options(ord_obj,cr_obj,prd_obj):                                                    #Create Orders Menu
        print('\n------------------ORDERS MENU----------------')                                    # Carry out similar operations as above
        ord_obj.print_dict(ord_obj.orders_menu)
        order_option=int(input("Please select one of the order_menu options:"))  
        ord_obj=Orders_Management(order_option,ord_obj,cr_obj,prd_obj)
        user_menu_choice=input('Would you like to go back to the Orders menu? Y/N: ')
        if user_menu_choice=='Y':
            show_order_options(ord_obj,cr_obj,prd_obj)
        else:
            print("--------------------------------------------\n")
            print("                 MAIN MENU             ")
            print("-------------------------------------------\n")
            main()
            
#Create a function to carry out operations in the Products list when the user chooses a suitable option from Products menu

def Product_Management(product_option,prd_obj):
    try: 
        match product_option:
                        case 0:
                            main()                  # Return to main menu
                        case 1:                                                 # View Products
                            prd_obj.tabulate_results(prd_obj.products_list)     # Tabulate the products list to which the product's table's data is saved
                            return prd_obj                                      # Return the product object
                        case 2:                                                 #Create Products
                            products_dict={}                                    #Initialize products dictionary
                            prd_name=input('Please enter product name:')
                            prd_price=input('Please enter product price:')
                            prd_stock=input('Please enter stock available: ')
                            products_dict['Name']=prd_name
                            products_dict['Price']=prd_price
                            products_dict['Stock']=prd_stock 
                            prd_obj.insert_data('Products',products_dict)       # Insert Products dictionary to Products table
                            print('\n Product created successfully !!\n','______________________________')
                            print('\n-------------------Updated Products--------------------\n')
                            prd_obj.products_list=prd_obj.retrieve_data('Products')      # Retrieve data from Products table to save in Products list
                            prd_obj.tabulate_results(prd_obj.products_list)              # Display Products list   
                            
                            return prd_obj
                        case 3:                                                 # Update new products based on chosen ID
                            prd_obj.tabulate_results(prd_obj.products_list)                
                            existing_pdt_index=input('Enter id of the product to be updated:')   
                            new_product=input('Enter the new product name: ') 
                            new_price=input('Enter the new product price: ')
                            new_stock=input('Enter the new stock: ')
                            
                            if new_product!='':
                                    prd_obj.update_table('Products','Name',new_product,existing_pdt_index)
                            if new_price!='':
                                    prd_obj.update_table('Products','Price',new_price,existing_pdt_index)
                            if new_stock!='':
                                    prd_obj.update_table('Products','Stock',new_stock,existing_pdt_index)        
                            print('\nProducts updated successfully!!\n')
                            print('\n-------------------Updated Products--------------------\n')
                            prd_obj.products_list=prd_obj.retrieve_data('Products')
                            prd_obj.tabulate_results(prd_obj.products_list)
                            return prd_obj
                        case 4:                                             # Delete products based on chosen ID
                            prd_obj.tabulate_results(prd_obj.products_list)
                            delete_id=input('Enter the ID of the product you want to delete:')
                            prd_obj.delete_records('Products',delete_id)
                            print('\nProduct deleted successfully!!\n')
                            print('\n-------------------Updated Products--------------------\n')
                            prd_obj.products_list=prd_obj.retrieve_data('Products')
                            prd_obj.tabulate_results(prd_obj.products_list)
                            return prd_obj
                        case 5:                                                 # Export Products in the DB to csv for visualisation
                            prd_obj.export_csv('products',prd_obj.products_list)
                            print('\nA file by the name products.csv has been saved on your computer!\n')
                            return prd_obj
                        case _:
                            print('Invalid selection')
    
    except Exception as e:
        print(e)
                         
#Create a function to carry out operations in the Couriers list when the user chooses a suitable option from Couriers menu

def Courier_Management(courier_option,cr_obj):
    try:
        
        match courier_option:
                        case 0:
                            main()                          #Return to main menu
                        case 1: 
                            cr_obj.tabulate_results(cr_obj.couriers_list)          # View Courier List
                            return cr_obj
                        case 2:                                                     # Create couriers        
                            couriers_dict={}
                            cr_name=input("Please enter courier handler's name:")
                            cr_phone= input('Please enter the phone number of the courier handler:')
                            #max_id=max(cr_obj.couriers_list,key=lambda x:x['ID'])['ID']       #Find the maximum ID available 
                            #couriers_dict['ID']=str(int(max_id)+1)
                            couriers_dict['Name']=cr_name
                            couriers_dict['Phone']=cr_phone
                            cr_obj.insert_data('Couriers',couriers_dict)                # Insert couriers to couriers table
                            print('\nCourier created successfully!!\n')
                            print('\n-------------------Updated Couriers--------------------\n')
                            cr_obj.couriers_list=cr_obj.retrieve_data('Couriers')       # Retrieve couriers data
                            cr_obj.tabulate_results(cr_obj.couriers_list)   
                            return cr_obj                                               
                        case 3:                                                         #
                            cr_obj.tabulate_results(cr_obj.couriers_list)
                            existing_cr_index=input('Enter index of the courier to be updated:')   
                            new_courier=input('Enter the new courier name: ')
                            phone_update=input('Enter the new phone number:') 
                            if new_courier!='':
                                    cr_obj.update_table('Couriers','Name',new_courier,existing_cr_index)
                            if phone_update!='':
                                    cr_obj.update_table('Couriers','Phone',phone_update,existing_cr_index)
                            print('\nCouriers updated successfully!!\n')
                            print('\n-------------------Updated Couriers--------------------\n')
                            cr_obj.couriers_list=cr_obj.retrieve_data('Couriers')
                            cr_obj.tabulate_results(cr_obj.couriers_list)
                            return cr_obj
                        case 4:
                            cr_obj.tabulate_results(cr_obj.couriers_list)
                            delete_id=input('Enter the ID of the courier you want to delete:')
                            cr_obj.delete_records('Couriers',delete_id)
                            print('\nCourier deleted successfully!!\n')
                            print('\n-------------------Updated Couriers--------------------\n')
                            cr_obj.couriers_list=cr_obj.retrieve_data('Couriers')
                            cr_obj.tabulate_results(cr_obj.couriers_list)
                            return cr_obj
                        case 5:
                            cr_obj.export_csv('couriers',cr_obj.couriers_list)
                            print('\nA file by the name couriers.csv has been saved on your computer!\n')
                            return cr_obj
                        case _:
                            print('Invalid selection')
                            
    except Exception as e:
        print(e)

#Create a function to carry out operations in the Orders list when the user chooses a suitable option from Orders menu

def Orders_Management(orders_option,ord_obj,cr_obj,prd_obj): 
    
    try:
        
        match orders_option:
                        case 0:
                            main()                                  # Return to main function
                        case 1: 
                            ord_obj.tabulate_results(ord_obj.orders_list)       # View orders
                            return ord_obj
                        case 2:                                                         # Create Orders
                            order_name=input('Please enter a name for the order: ')     # Enter a unique order_name for each customer              
                            cust_name=input('Customer Name:')           
                            cust_address=input('Customer Address: ')
                            cust_phone_number=input('Customer Phone Number: ')
                            #prd_obj.tabulate_results(prd_obj.products_list)
                            search_products=[]                                         # Introduce a search functionality to look for products in the products table
                            while len(search_products)==0:                              # Request for a search text until a product with the search text is found in the database  
                                search_text=input("Enter Product Name or Product Name's Part: ")
                                search_products=ord_obj.search(search_text,'Products')             # Use the search method of class DBOperations to retrieve data from Products table 
                                if len(search_products)!=0:                                        # Display the search_products corresponding to the search text if they are found in the Products table                                                                   
                                    prd_obj.tabulate_results(search_products)
                                else:
                                    print('No results found!')  
                            prd_ids=(input('Enter the product ids separated by commas:')).split(',')
                            cr_obj.tabulate_results(cr_obj.couriers_list)
                            select_courier=input("Select a courier using it's id: ")
                            
                            for i in range(len(prd_ids)):                               # Loop through product ids to create one row for every product id in the comma separated order items
                                order={}
                                order['Order_Name']=order_name                          #Create an order name for every customer, unique to them
                                order['Customer_Name']=cust_name
                                order['Customer_Address']=cust_address
                                order['Customer_Phone']=cust_phone_number
                                order['Courier_ID']=select_courier
                                ord_obj.order_status
                                order['Order_Status']=ord_obj.order_status[1]['ID']             # Retrieve the value of IDs from the list of dictionaries derived from the Order Status Table 
                                order['Items']=prd_ids[i]
                                ord_obj.insert_data('Orders',order)
                            ord_obj.orders_list=ord_obj.retrieve_orders_data()                  # Retrieve orders data
                            print('\n Order created successfully !!\n','______________________________')
                            print('\n-------------------Updated Orders--------------------\n')
                            ord_obj.tabulate_results(ord_obj.orders_list)
                            return ord_obj
                        case 3:                                                                 #Update Order Status
                            print('\n---------------EXISTING ORDERS-----------------\n')
                            ord_obj.tabulate_results(ord_obj.orders_list)
                            order_id=input('Please enter the Order ID to be updated: ')
                            print('\n---------------ORDER STATUS OPTIONS-----------------')
                            ord_obj.tabulate_results(ord_obj.order_status)
                            update_status=input('Please enter the index of the order status: ')
                            ord_obj.update_orders(order_id,'Order_Status',update_status)        # Update Order Status
                            print('Order status updated Successfully!!\n')
                            print('\n-------------------Updated Orders--------------------\n')
                            ord_obj.orders_list=ord_obj.retrieve_orders_data()
                            ord_obj.tabulate_results(ord_obj.orders_list)
                            
                            return ord_obj
                        case 4:                                                         # Update Orders
                            ord_obj.tabulate_results(ord_obj.orders_list)
                            order_id=input('Please enter the Order ID to be updated: ')
                            name_update=input('Enter the new customer name: ')
                            address_update=input('Enter the new address: ')
                            phone_update=input('Enter the new phone number: ')
                            prd_obj.tabulate_results(prd_obj.products_list)
                            prd_update=input('Enter the new products IDs:')
                            cr_obj.tabulate_results(cr_obj.couriers_list)
                            courier_update=input('Enter the id of the new courier: ')
                            
                            if name_update!='':                                                 # Update values only if the entered values are not blank
                                ord_obj.update_orders(order_id,'Customer_Name',name_update) 
                            if address_update!='':
                                ord_obj.update_orders(order_id,'Customer_Address',address_update) 
                            if phone_update!='':
                                ord_obj.update_orders(order_id,'Customer_Phone',phone_update) 
                            if prd_update!='':
                                ord_obj.update_table('Orders','Items',prd_update,order_id) 
                            if courier_update!='':
                                ord_obj.update_orders(order_id,'Courier_ID',courier_update)
                            print('\nOrder updated Successfully!!\n')
                            print('\n-------------------Updated Orders--------------------\n')
                            ord_obj.orders_list=ord_obj.retrieve_orders_data()
                            ord_obj.tabulate_results(ord_obj.orders_list) 
                            return ord_obj
                        case 5:                                                 # Delete Orders
                        
                            ord_obj.tabulate_results(ord_obj.orders_list)     
                            order__del_id=input('Please enter the Order ID to be deleted: ')
                            ord_obj.delete_records('Orders',order__del_id)
                            print('\nOrder deleted Successfully!!\n')
                            print('\n-------------------Updated Orders--------------------\n')
                            ord_obj.orders_list=ord_obj.retrieve_orders_data()
                            ord_obj.tabulate_results(ord_obj.orders_list)
                            return ord_obj
                        case 6:                                                 # Export Orders to csv
                            ord_obj.export_csv('Orders',ord_obj.orders_list)
                            print('\nA file by the name Orders.csv has been saved on your computer!\n')
                            return ord_obj
                        case _:
                            print('Invalid selection')
                            
    except Exception as e:
        print(e)



if __name__=='__main__':
    main()
    
    



    
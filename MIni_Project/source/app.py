#@Author: Asha Nair
#Date: 25 April 2022-01 June 2022

#import required libraries
from shop_name import logo
import pprint as pp
import json
import utils
# import tabulate
from utils import Utility

print(logo+'\n')
print('**Welcome to Aroma Mocha! Enjoy your day!!**\n')
print("--------------------------------------------\n")
print("                 MAIN MENU             ")
print("-------------------------------------------\n")

#Create Products,Courier which inherits the properties of Class Utility and 
# an Orders classes which inherits both Products and Courier classes 

#1. Create the Products Class
class Products(Utility):
    def __init__(self):
        super().__init__()
        #load the products.txt file
        with open(r'F:\Generation UK\Generation_UK_Codefiles\MIni_Project\source\products.txt','r') as txt_file:
                    self.products_list=txt_file.read().splitlines()
                    
        self.product_menu={
                    0: 'Return to main menu',               #Create the product_menu for the user to choose from
                    1: 'View Products',
                    2: 'Create Product',
                    3: 'Update Product',
                    4: 'Delete Product'
                                        }


#2. Create Courier Class
class Courier(Utility):
    
        def __init__(self):
            super().__init__()
            
            #Read the courier.txt file
            with open(r'F:\Generation UK\Generation_UK_Codefiles\MIni_Project\source\courier.txt','r') as txt_file:
                            self.courier_list=txt_file.read().splitlines()
                            
            self.couriers_menu={
                    0: 'Return to main menu',
                    1: 'View Courier',
                    2: 'Create Courier',                #Create the couriers menu for the user to choose from
                    3: 'Update Courier',
                    4: 'Delete Courier'
                                        }
            
#Create Orders class which will inherit from Products and Courier.
class Orders(Products,Courier):
        def __init__(self):
            super().__init__()
            
            # Read the orders.json file
            with open(r'F:\Generation UK\Generation_UK_Codefiles\MIni_Project\source\orders.json') as json_file:
                            self.orders_list=json.load(json_file)
             
            
            self.orders_menu={
                        0:'Return to main menu',
                        1:'View Orders',
                        2:'Create Order',                           #Create the Orders menu
                        3:'Update Order Status',
                        4:'Update Order',
                        5:'Delete Order'

                                }
            self.order_status=['PREPARING',                         #Create the list of Order Status types
                               'OUT FOR DELIVERY',
                               'DELIVERED'    
                                ]
                            
            
#Code execution starts here
#Introducing classes and objects to the code allows maintaining the state of the products and couriers list
def main():
    prd_obj=Products()            #Create object of Products class
    cr_obj=Courier()              #Create object of Courier class
    ord_obj=Orders()              # Create object of the Orders class
    
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
                show_order_options(ord_obj,cr_obj)

def show_product_options(prd_obj): 
        print('\n------------------PRODUCT MENU----------------')                           #Create product menu 
        pp.pprint(prd_obj.product_menu)
        product_option=int(input('Please select one of the following product options:'))  
        prd_obj=Product_Management(product_option,prd_obj)
        show_product_options(prd_obj)
        
def show_courier_options(cr_obj):                                                        #Create Courier Menu
        print('\n------------------COURIER MENU----------------')
        pp.pprint(cr_obj.couriers_menu)
        courier_option=int(input('Please select one of the following courier options:'))  
        cr_obj=Courier_Management(courier_option,cr_obj)
        show_courier_options(cr_obj)

def show_order_options(ord_obj,cr_obj):                                                    #Create Orders Menu
        print('\n------------------ORDERS MENU----------------')
        ord_obj.print_dict(ord_obj.orders_menu)
        #pp.pprint(ord_obj.orders_menu)
        order_option=int(input('Please select one of the following order_menu options:'))  
        ord_obj=Orders_Management(order_option,ord_obj,cr_obj)
        user_menu_choice=input('Would you like to go back to the Orders menu? Y/N: ')
        if user_menu_choice=='Y':
            show_order_options(ord_obj,cr_obj)
        else:
            ord_obj.write_json(ord_obj.orders_list,'Orders')
            main()
            
#Create a function to carry out operations in the Products list when the user chooses a suitable option from Products menu

def Product_Management(product_option,prd_obj):
    match product_option:
                    case 0:
                        with open(r'F:\Generation UK\Generation_UK_Codefiles\MIni_Project\source\products.txt','w') as txt_file:
                            for element in prd_obj.products_list:
                                txt_file.write(element + '\n')
                        main()
                    case 1: 
                        prd_obj.view_list_indices(prd_obj.products_list)
                        return prd_obj
                    case 2:
                        prd_name=input('Please enter product name:')
                        prd_obj.products_list= prd_obj.add(prd_name,prd_obj.products_list)
                        prd_obj.view_list_indices(prd_obj.products_list)
                        
                        return prd_obj
                    case 3:
                       prd_obj.view_list_indices(prd_obj.products_list)
                       existing_pdt_index=int(input('Enter index of the product to be updated:'))   
                       new_product=input('Enter the new product name: ') 
                       prd_obj.products_list=prd_obj.update(existing_pdt_index,new_product,prd_obj.products_list)
                       prd_obj.view_list_indices(prd_obj.products_list)
                       return prd_obj
                    case 4:
                        prd_obj.view_list_indices(prd_obj.products_list)
                        delete_index=int(input('Enter the index of the product you want to delete:'))
                        prd_obj.products_list=prd_obj.delete(delete_index,prd_obj.products_list)
                        prd_obj.view_list_indices(prd_obj.products_list)
                        return prd_obj
                    case _:
                        print('Invalid selection')
                         
#Create a function to carry out operations in the Couriers list when the user chooses a suitable option from Couriers menu

def Courier_Management(courier_option,cr_obj):
    match courier_option:
                    case 0:
                        with open(r'F:\Generation UK\Generation_UK_Codefiles\MIni_Project\source\courier.txt','w') as txt_file:
                            for element in cr_obj.courier_list:
                                
                                txt_file.write(element + '\n')
                        main()
                    case 1: 
                        cr_obj.view_list_indices(cr_obj.courier_list)
                        return cr_obj
                    case 2:
                        cr_name=input('Please enter courier name:')
                        cr_obj.courier_list=cr_obj.add(cr_name,cr_obj.courier_list)
                        cr_obj.view_list_indices(cr_obj.courier_list)
                        
                        return cr_obj
                    case 3:
                       cr_obj.view_list_indices(cr_obj.courier_list)
                       existing_cr_index=int(input('Enter index of the courier to be updated:'))   
                       new_courier=input('Enter the new courier name: ') 
                       cr_obj.courier_list=cr_obj.update(existing_cr_index,new_courier,cr_obj.courier_list)
                       cr_obj.view_list_indices(cr_obj.courier_list)
                       return cr_obj
                    case 4:
                        cr_obj.view_list_indices(cr_obj.courier_list)
                        delete_index=int(input('Enter the index of the courier you want to delete:'))
                        cr_obj.courier_list=cr_obj.delete(delete_index,cr_obj.courier_list)
                        cr_obj.view_list_indices(cr_obj.courier_list)
                        return cr_obj
                    case _:
                        print('Invalid selection')

#Create a function to carry out operations in the Orders list when the user chooses a suitable option from Orders menu

def Orders_Management(orders_option,ord_obj,cr_obj):
    match orders_option:
                    case 0:
                        ord_obj.write_json(ord_obj.orders_list,'Orders')
                        main()
                    case 1: 
                        ord_obj.tabulate_results(ord_obj.orders_list)
                        return ord_obj
                    case 2:
                        cust_name=input('Customer Name:')
                        cust_address=input('Customer Address: ')
                        cust_phone_number=input('Customer Phone Number: ')
                        cr_obj.view_list_indices(cr_obj.courier_list)
                        select_courier=int(input("Select a courier using it's index: "))
                        order={}
                        max_id=max(ord_obj.orders_list,key=lambda x:x['Id'])['Id']       #Find the maximum ID available in orders.json file
                       
                        order['Id']=int(max_id)+1                                 #Assign the next order the next ID.
                        order['Name']=cust_name
                        order['Address']=cust_address
                        order['Phone']=cust_phone_number
                        order['Courier']=cr_obj.courier_list[select_courier]
                        order['Status']='PREPARING'
                        ord_obj.orders_list=ord_obj.add(order,ord_obj.orders_list)
                        print('\n Order created Successfully !!\n','______________________________')
                        
                        return ord_obj
                    case 3:
                        ord_obj.tabulate_results(ord_obj.orders_list)
                        order_index=input('Please enter the Order ID to be updated: ')
                        print('\n---------------ORDER STATUS OPTIONS-----------------')
                        ord_obj.view_list_indices(ord_obj.order_status)
                        update_status=input('Please enter the index of the order status: ')
                        
                        ord_obj.orders_list[ord_obj.orders_list.index(next(iter(item for item in ord_obj.orders_list if item['Id']\
                                            ==int(order_index)),None))]['Status']=ord_obj.order_status[int(update_status)]
                        print('Order status updated Successfully!!\n')
                        return ord_obj
                    case 4: 
                        ord_obj.tabulate_results(ord_obj.orders_list)
                        
                        order_index=input('Please enter the Order ID to be updated: ')
                        name_update=input('Enter the new name: ')
                        address_update=input('Enter the new address: ')
                        phone_update=input('Enter the new phone number: ')
                        cr_obj.view_list_indices(cr_obj.courier_list)
                        courier_update=input('Enter the index of the new courier: ')
                        
                        if name_update!='':
                            ord_obj.orders_list[ord_obj.orders_list.index(next(iter(item for item in ord_obj.orders_list if item['Id']==int(order_index)),None))]['Name']=name_update
                        if address_update!='':
                            ord_obj.orders_list[ord_obj.orders_list.index(next(iter(item for item in ord_obj.orders_list if item['Id']==int(order_index)),None))]['Address']=address_update
                        if phone_update!='':
                            ord_obj.orders_list[ord_obj.orders_list.index(next(iter(item for item in ord_obj.orders_list if item['Id']==int(order_index)),None))]['Phone']=phone_update
                        if courier_update!='':
                            ord_obj.orders_list[ord_obj.orders_list.index(next(iter(item for item in ord_obj.orders_list if item['Id']==int(order_index)),None))]['Courier']=cr_obj.courier_list[int(courier_update)]
                        print('\nOrder updated Successfully!!\n') 
                        return ord_obj
                    case 5:
                        # rows=[x.values() for x in ord_obj.orders_list]
                        # header=ord_obj.orders_list[0].keys()
                        ord_obj.tabulate_results(ord_obj.orders_list)     
                        order__del_index=input('Please enter the Order ID to be deleted: ')
                        ord_obj.orders_list=ord_obj.delete(int(ord_obj.orders_list.index(next(iter(item for item in ord_obj.orders_list if item['Id']==int(order__del_index)),None))),ord_obj.orders_list)
                        print('\nOrder deleted Successfully!!\n')
                        return ord_obj
                    case _:
                        print('Invalid selection')



if __name__=='__main__':
    main()
    
    



    
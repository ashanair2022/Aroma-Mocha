#@Author: Asha Nair

#import required libraries

from shop_name import logo
import csv
import utils
from utils import Utility

print(logo+'\n')                            # Print the Organisation Logo
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
    
        #Read products from products.csv to products list which is a list of dictionaries
        self.products_list=self.csv_reader('products.csv')     
        
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
            
            #Read the courier.csv file to the couriers list which is a list of dictionaries
            self.couriers_list=self.csv_reader('couriers.csv')                   
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
            
            #Read the orders.csv file to the orders list which is a list of dictionaries
            self.orders_list=self.csv_reader('orders.csv')  
            
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
                show_order_options(ord_obj,cr_obj,prd_obj)

def show_product_options(prd_obj): 
        print('\n------------------PRODUCT MENU----------------')                           #Create product menu 
        prd_obj.print_dict(prd_obj.product_menu)
        product_option=int(input("Please select one of the product menu's options:"))  
        prd_obj=Product_Management(product_option,prd_obj)
        show_product_options(prd_obj)
        
def show_courier_options(cr_obj):                                                        #Create Courier Menu
        print('\n------------------COURIER MENU----------------')
        cr_obj.print_dict(cr_obj.couriers_menu)
        # pp.pprint(cr_obj.couriers_menu)
        courier_option=int(input("Please select one of the courier menu's options:"))  
        cr_obj=Courier_Management(courier_option,cr_obj)
        show_courier_options(cr_obj)

def show_order_options(ord_obj,cr_obj,prd_obj):                                                    #Create Orders Menu
        print('\n------------------ORDERS MENU----------------')
        ord_obj.print_dict(ord_obj.orders_menu)
        order_option=int(input("Please select one of the order_menu options:"))  
        ord_obj=Orders_Management(order_option,ord_obj,cr_obj,prd_obj)
        user_menu_choice=input('Would you like to go back to the Orders menu? Y/N: ')
        if user_menu_choice=='Y':
            show_order_options(ord_obj,cr_obj,prd_obj)
        else:
            keys = ord_obj.orders_list[0].keys()
            with open(r'F:\Generation-Mini Project\Aroma-Mocha\MIni_Project\source\orders.csv', 'w', newline='') as orders_file:
                dict_writer = csv.DictWriter(orders_file, keys)
                dict_writer.writeheader()
                dict_writer.writerows(ord_obj.orders_list)
            main()
            
#Create a function to carry out operations in the Products list when the user chooses a suitable option from Products menu

def Product_Management(product_option,prd_obj):
    match product_option:
                    case 0:
                        keys = prd_obj.products_list[0].keys()
                        with open(r'F:\Generation-Mini Project\Aroma-Mocha\MIni_Project\source\products.csv', 'w', newline='') as output_file:
                            dict_writer = csv.DictWriter(output_file, keys)
                            dict_writer.writeheader()
                            dict_writer.writerows(prd_obj.products_list)
                        #prd_obj.csv_writer(products.csv,products_list)
                        main()
                    case 1: 
                        prd_obj.tabulate_results(prd_obj.products_list)
                        #prd_obj.view_list_indices(prd_obj.products_list)
                        return prd_obj
                    case 2:
                        products_dict={}
                        prd_name=input('Please enter product name:')
                        prd_price=input('Please enter product price:')
                        max_id=max(prd_obj.products_list,key=lambda x:x['ID'])['ID']       #Find the maximum ID available 
                        products_dict['ID']=str(int(max_id)+1)
                        products_dict['Name']=prd_name
                        products_dict['Price']=prd_price
                        prd_obj.products_list= prd_obj.add(products_dict,prd_obj.products_list)
                        print('\n Order created Successfully !!\n','______________________________')
                        prd_obj.tabulate_results(prd_obj.products_list)
                        
                        return prd_obj
                    case 3:
                       prd_obj.tabulate_results(prd_obj.products_list)
                       existing_pdt_index=input('Enter id of the product to be updated:')   
                       new_product=input('Enter the new product name: ') 
                       new_price=input('Enter the new product price: ')
                       print(prd_obj.products_list)
                    #    print(prd_obj.find(prd_obj.products_list,'ID','2'))
                       if new_product!='':
                            prd_obj.products_list[prd_obj.products_list.index(next(iter(item for item in prd_obj.products_list if item['ID']==existing_pdt_index),None))]['Name']=new_product
                       if new_price!='':
                            prd_obj.products_list[prd_obj.products_list.index(next(iter(item for item in prd_obj.products_list if item['ID']==existing_pdt_index),None))]['Price']=new_price
   
                       print('\nProducts updated Successfully!!\n')
                       prd_obj.tabulate_results(prd_obj.products_list)
                       return prd_obj
                    case 4:
                        prd_obj.tabulate_results(prd_obj.products_list)
                        delete_index=input('Enter the ID of the product you want to delete:')
                        prd_obj.products_list=prd_obj.delete(int(prd_obj.products_list.index(next(iter(item for item in prd_obj.products_list if item['ID']==delete_index),None))),prd_obj.products_list)
                        print('\nProduct deleted Successfully!!\n')
                        prd_obj.tabulate_results(prd_obj.products_list)
                        return prd_obj
                    case _:
                        print('Invalid selection')
                         
#Create a function to carry out operations in the Couriers list when the user chooses a suitable option from Couriers menu

def Courier_Management(courier_option,cr_obj):
    match courier_option:
                    case 0:
                        keys = cr_obj.couriers_list[0].keys()
                        with open(r'F:\Generation-Mini Project\Aroma-Mocha\MIni_Project\source\couriers.csv', 'w', newline='') as courier_file:
                            dict_writer = csv.DictWriter(courier_file, keys)
                            dict_writer.writeheader()
                            dict_writer.writerows(cr_obj.couriers_list)
    
                        main()
                    case 1: 
                        cr_obj.tabulate_results(cr_obj.couriers_list)
                        return cr_obj
                    case 2:
                        couriers_dict={}
                        cr_name=input("Please enter courier handler's name:")
                        cr_phone= input('Please enter the phone number of the courier handler:')
                        max_id=max(cr_obj.couriers_list,key=lambda x:x['ID'])['ID']       #Find the maximum ID available 
                        couriers_dict['ID']=str(int(max_id)+1)
                        couriers_dict['Name']=cr_name
                        couriers_dict['Phone']=cr_phone
                        cr_obj.couriers_list=cr_obj.add(couriers_dict,cr_obj.couriers_list)
                        cr_obj.tabulate_results(cr_obj.couriers_list)   
                        return cr_obj
                    case 3:
                       cr_obj.tabulate_results(cr_obj.couriers_list)
                       existing_cr_index=input('Enter index of the courier to be updated:')   
                       new_courier=input('Enter the new courier name: ')
                       phone_update=input('Enter the new phone number:') 
                       print(cr_obj.couriers_list)
                       if new_courier!='':
                            cr_obj.couriers_list[cr_obj.couriers_list.index(next(iter(item for item in cr_obj.couriers_list if item['ID']==existing_cr_index),None))]['Name']=new_courier
                       if phone_update!='':
                            cr_obj.couriers_list[cr_obj.couriers_list.index(next(iter(item for item in cr_obj.couriers_list if item['ID']==existing_cr_index),None))]['Phone']=phone_update
                       print('\nCouriers updated Successfully!!\n')
                       
                       cr_obj.tabulate_results(cr_obj.couriers_list)
                       return cr_obj
                    case 4:
                        cr_obj.tabulate_results(cr_obj.couriers_list)
                        delete_id=input('Enter the ID of the courier you want to delete:')
                        cr_obj.couriers_list=cr_obj.delete(int(cr_obj.couriers_list.index(next(iter(item for item in cr_obj.couriers_list if item['ID']==delete_id),None))),cr_obj.couriers_list)
                        print('\nCourier Deleted Successfully!!\n')
                        cr_obj.tabulate_results(cr_obj.couriers_list)
                        return cr_obj
                    case _:
                        print('Invalid selection')

#Create a function to carry out operations in the Orders list when the user chooses a suitable option from Orders menu

def Orders_Management(orders_option,ord_obj,cr_obj,prd_obj):
    match orders_option:
                    case 0:
                        keys = ord_obj.orders_list[0].keys()
                        with open(r'F:\Generation-Mini Project\Aroma-Mocha\MIni_Project\source\orders.csv', 'w', newline='') as orders_file:
                            dict_writer = csv.DictWriter(orders_file, keys)
                            dict_writer.writeheader()
                            dict_writer.writerows(ord_obj.orders_list)
                        main()
                    case 1: 
                        ord_obj.tabulate_results(ord_obj.orders_list)
                        return ord_obj
                    case 2:
                        cust_name=input('Customer Name:')
                        cust_address=input('Customer Address: ')
                        cust_phone_number=input('Customer Phone Number: ')
                        prd_obj.tabulate_results(prd_obj.products_list)
                        prd_ids=input('Enter the product ids separated by commas:').split(',')
                        cr_obj.tabulate_results(cr_obj.couriers_list)
                        select_courier=input("Select a courier using it's id: ")
                        order={}
                        
                        max_id=max(ord_obj.orders_list,key=lambda x:x['Id'])['Id']       #Find the maximum ID available in orders.json file
                        order['Id']=int(max_id)+1                                 #Assign the next order the next ID.
                        order['Name']=cust_name
                        order['Address']=cust_address
                        order['Phone']=cust_phone_number
                        order['Product']=prd_ids
                        order['Courier']=cr_obj.couriers_list[cr_obj.couriers_list.index(next(iter(item for item in cr_obj.couriers_list if item['ID']==select_courier),None))]['Name']
                        order['Status']='PREPARING'
                        ord_obj.orders_list=ord_obj.add(order,ord_obj.orders_list)
                        print('\n Order created Successfully !!\n','______________________________')
                        
                        return ord_obj
                    case 3:
                        ord_obj.tabulate_results(ord_obj.orders_list)
                        order_id=input('Please enter the Order ID to be updated: ')
                        print('\n---------------ORDER STATUS OPTIONS-----------------')
                        ord_obj.view_list_indices(ord_obj.order_status)
                        update_status=input('Please enter the index of the order status: ')
                        
                        ord_obj.orders_list[ord_obj.orders_list.index(next(iter(item for item in ord_obj.orders_list if item['Id']\
                                            ==order_id),None))]['Status']=ord_obj.order_status[int(update_status)]
                        print('Order status updated Successfully!!\n')
                        return ord_obj
                    case 4: 
                        ord_obj.tabulate_results(ord_obj.orders_list)
                        
                        order_id=input('Please enter the Order ID to be updated: ')
                        name_update=input('Enter the new name: ')
                        address_update=input('Enter the new address: ')
                        phone_update=input('Enter the new phone number: ')
                        prd_update=input('Enter the new products:').split(',')

                        cr_obj.tabulate_results(cr_obj.couriers_list)
                        courier_update=input('Enter the index of the new courier: ')
                        
                        if name_update!='':
                            ord_obj.orders_list[ord_obj.orders_list.index(next(iter(item for item in ord_obj.orders_list if item['Id']==order_id),None))]['Name']=name_update
                        if address_update!='':
                            ord_obj.orders_list[ord_obj.orders_list.index(next(iter(item for item in ord_obj.orders_list if item['Id']==order_id),None))]['Address']=address_update
                        if phone_update!='':
                            ord_obj.orders_list[ord_obj.orders_list.index(next(iter(item for item in ord_obj.orders_list if item['Id']==order_id),None))]['Phone']=phone_update
                        if len(prd_update)!=0 and prd_update[0]!='' :
                                ord_obj.orders_list[ord_obj.orders_list.index(next(iter(item for item in ord_obj.orders_list if item['Id']==order_id),None))]['Product']=prd_update
                        if courier_update!='':
                            ord_obj.orders_list[ord_obj.orders_list.index(next(iter(item for item in ord_obj.orders_list if item['Id']==order_id),None))]['Courier']=cr_obj.couriers_list[int(cr_obj.couriers_list.index(next(iter(item for item in cr_obj.couriers_list if item['ID']==courier_update),None)))]['Name']
                        print('\nOrder updated Successfully!!\n') 
                        return ord_obj
                    case 5:
                       
                        ord_obj.tabulate_results(ord_obj.orders_list)     
                        order__del_id=input('Please enter the Order ID to be deleted: ')
                        ord_obj.orders_list=ord_obj.delete(int(ord_obj.orders_list.index(next(iter(item for item in ord_obj.orders_list if item['Id']==order__del_id),None))),ord_obj.orders_list)
                        print('\nOrder deleted Successfully!!\n')
                        return ord_obj
                    case _:
                        print('Invalid selection')



if __name__=='__main__':
    main()
    
    



    
import tabulate
import csv
class Utility:
    
    def __init__(self):
        pass
    
        
    def add(self,prd_dict,list):
        list.append(prd_dict)
        return list

    # def delete(self,index,list):
    #     list.pop(index)
    #     return list

    # def update(self,index,new_item,list):
    #     list[index]=new_item
    #     return list
    
    # def view_list_indices(self,list):
    #     print('\n')
    #     for index,name in enumerate(list):
    #         print(index,name)
    #     print('\n')
    
    def tabulate_results(self,list):
        print('\n')
        rows=[x.values() for x in list]
        header=list[0].keys()
        print(tabulate.tabulate(rows,header),'\n')
    
    def csv_reader(self,csv_file):
        with open('F:\\Generation-Mini Project\\Aroma-Mocha\\MIni_Project\\source\\'+csv_file) as f:
                lst= [{k: v for k, v in row.items()}
                for row in csv.DictReader(f, skipinitialspace=True)] 
        return lst
    
    # def csv_writer(self,csv_file,lst):
    #    keys = lst[0].keys()
    #    with open('F:\\Generation-Mini Project\\Aroma-Mocha\\MIni_Project\\source\\'+csv_file, 'w', newline='') as output_file:
    #                         dict_writer = csv.DictWriter(output_file, keys)
    #                         dict_writer.writeheader()
    #                         dict_writer.writerows(self.lst) 
    #    return lst
    
# Print Dictionary
    def print_dict(self,dict):
        print('\n')
        print( "{:<15} {:<15}".format('Index','Menu'),'\n')
        for key, value in dict.items():
            print(key,' ',value,'\n')

# Write to JSON file:
    # def write_json(self,list,file_name):
        
    #     with open('F:\\Generation UK\\Generation_UK_Codefiles\\MIni_Project\\source\\'+ file_name +'.json','w') as json_file:
                            
    #                         json_string=json.dumps(list)
    #                         json_file.write(json_string)

    # def find(self,lst, key, value):
    #     for i, dic in enumerate(lst):
    #         if dic[key] == value:
    #             return i
    #     return -1
    
def main_menu():
    main_menu_options={
                    0: exit,
                    1:'Products_Menu',
                    2: 'Couriers Menu',
                    3: 'Orders Menu'
                                        }
    return main_menu_options

    
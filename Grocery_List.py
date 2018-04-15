#Personal Project on the side

master_list = []

def show_list():
    print('Listed grocery items you have entered.')
    for grocery in master_list:
           print(' ' + grocery)

def update_list():
    old_item = input('What would you like to update in the list?: ')
    updated_item = input('What should the item be?: ')
    for idx, item in enumerate(master_list):  # enumerating the items in a list so I can use thier index num. to find position of item I want to be replaced. 
        if item == old_item: # compares the items to be updated.
            master_list[idx] = updated_item

def delete_item():
    deleting_item = input('What would you like to be deleted from the list?: ')
    for idx, item in enumerate(master_list):
        if item == deleting_item:
            master_list.pop(idx)
            print('The item ' + deleting_item + ' has been removed from your list.')
        
while True:
   grocery = input('Please enter grocery item: ')

   if grocery.lower() == 'exit':
       show_list()
       break

   elif grocery.lower()== 'show':
       show_list()

   elif grocery.lower()== 'update':
       update_list()
       
   elif grocery.lower()== 'delete':
       delete_item()
    
   else:
       master_list = master_list +  [grocery]
       show_list()
           


# Update: Run a funct. that allows you to update a particular item on the list.
# Delete: Create funct. to delete item from (list command).
# Try to increase if else statements to take more commands (do elif statements that take commands) 
       

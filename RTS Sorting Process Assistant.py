### MODULES ###

import json
import datetime
import os


### FUNCTIONS ###

# open file and read file, return blank dictionary on failure
def read_file():
    try:
        with open(f"{current_user}_{current_time.year}_{current_time.month}_{current_time.day}", 'r') as file_object:
            return json.load(file_object)
    except FileNotFoundError:
        return {}

# dump dictionary data into file name format: "user_year_month_day"
def write_to_file(dictionary):
    try:
        with open(f"{current_user}_{current_time.year}_{current_time.month}_{current_time.day}", 'w') as file_object:
            json.dump(dictionary, file_object)
    except Exception as e:
        print("Could not write to file:", e)
    quit()

# introductory statement on program capabilities and RTS purpose
def display_introduction():
    print(
f'''
INTRODUCTION
Welcome, {current_user}, to the Return to Stock (RTS) Sorting Process Assistant. This application has been developed to provide guidance for sorting through RTS items, which can often appear as a confusing assortment of random and damaged goods. As an RTS role, our main goals are as follows:

- Returning items to appropriate locations within the warehouse, to be sold and retained permanently by end consumers.
- Serving as a form of quality control by separating products with quality issues from the main inventory.
- Communicating discrepancies between physical inventory and warehouse system inventory.
- Minimizing profit loss resulting from mishandled goods.
- Maintaining overall organization within the warehouse.

In addition to offering guidance for sorting through products, this application is also a tool to record information on damaged goods or overages. Press "Enter" to begin.
''')   
    return input('Press "Enter" to begin...')

def display_main_menu():
    print(
f'''
User: {current_user}

*** MAIN MENU ***
1. Item Sorting Guidance
2. Item Information Entry
3. Display Entries (Today)
4. Quit
''')

def clear_screen(persisting_display_message = ""):
    os.system('cls')
    if len(persisting_display_message) > 0:
        print(persisting_display_message, "\n")
        
# ITEM SORTING GUIDANCE FUNCTIONS 
def item_sorting_guidance():
    clear_screen("(ITEM SORTING GUIDANCE)")
    input('''Item Sorting Guidance is a series of yes or no questions, designed to help you make a decision on what should be done with an item. Enter "Y" if your answer is yes, or "N" for no.
Press "Enter" to begin...''')
    clear_screen("(ITEM SORTING GUIDANCE)")

    # is the item identifiable?
    # NO
    if check_item_identification() is False:
        clear_screen("(ITEM SORTING GUIDANCE)")
        print('ITEM IDENTIFICATION')
        input('''Let's start by identifying the item. Please bring the case, or a sample from the case into the office for identification. Press "Enter" once the item has been identified.''')
        
    # is the item a full case?
    # NO
    clear_screen("(ITEM SORTING GUIDANCE)")
    if check_full_case() is False:
        # move to disposal question
        quit()
    # YES
    else:
        
        # any quality issues?
        # YES
        clear_screen("(ITEM SORTING GUIDANCE)")
        if check_quality_issue() is True:
        # move to disposal question
            quit()
        # NO 
        else:

            # on inventory?
            # YES
            clear_screen("(ITEM SORTING GUIDANCE)") 
            if check_on_inventory() is True:
                clear_screen("(ITEM SORTING GUIDANCE)")
                result_return_to_stock()
            # NO
            else:
                # similar item available?
                # YES
                clear_screen("(ITEM SORTING GUIDANCE)")
                if check_similar_item() is True:
                    clear_screen("(ITEM SORTING GUIDANCE)")
                    result_identical_item_return_to_stock()                  
        
def get_user_choice():
    while True:
        user_choice = input('(Y/N)\n> ').upper().strip()
        if user_choice == 'Y':
            return True
        elif user_choice == 'N':
            return False
        else:
            print('Invalid input. Enter "Y" if your answer is yes, or "N" for no.')

def check_item_identification(): # is the item identifiable?
    print('ITEM IDENTIFICATION')
    print('Does the item have a label that clearly indicates the contents of the package?')
    user_choice = get_user_choice()
    return user_choice
        
def check_full_case(): # is the item a full case?
    print('FULL CASE?')
    print(
'''Is the item a full case, with none of the weight missing? This can often be determined from reading the packaging. Look for either a printed total weight, or how the item was packed, which we will call the "pack size".
Here are some examples of how this information may be printed:

Examples of pack sizes:
- 4x5 (4 bags, each bag weighing 5LBS)
- 10x2 (10 bags, each bag weighing 2LBS)
- 1x10 (a single, 10LB box, with nothing separating the contents)

If this information is not printed onto the packaging, the weight can be determined by weighing the item on a scale.
Is the item a full case?''')
    user_choice = get_user_choice()
    return user_choice

def check_quality_issue(): # any quality issues?
    print('QUALITY ISSUES?')
    print(
'''Let's examine the item for any quality issues. If the contents of the package or item are compromised in any way, the item should be kept separate from the main inventory to ensure food safety and customer satisfaction.

Examples of quality issues may include, but are not limited to:
- Bad smell
- Thawed and refrozen product
- Busted or torn packaging

If the box is damaged but the contents are intact, the item may be repackaged in a plain box with printed labels on all sides of the box. Expiration dates will not be a factor in quality issues when dealing with frozen goods, as freezing
can preserve items beyond their expiration date.

While you are encouraged to make your own judgement, you may also consult the office if you are unsure. Does this item have any quality issues?''')
    user_choice = get_user_choice()
    return user_choice

def check_on_inventory(): # is the item on inventory?
    print('ON INVENTORY?')
    print(
'''Is this item on inventory? We can verify this by searching for the item in the warehouse management system by searching by keyword.

- From the Seasoft main menu, press "F12". A small, white window will appear with a list of warehouse management options.
- Inside the window, select "Inventory Inquiry Lookup" and press "Enter".
- Inside the "Inventory Inquiry Lookup" window, click on the blank white space to the right of "Item Number". 
- Inside the "Item Number" space, we can enter keywords pertaining to the item, then press "F2" to find results. 

Being more broad with keyword choices will pull a larger list of items that may be relevant. For example, typing in simply "catfish" will return a large list of items, all related to catfish.
The opposite is also true. Entering more specific keywords will return a smaller, more concise list of items. For example, typing in "7 superior catfish" will only return a size that starts with "7", the brand "Superior", and items related to catfish.
It may take more than one keyword search to find the item you are looking for within Seasoft.

If the quantity of the item showing on hand is greater than 0, the item is on inventory. If the quantity is 0 or less, or you are unable to find the item, the item can be considered as not on inventory.
Is the item on inventory?''')
    user_choice = get_user_choice()
    return user_choice

def check_similar_item(): # is there a similar item on inventory?
    print("IDENTICAL ITEM AVAILABLE?")
    print('''Sometimes a certain brand of an item will not show on inventory. However, there may be another item available that is identical in all but the brand name. Identical items can be put together. For an item to be considered identical, 
all the following criteria must be met:
          
- Matching item type. For example - "Shrimp P&D Tail-on" (shrimp, peeled and deveined, with the tail still attached) can be put together with another "Shrimp P&D Tail-on". "Snapper Fillet Skin-on" can be put together
with another "Snapper Fillet Skin-on".
          
- Matching color. Shrimp, for example, are available in colors of white (W or WT), neutral (NU), and pink (A). 
          
- Matching item size. A "4/6oz Snapper Fillet" (snapper fillets that range from 4 ounces to 6 ounces) can be put together with another "4/6oz Snapper Fillet". A "4oz Snapper Fillet" can be put together with a 
"4/6oz Snapper Fillet" as it falls into the range of "4/6oz". If the information is not printed anywhere on the packaging, this can be determined by weighing the item on an ounce scale. 
          - Examples of item sizes:
          16/20 Shrimp = 16 to 20 individual shrimp per pound of shrimp
          3/4-1# Snapper Fillet = Snapper fillets that range from 3/4 of a pound to 1 pound
          
- Matching weight and pack size. Not only the weight must match, but also the pack size. A 10x2 (10 bags, each weighing 2LBS) case can be put with another brand of a 10x2 item, but a 4x5 (4 bags, each weighing 5LBS)
cannot be put together with a 10x2, even though the items both weigh 20LBS in total.
          
- Matching origin. Imported items (harvested outside of the U.S.) can be put together with other imported items. Domestic (harvested within the U.S.) items can be put together with other domestic items. The country the item originates from
is typically printed on the packaging.
          
Is there an identical item available?''')
    user_choice = get_user_choice()
    return user_choice

def result_return_to_stock():
    print('RESULT:')
    print('''The item should be returned to stock. Print a label for the item to be scanned into a location and put the item in the location. When returning items to stock,
the item you are returning and the item at the location must be the same. If you are unable to find a pallet of the item you are returning, the item may be scanned
into a location within the RTS area.''')

def result_identical_item_return_to_stock():
    print("RESULT:")
    print('''The item should be repackaged in a plain box with printed labels on all sides of the box and returned to stock. The label will match the item you are putting it with. For example,
a case of "Brand A Swai Fillets" can be repackaged, then attached with printed labels for "Brand B Swai Fillets", assuming the items are identical. The "Brand A Swai Fillet" will be sold as
"Brand B Swai Fillets".
''')



### MAIN PROGRAM ###
    
# change working directory to specified path
os.chdir(r"C:\Users\hoand\Desktop\RTS_Data")

# get current date and user name
current_time = datetime.datetime.now()
current_user = input("Enter your name:\n> ").title().strip()
clear_screen()


user_data = read_file()

display_introduction()
clear_screen()

display_main_menu()
user_choice = input('Enter a selection\n> ')

if user_choice == '1':
    item_sorting_guidance()




write_to_file(user_data)



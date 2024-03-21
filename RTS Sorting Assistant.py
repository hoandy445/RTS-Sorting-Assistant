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
Welcome, {current_user}, to the Return to Stock (RTS) Sorting Assistant. This application has been developed to provide guidance for sorting through RTS items, which can often appear as a confusing assortment of random and damaged goods. As an RTS role, our main goals are as follows:

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
        
def item_sorting_guidance():
    try:
        while True:
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
            # missing weight or quality issues?
            # YES
            clear_screen("(ITEM SORTING GUIDANCE)")
            if check_full_case() is False or check_quality_issue() is True:
                # should the item be disposed?
                # YES
                clear_screen("(ITEM SORTING GUIDANCE)")
                if check_disposal() is True:
                    clear_screen("(ITEM SORTING GUIDANCE)")
                    result_disposal()
                # NO 
                else:                    
                    # is the item a type of crustacean?
                    # YES
                    clear_screen("(ITEM SORTING GUIDANCE)")
                    if check_crustacean() is True:
                        clear_screen("(ITEM SORTING GUIDANCE)")
                        result_crustacean()                   
                    # NO
                    else:
                    # is the item crab meat cup(s)?
                        # YES
                        clear_screen("(ITEM SORTING GUIDANCE)")
                        if check_crab_meat_cups() is True:
                            clear_screen("(ITEM SORTING GUIDANCE)")
                            result_crab_meat_cups()
                        # NO
                        else:
                            # is the item head-on shrimp?
                            clear_screen("(ITEM SORTING GUIDANCE)")
                            # YES
                            if check_head_on_shrimp() is True:
                                clear_screen("(ITEM SORTING GUIDANCE)")
                                result_head_on_shrimp()
                            # NO 
                            else:
                                # is the item block-frozen shrimp?
                                clear_screen("(ITEM SORTING GUIDANCE)")
                                if check_block_shrimp() is True:
                                    clear_screen("(ITEM SORTING GUIDANCE)")
                                    result_block_shrimp()
                                # NO
                                else:                               
                                # is the item Type B?
                                    # YES
                                    clear_screen("(ITEM SORTING GUIDANCE)")
                                    if check_type_b() is True:
                                        clear_screen("(ITEM SORTING GUIDANCE)")
                                        result_type_b()
                                    # NO
                                    else:
                                        clear_screen("(ITEM SORTING GUIDANCE)")
                                        result_type_a()                
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
                    # NO
                    else:
                        clear_screen("(ITEM SORTING GUIDANCE)")
                        result_overage()

    except main_menu:
        clear_screen()                            
        
def get_user_choice():
    while True:
        user_choice = input('\n(Y/N)\n(M: Return to main menu)\n\n> ').upper().strip()
        if user_choice == 'Y':
            return True
        elif user_choice == 'N':
            return False
        elif user_choice == 'M':
            raise main_menu
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
'''Is the item a full case, with none of the weight missing? This can be determined from reading the packaging and ensuring none of the contents are missing. Look for either a printed total weight, or how the item was packed, which we will call the "pack size".
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
    clear_screen("(ITEM SORTING GUIDANCE)")
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
Conversely, entering more specific keywords will return a smaller, more concise list of items. For example, typing in "7 superior catfish" will only return a size that starts with "7", the brand "Superior", and items related to catfish.
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

def check_disposal(): # should the item be thrown away?
    print("DISPOSAL")
    print('''When assessing whether an item should be disposed of, you wiil need to use your senses to make the judgement. Here are some clues that an item may need to be thrown away:

- Smell. Trust your nose. While seafood often has a distinct "fishy" odor, spoiled food emits a stronger, foul smell of rot or chemicals. 

- Freezer burn. Freezer burn is characterized by dry, grayish-brown spots cause by air reaching the surface of the food. Freezer burn is not harmful, but is unattractive to customers and not appealing to eat. 
An item lightly freezer burned may be resold, but an item that is badly freezer burned cannot.

- Thawed and refrozen. This is due to improper storage. Some indicators that an item may include:
  - An item that was originally "IQF" (Individually Quick-Frozen), but has turned into a solid block
  - Liquids or juices that have frozen and dried on the packaging or leaked onto other items

Do any of these qualities apply to the item?
''')
    user_choice = get_user_choice()
    return user_choice
    
def check_crustacean(): # is it a crustacean?
    print('CRUSTACEAN?')
    print('''Is this item a damaged case of any crustacean type? This includes snow crab legs, king crab legs, Jonah crab claws, lobster tails, whole lobster, Dungeness crab legs, etc. 
This does not include cups of any type of crab meat (cocktail fingers, clawmeat, and lump crabmeat) or stuffed crabs. ''')
    user_choice = get_user_choice()
    return user_choice

def check_crab_meat_cups(): # is it crab meat cups?
    print('CRAB MEAT CUPS?')
    print('''Is the item crab meat cup(s? These items are packaged in 1LB plastic cups, and include cocktail fingers, claw meat, and lump crab meat.''')
    user_choice = get_user_choice()
    return user_choice

def check_head_on_shrimp(): # is it head-on shrimp?
    print('DISCOLORED HEAD-ON SHRIMP?')
    print('''Head-on shrimp is, as the name implies, shell-on shrimp with the head still attached. Shrimp are harvested in colors of white, neutral (brown), and pink. After harvesting, shrimp will begin to darken in color due
to an enzymatic process that causes oxidation. This is similar to how the inside of an apple might darken after being cut. Darkened shrimp are not harmful, but is unattractive to consumers.

Is this item head-on shrimp that has darkened in color?''')
    user_choice = get_user_choice()
    return user_choice

def check_block_shrimp(): # is it block-frozen shrimp?
    print('BLOCK SHRIMP?')
    print('''Is this item block-frozen shrimp? These items are rectangular blocks of shrimp, typically packaged in cardboard cartons.''')
    user_choice = get_user_choice()
    return user_choice

def check_type_b(): # are the contents of the item edible, but damaged?
    print("TYPE B ITEM?")
    print('''Examine the item for the following qualities:

- Damaged bags
- Loose contents, such as shrimp or fish that have left its packaging and been exposed to air
          
Do these qualities describe the item?''')
    user_choice = get_user_choice()
    return user_choice

def result_return_to_stock():
    print('RESULT:')
    print('''The item should be returned to stock. Print a label for the item to be scanned into a location and put the item an appropriate location. When returning items to stock,
the item you are returning and the item at the location must be the same. If you are unable to find a pallet of the item you are returning, the item should be scanned
into a location within the RTS area.''')
    
    input('\nInput "Enter" to restart Item Sorting Guidance...')

def result_identical_item_return_to_stock():
    print("RESULT:")
    print('''The item should be repackaged in a plain box with printed labels on all sides of the box and returned to stock. The label will match the item you are putting it with. For example,
a case of "Brand A Swai Fillets" can be repackaged, then attached with printed labels for "Brand B Swai Fillets", assuming the items are identical. The "Brand A Swai Fillet" will be sold as
"Brand B Swai Fillets".
          
When returning items to stock, the item you are returning and the item at the location must be the same. If you are unable to find a pallet of the item you are returning, the item should be scanned
into a location within the RTS area.
''')
    
    input('\nPress "Enter" to restart Item Sorting Guidance...')

def result_overage(): ### add prompt to record information
    print("RESULT:")
    print('''The item is an overage. An overage is a discrepancy - a difference, between the warehouse management system inventory and physical inventory. We physically have the item, but it is not accounted for in the system inventory. 

Label the item as "overage" (this can be handwritten on a sticker) and put the item on an overage pallet. An overage pallet can be found on the floor within the RTS area. Once an overage pallet reaches bin height, it should be wrapped, labeled 
as "OVERAGE" and inbounded (slotted into a bin) within the RTS area.''')
    
    input('\nPress "Enter" to restart Item Sorting Guidance...')

def result_disposal():
    print('RESULT:')
    print('''The item should be disposed. It is not safe to eat, and or not resellable.  If the item is not on inventory, it can be dumped into a waste vat (large, cube-shaped tub), or directly into the dumpster.
If the item is on inventory, notify the office before disposal.''')
    input('\nPress "Enter" to restart Item Sorting Guidance...')

def result_crustacean(): # type C item
    print('RESULT:')
    print('''This item should be labeled "C" (this can be handwritten on a sticker) and put together on a pallet with other type "C" items. Crustacean type items are generally high value. Because these type C items are damaged, we must separate
them from the main inventory as they cannot be sold for their original value, but can be sold to willing consumers for a percentage of their original value to recover some of the cost.

Ensure the following information is clearly labeled on the box (if applicable). This will only be necessary if the original label is not attached:
- Size (4/UP, 5/8 etc.)
- Type of food (lobster, snow crab, etc.)
- The way the food has been processed (legs, tail, etc.)
- Country of origin
- Brand name
- Total weight
[ Example of item label: 4/UP Snow Crab Legs Canada OCI 25# ]    

A type C pallet can be found on the floor of the RTS area. If there is no type C pallet on the floor, a new type C pallet can be started. Once a type C pallet reaches bin height, the pallet should be labeled "Type C", then inbounded (slotted into a bin) in the RTS area.''')
    
    input('\nPress "Enter" to restart Item Sorting Guidance...')

def result_head_on_shrimp(): # type P item
    print('RESULT:')
    print('''This item should be labeled "P" (this can be handwritten on a sticker) and put together on a pallet with other type "P" items. Because the head-on shrimp are too discolored to be accepted by customers, we are separating it from
the main inventory. These type P pallets will be sent to a "peeling plant" to be peeled, repackaged, and returned to the warehouse in a state that is sellable.
          
A type P pallet can be found on the floor of the RTS area. If there is no type P pallet on the floor, a new type P pallet can be started. Once a type P pallet reaches bin height, the pallet should be labeled "Type P", then inbounded (slotted into a bin) in the RTS area.''')
    
    input('\nPress "Enter" to restart Item Sorting Guidance...')

def result_crab_meat_cups(): # type F item; result needs changed when re-cupping is possible
    print('RESULT:')
    print('''This item should be put into a box and labeled "F" (this can be handwritten on a sticker) and put together on a pallet with other type "F" items. The warehouse currently does not have the supplies to re-cup these items and return them to stock, and so
will be held in the RTS area until supplies are ordered.
          
A type F pallet can be found on the floor of the RTS area. If there is no type F pallet on the floor, a new type F pallet can be started. Once a type F pallet reaches bin height, the pallet should be labeled "Type F", then inbounded (slotted into a bin) in the RTS area.''')
    
    input('\nPress "Enter" to restart Item Sorting Guidance...')    

def result_block_shrimp():
    print('RESULT:')
    print('''This item and its contents should be put into a vat (large, cube-shaped tub) that contains other block shrimp cartons. Block shrimp are generally only sold by the case, and not sold by the piece (individual cartons). These block shrimp vats
are shipped out periodically to a "peeling plant", where the shrimp are reprocessed and repackaged, then returned to the warehouse in a sellable condition.
          
Block shrimp vats can be found in the RTS area. If all current vats are filled, or there are no vats, place the contents of the item into an empty vat. Move this vat to the RTS area.''')
    
    input('\nPress "Enter" to restart Item Sorting Guidance...')
    
def result_type_b(): # checking for busted bags, loose food
    print('RESULT:')
    print('''This item should be put into a box and labeled "B" (this can be handwritten on a sticker) and put together on a pallet with other type "B" items. 

Ensure the following information is clearly labeled on the box (if applicable). This will only be necessary if the original label is not attached:
- Size (4oz, 4/6oz, 2/4LB, 16/20, etc.)
- Type of food (shrimp, catfish, flounder, chicken, etc.)
- The way the food has been processed (fillet, tail-on, headless, wing, etc.)
- Color (white, neutral, pink, scarlet, crimson, etc.)
- Country of origin
- How the item is packaged (IQF, IVP, IWP, etc.)
- Brand name
- Total weight
[ Example of item label: 31/35 Shrimp P&D Tail-off White Ecuador IQF Vanoni 7# ]          
          
The item is in poor condition, likely due to mishandling, and must be kept separate from the main inventory. Type B items will be sold to willing customers at a heavily discounted price, or potentially disposed of in the future.
        
A type B pallet can be found on the floor of the RTS area. If there is no type B pallet on the floor, a new type B pallet can be started. Once a type B pallet reaches bin height, the pallet should be labeled "Type B", then inbounded (slotted into a bin) in the RTS area.''')

    input('\nPress "Enter" to restart Item Sorting Guidance...')

def result_type_a(): # item is good quality
    print('RESULT:')
    print('''This item should be put into a box and labeled "A" (this can be handwritten on a sticker) and put together on a pallet with other type "A" items. 

Ensure the following information is clearly labeled on the box (if applicable). This will only be necessary if the original label is not attached:
- Size (4oz, 4/6oz, 2/4LB, 16/20, etc.)
- Type of food (shrimp, catfish, flounder, chicken, etc.)
- The way the food has been processed (fillet, tail-on, headless, wing, etc.)
- Color (white, neutral, pink, scarlet, crimson, etc.)
- Country of origin
- How the item is packaged (IQF, IVP, IWP, etc.)
- Brand name
- Pack size (4X5LB, 1x10LB, etc.) or total weight if not applicable
[ Example of item label: 31/35 Shrimp P&D Tail-off White Ecuador IQF Vanoni 4x2# ]

The item is in acceptable condition, but cannot be sold for its full value as it is likely not a full case, and so must be kept from the main inventory. Type A items will be sold to willing customers at cost, or a slightly discounted price.
          
A type A pallet can be found on the floor of the RTS area. If there is no type A pallet on the floor, a new type A pallet can be started. Once a type A pallet reaches bin height, the pallet should be labeled "Type A", then inbounded (slotted into a bin) in the RTS area.''')
    
    input('\nPress "Enter" to restart Item Sorting Guidance...')






### MAIN PROGRAM ###
    
# change working directory to specified path
os.chdir(r"C:\Users\hoand\Desktop\RTS_Data")

# used to return to main menu
class main_menu(Exception): pass

# get current date and user name
current_time = datetime.datetime.now()
current_user = input("Enter your name:\n> ").title().strip()
clear_screen()


user_data = read_file()


display_introduction()
clear_screen()

while True:
    display_main_menu()
    user_choice = input('Enter a selection\n> ')

    if user_choice == '1':
        item_sorting_guidance()
    elif user_choice =='4':
        break




write_to_file(user_data)



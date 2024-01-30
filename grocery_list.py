import json


def main():
    with open('grocery_list.txt', 'r', encoding="utf-8") as grocery_list_file:
        grocery_list = json.load(grocery_list_file)

    mode = 'Yes'

    while mode == 'Yes':
        mode = get_mode()

        if mode == 'View':
            view_item(grocery_list)
        elif mode == 'Add/Update':
            update_item(grocery_list)
        else:
            delete_item(grocery_list)

        mode = input('Switch to other mode? (Yes / No)')

        if (mode == 'y' or mode == 'Y' or mode == 'yes' or mode == 'Yes'):
            mode = 'Yes'
        else:
            break

    with open('grocery_list.txt', 'w', encoding="utf-8") as grocery_list_file:
        json.dump(grocery_list, grocery_list_file, sort_keys=True, indent=4)


def get_mode():
    mode_list = {1: 'View', 2: 'Add/Update', 3: 'Delete'}

    while True:
        try:
            user_input = int(input('Please choose a mode:\n1 View\n2 Add/Update\n3 Delete\n'))

            if user_input in mode_list.keys():
                print(f'Current mode: {mode_list[user_input]}')
                return mode_list[user_input]

            else:
                print('Not a valid mode. Please choose again.')

        except:
            print('Not a valid mode. Please choose again.')


def view_item(grocery_list):
    print(grocery_list)


def update_item(grocery_list):
    item = input('What item do you want to add/update?').capitalize()
    quantity = input('How many do you want to buy?')
    grocery_list.update({item: quantity})
    print('Updated.')
    return grocery_list


def delete_item(grocery_list):
    try:
        item = input('What item do you want to delete?').capitalize()
        del grocery_list[item]
        return grocery_list

    except:
        print('Item not found.')
        return


if __name__ == '__main__':
    main()
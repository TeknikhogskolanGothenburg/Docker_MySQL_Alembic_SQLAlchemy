from Controllers.customers_controller import get_all_customers, get_customer_by_id, get_customer_by_name, store_changes, \
    store_new_first_name


def customers_menu():
    while True:
        print("Customers Menu")
        print("==============")
        print("1. View All Customers")
        print("2. View Customer by Id")
        print("3. Find Customers by Name")

        print("5. Quit Customers Menu")

        selection = input("> ")

        if selection == "1":
            customers = get_all_customers()
            for customer in customers:
                print(customer)
        elif selection == "2":
            id = input("Enter Customer Id: ")
            customer = get_customer_by_id(id)
            if customer:
                print(customer)
            else:
                print("Could not find customer with id ", id)
        elif selection == "3":
            pattern = input("Enter full or partial customer name: ")
            customers = get_customer_by_name(pattern)
            for key, customer in customers.items():
                print(f'{key}. {customer}')

            edit_selection = input("Enter number for customer to edit: ")
            edit_selection = int(edit_selection)

            customer = customers[edit_selection]
            print(f'1. Customer Name: {customer.customerName}')
            print(f'2. Contact First Name: {customer.contactFirstName}')
            print(f'3. Contact Last Name: {customer.contactLastName}')
            print(f'4. Phone: {customer.phone}')
            print(f'5. Address Line 1: {customer.addressLine1}')
            print(f'6. Address Line 2: {customer.addressLine2}')
            print(f'7. City: {customer.city}')
            print(f'8. State: {customer.state}')
            print(f'9. Postal Code: {customer.postalCode}')
            print(f'10. Country: {customer.country}')

            line = input("Enter number for what line to edit: ")
            if line == "2":
                new_value = input("Enter new First Name: ")
                store_new_first_name(customer, new_value)
        else:
            break
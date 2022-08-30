import PySimpleGUI as sg
import csv

import main


def menu_window():
    main_layout = [
        [sg.Text("Welcome to Product Control Center!\nChoose what you'd like to do:", font=("Arial", 12))],
        [sg.Button("Show product list")],
        [sg.Button("Exit")]
    ]

    window = sg.Window("Product Control Center", main_layout)

    while True:
        event, values = window.read()

        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        elif event == "Show product list":
            product_list_window()

    window.close()


def product_list_window():
    data = []
    header_list = []
    filename = "products.csv"
    if filename is not None:
        with open(filename, "r") as infile:
            reader = csv.reader(infile)
            header_list = next(reader)
            data = list(reader)
    sg.set_options(element_padding=(0, 0))

    list_layout = [[sg.Text("List of your products:", font=("Arial", 12))],
                   [sg.Table(values=data,
                             headings=header_list,
                             alternating_row_color='lightblue',
                             num_rows=32,
                             auto_size_columns=True,
                             size=(300, 300),
                             display_row_numbers=True,
                             col_widths=50,
                             enable_events=True,
                             key="CONTACT")],
                   [sg.Button("Add a product")],
                   [sg.Button("Change values (click desired product first)")],
                   [sg.Button("To main menu")]
                   ]
    window_list = sg.Window("Product Control Center", list_layout, size=(250, 465))
    click = False
    while True:
        event, values = window_list.read()

        if event == "To main menu":
            break
        elif event == sg.WIN_CLOSED:
            break
        elif event == "Change values (click desired product first)":
            prod_id = values["CONTACT"]
            window_list.close()
            change_value(prod_id)

        elif event == "Add a product":
            window_list.close()
            add_product_window()
            break

    window_list.close()


def add_product_window():
    add_layout = [
        [sg.Text("Enter product name"), sg.Input(key='NAME', do_not_clear=True, size=(20, 1))],
        [sg.Text("Enter product quantity"), sg.Input(key='QUANTITY', do_not_clear=True, size=(20, 1))],
        [sg.Text("Enter product price"), sg.Input(key='PRICE', do_not_clear=True, size=(20, 1))],
        [sg.Button("Add a product")],
        [sg.Button("To product list")]
    ]

    window_add = sg.Window("Product Control Center", add_layout, size=(800, 450))
    while True:
        event, values = window_add.read()
        name = values['NAME']
        quantity = values['QUANTITY']
        price = values['PRICE']
        if event == "To product list":
            window_add.close()
            product_list_window()
            break
        elif event == sg.WIN_CLOSED:
            break
        elif event == "Add a product":
            main.add_new_product(name, quantity, price)
            window_add.close()
            product_list_window()
            break

    window_add.close()


def change_value(prod_id):
    change_layout = [
        [sg.Text("ID of chosen product: " + str(prod_id))],
        [sg.Text("Enter product name"), sg.Input(key='NAME2', do_not_clear=True, size=(20, 1))],
        [sg.Text("Enter product quantity"), sg.Input(key='QUANTITY2', do_not_clear=True, size=(20, 1))],
        [sg.Text("Enter product price"), sg.Input(key='PRICE2', do_not_clear=True, size=(20, 1))],
        [sg.Button("Change value")],
        [sg.Button("To product list")]
    ]

    window_change = sg.Window("Product Control Center", change_layout, size=(800, 450))

    while True:
        event, values = window_change.read()
        name = values['NAME2']
        quantity = values['QUANTITY2']
        price = values['PRICE2']
        if event == "To product list":
            window_change.close()
            product_list_window()
            break
        elif event == sg.WIN_CLOSED:
            break
        elif event == "Change value":
            main.change_values(name, quantity, price, prod_id)
            window_change.close()
            product_list_window()
            break

    window_change.close()

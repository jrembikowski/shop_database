import csv
from csv import writer
import pandas as pd


def change_values(name, quantity, price, prod_id):
    file = open("products.csv", "r")
    product_data = list(csv.DictReader(file, delimiter=","))
    file.close()
    data = pd.DataFrame(product_data)
    data
    df = pd.read_csv("products.csv")
    new_value = [name, quantity, price]
    df.loc[prod_id] = new_value
    df.to_csv("products.csv", index=False)


def add_new_product(name, quantity, price):

    new_prod = [name, quantity, price]

    with open('products.csv', 'a+') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(new_prod)
        f_object.close()




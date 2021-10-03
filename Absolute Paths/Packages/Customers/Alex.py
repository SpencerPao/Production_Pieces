"""Customer Alex inquiry"""

from Packages.Supermarkets import Costco, CVS, Walmart
import pandas as pd


def inquiry_store():
    Costco.costco_info()
    CVS.cvs_info()
    Walmart.walmart_info()


def get_receipt(receipt_address: str):
    file = pd.read_csv(receipt_address, delimiter=",")
    file.index = ["Money (USD)"]
    print(file)

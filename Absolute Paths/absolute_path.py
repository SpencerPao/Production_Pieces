"""A demonstration on absolute pathways in python."""
import yaml
from Packages.Customers import Alex


with open('configs/file_address.yaml') as f:
    my_dict = yaml.safe_load(f)


def main():
    with open(my_dict['file_address']) as f:
        lines = f.readlines()
    print(lines)
    print("Alex line")
    Alex.inquiry_store()
    Alex.get_receipt(my_dict['receipt_addres'])


if __name__ == '__main__':
    main()

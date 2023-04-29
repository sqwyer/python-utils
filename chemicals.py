from utils.csv_util import csv_to_list
from utils.list_util import find

chemical = input("CHEMICAL NAME: ")
chems = csv_to_list("chemicals.csv")
found_chemical = find(chems, lambda s: s.Name == chemical)
print(found_chemical)
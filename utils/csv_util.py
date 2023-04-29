import csv
# import list_util

def csv_to_list(file: str) -> list:
    headers = []
    result = []
    n = 0
    with open(file, newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        for line in csv_reader:
            if n == 0:
                for header in line:
                    headers.append(header)
            else:
                kn = 0
                current = {}
                for key in line:
                    current[headers[kn]] = key
                    kn+=1
                result.append(current)
            n += 1
        return result

# arr = csv_to_list("chemicals.csv")
# found = list_util.find(arr, lambda item: item["ChemicalFormula"] == "NaCl")
# print(found)
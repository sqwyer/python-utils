def find(arr, match):
    result = None
    for item in arr:
        if match(item):
            result = item
    return result
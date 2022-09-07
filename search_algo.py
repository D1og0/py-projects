arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = 10
element_to_be_searched = 10

def search_element(arr, length, element):
    for i in range(length):
        if arr[i] == element:
            return True

    return False


if search_element(arr, n, element_to_be_searched):
	print(element_to_be_searched, "is found")
else:
	print(element_to_be_searched, "is not found")
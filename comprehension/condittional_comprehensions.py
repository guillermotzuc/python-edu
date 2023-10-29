#condittional comprehensions
def old_find_usable_data(data_list):
    temp = []
    for datum in data_list:
        if datum > 90 and datum % 2 == 0:
            temp.append(datum)
        else:
            temp.append(-100)
    return temp

# before the for is part of the value, at the end its if we should include the value
def find_usable_data(data_list):
    #return [datum for datum in data_list if datum > 90]
    return [datum if datum > 90 and datum % 2 == 0 else -100 for datum in data_list ]

if __name__ == "__main__":
    data_list = [1,2,90,91,93,94]
    print(find_usable_data(data_list) == old_find_usable_data(data_list))
def old_calculate_value(data_list, divisors_list):
    temp=[]
    for datum in data_list:
        for divisor in divisors_list:
            temp.append(datum / divisor)
    return temp
        
def calculate_value(data_list, divisors_list):
    return [datum / divisor for datum in data_list for divisor in divisors_list]

if __name__ == "__main__":
    data_list = [1,2,3,4,5]
    divisor_list = [20,21,22]
    print(calculate_value(data_list, divisor_list) == old_calculate_value(data_list, divisor_list))

        
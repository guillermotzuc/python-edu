from unittest import result


def corrected_value(value):
    return value * 32

if __name__ == "__main__":
    data_list = [1,2,3]
    old_results = map(corrected_value, data_list)
    results = [corrected_value(datum) for datum in data_list]
    print(list(results) == results)

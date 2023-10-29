from math import cos, radians

def cos_correction(value, angle):
    return value * cos(radians(angle))

def old_adjust_for_angle(data_list):
    temp = []
    for datum in data_list:
        for j in [0, 15, 30, 45, 60, 90]:
            temp.append(cos_correction(datum, j))
    return temp

def adjust_for_angle(data_list):
    return [datum * cos(radians(angle)) for datum in data_list for angle in [0, 15, 30, 45, 60, 90]] 

if __name__ == "__main__":
    data_list = [5, 10, 15]
    print(old_adjust_for_angle(data_list) == adjust_for_angle(data_list))
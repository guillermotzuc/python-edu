# for loop

#float_list = []

#For I in range(100):
#	float_list.append(I*100.0)

# List comprehensions
#float_list = [I*100.0 for I in range(100)]


#float_dict = {}

#for i in range(10):
#    float_dict[i] = i * 100.0

# dictionary comprehension
#float_dict = {i:i*100.0 for i in range(10)}

def old_saturation_levels(data_dict):
    temp = {}
    for key, value in data_dict.items():
        temp[key] = (value**3)/(2**value)
    return temp

def saturation_levels(data_dict):
    return { k:v**3/2**v for k,v in data_dict.items() }

if __name__ == "__main__":
    hydration_levels = { "arc1" : 23, "arc2" : 64, "arc3": 104 }
    print(old_saturation_levels(hydration_levels) == saturation_levels(hydration_levels))

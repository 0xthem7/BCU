def create_list():
    '''Function that takes no input and returns a list'''
    data =  ['Playstation','Xbox', 'Steam', 'iOS', 'Google Play']
    return data

def get_info(my_list):
    data = (my_list[0], my_list[-2], len(my_list))
    return data
    

def get_partial(my_list):
    data = [my_list[1], my_list[2], my_list[3]]
    return data

def get_last_three(my_list):
    data = []
    for i in range(1,4):
        data.append(my_list[-i])
    return data 

def double_list(my_list):
    data = my_list + my_list
    return data

def amend(my_list):
    my_list[1] = 'None'
    my_list[-2] = 'Bye'
    return my_list


if __name__ == "__main__":
    test_list = create_list()
    print(test_list)
    print(get_info(test_list))
    print(get_partial(test_list))
    print(double_list(test_list))
    print(amend(test_list))

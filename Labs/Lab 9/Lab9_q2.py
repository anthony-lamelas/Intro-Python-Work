def is_impostor(information, corrupter_function):

    lst = corrupter_function(information)

    deep = lst is not information and lst == information
    
    return deep






import super_secret_module
def main():
    original_list = [1, 2, 3]
    print(is_impostor(original_list, super_secret_module.corrupter))
    
main()
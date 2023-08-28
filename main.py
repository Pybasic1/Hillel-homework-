'''Lesson6'''

'''task1'''
def merge_tuples_to_dict(keys, values):
    result_dict = {keys[i]: values[i] for i in range(len(keys))}
    return result_dict

coin = ('Bitcoin', 'Ether', 'Ripple', 'Litecoin')
code = ('BTC', 'ETH', 'XRP', 'LTC')

merged_dict = merge_tuples_to_dict(coin, code)
print(merged_dict)

'''task2-не смог разобраться(('''

'''task3'''
def list_to_dict(lst):
    result_dict = {index: value for index, value in enumerate(lst)}
    return result_dict

input_list = ['a', 'b', 'c', 'd', 'e']

output_dict = list_to_dict(input_list)
print(output_dict)

'''task4'''
import time

def countdown_decorator(func):
    def wrapper():
        for i in range(3, 0, -1):
            print(i)
            time.sleep(1)
        return func()
    return wrapper

@countdown_decorator
def what_time_is_it_now():
    current_time = time.strftime('%H:%M')
    return current_time

result = what_time_is_it_now()
print(result)
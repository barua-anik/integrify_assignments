#Find the missing number

def missing_numbers(num_list):
      original_list = [x for x in range(num_list[0], num_list[-1] + 1)]
      num_list = set(num_list)
      return (list(num_list ^ set(original_list)))

print("Missing number:", missing_numbers([1,2,3,5]))

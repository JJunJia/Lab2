
def main():
  print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
  display_main_menu()
  num_list = get_user_input()
  average=calc_average(num_list)
  min_max=calc_min_max_temperature(num_list)
  print(average)
  print("Minimum & Maximum temperature is ")
  print(min_max)
  

def display_main_menu():
    print("Enter some numbers separated by commas")

def get_user_input():
  numbers=input("Enter your numbers:")
  x = [float(value) for value in numbers.split(", ")]
  return x

def calc_average(num_list):
 print("calc_average")
 countave=sum(num_list)/len(num_list)
 return countave

def calc_min_max_temperature(num_list):
  countmin_max=[min(num_list),max(num_list)]
  return countmin_max

if __name__ == "__main__":
 main()

 

def main():
  print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
  display_main_menu()
  num_list = get_user_input()
  average=calc_average(num_list)
  min_max=calc_min_max_temperature(num_list)
  ascending=sort_temperature(num_list)
  median=calc_median_temperature(ascending)
  print("Minimum & Maximum temperature is ")
  print(min_max)
  print(ascending)
  print("Average is")
  print (average)
  print("Median is ")
  print(median)
  

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

def sort_temperature(num_list):
  num_list.sort()
  return num_list

def calc_median_temperature(ascending):
  median_position=int((len(ascending)+1)/2)
  if len(ascending)%2!=0: 
    return(ascending[median_position-1])
  elif len(ascending)%2==0:
    eveno=(ascending[median_position-1] + ascending[median_position])/2
    return(eveno)
  
if __name__ == "__main__":
 main()

 
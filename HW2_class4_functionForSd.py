import statistics
import math



def my_sd_function(ls):
    sq = 0
    for i in ls:
        sq += (i - statistics.mean((ls)))**2
    div = math.sqrt(sq/(len(ls)-1))
    return div

my_list = [1,2,3]
my_list2 = range(1,11)
my_list3 = range(1,101)
print(my_sd_function(my_list3))




        
    

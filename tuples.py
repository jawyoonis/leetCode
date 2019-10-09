survey1= (12, "jamalito", "Somali")
age, name, country_of_origin= survey1
print("age=", age)
print("name=", name)
print("country of origin=", country_of_origin)
import timeit

list_time= timeit.timeit(stmt="[1,2,3,4,5]", number=1000000)

tuble_time= timeit.timeit(stmt="(1,2,3,4,5)", number=1000000)


print("tubple time:", tuble_time)
print("list_time :", list_time)







import sys 

print(sys.getsizeof([1,2,2,3,3,4]))





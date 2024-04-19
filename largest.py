def find_largest_elements(lst,n):
    sorted_list=sorted(lst,reverse=True)
    largest_elements=sorted_list[:n]
    return largest_elements 
numbers=[30,10,45,5,20,50,15,3,345,54,87,98,100,34]
N=int(input("how many you want"))
result=find_largest_elements(numbers,N)
print(f"the{N}largest elements in the list are :",result)
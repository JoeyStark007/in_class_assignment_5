#Problem 1. Sort With Quicksort.
# Please build a function called "quicksort" that uses recursion to define the quicksort algorithm for a list of any length. 
# Build a main script that reads in the list provided, "numbers.txt", and runs it through your quicksort algorithm. 
# The main script should return the finished sorted list as "sorted.txt"
# All 3 files "In_class_assignment_5.py", "numbers.txt", and "sorted.txt" should all be added to your github repository and submitted as a github link.


'''Info on Quicksort Algorithm: 
The Quicksort algorithm is an efficient sorting algorithm developed by British computer scientist Tony Hoare in 1959.

Quicksort is a divide-and-conquer algorithm. Suppose you have a list of objects to sort. You start by choosing an item in the list, called the *pivot item*. 
This can be any item in the list. You then partition the list into two sublists based on the pivot item and recursively sort the sublists.

The steps of the algorithm are as follows:

1. Choose the pivot item.
2. Partition the list into two sublists:
        Those items that are less than the pivot item
        Those items that are greater than the pivot item
3. Quicksort the sublists recursively.
4. Each partitioning produces smaller sublists, so the algorithm is reductive. 

The base cases occur when the sublists are either empty or have one element, as these are inherently sorted. 
 '''


def quicksort(numbers_in_a_list):

#WRITE YOUR CODE HERE FOR THE RECURSIVE SORTING FUNCTION

    # Base
    
    if len(numbers_in_a_list) <= 1:
        return numbers_in_a_list
   
    
   #sublists
    list_A = numbers_in_a_list[0:len(numbers_in_a_list) // 2]
    list_B = numbers_in_a_list[len(numbers_in_a_list) // 2:]
    
    #Recursive sublists
    part1 = quicksort(list_A)
    part2 = quicksort(list_B)
    
    # Sorting and merging two sublists
    sorted_list = sort_two_list(part1, part2)
    return sorted_list

def sort_two_list(list_A, list_B):
    merged_list = []
    x = 0
    y = 0
    while x < len(list_A) and y < len(list_B):
        if list_A[x] <= list_B[y]:
            merged_list.append(list_A[x])
            x += 1
            continue
        merged_list.append(list_B[y])
        y += 1

    while x < len(list_A):
        merged_list.append(list_A[x])
        x = x + 1
        
    while y < len(list_B):
        merged_list.append(list_B[y])
        y = y + 1
        
    return merged_list
  
    
def main():

# WRITE YOUR MAIN FUNCTION HERE TO READ IN YOUR numbers.txt FILE, RUN THE LIST THROUGH YOUR SORTING ALGORITHM, 
# AND WRITE OUT YOUR FILE


    #read file
    numbers = 'numbers.txt'
    
    my_file = open(numbers, 'r')
    content = my_file.read()
    
    #rearrange file into a list of ints
    adj_content = content.strip('[]')
    
    content_list = adj_content.split(",")
    my_file.close()
    
    fixed_list = [eval(i) for i in content_list]
    
    #run function on list of ints 
    final = quicksort(fixed_list) 
        
   
    
    
    
    #Turn result into output file aka write a file 
    
    file_name = 'sorted.txt'
    with open(file_name, 'w') as file_object:
        return file_object.write(str(final))
            



if __name__ == "__main__":
    main()

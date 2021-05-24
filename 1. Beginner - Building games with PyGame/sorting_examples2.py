# Sample Python/Pygame Programs
# Simpson College Computer Science
# http://programarcadegames.com/
# http://simpson.edu/computer-science/

import random

# The selection sort
def selection_sort(list):
    # Loop through the entire array
    for curPos in range( len(list) ):
        # Find the position that has the smallest number
        # Start with the current position
        minPos = curPos
        # Scan left
        for scanPos in range(curPos+1, len(list) ):
            # Is this position smallest?
            if list[scanPos] < list[minPos]:
                # It is, mark this position as the smallest
                minPos = scanPos
        
        # Swap the two values
        temp = list[minPos]
        list[minPos] = list[curPos]
        list[curPos] = temp

def insertion_sort(list):
    print_list2(list,0)
    for j in range(1, len(list)):
        key = list[j]
        i = j - 1
        while (i >=0) and (list[i] > key):
            list[i+1] = list[i]
            print("node%d:f%d -> node%d:f%d [color=blue];" % (j-1,i,j,i+1))
            i = i - 1
        list[i+1] = key
        print_list2(list,j)
        if( j != len(list )-1):
            for k in range(len(list)):
                print("node%d:f%d -> node%d:f%d [style=invis];" % (j,k,j+1,k))
        print("node%d:f%d -> node%d:f%d [color=red];" % (j-1,j,j,i+1))
        
# This will point out a list
def print_list(list):
    for item in list:
        print( "%3d" % item,end="" )
    print()

def print_list2(list,step):
    print("node%d [ label = \"" % step,end="")
    
    for i in range(len(list)):
        if i != 0:
            print ("| ",end="")
        print("<f%d> %d" % (i,list[i]),end="")
    print ("\"];")
    
# Create a list of random numbers
list = []
for i in range(10):
    list.append(random.randrange(100))

# Try out the sort
#print_list(list)
print("""digraph G
{
        node [shape = record];""")
insertion_sort(list)        
#print_list(list)
print("}",end="")
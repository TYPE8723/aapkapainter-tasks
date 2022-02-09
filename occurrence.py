import re
l1 = input('enter the list : ').replace('[','').replace(']','').replace(' ','')# format of list entry->[1,2,3,2,1].alphabets,whitespace,'[],' will be excluded.
l3 = l1.split(',')#convert given input to list
l2 = []# empty list to store filtered input
for i in l3:
    try:#exception to clear out non numeric numbers
       val = int(i) #check wether the element is a list.if a non numeric element is found it will be skipped
       l2.append(val)# if element is number it will be added to a new list l2
       if val in l2:# checks wether the element is present in the list or not
           if l2.count(val) == 2:#checks wether the count of element is greater than 1 or is equal to 2.if its equal to 2 it means that a duplicate is found
               print(val)
               del(l2)#stops looping to find next duplicate
    except:
        continue#if a non numeric element is found it skips this check and moves to another

try:
    if l2:# if list has no duplicates, the new list wont be deleted.
        print('no duplication found')
except:
    print()


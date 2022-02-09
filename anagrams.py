x = input('enter two string to check anagram : ')#input: mary army
l = x.split(' ')#splitting first string to list
l1 = sorted(l[0].lower())#taking out first element and sorting
l2 = sorted(l[1].lower())#taking out second element and sorting
if l1 == l2:#comparing two lists
    print(x ,' is anagram')
else:
    print(x ,' is not anagram')

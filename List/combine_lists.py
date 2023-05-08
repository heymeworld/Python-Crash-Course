def combine_lists(list1, list2):
  # Generate a new list containing the elements of list2
  # Followed by the elements of list1 in reverse order
  reverse_list = []
  
  for i in range(len(list1)-1, -1, -1):
    reverse_list.append(list1[i])
  list2.extend(reverse_list)
  return list2
  
    
Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]

print(combine_lists(Jamies_list, Drews_list))

def insertion_sort(input_list):
    
#mark first item as sorted, separate first element?
        #already implied that it will be marked as first item in the item (conceptual)
#(for every item starting at the second element)
        #start at 1
        #length of input_list
    for i in range(1, len(input_list)):
        #put current item in temp variable
        current_item = input_list[i]
        #because left is alway i -1
        look_left_index = i-1
        #look left, until we find where it belongs


        #if are not at the beginning and current item is less than sorted
        #if current item is greater than sorted or we are at the beginning of sorted , insert item
        while look_left_index > 0 and current_item < input_list[look_left_index]:
            #to find where it belongs compare current item to sorted item
            #if sorted item is bigger
                #shift sorted item rightward
            input_list[look_left_index + 1] = input_list[look_left_index]
            look_left_index -= 1

        input_list[look_left_index] = current_item
        
    return input_list
        


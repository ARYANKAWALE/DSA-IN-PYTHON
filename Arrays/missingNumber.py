card_array = [1,2,3,4,5]
missing_array = [1,3,4,5]

total_sum = sum(card_array)
missing_card_sum = sum(missing_array)

MissingNumber = total_sum - missing_card_sum
print("The missing number is :",MissingNumber)
# def findSublists(nums, target):
 
#     for i in range(len(nums)):
 
#         sum_so_far = 0
 
        
#         for j in range(i, len(nums)):
 
           
#             sum_so_far += nums[j]
 
           
#             if sum_so_far == target:
 
#                 if len(nums[i:j+1]) >= 3:
                     
#                     print (nums[i:j+1])
 
 

# nums = [3, 4, -7, 1, 3, 3, 1, -4]
# target = 7
 
# findSublists(nums, target)


foods = {
    "Rice" : 353.7,
    "Wheat_flour" : 320.2,
    "Bengal_gram" : 287,
    "cabbage" : 21.5,
    "peas" : 303.2,
    "rajma" :299.2,
    "red_gram" : 330
}
print(foods.values())
for i in foods:
    print(i.values)
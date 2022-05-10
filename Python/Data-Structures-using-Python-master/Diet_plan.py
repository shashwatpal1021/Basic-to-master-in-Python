def consume_quantity_grocery_per_day(Character,foods,targetd_calories):

    value = map(int,foods.values().split())
    for i in range(len(value)):

        sum_so_far = 0

        for j in range(len(value)):

            sum_so_far += value[j]

            if sum_so_far <= targetd_calories:
                
                if len(foods[i:j+1] >= 3):
                
                    print(foods[i:j+1])





foods = {
    "Rice" : 353.7,
    "Wheat_flour" : 320.2,
    "Bengal_gram" : 287,
    "cabbage" : 21.5,
    "peas" : 303.2,
    "rajma" :299.2,
    "red_gram" : 330
}

target = 1320
consume_quantity_grocery_per_day(A,foods,1320)
consume_quantity_grocery_per_day(B,foods,1550)
consume_quantity_grocery_per_day(A,foods,1300)



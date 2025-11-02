# #Q1.WAP to create following structure
# Sample lists: ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]

# Expected Output: [{'color_name': 'Black', 'color_code': '#000000'}, 
# {'color_name': 'Red', 'color_code': '#FF0000'}, 
# {'color_name': 'Maroon', 'color_code': '#800000'}, 
# {'color_name': 'Yellow', 'color_code': '#FFFF00'}]


color_names = ["Black", "Red", "Maroon", "Yellow"]
color_codes = ["#000000", "#FF0000", "#800000", "#FFFF00"]
# print(color_names)
total=[]

for i in range(4):
    dic={"color_names":color_names[i],"color_codes":color_codes[i]}
    total.append(dic)

print(total)


# Calculate the viewing distance depending on the TV you have.
# And if you don't have a TV, it will tell you the size of the
# TV you need to buy.
import random

# Variables for 1080p TV
distance_ratio_27_1080 = random.randint(5, 9)
distance_ratio_32_1080 = random.randint(5, 9)
distance_ratio_40_1080 = random.randint(5, 9)
distance_ratio_43_1080 = random.randint(6, 10)
distance_ratio_50_1080 = random.randint(7, 11)
distance_ratio_55_1080 = random.randint(8, 12)
distance_ratio_60_1080 = random.randint(8, 13)
distance_ratio_65_1080 = random.randint(9, 14)
distance_ratio_70_1080 = random.randint(10, 15)
distance_ratio_75_1080 = random.randint(10, 16)
distance_ratio_80_1080 = random.randint(11, 17)
distance_ratio_85_1080 = random.randint(11, 18)

# Variables for 4K TV
distance_ratio_27_4k = random.randint(3, 5)
distance_ratio_32_4k = random.randint(3, 5)
distance_ratio_40_4k = random.randint(3, 5)
distance_ratio_43_4k = random.randint(3, 6)
distance_ratio_50_4k = random.randint(4, 7)
distance_ratio_55_4k = random.randint(5, 7)
distance_ratio_60_4k = random.randint(5, 8)
distance_ratio_65_4k = random.randint(6, 8)
distance_ratio_70_4k = random.randint(6, 9)
distance_ratio_75_4k = random.randint(7, 10)
distance_ratio_80_4k = random.randint(7, 10)
distance_ratio_85_4k = random.randint(7, 11)

have_a_tv = input("Do you have a TV at home? ").lower()
if have_a_tv == "yes":    
    tv_type = input("Is it a 1080 or 4k? ")
    if tv_type == "1080":
        size_of_tv = input("How many inches? ")
        if size_of_tv == "21" or size_of_tv == "24":
            print("Sell it, and buy a new one. We're in the 21st Century.")
        if size_of_tv == "27":            
            distance_ratio_27_1080_in = distance_ratio_27_1080 * 12            
            print(f"You have to be {distance_ratio_27_1080_in} inches away from the TV, approximately.")
        if size_of_tv == "32": 
            distance_ratio_32_1080_in = distance_ratio_32_1080 * 12            
            print(f"You have to be {distance_ratio_32_1080_in} inches away from the TV, approximately.")
        if size_of_tv == "40": 
            distance_ratio_40_1080_in = distance_ratio_40_1080 * 12            
            print(f"You have to be {distance_ratio_40_1080_in} inches away from the TV, approximately.")
        if size_of_tv == "43": 
            distance_ratio_43_1080_in = distance_ratio_43_1080 * 12            
            print(f"You have to be {distance_ratio_43_1080_in} inches away from the TV, approximately.") 
        if size_of_tv == "50": 
            distance_ratio_50_1080_in = distance_ratio_50_1080 * 12            
            print(f"You have to be {distance_ratio_50_1080_in} inches away from the TV, approximately.") 
        if size_of_tv == "55": 
            distance_ratio_55_1080_in = distance_ratio_55_1080 * 12            
            print(f"You have to be {distance_ratio_55_1080_in} inches away from the TV, approximately.") 
        if size_of_tv == "60": 
            distance_ratio_60_1080_in = distance_ratio_60_1080 * 12            
            print(f"You have to be {distance_ratio_60_1080_in} inches away from the TV, approximately.") 
        if size_of_tv == "65": 
            distance_ratio_65_1080_in = distance_ratio_65_1080 * 12            
            print(f"You have to be {distance_ratio_65_1080_in} inches away from the TV, approximately.") 
        if size_of_tv == "70": 
            distance_ratio_70_1080_in = distance_ratio_70_1080 * 12            
            print(f"You have to be {distance_ratio_70_1080_in} inches away from the TV, approximately.") 
        if size_of_tv == "75": 
            distance_ratio_75_1080_in = distance_ratio_75_1080 * 12            
            print(f"You have to be {distance_ratio_75_1080_in} inches away from the TV, approximately.") 
        if size_of_tv == "80": 
            distance_ratio_80_1080_in = distance_ratio_80_1080 * 12            
            print(f"You have to be {distance_ratio_80_1080_in} inches away from the TV, approximately.")        
    elif tv_type == "4k":                
        size_of_tv = input("How many inches? ")
        if size_of_tv == "21" or size_of_tv == "24":
            print("Sell it, and buy a new one. We're in the 21st Century.")
        if size_of_tv == "27":            
            distance_ratio_27_4k_in = distance_ratio_27_4k * 12            
            print(f"You have to be {distance_ratio_27_4k_in} inches away from the TV, approximately.")
        if size_of_tv == "32": 
            distance_ratio_32_4k_in = distance_ratio_32_4k * 12            
            print(f"You have to be {distance_ratio_32_4k_in} inches away from the TV, approximately.")
        if size_of_tv == "40": 
            distance_ratio_40_4k_in = distance_ratio_40_4k * 12            
            print(f"You have to be {distance_ratio_40_4k_in} inches away from the TV, approximately.")
        if size_of_tv == "43": 
            distance_ratio_43_4k_in = distance_ratio_43_4k * 12            
            print(f"You have to be {distance_ratio_43_4k_in} inches away from the TV, approximately.") 
        if size_of_tv == "50": 
            distance_ratio_50_4k_in = distance_ratio_50_4k * 12            
            print(f"You have to be {distance_ratio_50_4k_in} inches away from the TV, approximately.") 
        if size_of_tv == "55": 
            distance_ratio_55_4k_in = distance_ratio_55_4k * 12            
            print(f"You have to be {distance_ratio_55_4k_in} inches away from the TV, approximately.") 
        if size_of_tv == "60": 
            distance_ratio_60_4k_in = distance_ratio_60_4k * 12            
            print(f"You have to be {distance_ratio_60_4k_in} inches away from the TV, approximately.") 
        if size_of_tv == "65": 
            distance_ratio_65_4k_in = distance_ratio_65_4k * 12            
            print(f"You have to be {distance_ratio_65_4k_in} inches away from the TV, approximately.") 
        if size_of_tv == "70": 
            distance_ratio_70_4k_in = distance_ratio_70_4k * 12            
            print(f"You have to be {distance_ratio_70_4k_in} inches away from the TV, approximately.") 
        if size_of_tv == "75": 
            distance_ratio_75_4k_in = distance_ratio_75_4k * 12            
            print(f"You have to be {distance_ratio_75_4k_in} inches away from the TV, approximately.") 
        if size_of_tv == "80": 
            distance_ratio_80_4k_in = distance_ratio_80_4k * 12            
            print(f"You have to be {distance_ratio_80_4k_in} inches away from the TV, approximately.") 
elif have_a_tv == "no":
    print("We recommend you buy a 75-inch 4K TV and watch it 96 inches away from it.")
        
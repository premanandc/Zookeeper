# put your python code here
duration_in_days = int(input())
food_cost_per_day = int(input())
flight_cost = int(input())
hotel_cost_per_night = int(input())

total_food_cost = food_cost_per_day * duration_in_days
total_hotel_cost = hotel_cost_per_night * (duration_in_days - 1)
total_cost = total_hotel_cost + total_food_cost + flight_cost * 2
print(total_cost)

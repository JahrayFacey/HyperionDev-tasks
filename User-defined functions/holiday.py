# This is a program modelling a trip-booking system. All of the inputs will be used to calculate and display the final holiday cost.
cities = {
    "paris": 52,
    "toronto": 350,
    "new york": 275,
    "kingston": 582,
    "madrid": 35
}
city_flight = input("Madrid, New York, Toronto, Paris, Kingston ").lower()
num_nights = int(input("How many nights will you be staying for? "))
rental_days = int(input("How many days will you be hiring a car? "))


def hotel_cost(num_nights):
  num_nights = int(num_nights * 200)
  print(num_nights)
  return num_nights


def plane_cost(city_flight):
  for city in cities:
   if city_flight == city:
      print(f"The price will be {cities[city]} pounds")
      return cities[city]
  print("Invalid city")
plane_cost(city_flight)


def car_rental(rental_days):
  hiring_car = 100 * int(rental_days)
  print(
      f"The price to rent a car a day is £100. The total price is {hiring_car}"
  )
  return hiring_car






def holiday_cost(hotel_cost, plane_cost, car_rental):
 hotel_price = hotel_cost(num_nights)
 car_price = car_rental(rental_days)
 plane_price = plane_cost(city_flight)
 holiday = hotel_price + plane_price + car_price
 print(f"The total cost of your holiday to {city_flight} will be £{holiday}")
 return holiday

holiday_cost(hotel_cost, plane_cost, car_rental) 


    
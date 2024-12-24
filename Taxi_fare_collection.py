def calculate_fare(distance):
    base_fare = 50 
    distance_fare = 10 * distance 
    total_fare = base_fare + distance_fare  
    return total_fare

def main():
    trips = [5, 10, 3]
    total_fare = 0
    print("```")
    for i, distance in enumerate(trips, 1):
        fare = calculate_fare(distance)
        print(f"Trip {i}: ${fare}")
        total_fare += fare
    print(f"Total Fare: ${total_fare}")
    print("```")
if __name__ == "__main__":
    main()

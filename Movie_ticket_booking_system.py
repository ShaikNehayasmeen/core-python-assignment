def get_available_seats(total_seats, booked_seats):
   
    return [seat for seat in range(1, total_seats + 1) if seat not in booked_seats]

def book_seat(booked_seats, seat_to_book, total_seats):
    
    if seat_to_book in booked_seats:
        print(f"Seat {seat_to_book} is already booked.")
    elif seat_to_book > total_seats or seat_to_book < 1:
        print(f"Seat {seat_to_book} is invalid.")
    else:
        booked_seats.append(seat_to_book)
        # print(f"Seat {seat_to_book} has been successfully booked.")

def cancel_seat(booked_seats, seat_to_cancel):
   
    if seat_to_cancel in booked_seats:
        booked_seats.remove(seat_to_cancel)
        # print(f"Seat {seat_to_cancel} booking has been canceled.")
    else:
        print(f"Seat {seat_to_cancel} is not currently booked.")
total_seats = 10
booked_seats = [2, 5, 7]
book_seat_input = 3
cancel_seat_input = 5
book_seat(booked_seats, book_seat_input, total_seats)
cancel_seat(booked_seats, cancel_seat_input)
available_seats = get_available_seats(total_seats, booked_seats)
print(f"Available seats: {available_seats}")

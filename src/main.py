# src/main.py
from src.views.create_booking import CreateBooking


def main():
    print("Welcome To Appointment Genie!")
    view = CreateBooking(title="App Genie: Create Booking")
    view.tk.mainloop()


if __name__ == '__main__':
    main()

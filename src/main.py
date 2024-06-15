# src/main.py
from src.views.create_booking import CreateBooking
from src.controller.controller import Controller


def main():
    print("Welcome To Appointment Genie!")
    controller = Controller()
    view = CreateBooking(controller=controller, title="App Genie: Create Booking")
    view.tk.mainloop()


if __name__ == '__main__':
    main()

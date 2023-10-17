"""

This is a basic (prototype) software that we would provide to the Restaurant. This software aims to provides the
user a variety of service, while at the same time reducing the human efforts and work-load at the restaurant.

The manager can sit in his room, probably watch some NETFLIX show, while this software increases his profits, and saves
the money spent for more workers. So, not only are we solving the problem, but also brings you one step closer to
Mr. Ambani.

"""

# Importing Modules
import time
import string
import random
from collections import Counter


# Initial Greetings
print('*' * 75)
print("\t\t  Welcome to 'The Singh Restaurant'")
print("\tThe one stop destination for all your food cravings")
print('*' * 75)


# Defining Functions
def space():
    """
    Providing breaks while printing data on console.
    """
    
    print('*' * 75)


def error():
    """
    Error texts, in case of bogus input.
    """
    
    print("Oops, something went wrong. Please try again")


def ask_data():
    """
    Collect user data.
    """
    
    print("\t  We would like to know some information from you,")
    print("\t   in order to give you a better user experience.")
    print('*' * 75)

    naam = input("May we know your name : ")
    p = int(input("Phone Number : "))
    pos = input("Address : ")

    return naam, p, pos


def ask_query():
    """
    User's FAQ / Query Resolving Function.
    TODO : Add some sort of text recognition to make the program smart
    """
    
    ques = input("What is your query (enter 'Q' to quit) ? ")

    if ques.casefold() != 'q':
        space()
        
        if ('time' in ques.casefold()) or ('timing' in ques.casefold()) or ('timings' in ques.casefold()):
            print("The restaurant is open from 10AM in the morning to 10PM on the evening, on all 7 days of the week.")
            space()
            ask_query()

        elif ('contact' in ques.casefold()) or ('phone' in ques.casefold()) or ('mail' in ques.casefold()):
            print("You can reach us on 9876543210, or just mail us at thesingh.restaurant@themis.in.")
            space()
            ask_query()

        elif ('offer' in ques.casefold()) or ('discount' in ques.casefold()) or ('cashback' in ques.casefold()):
            print("You can avail up to a 50% discount on your order. All you need is to be lucky. So, get on"
                  "\n your lucky shirt, grab your lucky ring, and roll the dice of your fortune (Service Code"
                  "3). However, you/ll lose the offer, if you don't avail it just after winning, only.")

            space()
            ask_query()

        elif ('safety' in ques.casefold()) or ('covid' in ques.casefold()) or ('cleanliness' in ques.casefold()):
            print("Safety of our customers is our No. 1 priority. At Singh’s, we take food safety \n"
                  "concerns very seriously, and understand that food safety is on everyone’s mind \n"
                  "during this time. In addition to offering contactless delivery, we are adhering \n"
                  "to the highest cleanliness standards in the industry. And, what's better than \n"
                  "the AVGPTFC cleanliness and safety award, to prove our dedication to keep the \n"
                  "food,not only tasty, but healthy and safe, too.")

            space()
            ask_query()

        else:
            print("Sorry, please contact us on 9876543210 or thesingh.restaurant@themis.in,"
                  "\nas my AI is unable to process your query. Sorry for the inconvenience.")

            space()
            ask_query()

    else:
        finalmessage()


def order(cost):
    """
    Processing orders [ Calculations / Billing / Storing / Repeat ]
    """

    # Menu
    food = {500: "Kadhai-Paneer",
            750: "Butter-Chicken-Masala",
            150: "Masala-Dosa",
            120: "Gulab-Jamun",
            450: "Dessert"}

    # Taking order
    print("We serve the following mouth-watering delights: ")
    print("750 : Butter Chicken Masala (with 5 rotis)")
    print("500 : Kadhai Paneer (with 5 Rotis)")
    print("150 : Masala Dosa (with Sambar and Chutney)")
    print("120 : Gulab Jamun (2 pieces)")
    print("450 : Dessert (Chocolate Truffle Ice-cream)")
    print("F : Finalise Order\n")
    ag = input("Please enter the respective code for the dish : ")

    if ag.casefold() == 'f':
        # Finalising Order
        
        space()
        print("Your final order is as follows:")
        for b in order_list:
            print(b)

        if offer: # is not None
            # Applying offer, if any
            payable = (offer // 100) * cost
            print("The final payable amount is {}.".format(str(payable)))
            var = payable

        else:
            # Final billing amount
            print("The final payable amount is {}.".format(str(cost)))
            var = cost

        space()
        return var, order_list
        # Order Completed :)

    elif int(ag) in [500, 750, 150, 120, 450]:
        order_list.append(food[int(ag)])
        cost += int(ag)
        var_cost, var_order = order(cost)
        return var_cost, var_order
        # Added to Cart

    else:
        error()


def code():
    """
    Generating promo codes
    """
    
    randomiser = string.ascii_uppercase
    s1 = random.choice(randomiser)
    s2 = random.choice(randomiser)
    s3 = random.choice(randomiser)
    s4 = random.choice(randomiser)
    s5 = random.choice(randomiser)
    s6 = random.choice(randomiser)
    promo = s1 + s2 + s3 + s4 + s5 + s6

    with open('PromoCodes.txt', 'a') as promos:
        # Adding promocode to database
        print(promo, end=' ', file=promos)

    print("\t Here's a small gift from us for when you feast with us again : {}. \n"
          "Use it the next time you visit us, and get a chance to avail a discount for upto 50% off.".format(promo))


def finalmessage():
    """
    Function to print the final goodbye message.
    """
    
    print('*' * 75)
    print("\t\tThank You for choosing 'The Singh Restaurant'")
    print("\tHope the food and service was as good as our customers")
    print('\t\t\t"Life is too short for boring food."')
    print('*' * 75)


### Main Program Starts

with open('Earnings.txt', 'r') as earnings:                         # Extracting the current earnings from the restaurant's database.
    for val in earnings:
        net_earning = int(val)
earnings.close()

with open('Vacancy.txt', 'r') as vacant:                            # Extracting the current earnings from the restaurant's database.
    for seats in vacant:
        rem_seat = int(seats)
earnings.close()                                                    # Max number of dine-in customers is 25

code_list = []
with open('PromoCodes.txt', 'r') as promocode:                      # Extracting all valid promos from the database.
    for codes in promocode:
        code_list = codes.split()
promocode.close()

available_slots = []
with open('ParkingSlots.txt', 'r') as slots:                        # Extracting available parking slots from database.
    for slot in slots:
        available_slots = slot.split()
slots.close()

print("We provide you with the following services")                 # Displaying the set of services, our program serves
print("1 : Order Placement (For Delivery and Takeaway Only)")
print("2 : Reserving Seat (Order Placement Included)")
print("3 : Use your Promo-Code")
print("4 : Order by Mood")
print("5 : Our Menu")
print("6 : Queries and FAQs")
print("7 : Complaints and Feedbacks ")

service = int(input("\nHow may we help you? (use the numeric code for the respective service) : "))
space()

if service == 1:                                                     # If the user opts for delivery.
    name, ph, loc = ask_data()                                       # Asking user's data
    space()
    order_list = []
    bill = 0
    offer = None
    final_cost, final_order = order(bill)                            # Calling the function, to place the order

    with open('DeliveryData.txt', 'a') as DeliveryData:              # Saving user data in our data-storages.
        clock = time.strftime("%H:%M:%S", time.localtime())
        print("Transaction Time : " + clock, file=DeliveryData)
        print("User Name : " + name, file=DeliveryData)
        print("User Phone Number : " + str(ph), file=DeliveryData)   # This data can be shared to a partner-delivery-
        print("User Address : " + loc, file=DeliveryData)            # company, which will not only reduce the cost of
        print("Order : ", end='', file=DeliveryData)                 # dine-in services (like water, AC, electricity),
        for a in order_list:                                         # but also reduce the man-force required at the
            print(a, end=' , ', file=DeliveryData)                   # restaurant, which was the main problem.
        print("Final Amount : " + str(final_cost), file=DeliveryData)
        print('*' * 50, file=DeliveryData)

    net_earning += final_cost                                        # Updating the Total earnings of the restaurant.
    with open('Earnings.txt', 'w') as earnings:
        print(net_earning, file=earnings)

    code()
    finalmessage()

elif service == 2:                                                   # If th user wants to dine-in
    name, ph, loc = ask_data()                                       # Asking user's data
    c = int(input("No. of customers : "))
    res_date = input("Date of reservation (DD/MM/YYYY): ")
    res_time = input("Starting of the time of Reservation (only 1 hour reservations can be confirmed) : ")
    valet = input("Would you like to use our valet service (Y/N) : ")

    if valet.casefold() == 'n':
        pass

    else:
        car_num = input("Your vehicle Registration Number : ")
        parking = available_slots[0]
        available_slots.pop(0)

        with open('ValetData.txt', 'a') as vdata:
            print("{}'s vehicle, numbered {}, is parked at {}.".format(name, car_num, parking), file=vdata)
            print('*' * 75, file=vdata)
        vdata.close()

        with open('ParkingSlots.txt', 'w') as slots:
            for slot in available_slots:
                print(slot, end=' ', file=slots)

    with open('Reservations.txt', 'a') as reserve:
        print("A table of {} to be reserved on {} at {}.".format(c, res_date, res_time), file=reserve)
        print('*' * 75, file=reserve)

    space()
    order_list = []
    offer = None
    bill = 0
    final_cost, final_order = order(int(bill))                        # Calling the function, to place the order

    try:
        print("Your vehicle ({}) will be parked by our official at '{}' slot.".format(car_num, parking))
        space()
    except NameError:
        pass

    with open('DineData.txt', 'a') as DineData:                       # Saving user data in our data-storages.
        clock = time.strftime("%H:%M:%S", time.localtime())
        print("Transaction Time : " + clock, file=DineData)
        print("User Name : " + name, file=DineData)
        print("User Phone Number : " + str(ph), file=DineData)
        print("User Address : " + loc, file=DineData)
        print("No. of customers : " + str(c), file=DineData)
        print("Order : ", end='', file=DineData)
        for a in order_list:
            print(a, end=" , ", file=DineData)
        print("Final Amount : " + str(final_cost), file=DineData)
        print('*' * 50, file=DineData)

    net_earning += final_cost
    with open('Earnings.txt', 'w') as earnings:                        # Updating Logs
        print(net_earning, file=earnings)

    rem_seat -= 1
    with open('Vacancy.txt', 'w') as vacant:
        print(rem_seat, file=vacant)

    code()
    finalmessage()

elif service == 3:                                                     # Giving offers, is an old trick to attract
    user_code = input("Enter your promo code here : ")                 # more customers, and that's what we do, to help
    if user_code in code_list:                                         # the restaurant widen its service area and also
        x = random.randint(1, 100)                                     # keep hold of its customers.

        if x == 69:
            offer = 50
            print("Congratulation!, feast now to get a 50% off.")

        elif x in [2, 4, 6, 9, 42]:
            offer = 10
            print("Congrats!, eat now to get a 10% off.")

        else:
            offer = None
            print("Oh, not your day today. Better Luck Next Time.")

        if offer is not None:                                            # Just recalling the services 1 and services
            print("We provide you with the following services")          # 2, but with the offer this time.
            print("1 : Order Placement (For Delivery and Takeaway Only)")
            print("2 : Reserving Seat (Order Placement Included)")
            offer_service = int(input("\nHow may we help you? (use the numeric code for the respective service) : "))
            space()

            if offer_service == 1:
                name, ph, loc = ask_data()                               # Asking user's data
                space()
                order_list = []
                bill = 0
                final_cost, final_order = order(bill)                    # Placing Order

                with open('DeliveryData.txt', 'a') as DeliveryData:      # Storing data
                    clock = time.strftime("%H:%M:%S", time.localtime())
                    print("Transaction Time : " + clock, file=DeliveryData)
                    print("User Name : " + name, file=DeliveryData)
                    print("User Phone Number : " + str(ph), file=DeliveryData)
                    print("User Address : " + loc, file=DeliveryData)
                    print("Order : ", end='', file=DeliveryData)
                    for a in order_list:
                        print(a, end=' , ', file=DeliveryData)
                    print("Final Amount : " + str(final_cost), file=DeliveryData)
                    print('*' * 50, file=DeliveryData)

                net_earning += final_cost
                with open('Earnings.txt', 'w') as earnings:              # Updating Logs
                    print(net_earning, file=earnings)

            elif offer_service == 2:
                name, ph, loc = ask_data()                               # Asking user's data
                c = int(input("No. of customers : "))
                res_date = input("Date of reservation (DD/MM/YYYY): ")
                res_time = input("Starting of the time of Reservation (only 1 hour reservations can be confirmed) : ")

                with open('Reservations.txt', 'a') as reserve:
                    print("A table of {} to be reserved on {} at {}.".format(c, res_date, res_time), file=reserve)
                    print('*' * 75, file=reserve)

                space()
                order_list = []
                bill = 0
                final_cost, final_order = order(int(bill))               # Placing Order

                with open('DineData.txt', 'a') as DineData:              # Storing Data
                    clock = time.strftime("%H:%M:%S", time.localtime())
                    print("Transaction Time : " + clock, file=DineData)
                    print("User Name : " + name, file=DineData)
                    print("User Phone Number : " + str(ph), file=DineData)
                    print("User Address : " + loc, file=DineData)
                    print("No. of customers : " + str(c), file=DineData)
                    print("Order : ", end='', file=DineData)
                    for a in order_list:
                        print(a, end="  , ", file=DineData)
                    print("Final Amount : " + str(final_cost), file=DineData)
                    print('*' * 50, file=DineData)

                net_earning += final_cost
                with open('Earnings.txt', 'w') as earnings:              # Updating Logs
                    print(net_earning, file=earnings)

                rem_seat -= 1
                with open('Vacancy.txt', 'w') as vacant:
                    print(rem_seat, file=vacant)

            finalmessage()

        code_list.remove(user_code)
        with open('PromoCodes.txt', 'w') as promocodes:
            for codes in code_list:
                print(codes, end=' ', file=promocodes)

    else:
        print("Sorry, that's an INVALID code.")

elif service == 4:
    print("We have dishes curated perfectly for your mood")
    print("1 : Speciality (The Best our Restaurant serves)")
    print("2 : Random (A random dish, lets see what your tummy gets)")
    print("3 : Veg Soul Food (Some food just provide us with Inner Peace, isn't it)")
    print("4 : Non-Veg Soul Food (Some food just provide us with Inner Peace, isn't it)")
    print("5 : Celebration (Open up your pockets, its party time)")
    print()
    mood = int(input("Please enter the respective code for your mood : "))
    space()

    name, ph, loc = ask_data()
    space()

    if mood == 1:
        menu = ["Butter-Chicken-Masala", "Kadhai-Paneer", "Masala Dosa", "Gulab-Jamun", "Dessert"]
        data_list = []

        with open('DeliveryData.txt', 'r') as dinein_data:
            for pb in dinein_data:
                for sg in pb.split():
                    if sg in menu:
                        data_list.append(sg)
        dinein_data.close()

        count = Counter(data_list)
        most_occur = count.most_common(1)
        for n in most_occur:
            print("Your final order is {}.".format(n[0]))
            print("And the net payable amount is 500 INR.")
        space()

        with open('DeliveryData.txt', 'a') as DeliveryData:               # Storing Data
            clock = time.strftime("%H:%M:%S", time.localtime())
            print("Transaction Time : " + clock, file=DeliveryData)
            print("User Name : " + name, file=DeliveryData)
            print("User Phone Number : " + str(ph), file=DeliveryData)
            print("User Address : " + loc, file=DeliveryData)
            print("Order : ", end='', file=DeliveryData)
            for a in data_list:
                print(a, end=" , ", file=DeliveryData)
            print("Final Amount : 500", file=DeliveryData)
            print('*' * 50, file=DeliveryData)

    elif mood == 2:
        print("Your final order is Kadhai Paneer.")
        print("And the net payable amount is 500 INR.")

        with open('DeliveryData.txt', 'a') as DeliveryData:               # Storing Data
            clock = time.strftime("%H:%M:%S", time.localtime())
            print("Transaction Time : " + clock, file=DeliveryData)
            print("User Name : " + name, file=DeliveryData)
            print("User Phone Number : " + str(ph), file=DeliveryData)
            print("User Address : " + loc, file=DeliveryData)
            print("Order : Kadhai-Paneer", end=' , ', file=DeliveryData)
            print("Final Amount : 500", file=DeliveryData)
            print('*' * 50, file=DeliveryData)

    elif mood == 3:
        print("Your final order is Kadhai Paneer, Dessert.")
        print("And the net payable amount is 950 INR.")

        with open('DeliveryData.txt', 'a') as DeliveryData:               # Storing Data
            clock = time.strftime("%H:%M:%S", time.localtime())
            print("Transaction Time : " + clock, file=DeliveryData)
            print("User Name : " + name, file=DeliveryData)
            print("User Phone Number : " + str(ph), file=DeliveryData)
            print("User Address : " + loc, file=DeliveryData)
            print("Order : Kadhai-Paneer , Dessert", end=' , ', file=DeliveryData)
            print("Final Amount : 950", file=DeliveryData)
            print('*' * 50, file=DeliveryData)

    elif mood == 4:
        print("Your final order is Butter Chicken Masala, Gulab Jamun.")
        print("And the net payable amount is 950 INR.")

        with open('DeliveryData.txt', 'a') as DeliveryData:               # Storing Data
            clock = time.strftime("%H:%M:%S", time.localtime())
            print("Transaction Time : " + clock, file=DeliveryData)
            print("User Name : " + name, file=DeliveryData)
            print("User Phone Number : " + str(ph), file=DeliveryData)
            print("User Address : " + loc, file=DeliveryData)
            print("Order : Butter-Chicken-Masala , Gulab-Jamun", end=', ', file=DeliveryData)
            print("Final Amount : 870", file=DeliveryData)
            print('*' * 50, file=DeliveryData)

    elif mood == 5:
        print("Your final order is Kadhai Paneer, Butter Chiken Masala.")
        print("And the net payable amount is 1250 INR.")

        with open('DeliveryData.txt', 'a') as DeliveryData:               # Storing Data
            clock = time.strftime("%H:%M:%S", time.localtime())
            print("Transaction Time : " + clock, file=DeliveryData)
            print("User Name : " + name, file=DeliveryData)
            print("User Phone Number : " + str(ph), file=DeliveryData)
            print("User Address : " + loc, file=DeliveryData)
            print("Order : Kadhai-Paneer , Butter-Chicken-Masala", end=' , ', file=DeliveryData)
            print("Final Amount : 500", file=DeliveryData)
            print('*' * 50, file=DeliveryData)

    else:
        error()
    finalmessage()


elif service == 5:                                                    # Displaying Menu
    print("We serve the following mouth-watering delights: ")
    print("1 : Kadhai Paneer (with 5 Rotis)          : 500 INR")
    print("2 : Butter Chicken Masala (with 5 rotis)  : 750 INR")
    print("3 : Masala Dosa (with Sambar and Chutney) : 150 INR")
    print("4 : Gulab Jamun (2 pieces)                : 120 INR")
    print("5 : Dessert (Chocolate Truffle Ice-cream) : 450 INR")
    finalmessage()

elif service == 6:                                                    # Calling the function to clear user's query,
    ask_query()                                                       # by identifying keywords in the question.

elif service == 7:                                                    # Taking user's Feedback
    name = input("May we know your name : ")
    ph = int(input("Phone Number : "))
    loc = input("Address : ")
    space()

    print(" You have a query, or want to help us improve. Then we always have our ears")
    print("for you. We would very much like to know what our customers think of us, and")
    print("how can we improve to give you a service, that is not only delicious but also")
    print("\tuser-friendly. Please give your feedback/suggestion/complaint, below:")
    print('*' * 75)
    fb = input()
    finalmessage()

    with open('Feedback.txt', 'a') as feedback:                       # Updating data storages
        clock = time.strftime("%H:%M:%S", time.localtime())
        print("Transaction Time : " + clock, file=feedback)
        print("User Name : " + name, file=feedback)
        print("User Phone Number : " + str(ph), file=feedback)
        print("User Address : " + loc, file=feedback)
        print('"{}"'.format(fb), file=feedback)
        print('*' * 50, file=feedback)

elif service == 1991478:                                              # admin-exclusive command, to know his stats,
    print("1 : My Earnings")                                          # view logs, toggle data storage and calculate
    print("2 : My Expenditure (on Food)")                             # his monetary exchange.
    print("3 : Customer's Feedback Data")
    print("4 : Dine-In Guests Data")
    print("5 : Online Delivery/Takeaway Data")
    print("6 : Reservations")
    print("7 : Best-seller of the Restaurant")
    print("8 : Parking Data")
    admin = int(input("\nWelcome Sir, how may we help you? "))
    space()

    expend = 2550

    if admin == 1:                                                    # Retrieve earnings from the data-storage.
        print("The total earnings of the day have been {}INR.".format(net_earning))

    elif admin == 2:                                                  # Retrieve expenditure from the data-storage.
        print("The total expenditure on food today has been {}INR.".format(expend))

    elif admin == 3:                                                  # Retrieve users' feedback.
        with open('Feedback.txt', 'r') as feedback:
            for data in feedback:
                print(data)
        feedback.close()

    elif admin == 4:                                                  # Retrieve diner's data.
        with open('DineData.txt', 'r') as dinedata:
            for data in dinedata:
                print(data)
        dinedata.close()

    elif admin == 5:                                                  # Retrieve orderer's data.
        with open('DeliveryData.txt', 'r') as deliverydata:
            for data in deliverydata:
                print(data)
        deliverydata.close()

    elif admin == 6:                                                  # Retrieve reservations booked for the day.
        with open('Reservations.txt', 'r') as reserve:
            for data in reserve:
                print(data)
        reserve.close()

    elif admin == 7:                                                  # Retrieve data from the orders' data files.
        menu = ["Butter-Chicken-Masala", "Kadhai-Paneer", "Masala Dosa", "Gulab-Jamun", "Dessert"]
        data_list = []

        with open('DeliveryData.txt', 'r') as delivery_data:
            for pb in delivery_data:
                for sg in pb.split():
                    if sg in menu:
                        data_list.append(sg)
        delivery_data.close()

        with open('DeliveryData.txt', 'r') as dinein_data:
            for pb in dinein_data:
                for sg in pb.split():
                    if sg in menu:
                        data_list.append(sg)
        dinein_data.close()

        count = Counter(data_list)
        most_occur = count.most_common(1)
        for n in most_occur:
            print("The most sold dish of the restaurant is {}.".format(n[0]))

    elif admin == 8:                                                  # Retrieve reservations booked for the day.
        with open('ValetData.txt', 'r') as valet:
            for data in valet:
                print(data)
            valet.close()

    else:                                                              # If in case of bogus input.
        error()
else:
    error()

final = input()

# And that's pretty much it :)

import random

Chinese_cuisine = ["stir-fried chicken with chili and Sichuan pepper in Sichuan style", "winter melon, shrimp and cellophane noodle soup", "Kung pao chicken and noodles","Lion's head with crab meat" ]
Colombian_cuisine = ["Patacones and hogao", "Locro soup", "Valluna", "Tamales", "rice atollao"]
Cuban_cuisine = ["Sopa de pollo", "Vaca Frita", "Sandwich Cubano", "Medianoche Sandwich", "Boliche", "Bistec de Palomilla"]
Louisiana_cuisine = [" jambalaya", "Oysters Rockefeller", "Crawfish étouffée", "Shrimp creole", "Bisque Soup", "Gumbo", "Pompano en Papillote"]
Indian_cuisine = ["Aloo gobi", " Chicken Makhani (Butter Chicken)", " Rogan Josh (Curried Meat)", " Kakori Kebab", "Karan Mittal’s chicken tikka."]
def what_to_eat():
    place = input("Where would you like to eat this fine afternoon?")
    if place == "Chinese_cuisine":
        print("Ok! Let me find you something to eat... one second.")
        print("You should eat : "+random.choice (Chinese_cuisine))
    elif place == "Colombian_cuisine":
        print("Ok! Let me find you something to eat... one second.")
        print("You should eat : "+random.choice (Colombian_cuisine))
    elif place == "Cuban_cuisine":
        print("Ok! Let me find you something to eat... one second.")
        print("You should eat : "+random.choice (Cuban_cuisine))
    elif place == "Louisiana_cuisine":
        print("Ok! Let me find you something to eat... one second.")
        print("You should eat : "+random.choice (Louisiana_cuisine))
    elif place == "Indian_cuisine":
        print("Ok! Let me find you something to eat... one second.")
        print("You should eat : "+random.choice (Indian_cuisine))
    else:
        print (input("It is ok if you are not sure what you feel like eating, I am the same way! Just pick a number from 1-5 "))
        random_choice = random.randint(1,5)
        if random_choice == 1:
                print("GREAT! Looks like your lunch this afternoon is:  " +random.choice(Chinese_cuisine))
        elif random_choice == 2:
            print("GREAT! Looks like your lunch this afternoon is:  " +random.choice(Colombian_cuisine))
        elif random_choice == 3:
            print("GREAT! Looks like your lunch this afternoon is:  " +random.choice(Cuban_cuisine))
        elif random_choice == 4:
            print("GREAT! Looks like your lunch this afternoon is:  " +random.choice(Louisiana_cuisine))
        elif random_choice == 5:
            print("GREAT! Looks like your lunch this afternoon is:  " +random.choice(Indian_cuisine))
        else:
            print("Why didn't you follow directions.... 1 through 5, ONLY!")

what_to_eat()


# Import the random module
import random
from datetime import datetime

# Define the save function at the beginning
def save_user_input(user_text):
    """Save user input to a file if they want."""
    
    choice = input("💾📢 Kya aap is dhamakedar headline ko hamesha ke liye bacha ke rakhna chahte hain? (y/n) 🗞️✨ ").strip().lower()
    

    if choice == "y":
        # Create unique file name with date & time
        filename = "saved_headlines.txt"  # Single file for all saved headlines

        try:
            # Open file and append text
            with open(filename, "a", encoding="utf-8") as file:
                file.write(user_text + "\n")
                file.write("="*50 + "\n")  # Separator between headlines
            print(f"\n 👍 Headline saved to {filename} \n ")

        except Exception as e:
            print(f"🔴 Error saving file: {e}")
    else:
        print("\n❌📰 Headline save nahi hui... lagta hai ye khabar hawa mein udd gayi! 💨😂\n")

print("=" * 120)
print("🎉  Welcome to Fake News Generator 🎉".center(120))
print("=" * 120)

input_user = int( input ("🎯 Choose your fake news theme (1-10):"
                        "\n 1.International Mix – Funny and random headlines from around the world 🌍"
                        "\n 2.National Buzz – Pakistan‑themed humorous fake news 🇵🇰"
                        "\n 3.Political Circus – Exaggerated, light‑hearted political headlines 🎩"
                        "\n 4.Sports Madness – Over‑the‑top sports news 🏆"
                        "\n 5.Celebrity Scoop – Silly and weird celebrity headlines 🎬"
                        "\n 6.Foodie Headlines – Bizarre food‑related fake news 🍔"
                        "\n 7.Tech & Space Craze – Weird tech, gadgets, and space exploration 🚀"
                        "\n 8.Animal Adventures – Animals doing unbelievable things 🐒"
                        "\n 9.Festival Fun – Fake news about holidays and cultural events 🎉"
                        "\n 10.Random Ridiculousness – Anything goes, pure chaos 🤪\n"
                        "Enter a number between 1 and 10 : "
                    )
                )


if input_user == 1:
    print("=" * 120)
    print("International Mix – Funny and random headlines from around the world 🌍".center(120))
    print("=" * 120)
    international_subjects = [
        "Donald Trump", "Elon Musk", "Cristiano Ronaldo", "Taylor Swift", "Lionel Messi",
        "Kim Kardashian", "Bill Gates", "Mark Zuckerberg", "Justin Bieber", "Tom Cruise"
    ]

    international_verbs = [
        "ne launch ki", "ne banayi", "ne invent ki", "ne shuru ki", "ne paint kar diya",
        "ne banaya world's first", "ne start ki", "ne open ki", "ne banayi flying", "ne replace kar diya"
    ]

    international_objects = [
        "flying naan", "drone-delivered pizza", "samosa-powered car", "invisible mobile", "mango toothpaste",
        "selfie chai machine", "golgappa ATM", "robo goat", "pillow-fighting championship", "ice-cream rocket"
    ]
    
    while True:
        international_subject = random.choice(international_subjects)
        international_verb = random.choice(international_verbs)
        international_object = random.choice(international_objects)
        
        head_line = f"Breaking News: {international_subject} {international_verb} {international_object}"
        print("\n\t", head_line, "\n")
        
        # Ask to save each headline
        save_user_input(head_line)

        user_input = input("🔄🤣 Kya aap ek aur chutkule wali fake news chahte hain? (yes/no) 📰🎭 ").strip().lower()
        if user_input == "no":
            break

elif input_user == 2:
    print("=" * 120)
    print("National Buzz – Pakistan‑themed humorous fake news 🇵🇰".center(120))
    print("=" * 120)
    national_subjects = [
        "Karachi chai wala", "Lahore traffic warden", "Pindi boy", "Faisalabad samosa seller", "Multan mango farmer",
        "Gwadar fisherman", "Cholistan camel", "Truck artist from Gujranwala", "Islamabad cat", "Lahore's singing donkey"
    ]

    national_verbs = [
        "ne shuru ki", "ne invent ki", "ne banayi", "ne launch ki", "ne open ki",
        "ne banaya", "ne challenge ki", "ne banayi flying", "ne paint kar diya", "ne banaya record"
    ]

    national_objects = [
        "golgappa drone", "flying samosa service", "chai ki fountain", "mango pizza", "buffalo Uber service",
        "goat beauty contest", "biryani delivery rocket", "solar chapati maker", "pakora perfume", "Wi-Fi rickshaw"
    ]

    while True:
        national_subject = random.choice(national_subjects)
        national_verb = random.choice(national_verbs)
        national_object = random.choice(national_objects)

        head_line = f"Breaking News: {national_subject} {national_verb} {national_object}"
        print("\n\t", head_line, "\n")
        
        save_user_input(head_line)

        user_input = input("Kya aap aur fake news generate karna chahtai hai? (yes/no): ").strip().lower()
        if user_input == "no":
            break

# [Similar pattern for categories 3-10 - shortened for brevity]
# Each category would follow the same structure as above

elif input_user == 3:
    print("=" * 120)
    print(" Political Circus – Exaggerated, light‑hearted political headlines 🎩".center(120))
    print("=" * 120)
    political_subjects = [
                         "Imran Khan", "Bilawal Bhutto", "Shehbaz Sharif", "Donald Trump", "Narendra Modi",
                         "Joe Biden", "Barack Obama", "Vladimir Putin", "Nawaz Sharif", "Maryam Nawaz"
                         ]

    political_verbs = [
                        "ne banaya", "ne invent ki", "ne start ki", "ne banayi flying", "ne paint kar diya",
                        "ne replace kar diya", "ne open ki", "ne banayi golgappa machine", "ne shuru ki", "ne banaya record"
                    ]

    political_objects = [
                        "chai parliament", "biryani constitution", "flying ballot box", "selfie voting machine", "samosa cabinet",
                        "mango diplomacy", "pakora parliament", "goat army", "pillow-fighting election", "golgappa foreign policy"
                        ]

    while True:
        political_subject = random.choice(political_subjects)
        political_verb = random.choice(political_verbs)
        political_object = random.choice(political_objects)

        head_line = f" \n Breaking News: { political_subject } { political_verb } { political_object }"
        print("\t",head_line,"\n")

        save_user_input(head_line)

        user_input = input("\t If you to regenerate the fake news yes/no : ").strip().lower()
        if user_input == "no":
            break

    


elif input_user == 4:
    print("=" * 120)
    print(" Sports Madness – Over‑the‑top sports news 🏆".center(120))
    print("=" * 120)
    sports_subjects = [
                        "Cristiano Ronaldo", "Lionel Messi", "Babar Azam", "Virat Kohli", "Shoaib Akhtar",
                        "Shaheen Afridi", "Neymar Jr", "Novak Djokovic", "Michael Jordan", "Usain Bolt"
                    ]

    sports_verbs = [
                        "ne banaya record for", "ne invent ki", "ne banayi flying", "ne shuru ki", "ne paint kar diya",
                        "ne replace kar diya", "ne open ki", "ne banaya robot for", "ne start ki", "ne launch ki"
                        ]

    sports_objects = [
                        "cricket with watermelon", "goat football team", "flying cricket ball", "samosa marathon", "mango basketball",
                        "selfie tennis racket", "chapati cricket bat", "pakora swimming race", "golgappa cycling", "buffalo Olympics"
                    ]

    while True:
        sports_subject = random.choice(sports_subjects)
        sports_verb = random.choice(sports_verbs)
        sports_object = random.choice(sports_objects)

        head_line = f" \n Breaking News: { sports_subject } { sports_verb } { sports_object }"
        print("\t",head_line,"\n")

        save_user_input(head_line)

        user_input = input("\t If you to regenerate the fake news yes/no : ").strip().lower()
        if user_input == "no":
            break



elif input_user == 5:
    print("=" * 120)
    print("Celebrity Scoop – Silly and weird celebrity headlines 🎬".center(120))
    print("=" * 120)
    celebrity_subjects = [
                            "Taylor Swift", "Selena Gomez", "Justin Bieber", "Kim Kardashian", "Ariana Grande",
                            "Shah Rukh Khan", "Salman Khan", "Deepika Padukone", "Ranveer Singh", "Priyanka Chopra"
                         ]

    celebrity_verbs = [
                         "ne wear ki", "ne banayi", "ne invent ki", "ne shuru ki", "ne paint kar diya",
                         "ne launch ki", "ne open ki", "ne start ki", "ne replace kar diya", "ne banaya"
                        ]

    celebrity_objects = [
                            "shalwar kameez in New York", "mango perfume", "golgappa jewelry", "pakora dress", "flying sari",
                            "samosa handbag", "selfie dupatta", "chapati hat", "goat necklace", "biryani crown"
                        ]

    while True:
        celebrity_subject = random.choice(celebrity_subjects)
        celebrity_verb = random.choice(celebrity_verbs)
        celebrity_object = random.choice(celebrity_objects)

        head_line = f" \n Breaking News: { celebrity_subject } { celebrity_verb } { celebrity_object }"
        print("\t",head_line,"\n")

        save_user_input(head_line)

        user_input = input("\t If you to regenerate the fake news yes/no : ").strip().lower()
        if user_input == "no":
            break

elif input_user == 6:
    print("=" * 120)
    print("Foodie Headlines – Bizarre food‑related fake news 🍔".center(120))
    print("=" * 120)
    food_subjects = [
                        "Gordon Ramsay", "Nusrat Salt Bae", "Pakistani chef from Lahore", "Italian pizza master", "Turkish kebab seller",
                        "Multan mango farmer", "Karachi biryani expert", "Paris pastry chef", "Indian street food king", "New York burger master"
                    ]

    food_verbs = [
                    "ne banayi", "ne launch ki", "ne invent ki", "ne start ki", "ne banaya world’s biggest",
                    "ne open ki", "ne banaya robot for", "ne replace ki", "ne create ki", "ne paint kar diya"
                ]

    food_objects = [
                    "flying samosa", "golgappa burger", "mango ice-cream kebab", "pakora cake", "biryani chocolate",
                    "samosa pizza", "chapati pancake", "buffalo milk coffee", "goat cheese golgappa", "watermelon curry"
                ]

    while True:
        food_subject = random.choice(food_subjects)
        food_verb = random.choice(food_verbs)
        food_object = random.choice(food_objects)

        head_line = f" \n Breaking News: { food_subject } { food_verb } { food_object }"
        print("\t",head_line,"\n")

        save_user_input(head_line)

        user_input = input("\t If you to regenerate the fake news yes/no : ").strip().lower()
        if user_input == "no":
            break


elif input_user == 7:
    print("=" * 120)
    print("Tech & Space Craze – Weird tech, gadgets, and space exploration 🚀".center(120))
    print("=" * 120)

    tech_subjects = [
                        "Elon Musk", "Bill Gates", "Jeff Bezos", "Mark Zuckerberg", "Steve Jobs ka ghost",
                        "NASA scientist", "Chinese tech guru", "Indian ISRO engineer", "SpaceX astronaut", "Japanese robot inventor"
                    ]

    tech_verbs =    [
                        "ne invent ki", "ne banayi", "ne launch ki", "ne start ki", "ne create ki",
                        "ne banaya world’s first", "ne open ki", "ne paint kar diya", "ne replace ki", "ne shuru ki"
                    ]

    tech_objects =  [
                        "samosa-powered rocket", "golgappa Wi-Fi router", "flying chai cup", "mango laptop", "pakora AI robot",
                        "buffalo-shaped spaceship", "chapati drone", "goat-powered car", "ice-cream solar panel", "watermelon mobile"
                    ]

    while True:
        tech_subject = random.choice(tech_subjects)
        tech_verb = random.choice(tech_verbs)
        tech_object = random.choice(tech_objects)

        head_line = f" \n Breaking News: { tech_subject } { tech_verb } { tech_object }"
        print("\t",head_line,"\n")

        save_user_input(head_line)

        user_input = input("\t If you to regenerate the fake news yes/no : ").strip().lower()
        if user_input == "no":
            break


elif input_user == 8:
    print("=" * 120)
    print("Animal Adventures – Animals doing unbelievable things 🐒".center(120))
    print("=" * 120)

    animal_subjects = [
                        "dancing buffalo", "singing goat", "cricket-playing pigeon", "karate camel", "cycling monkey",
                        "selfie-taking cat", "DJ parrot", "swimming cow", "mango-lover elephant", "flying dog"
                    ]

    animal_verbs = [
                        "ne banaya record for", "ne start ki", "ne invent ki", "ne launch ki", "ne paint kar diya",
                        "ne shuru ki", "ne replace ki", "ne banaya", "ne open ki", "ne create ki"
                    ]

    animal_objects = [  
                        "goat Olympics", "buffalo fashion show", "mango eating contest", "chapati football match", "pakora swimming race",
                        "golgappa cricket match", "samosa marathon", "ice-cream cycling", "biryani eating challenge", "watermelon polo"
                    ]

    while True:
        animal_subject = random.choice(animal_subjects)
        animal_verb = random.choice(animal_verbs)
        animal_object = random.choice(animal_objects)

        head_line = f" \n Breaking News: { animal_subject } { animal_verb } { animal_object }"
        print("\t",head_line,"\n")

        save_user_input(head_line)

        user_input = input("\t If you to regenerate the fake news yes/no : ").strip().lower()
        if user_input == "no":
            break


elif input_user == 9:
    print("=" * 120)
    print("Festival Fun – Fake news about holidays and cultural events 🎉".center(120))
    print("=" * 120)

    festival_subjects = [
                        "Holi ke dancers", "Eid ke bakray", "Christmas Santa", "New Year fireworks master", "Basant kite master",
                        "Diwali ka pandit", "Halloween pumpkin king", "Independence Day parade leader", "Shab-e-Barat ke ladke", "Ramzan iftar chef"
                        ]

    festival_verbs = [
                        "ne banayi", "ne start ki", "ne invent ki", "ne launch ki", "ne paint kar diya",
                        "ne shuru ki", "ne replace ki", "ne open ki", "ne create ki", "ne organize ki"
                    ]

    festival_objects = [
                        "mango fireworks", "samosa kite", "golgappa Santa gift", "pakora Christmas tree", "biryani diya",
                        "chapati moon", "goat costume party", "watermelon lanterns", "ice-cream iftar", "buffalo parade"
                    ]


    while True:
        festival_subject = random.choice(festival_subjects)
        festival_verb = random.choice(festival_verbs)
        festival_object = random.choice(festival_objects)

        head_line = f" \n Breaking News: { festival_subject } { festival_verb } { festival_object }"
        print("\t",head_line,"\n")

        save_user_input(head_line)

        user_input = input("\t If you to regenerate the fake news yes/no : ").strip().lower()
        if user_input == "no":
            break



elif input_user == 10:
    print("=" * 120)
    print("Random Ridiculousness – Anything goes, pure chaos 🤪".center(120))
    print("=" * 120)
    random_subjects = [
                        "invisible man from Karachi", "talking chapati", "flying rickshaw driver", "laughing goat", "serious buffalo",
                        "mango scientist", "disco camel", "potato politician", "pizza artist", "selfie naan"
                    ]

    random_verbs = [
                        "ne invent ki", "ne start ki", "ne banayi", "ne launch ki", "ne shuru ki",
                        "ne paint kar diya", "ne replace ki", "ne open ki", "ne create ki", "ne banaya"
                    ]

    random_objects = [
                        "golgappa rain", "samosa-powered kite", "pakora moon", "watermelon robot", "chapati helicopter",
                        "goat submarine", "buffalo drone", "ice-cream volcano", "mango train", "pillow rocket"
                    ]

    while True:
        random_subject = random.choice(random_subjects)
        random_verb = random.choice(random_verbs)
        random_object = random.choice(random_objects)

        head_line = f" \n Breaking News: { random_subject } { random_verb } { random_object }"
        print("\t",head_line,"\n")

        save_user_input(head_line)

        user_input = input("\t If you to regenerate the fake news yes/no : ").strip().lower()
        if user_input == "no":
            break



print("\n" + "=" * 120)
print("Thanks for using fake news generator!".center(120))
print("=" * 120 + "\n")

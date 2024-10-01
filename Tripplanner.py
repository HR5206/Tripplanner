import mysql.connector
a1=r"""
         ________________________________________________
________|                                               |_______
\       |                  Trip Planner                 |      /
 \      |                                               |     /
 /      |_______________________________________________|     \
/__________)                                        (__________\
"""
a2=r"""
Vellore
   `,.      .   .        *   .    .      .  _    ..          .
     \,~-.         *           .    .       ))       *    .
          \ *          .   .   |    *  . .  ~    .      .  .  ,
 ,           `-.  .            :               *           ,-
  -             `-.        *._/_\_.       .       .   ,-‘
  -                 `-_.,     |n|     .      .       ;
    -                    \ ._/_,_\_.  .          . ,’         ,
     -                    `-.|.n.|      .   ,-.__,’         -
      -                   ._/_,_,_\_.    ,-‘              -
      -                     |..n..|-`’-‘                -
       -                 ._/_,_,_,_\_.                 –
         -               ,-. |…n…|                  -
           -         ,-‘._/_,_,_,_,_\_.              –
             -              |….n….|              -
              -       ._/_,_,_,_,_,_\_.         –
              -            |…..n…..|          -
           ,;         ._/_,_,_,_,_,_,_\_.         –
  `,  ‘.  `.  “.  `,  ‘.| n   ,-.   N |  “,  `.  `,  ‘.  `,  ‘,
,.:;..;;..;;.,:;,.;:,o__|__o !.|.! o__|__o;,.:;.,;;,,:;,.:;,;;:
 ][  ][  ][  ][  ][  |_i_i_H_|_|_|_H_i_i_|  ][  ][  ][  ][  ][
                     |     //=====\\     |
                     |____//=======\\____|
                         //=========\\
"""
a3=r"""
Bangalore
        __   __                     ___      _
       |  | |  |      /|           |   |   _/ \_
       |  | |  |  _  | |__         |   |_-/     \-_     _
     __|  | |  |_| | | |  |/\_     |   |  \     /  |___|
    |  |  | |  | | __| |  |   |_   |   |   |___|   |   |
    |  |  |^|  | ||  | |  |   | |__|   |   |   |   |   |
    |  |  |||  | ||  | |  |   | /\ |   |   |   |   |   |
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~/  \~~~~~~~~~~~~~~~~~~~~~~~
   ~ ~~  ~ ~~ ~~~ ~ ~ ~~ ~~ ~~ \   \__   ~  ~  ~~~~ ~~~ ~~
 ~~ ~ ~ ~~~ ~~  ~~ ~~~~~~~~~~ ~ \   \o\  ~~ ~ ~~~~ ~ ~ ~~~
   ~ ~~~~~~~~ ~ ~ ~~ ~ ~ ~ ~ ~~~ \   \o\=   ~~ ~~  ~~ ~ ~~
~ ~ ~ ~~~~~~~ ~  ~~ ~~ ~ ~~ ~ ~ ~~ ~ ~ ~~ ~~~ ~ ~ ~ ~ ~~~~
"""
a4=r"""
Gulmarg
                                   /\
                              /\  //\\
                       /\    //\\///\\\        /\
                      //\\  ///\////\\\\  /\  //\\
         /\          /  ^ \/^ ^/^  ^  ^ \/^ \/  ^ \
        / ^\    /\  / ^   /  ^/ ^ ^ ^   ^\ ^/  ^^  \
       /^   \  / ^\/ ^ ^   ^ / ^  ^    ^  \/ ^   ^  \       *
      /  ^ ^ \/^  ^\ ^ ^ ^   ^  ^   ^   ____  ^   ^  \     /|\
     / ^ ^  ^ \ ^  _\___________________|  |_____^ ^  \   /||o\
    / ^^  ^ ^ ^\  /______________________________\ ^ ^ \ /|o|||\
   /  ^  ^^ ^ ^  /________________________________\  ^  /|||||o|\
  /^ ^  ^ ^^  ^    ||___|___||||||||||||___|__|||      /||o||||||\       |
 / ^   ^   ^    ^  ||___|___||||||||||||___|__|||          | |           |
/ ^ ^ ^  ^  ^  ^   ||||||||||||||||||||||||||||||oooooooooo| |ooooooooooo|
Ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo|
"""
a5=r"""
Mumbai
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣤⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢰⣶⣶⣶⡾⠻⣿⣿⣿⣿⠟⢷⣶⣶⣶⡆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣦⣤⣿⣿⣿⣿⣤⣴⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢠⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⡄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣈⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠘⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠃⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠈⢻⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣭⣭⣭⣭⣭⣭⠀⠀⠀⠀⠀⠀⣭⣭⣭⣭⣭⣭⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠘⠛⠛⠛⠛⠛⢿⠀⠀⠀⠀⠀⠀⡿⠛⠛⠛⠛⠛⠃⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠘⠛⠛⠛⠛⠛⠛⠀⠀⠀⠀⠀⠀⠛⠛⠛⠛⠛⠛⠃⠀⠀⠀⠀
"""
a6=r"""
Goa
_\/_                 |                _\/_
/o\\             \       /            //o\
 |                 .---.                |
_|_______     --  /     \  --     ______|__
         `~^~^~^~^~^~^~^~^~^~^~^~`
"""
a7=r"""
Kolkata
                                         ^^
    ^^      ..                                       ..
            []                                       []
          .:[]:_          ^^                       ,:[]:.
        .: :[]: :-.                             ,-: :[]: :.
      .: : :[]: : :`._                       ,.': : :[]: : :.
    .: : : :[]: : : : :-._               _,-: : : : :[]: : : :.
_..: : : : :[]: : : : : : :-._________.-: : : : : : :[]: : : : :-._
_:_:_:_:_:_:[]:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:[]:_:_:_:_:_:_
!!!!!!!!!!!![]!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!![]!!!!!!!!!!!!!
^^^^^^^^^^^^[]^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^[]^^^^^^^^^^^^^
            []                                       []
            []                                       []
            []                                       []
 ~~^-~^_~^~/  \~^-~^~_~^-~_^~-^~_^~~-^~_~^~-~_~-^~_^/  \~^-~_~^-~~-
~ _~~- ~^-^~-^~~- ^~_^-^~~_ -~^_ -~_-~~^- _~~_~-^_ ~^-^~~-_^-~ ~^
   ~ ^- _~~_-  ~~ _ ~  ^~  - ~~^ _ -  ^~-  ~ _  ~~^  - ~_   - ~^_~
"""
a8=r"""
Shimla
     .-.                                                   \ /
  ( (                                |                  - * -
   ‘-`                              -+-                  / \
            \            o          _|_          \
            ))          }^{        /___\         ))
          .-#-----.     /|\     .---‘-‘---.    .-#-----.
     ___ /_________\   //|\\   /___________\  /_________\  
    /___\ |[] _ []|    //|\\    | A /^\ A |    |[] _ []| _.O,_
  ….|”#”|.|  |*|  |  …///|\\\...|   |”|   |….| |*|   |..(^)….
"""
a9=r"""
Jaipur
    |>>>                                                      |>>>
    |                     |>>>          |>>>                  |
    •	                  |             |                     *
   / \                    *             *                    / \
  /___\                 _/ \           / \_                 /___\
  [   ]                |/   \_________/   \|                [   ]
  [ I ]                /     \       /     \                [ I ]
  [   ]_ _ _          /       \     /       \          _ _ _[   ]
  [   ] U U |        {#########}   {#########}        | U U [   ]
  [   ]====/          \=======/     \=======/          \====[   ]
  [   ]    |           |   I |_ _ _ _| I   |           |    [   ]
  [___]    |_ _ _ _ _ _|     | U U U |     |_ _ _ _ _ _|    [___]
  \===/  I | U U U U U |     |=======|     | U U U U U | I  \===/
   \=/     |===========| I   | + W + |   I |===========|     \=/
    |  I   |           |     |_______|     |           |   I  |
    |      |           |     |||||||||     |           |      |
    |      |           |   I ||vvvvv|| I   |           |      |
_-_-|______|-----------|_____||     ||_____|-----------|______|-_-_
   /________\         /______||     ||______\         /________\
  |__________|-------|________\_____/________|-------|__________|
"""
a10=r"""
Indore
                                                |>>>
                                                |
                                            _  _|_  _
                                           |;|_|;|_|;|
                                           \\.    .  /
                                            \\:  .  /
                                             ||:   |
                                             ||:.  |
                                             ||:  .|
                                             ||:   |       
                                             ||: , |            
                                             ||:   |
                                             ||: . |
                                            _||_   |
                                       __ ----~    ~`---,              
"""
a4=r"""
                                  |>>>
                                  |
                    |>>>      _  _|_  _         |>>>
                    |        |;| |;| |;|        |
                _  _|_  _     \\.    .  /    _  _|_  _
               |;|_|;|_|;|    \\:. ,  /     |;|_|;|_|;|
               \\..      /    ||;   . |     \\.    .  /
                \\.  ,  /     ||:  .  |      \\:  .  /
                 ||:   |_   _ ||_ . _ | _   _||:   |
                 ||:  .|||_|;|_|;|_|;|_|;|_|;||:.  |
                 ||:   ||.    .     .      . ||:  .|
                 ||: . || .     . .   .  ,   ||:   |       
                 ||:   ||:  ,  _______   .   ||: , |        
                 ||:   || .   /+++++++\    . ||:   |
                 ||:   ||.    |+++++++| .    ||: . |
              __ ||: . ||: ,  |+++++++|.  . _||_   |
     ____--`~    ‘--~~__|.    |+++++++|----~    ~`---,

"""
a12=r"""
 ____________________
/                    \
|     Thank you !!!  |
| Your feedback will |
|    make us better  |
\____________________/
         !  !
         !  !
         L_ !
        / _)!
       / /__L
 _____/ (____)
        (____)
 _____  (____)
      \_(____)
         !  !
         !  !
         \__/
"""

a13=r"""
+==========================================+
| ______   __         ______     __   __   |
|/\  == \ /\ \       /\  __ \   /\ "-.\ \  |
|\ \  _-/ \ \ \____  \ \  __ \  \ \ \-.  \ |
| \ \_\    \ \_____\  \ \_\ \_\  \ \_\\"\_\|
|  \/_/     \/_____/   \/_/\/_/   \/_/ \/_/|
+==========================================+
"""
a14=r"""
+========================================+
| ______   ______     ______     _____   |
|/\  ___\ /\  __ \   /\  __ \   /\  __-. |
|\ \  __\ \ \ \/\ \  \ \ \/\ \  \ \ \/\ \|
| \ \_\    \ \_____\  \ \_____\  \ \____-|
|  \/_/     \/_____/   \/_____/   \/____/|
+========================================+
"""
a15=r"""
+=========================================+
| ______     ______   ______     __  __   |
|/\  ___\   /\__  _\ /\  __ \   /\ \_\ \  |
|\ \___  \  \/_/\ \/ \ \  __ \  \ \____ \ |
| \/\_____\    \ \_\  \ \_\ \_\  \/\_____\|
|  \/_____/     \/_/   \/_/\/_/   \/_____/|
+=========================================+
"""
a16=r"""
+====================================================================================================+
| ______     ______   ______   ______     ______     ______     ______   __     ______     __   __   |
|/\  __ \   /\__  _\ /\__  _\ /\  == \   /\  __ \   /\  ___\   /\__  _\ /\ \   /\  __ \   /\ "-.\ \  |
|\ \  __ \  \/_/\ \/ \/_/\ \/ \ \  __<   \ \  __ \  \ \ \____  \/_/\ \/ \ \ \  \ \ \/\ \  \ \ \-.  \ |
| \ \_\ \_\    \ \_\    \ \_\  \ \_\ \_\  \ \_\ \_\  \ \_____\    \ \_\  \ \_\  \ \_____\  \ \_\\"\_\|
|  \/_/\/_/     \/_/     \/_/   \/_/ /_/   \/_/\/_/   \/_____/     \/_/   \/_/   \/_____/   \/_/ \/_/|
+====================================================================================================+
"""

print(a1)
print("List of places") 
print("""
1.Bangalore
2.Bhubaneswar
3.Goa
4.Gulmarg
5.Indore
6.Jaipur
7.Kolkata
8.Mumbai
9.Shimla
10.Vellore
""")
def view(cursor, city):
    print("🍽 1. Local cuisine")
    print("🏨 2. Explore cozy places to stay")
    print("🎡 3. Discover exciting attractions")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print(a14)
        cursor.execute(f"SELECT food_name, food_rating, food_cost, famous_hotel FROM {city}")
        rows = cursor.fetchall()
        for row in rows:
            print(f"Food Name: {row[0]}\nFood Rating: {row[1]}\nFood Cost: {row[2]}\nFamous Hotel: {row[3]}\n")
    elif choice == 2:
        print(a15)
        cursor.execute(f"SELECT place_name, place_rating, place_expenses FROM {city}")
        rows = cursor.fetchall()
        for row in rows:
            print(f"Place Name: {row[0]}\nPlace Rating: {row[1]}\nPlace Expenses: {row[2]}\n")
    elif choice == 3:
        print(a16)
        cursor.execute(f"SELECT attraction_name, attraction_rating, attraction_expenses FROM {city}")
        rows = cursor.fetchall()
        for row in rows:
            print(f"Attraction Name: {row[0]}\nAttraction Rating: {row[1]}\nAttraction Expenses: {row[2]}\n")

def plan(cursor, city):
    connection = mysql.connector.connect(user='root', password='5206', host='localhost',database="tripplanner5206")
    cursor = connection.cursor()
    cursor.execute(f"SELECT food_name FROM {city}")
    foods = cursor.fetchall()
    cursor.execute(f"SELECT place_name FROM {city}")
    places = cursor.fetchall()
    cursor.execute(f"SELECT attraction_name FROM {city}")
    attractions = cursor.fetchall()
    print("🍲 Foods:")
    i = 1
    for food in foods:
        print(f"{i}. {food[0]}")
        i += 1
    print("🏠 Places to stay:")
    
    i = 1
    for place in places:
        print(f"{i}. {place[0]}")
        i += 1
    print("🎡 Attractions:")
    
    i = 1
    for attraction in attractions:
        print(f"{i}. {attraction[0]}")
        i += 1
    food_indices = input("Enter the serial numbers of the foods: ").split()
    place_indices = input("Enter the serial numbers of the places: ").split()
    attraction_indices = input("Enter the serial numbers of the attractions: ").split()
    total_cost = 0
    plan = "🗺️ Your Adventure: "
    for food_index in food_indices:
        cursor.execute(f"SELECT food_cost FROM {city} WHERE food_name = '{foods[int(food_index)-1][0]}'")
        food_cost = cursor.fetchone()[0]
        total_cost += food_cost
        plan += f"\n🍲 Food: {foods[int(food_index)-1][0]}"
    for place_index in place_indices:
        cursor.execute(f"SELECT place_expenses FROM {city} WHERE place_name = '{places[int(place_index)-1][0]}'")
        place_expenses = cursor.fetchone()[0]
        total_cost += place_expenses
        plan += f"\n🏠 Place: {places[int(place_index)-1][0]}"
    for attraction_index in attraction_indices:
        cursor.execute(f"SELECT attraction_expenses FROM {city} WHERE attraction_name = '{attractions[int(attraction_index)-1][0]}'")
        attraction_expenses = cursor.fetchone()[0]
        total_cost += attraction_expenses
        plan += f"\n🎡 Attraction: {attractions[int(attraction_index)-1][0]}"
    num_people = int(input("Enter the number of adventurers: "))
    total_cost *= num_people
    plan += f"\n💰 Total cost for {num_people} adventurers: {total_cost}"
    print("📅 Enter the time of visit for each activity:")
    food_times = {}
    for food_index in food_indices:
        food_time = input(f"Time for {foods[int(food_index)-1][0]}: ")
        food_times[foods[int(food_index)-1][0]] = food_time
    place_times = {}
    for place_index in place_indices:
        place_time = input(f"Time for {places[int(place_index)-1][0]}: ")
        place_times[places[int(place_index)-1][0]] = place_time
    attraction_times = {}
    for attraction_index in attraction_indices:
        attraction_time = input(f"Time for {attractions[int(attraction_index)-1][0]}: ")
        attraction_times[attractions[int(attraction_index)-1][0]] = attraction_time
        
    for food, time in food_times.items():
        plan += f"\n🕒 Food: {food}, Time planned: {time}"
    
    for place, time in place_times.items():
        plan += f"\n🕒 Place: {place}, Time planned: {time}"
    
    for attraction, time in attraction_times.items():
        plan += f"\n🕒 Attraction: {attraction}, Time planned: {time}"
    
    print(a13)
    print(plan)
     
    cursor.execute("INSERT INTO plan (plan_details) VALUES (%s)", (plan,))
    connection.commit()
    cursor.execute("SELECT LAST_INSERT_ID()")
    plan_id = cursor.fetchone()[0]
    print("Plan_id:",plan_id)

    return plan_id

def feedback(plan_id):
    connection = mysql.connector.connect(user='root', password='5206', host='localhost',database="tripplanner5206")
    cursor = connection.cursor()
    cursor.execute("SELECT plan_details FROM plan WHERE plan_id = %s", (plan_id,))
    print(a13)
    plan = cursor.fetchone()[0]
     
    print(f"Your adventure was:\n{plan}")
    rating = input("Rate your adventure (1-5): ")
    feedback = input("Share your feedback: ")
    print(a12)
    cursor.close()
    connection.close()

def main():
    connection = mysql.connector.connect(user='root', password='5206', host='localhost',database="tripplanner5206")
    cursor = connection.cursor()
    while True:
        print("Options")
        print()
        print("👀 1. View the adventure options")
        print("📝 2. Plan your adventure")
        print("💬 3. Share your Feedback")
        print("🚪 4. Exit the adventure")
        print()
        choice = int(input("Choose your next step: "))
        if choice in [1, 2]:
            city = input("Enter the city of your next adventure: ")
            if city.lower()=="bangalore":
                print(a3)
                print("""Bangalore, also known as Bengaluru, is a city in the southern part of India. It is the capital of the state of Karnataka and is located on the Deccan Plateau. The city is known for its prestigious institutes, colleges, and universities. It is also home to several IT organizations and aerospace industries, making it one of the fastest-growing cities in India. Bangalore has a tropical climate with three prominent seasons: monsoon, winter, and summer. The city is famous for its parks and gardens, including Lal Bagh Botanical Gardens and Ulsoor Lake. Bangalore is also known for its arts and crafts like ivory carving, doll making, Mysore painting, and wood carving""")
            elif city.lower()=="bhubaneswar":
                print(a4)
                print("""Bhubaneswar, the capital of the Indian state of Odisha, is a city with a rich cultural heritage. The city is known for its ancient temples, including the Lingaraj Temple and the Mukteswara Temple. Bhubaneswar is also home to several educational institutions, including the Indian Institute of Technology and the National Institute of Science Education and Research. The city has a tropical climate with three prominent seasons: summer, monsoon, and winter. Bhubaneswar is also known for its arts and crafts like applique work, stone carving, and Pattachitra painting. The city has a rich history dating back to the 3rd century BCE and is a popular tourist destination in India""")
            elif city.lower()=="goa":
                print(a6)
                print("""Goa is a state located on the west coast of India. It is known for its beautiful beaches, vibrant nightlife, and unique blend of Indian and Portuguese cultures. The state was a Portuguese colony until 1961, and this influence can still be seen in its architecture, cuisine, and culture 12. Goa’s beaches are some of the most beautiful in the world, with clear blue waters and golden sands. The state is also home to several wildlife sanctuaries and nature reserves, such as the Bhagwan Mahavir Wildlife Sanctuary and the Salim Ali Bird Sanctuary. Goa is a popular tourist destination, attracting visitors from all over the world""")
            elif city.lower()=="gulmarg":
                print(a4)
                print("""Gulmarg is a town, hill station, and popular tourist destination located in the Pir Panjal Range of the Indian union territory of Jammu and Kashmir. It is situated at an altitude of 2,730 meters (8,960 feet) above sea level 12. The town is surrounded by snow-covered lofty Himalayas, meadows of flowers, deep ravines, and evergreen forested valleys 2. Gulmarg is known for its skiing opportunities and has the world’s second-highest Gondola ride 2. The name Gulmarg is derived from two Persian words: “Gul” meaning flowers and “Marg” meaning meadow 1. The town has historical importance for Kashmiris and was discovered by Yousuf Shah Chak, the last Chak ruler who reigned from 1579 to 1586 AD""")
            elif city.lower()=="indore":
                print(a10)
                print("""Indore is the largest city in the Indian state of Madhya Pradesh. It is known for its rich black soil and cotton textiles, which have earned it the fourth position in the country. The city is also famous for its elegant bangles and delicious food. Indore is home to several prestigious universities and colleges, making it an educational hub. The people of Indore are known for their hospitality and formality. The city celebrates several festivals with happiness and excitement. The Yeshwant club, named after Maharaja Yeshwant Rao Holkar II, is a popular art center in Indore. The city has several historical locations that attract tourists. Jalebi and Poha are the most popular delicacies in Indore""")
            elif city.lower()=="jaipur":
                print(a9)
                print("""Jaipur is the capital of Rajasthan, India. It is also known as the Pink City because of the terracotta pink color of its buildings. The city was founded in 1727 by Maharaja Sawai Jai Singh II and is famous for its rich history, culture, and architecture. Jaipur has several tourist attractions, including the City Palace, Hawa Mahal, and Amber Fort. The city is also known for its textiles, jewelry, and handicrafts. Jaipur is home to several prestigious universities and colleges, making it an educational hub. The city celebrates several festivals with happiness and excitement. Jalebi and Poha are the most popular delicacies in Jaipur""")
            elif city.lower()=="kolkata":
                print(a7)
                print("""Kolkata is the capital of the Indian state of West Bengal. It is known as the “City of Joy” and is famous for its rich history, artistic heritage, and intellectual prowess. The city has a deep history and was the capital of British India. Kolkata is home to several prestigious universities and colleges, making it an educational hub. The city celebrates several festivals with happiness and excitement. Kolkata is famous for its places of visit like the Victoria Memorial Hall, the Alipore Zoo, the National Library, the Eden Gardens, the Maidan, the Esplanade, The Birla Planetarium, and others. Kolkata is also famous for its sweets like Rasgulla, Pantua, Sandesh, and Misti Doi""")
            elif city.lower()=="mumbai":
                print(a5)
                print("""Mumbai, also known as Bombay, is the capital city of the Indian state of Maharashtra. It is the financial capital of India and is home to several prestigious universities and colleges. Mumbai has a diverse culture with people from different religions, speaking various languages. The city is known for its rich history, artistic heritage, and intellectual prowess. Mumbai is the birthplace of Indian cinema and has a blend of traditional and cosmopolitan cultures due to its history as a major trading center. The city has contemporary art featured in art spaces and private commercial galleries. Mumbai is the sixth most populous metropolitan area in the world with a population of over 23 million""")
            elif city.lower()=="shimla":
                print(a8)
                print("""Shimla is a beautiful hill station located in the Indian state of Himachal Pradesh. It is situated at an altitude of 2,276 meters (7,467 feet) above sea level 1. The town is surrounded by lush green hills, snow-capped mountains, and dense forests. Shimla is known for its pleasant weather and scenic beauty. It was discovered by the British in the early 19th century and served as the summer capital of India during the British Raj 1. The town has several tourist attractions, including the Mall Road, Ridge, and Jakhu Temple. Shimla is also famous for its handicrafts, woolen clothes, and wooden artifacts""")
            elif city.lower()=="vellore":
                print(a2)
                print("""Vellore is a city located in the Indian state of Tamil Nadu. It is situated on the banks of the Palar River and is separated into four zones that are further subdivided into 60 wards, covering an area of 87.915 km² and housing a population of 696,110 as per the 2011 census 1. The city is known for its rich history, culture, and heritage. Vellore is home to several prestigious universities and colleges, including Christian Medical College & Hospital and Vellore Institute of Technology (VIT) 1. The city is also famous for its leather exports, which account for more than 37% of India’s leather exports and leather-related products""")
            print()
            if choice == 1:
                view(cursor, city)
            elif choice == 2:
                plan_id = plan(cursor, city)
        elif choice == 3:
            plan_id = int(input("Enter the ID of your planned adventure: "))
            feedback(plan_id)
        elif choice == 4:
            print("👋 Safe travels on your next adventure!")
            break

    cursor.close()
    connection.close()

if __name__ == "__main__":
    main()

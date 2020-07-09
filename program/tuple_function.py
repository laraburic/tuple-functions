FileName = input("File name: ")
FileData = []
over = 0
try:
    file = open(FileName,"r") 
    FileData = file.read() 
    FileData = FileData.strip()
    FileData = FileData.split("\n")
except Exception as e: 
    print("Wrong file name: ", FileName)
    over = 1
if over != 1:

    def player_tuple(str):
        player_tuple = tuple(str.split(" "))
        return(player_tuple)

    players_data = []
    for line in FileData:
        players_data.append(player_tuple(line))

    def print_playerTu(player_tuple):
        name = player_tuple[3] + ", " + player_tuple[2]
        print("{:30} {:15} {:15} {:8}".format (name, player_tuple[4], player_tuple[1], player_tuple[0]))
    for i in range (len(players_data)):
        print_playerTu(players_data[i])
    error = 0
    print("\n")
    print("Choose your option: ")
    print("1. Full details of a player with a given last name.")
    print("2. Full details of all players with a salary in a particular range.")
    print("3. First and last names of all players of a team.")
    print("4. Quit.")
          
    option = input()
    while option != "4":
        if option =="1":
            last_name = input("Please enter the player's last name:")
            nores = 0
            for i in range(len(players_data)):
                player = str(players_data[i]).split(", ")
                playerlast_name="'"+last_name+"'"
                if player[3] == playerlast_name:
                    nores = 1
                    print_playerTu(players_data[i])
            if nores == 0:
                print("No results found.")
           
                
        elif option == "2":
            min_salary = int(input("Your minimum salary:"))
            max_salary = int(input("Your maximum salary:"))
            while min_salary > max_salary:
                print("Minimum salary is greater than maximum salary!")
                min_salary = int(input("Your minimum salary:"))
                max_salary = int(input("Your maximum salary:"))
            error = 0
            for i in range(len(players_data)):
                player = str(players_data[i]).split(", ")
                salary = int(float(player[4].replace("'","").replace(",","").replace(")","")))
                if salary in range (min_salary, max_salary + 1):
                    print_playerTu(players_data[i])
                    error = 1
            if error == 0:
                print("No result")
            
                
        elif option == "3":
            chosenTeam = input("Enter team name:")
            error = 0
            for i in range(len(players_data)):
                player=str(players_data[i]).split(", ")
                playersTeam = player[0].replace("'", "").replace("(", "")
                if chosenTeam == playersTeam:
                    print(player[3].replace("'", "")+" "+player[2].replace("'", ""))
                    error = 1
            if error == 0:
                print("No result")
                            
        else:
            print("Incorrect input.")
            option = input()
            error = 1

#after the loop:
            
        if error == 0:
            option = input("Type 1 to search using position and team or type 2 to search using min and max salary.")
            error = 1
            if option == "1":
                chosenPosition = input("Supply the position:")
                error = 0
                for i in range(len(players_data)):
                    player=str(players_data[i]).split(", ")
                    playersPosition = player[1].replace("'", "")
                    if playersPosition == chosenPosition:
                        print_playerTu(players_data[i])
                        error = 1
                if error == 0:
                    print("No result")
                chosenTeam = input("Supply the team:")
                error = 0
                for i in range(len(players_data)):
                    player = str(players_data[i]).split(", ")
                    playersTeam = player[0].replace("'", "").replace("(", "")
                    if chosenTeam == playersTeam:
                        print(player[3].replace("'", "")+" " + player[2].replace("'", ""))
                        error = 1

                #if chosenPosition and chosenTeam
                if error == 0:
                    print("No result")
                break

            if option == "2":
                min_salary = int(input("Your minimum salary:"))
                max_salary = int(input("Your maximum salary:"))
                while min_salary > max_salary:
                    print("Minimum salary is greater than maximum salary!")
                    min_salary = int(input("Your minimum salary:"))
                    max_salary = int(input("Your maximum salary:"))
                error = 0
                for i in range(len(players_data)):
                    player = str(players_data[i]).split(", ")
                    salary = int(float(player[4].replace("'","").replace(",","").replace(")","")))
                    if salary in range (min_salary, max_salary +  1):
                        print_playerTu(players_data[i])
                        error = 1
                if error == 0:
                    print("No result")
        error == 0

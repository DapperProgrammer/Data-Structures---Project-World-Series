# Arrays defined outside the scope of the functions so they may be accessed globally.
team_AL_Winning_Teams_dict = {}
team_NL_Winning_Teams_dict = {}
winning_teams_dict = {}
times_in_world_series_dict= {}
specific_year_teams_dict = {}


def get_Data():
	# Assigns contents of worldSeries.txt to 'baseball_teams' "r" means read
	baseball_teams = open('worldSeries.txt','r')

	# For every item of information in the worldSeries.txt file which is assigned to 'baseball_teams'
	for item in baseball_teams:
		# Split the information by ',' and add it to a list array called "line"
		line = item.split(',')
		# Assign the contents at index '0' to the variable 'year'
		year = line[0]
		team_name1 = line[1]
		league1 = line[2]
		win_loss = line[3]
		team_name2 = line[4]
		league2 = line[5]

		# Winning AL Teams
		if league1 == "AL":
			# check to see if that team is in team_AL_dict
			if team_name1 in team_AL_Winning_Teams_dict:
				# If the team is already in team_AL_dict, add to score.
				team_AL_Winning_Teams_dict[team_name1] = team_AL_Winning_Teams_dict[team_name1] + 1
			else:
				# If team not in team_AL_dict, add team to the dictionary.
				team_AL_Winning_Teams_dict[team_name1] = 1

		# Winning NL Teams
		if league1 == "NL":
			if team_name1 in team_NL_Winning_Teams_dict:
				team_NL_Winning_Teams_dict[team_name1] +=1
			else:
				team_NL_Winning_Teams_dict[team_name1] = 1

		# Times a team won the world series
		if team_name1 in winning_teams_dict:
			winning_teams_dict[team_name1] = winning_teams_dict[team_name1] + 1
		else:
			winning_teams_dict[team_name1] = 1

		# Specific year for a winning and losing team
		specific_year_teams_dict[year] = [team_name1, team_name2]

def AL_winningTeams():
	# For every key and value in team_AL_Winning_Teams_dict
	for key, value in team_AL_Winning_Teams_dict.items():
		print('Team:', key, 'won', value, 'time(s),', 'League, AL')

	print()
	print("**************************************")	
	print()
	
def NL_winningTeams():
	# For every key and value in team_NL_Winning_Teams_dict
	for key, value in team_NL_Winning_Teams_dict.items():
		print('Team:', key, 'won', value, 'time(s),', 'League, NL')
		
	print()
	print("**************************************")	
	print()

def specific_team_times_won():
	user_team_choice = input('Enter a team name: ')
	team = user_team_choice.title()

	if team in winning_teams_dict:
		print("Team: ", team, "won", winning_teams_dict[team], "time(s).")
	else:
		print("Team name not found!")
		
	print()
	print("**************************************")	
	print()

def specific_Team_Times_In_World_Series():
	total = 0
	user_team_choice = input("Enter a team: ")
	team = user_team_choice.title()

	# Finds how many times the users choice appears within the file
	with open('worldSeries.txt','r') as baseball_teams:
		for items in baseball_teams:
			team_to_find = items.find(team)
			if team_to_find != -1 and team_to_find != 0:
				total = total + 1
	print(total)

	print()
	print("**************************************")
	print()


def specific_year_who_won_who_lost():
  year_choice = input('Enter a year to see who won and who lost: ')
  if year_choice in specific_year_teams_dict:
    print(specific_year_teams_dict[year_choice])
  else:
    print('Error: Year not found')

def main():
	user_choice = 0
	while (user_choice != 6):
		print('1. All willing teams from AL')
		print('2. All winning teams from NL')
		print('3. How many times a specific team has won')
		print('4. Specific team how many times they were in the World Series')
		print('5. Specific year who won who lost')
		print('6. Quit')
		print()
		user_choice = (int(input('Welcome to the main menu, please choose an option: ')))
		print()

		if user_choice == 1:
			AL_winningTeams()
		elif user_choice == 2:
			NL_winningTeams()
		elif user_choice == 3:
			specific_team_times_won()
		elif user_choice == 4:
			specific_Team_Times_In_World_Series()
		elif user_choice == 5:
			specific_year_who_won_who_lost()
		elif user_choice == 6:
			print("Session Ended.")
		else:
			print('Error Invalid selection. Please try again.')

get_Data() #Calls the function 'get_Data'
main()
line = []
winningTeamDict = {}
team_AL_dict = {}

def getData():
    baseball_teams = open('worldSeries.txt','r')
    for item in baseball_teams:
        line = item.split(',')
        year = line[0]
        team_name1 = line[1]
        league1 = line[2]
        win_loss = line[3]
        team_name2 = line[4]
        league2 = line[5]
        lineStrip= map(str.strip, line)
        print(line)

        # If league1 in line[2] i1s 'AL'
        if league1 == "AL":
            # check to see if that team is in team_AL_dict
            if team_name1 in team_AL_dict:
                # If the team is already in team_AL_dict, add to score.
                team_AL_dict[team_name1] = team_AL_dict[team_name1] + 1
            else:
                # If team not in team_AL_dict, add team to the dictionary.
                team_AL_dict[team_name1] = 1

        if team_name1 in winningTeamDict:
            winningTeamDict[team_name1] = winningTeamDict[team_name1] + 1
        else:
            winningTeamDict[team_name1] = 1

def main():
    getData()


main()

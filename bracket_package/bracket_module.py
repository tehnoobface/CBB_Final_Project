import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
import seaborn as sns
import os
#import math


class Bracket:
    """Create a bracket object"""
    def __init__(self):
        self.teams = self.getData()
        self.method = self.getMethod()
        # Save the next four as empty dataframes:
        self.south = pd.DataFrame()
        self.east = pd.DataFrame()
        self.west = pd.DataFrame()
        self.midwest = pd.DataFrame()
        self.region_winner = pd.DataFrame()
    
    def getData(self):
        #teams = pd.read_csv('data/cbb20.csv')
        #return teams
        print("Choose a dataset. Data found in /data, with 2020 test dataset being ../data/cbb20.csv : ", end='')
        teams = pd.read_csv(input())    # Input path to (and including) the dataset
        #print(teams.head())
        return teams
        
    """
    def getPower(self, teams):
        power = teams['BARTHAG']
        print("Power test! ", end='')
        return power
        
    def getRank(self, teams):
        rank = teams['RK']
        print("Rank test! ", end='')
        return rank
        
    def getWins(self, teams):
        wins = teams['W']
        print("Win test! ", end='')
        return wins
    """
    def getBracketTeams(self):
        teams = self.teams
        print("Enter the Playoff Bracket Year (ex. '2020'): ", end='')
        year = input()
        if year == '2020':
            south_teams = ["Baylor", "Texas Southern", "Cincinnati", "VCU", "Illinois", "East Tennessee St.", "Auburn", "College of Charleston", "Iowa", "Mississippi St.", "Seton Hall", "Bowling Green", "Ohio St.", "Northern Iowa", "Louisville", "Murray St."]
            east_teams = ["San Deigo St.", "Memphis", "Saint Mary's", "Texas Tech", "Kentucky", "Arizona St.", "Butler", "Vermont", "Creighton", "Virginia", "Maryland", "UC Irvine", "Rutgers", "Houston", "Duke", "Wright St."]
            west_teams = ["Gonzaga", "Montana", "Florida", "Stanford", "Penn St.", "Stephenn F. Austin", "Oregon", "New Mexico State", "Colorado", "BYU", "Villanova", "Colgate", "Michigan", "Arkansas", "West Virginia", "North Dakota St."]
            midwest_teams = ["Kansas", "Princeton", "Wisconsin", "Rhode Island", "Arizona", "Liberty", "Michigan St.", "North Texas", "LSU", "Purdue", "Florida St.", "Little Rock", "Marquette", "Indiana", "Dayton", "Winthrop"]
        elif year == '2021':
            south_teams = ["Baylor", "Hartford", "North Carolina", "Wisconsin", "Villanova", "Winthrop", "Purdue", "North Texas", "Texas Tech", "Utah St.", "Arkansas", "Colgate", "Florida", "Virginia Tech", "Ohio St.", "Oral Roberts"]
            east_teams = ["Michigan", "Texas Southern", "LSU", "St. Bonaventure", "Colorado", "Georgetown", "Florida St.", "UNC Greensboro", "BYU", "UCLA", "Abilene Christian", "Texas", "UConn", "Maryland", "Alabama", "Iona"]
            west_teams = ["Gonzaga", "Norfolk St.", "Oklahoma", "Missouri", "Creighton", "UC Santa Barbara", "Virginia", "Ohio", "USC", "Drake", "Kansas", "Eastern Washington", "Oregon", "VCU", "Iowa", "Grand Canyon"]
            midwest_teams = ["Illinois", "Drexel", "Loyola Chicago", "Georgia Tech", "Tennessee", "Oregon St.", "Oklahoma St.", "Liberty", "San Diego St.", "Syracuse", "West Virginia", "Morehead St.", "Clemson", "Rutgers", "Houston", "Cleveland St."]
        elif year == '2022':
            south_teams = ['Arizona', 'Wright St.', 'Seton Hall', 'TCU', 'Houston', ' UAB', 'Illinois', 'Chattanooga', 'Colorado St.', 'Michigan', 'Tennessee', 'Longwood', 'Ohio St.', 'Loyola Chicago', 'Villanova', 'Delaware']
            east_teams = ['Baylor', 'Norfolk St.', 'North Caroina', 'Marquette', "Saint Mary's", 'Indiana', 'UCLA', 'Akron', 'Texas', 'Virginia Tech', 'Purdue', 'Yale', 'Murray St.', 'San Francisco', 'Kentucky', "Saint Peter's"]
            west_teams = ['Gonzaga', 'Georgia St.', 'Boise St.', 'Memphis', 'UConn', 'New Mexico St.', 'Arkansas', 'Vermont', 'Alabama', 'Notre Dame', 'Texas Tech', 'Montana St.', 'Michigan St.', 'Davidson', 'Duke', 'Cal St. Fullerton']
            midwest_teams = ['Kansas', 'Texas Southern', 'San Diego St.', 'Creighton', 'Iowa', 'Richmond', 'Providence', 'South Dakota St.', 'LSU', 'Iowa St.', 'Wisconsin', 'Colgate', 'Southern California', 'Miami', 'Auburn', 'Jacksonville St.']
        elif year == '2019':
            south_teams = ['Virginia', 'Gardner Webb', 'Mississippi', 'Oklahoma', 'Wisconsin', 'Oregon', 'Kansas St.', 'UC Irvine', 'Villanova', "Saint Mary's", 'Purdue', 'Old Dominion', 'Cincinnati', 'Iowa', 'Tennessee', 'Colgate']
            east_teams = ['Duke', 'North Dakota St.', 'VCU', 'UCF', 'Mississippi St.', 'Liberty', 'Virginia Tech', 'Saint Louis', 'Maryland', 'Belmont', 'LSU', 'Yale', 'Louisville', 'Minnesota', 'Michigan St.', 'Bradley']
            west_teams = ['Gonzaga', 'Fairleigh Dickinson', 'Syracuse', 'Baylor', 'Marquette', 'Murray St.', 'Florida St.', 'Vermont', 'Buffalo', 'Arizona St.', 'Texas Tech', 'Northern Kentucky', 'Nevada', 'Florida', 'Michigan', 'Montana']
            midwest_teams = ['North Carolina', 'Iona', 'Utah St.', 'Washington', 'Auburn', 'New Mexico St.', 'Kansas', 'Northeastern', 'Iowa St.', 'Ohio St.', 'Houston', 'Georgia St.', 'Wofford', 'Seton Hall', 'Kentucky', 'Abilene Christian']
        elif year == '2023':
            south_teams = []
            east_teams = []
            west_teams = []
            midwest_teams = []
        else:
            print("Invalid year. Try again.")
            self.getBracketTeams()
        
        #south = teams[teams["TEAM"].isin(south_teams)]
        south = teams.loc[teams["TEAM"].isin(south_teams)].set_index("TEAM").reindex(south_teams).reset_index()
        east = teams.loc[teams["TEAM"].isin(east_teams)].set_index("TEAM").reindex(east_teams).reset_index()
        west = teams.loc[teams["TEAM"].isin(west_teams)].set_index("TEAM").reindex(west_teams).reset_index()
        midwest = teams.loc[teams["TEAM"].isin(midwest_teams)].set_index("TEAM").reindex(midwest_teams).reset_index()
        # print south to double check
        #print(south)
        self.south = south
        self.east = east
        self.west = west
        self.midwest = midwest

    def getMethod(self):
        teams = self.teams
        #combine south, east, west, and midwest teams into one "teams" df:
        print("Select Ranking Method; POWER, RANK, WIN, SEED? ", end='')
        rank = input().upper()
        if rank == 'POWER':
            method = getPower(teams)
            #print(method.head())  # Test methods, works! All power column values are stored as list in method
            return method
        elif rank == 'RANK':
            method = getRank(teams)
            return method
        elif rank == 'WIN':
            method = getWins(teams)
            return method
        elif rank == 'SEED':
            method = getSeed(teams)
            return method
        else:
            print("Invalid input. Try again.")
            self.getMethod()
            #getMethod(self)


    def generateBracket(self, region_teams, method):
        num_teams = len(region_teams)
        num_rounds = int(4)

        for round_num in range(num_rounds):
            round_teams = int(num_teams / (2 ** (round_num + 1)))
            spacing = " " * (2 ** (num_rounds + round_num - 1))
            winners = []
            winner = []
            print(f"Round {round_num + 1}:")

            for i in range(round_teams):
                # team1 is the first team in the TEAM column of region_teams:
                team1 = region_teams.iloc[i * 2]
                team2 = region_teams.iloc[i * 2 + 1]
                method = str(method)

                if method == 'W' or method == 'BARTHAG':
                    winner = team1 if team1[method] > team2[method] else team2
                elif method == 'RK' or method == 'SEED':
                    winner = team1 if team1[method] < team2[method] else team2
                else:
                    print("Invalid method. Try again.")
                    self.getMethod()
                winners.append(winner)
                print(f"{spacing}{team1['TEAM']} vs {team2['TEAM']} -> Winner: {winner['TEAM']}")

            region_teams = pd.DataFrame(winners)

        final_winner = region_teams.iloc[0]['TEAM']
        print(f"{final_winner} advances to the Final Four!")

        #print(self.region_winner)  # Prints the dataframe of winners after all rounds
        #return self.region_winner
            

            
    def simulateOverallWinner(self, method):

        method = str(method)

        if method == 'W' or method == 'BARTHAG':
            winner1 = self.south.loc[self.south[method].idxmax()]
            winner2 = self.east.loc[self.east[method].idxmax()]
            winner3 = self.west.loc[self.west[method].idxmax()]
            winner4 = self.midwest.loc[self.midwest[method].idxmax()]
        elif method == 'RK' or method == 'SEED':
            winner1 = self.south.loc[self.south[method].idxmin()]
            winner2 = self.east.loc[self.east[method].idxmin()]
            winner3 = self.west.loc[self.west[method].idxmin()]
            winner4 = self.midwest.loc[self.midwest[method].idxmin()]
        else:
            print("An Error Occured While Getting Final 4.")
            self.getMethod()
        print()
        print(f"Final Four: {winner1['TEAM']}, {winner2['TEAM']}, {winner3['TEAM']}, {winner4['TEAM']}")
        if method == 'W' or method == 'BARTHAG':
            final_winner1 = winner1 if winner1[method] > winner2[method] else winner2
            final_winner2 = winner3 if winner3[method] > winner4[method] else winner4
        elif method == 'RK' or method == 'SEED':
            if winner1[method] < winner2[method]:
                final_winner1 = winner1
            elif winner1[method] > winner2[method]:
                final_winner1 = winner2
            else:
                print("The teams are the same Seed and tied. Selecting Random Winner.")
                final_winner1 = winner1 if np.random.randint(2) == 0 else winner2
            if winner3[method] < winner4[method]:
                final_winner2 = winner3
            elif winner3[method] > winner4[method]:
                final_winner2 = winner4
            else:
                print("The teams are the same Seed and tied. Selecting Random Winner.")
                final_winner2 = winner3 if np.random.randint(2) == 0 else winner4
        else:
            print("An Error Occured While Ranking the Final 4.")
            self.getMethod()
        print()
        print(f"Playoff Finals: {final_winner1['TEAM']} vs {final_winner2['TEAM']}")

    # Determine the overall winner
        overall_winner = final_winner1 if final_winner1.loc[method] < final_winner2.loc[method] else final_winner2
        print()
        print(f"NCAA D1 Division Champs: {overall_winner['TEAM']}")
        return overall_winner

        


def getPower(teams):
    power = 'BARTHAG'
    #power = teams['BARTHAG']
    #print("Power test! ", end='')
    return power

def getRank(teams):
    rank = 'RK'
    #rank = teams['RK']
    #print("Rank test! ", end='')
    return rank

def getWins(teams):
    wins = 'W'
    #wins = teams['W']
    #print("Win test! ", end='')
    return wins

def getSeed(teams):
    seed = 'SEED'
    return seed


def run():
    os.system('cls' if os.name == 'nt' else 'clear')
    bracket = Bracket()
    #bracket.getData()
    #bracket.getMethod()
    bracket.getBracketTeams()
    bracket.generateBracket(bracket.south, bracket.method)
    bracket.generateBracket(bracket.east, bracket.method)
    bracket.generateBracket(bracket.west, bracket.method)
    bracket.generateBracket(bracket.midwest, bracket.method)
    bracket.simulateOverallWinner(bracket.method)

if __name__=='__main__':
    run()

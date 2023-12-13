import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import math


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
        print("Choose a dataset. The 2020 test dataset is ../data/cbb20.csv : ", end='')
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
            south_teams = []
            east_teams = []
            west_teams = []
            midwest_teams = []
        
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
        print("Select Ranking Method; POWER, RANK, or WIN? ", end='')
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
                elif method == 'RK':
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
        elif method == 'RK':
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
        elif method == 'RK':
            final_winner1 = winner1 if winner1[method] < winner2[method] else winner2
            final_winner2 = winner3 if winner3[method] < winner4[method] else winner4
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
    print("Power test! ", end='')
    return power

def getRank(teams):
    rank = 'RK'
    #rank = teams['RK']
    print("Rank test! ", end='')
    return rank

def getWins(teams):
    wins = 'W'
    #wins = teams['W']
    print("Win test! ", end='')
    return wins


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

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import os
import math
import random


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
        south_teams = ["Baylor", "Texas Southern", "Cincinnati", "VCU", "Illinois", "East Tennessee St.", "Auburn", "Charleston", "Iowa", "Mississippi State", "Seton Hall", "Bowling Green", "Ohio State", "Northern Iowa", "Louisville", "Murray State"]
        east_teams = ["San Deigo St.", "Memphis", "Saint Mary's", "Texas Tech", "Kentucky", "Arizona St.", "Butler", "Vermont", "Creighton", "Virginia", "Maryland", "UC Irvine", "Rutgers", "Houston", "Duke", "Wright St."]
        west_teams = ["Gonzaga", "Montana", "Florida", "Stanford", "Penn St.", "Stephenn F. Austin", "Oregon", "New Mexico State", "Colorado", "BYU", "Villanova", "Colgate", "Michigan", "Arkansas", "West Virginia", "North Dakota St."]
        midwest_teams = ["Kansas", "Princeton", "Wisconsin", "Rhode Island", "Arizona", "Liberty", "Michigan St.", "North Texas", "LSU", "Purdue", "Florida St.", "Little Rock", "Marquette", "Indiana", "Dayton", "Winthrop"]
        south = teams[teams["TEAM"].isin(south_teams)]
        east = teams[teams["TEAM"].isin(east_teams)]
        west = teams[teams["TEAM"].isin(west_teams)]
        midwest = teams[teams["TEAM"].isin(midwest_teams)]
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
            print(method.head())  # Test methods, works! All power column values are stored as list in method
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
        #os.system('cls' if os.name == 'nt' else 'clear')
        num_teams = len(region_teams)
        num_rounds = int(4)

        for round_num in range(num_rounds):
            round_teams = int(num_teams / (2 ** (round_num + 1)))
            spacing = " " * (2 ** (num_rounds - round_num - 1))
            winners = []

            for i in range(round_teams):
                # team1 is the first team in the TEAM column of region_teams:
                team1 = region_teams.iloc[i * 2]
                team2 = region_teams.iloc[i * 2 + 1]
                method = str(method)
                #print("MADE IT THIS FAR")
                winner = team1 if team1.loc[method] < team2.loc[method] else team2
                winners.append(winner)
                print(f"{spacing}{team1['TEAM']} vs {team2['TEAM']} -> Winner: {winner['TEAM']}")
            region_teams = pd.DataFrame(winners)

        


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


if __name__=='__main__':
    run()

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
    
    def getData(self):
        #teams = pd.read_csv('data/cbb20.csv')
        #return teams
        print("Which Dataset? Test set is ../data/cbb20.csv ", end='')
        teams = pd.read_csv(input())    # Input path to (and including) the dataset
        print(teams.head())
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

    def getMethod(self):
        teams = self.teams
        print("Select Ranking Method; POWER, RANK, or WIN? ", end='')
        if input() == 'POWER' or 'power' or 'Power':
            method = getPower(teams)
        elif input() == 'RANK' or 'rank' or 'Rank':
            method = getRank(teams)
        elif input() == 'WIN' or 'win' or 'Win':
            method = getWins(teams)
        else:
            print("Invalid input. Try again.")
            # getMethod(teams)
    def organizeBracket(self):
        teams = self.teams
        method = self.method
        south = teams[teams['Baylor', 'Texas Southern', 'Cincinnati', 'VCU', 'Illinois', 'East Tennessee St.', 'Auburn', 'Charleston', 'Iowa', 'Mississippi State', 'Seton Hall', 'Bowling Green', 'Ohio State', 'Northern Iowa', 'Louisville', 'Murray State']]


def getPower(teams):
    power = teams['BARTHAG']
    print("Power test! ", end='')
    return power

def getRank(teams):
    rank = teams['RK']
    print("Rank test! ", end='')
    return rank

def getWins(teams):
    wins = teams['W']
    print("Win test! ", end='')
    return wins


def run():
    os.system('cls' if os.name == 'nt' else 'clear')
    bracket = Bracket()
    bracket.getData()
    bracket.getMethod()


if __name__=='__main__':
    run()

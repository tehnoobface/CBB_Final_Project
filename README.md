# Basketball Bracket Generator
## By: Kayla Tansiongco and Maclean Sherren

The Basketball Bracket Generator package generates playoff brackets and outcomes for the NCAA March Madness Playoff tournament based on a method of prediction. Those methods are chosen by the user and include the power ranking, seeding (or rank for 2020 data), or total wins.

# Installation

The pip package manager is used to install the bracket_package. The package requires python 3.7>=, numpy>=1.25.2, 
pandas>=2.1.2, seaborn>=0.13.0, and setuptools>=68.0.0.

```console
pip install "git+https://github.com/tehnoobface/CBB_Final_Project.git"
```

Additionally, the repository containing the python code and executable script for the bracket_package - bracket - and all cleaned test data can be cloned with the following code:

```console
git clone https://github.com/tehnoobface/CBB_Final_Project.git
```

# Demo: The 2020 NCAA D1 Playoffs

This package is inspired by the 2020 NCAA D1 basketball season, which ended without a playoff tournament due to the pandemic. It takes a parameter and predicts and entire playoff bracket including the final four and tournament winner based on the selected method.

Here is a quick demo of the 2020 data once the repository with the data and executable have been cloned:
```console
cd CBB_FINAL_PROJECT/bracket_package/

python bracket
```
This code will launch the package, which takes command line inputs and outputs the playoff bracket results:
```
Choose a dataset. Data found in /data, with 2020 test dataset being ../data/cbb20.csv : data/cbb20.csv
Select Ranking Method; POWER, RANK, WIN, SEED? Win
Enter the Playoff Bracket Year (ex. '2020'): 2020

Round 1:
        Baylor vs Texas Southern -> Winner: Baylor
        Cincinnati vs VCU -> Winner: Cincinnati
        Illinois vs East Tennessee St. -> Winner: East Tennessee St.
        Auburn vs College of Charleston -> Winner: Auburn
        Iowa vs Mississippi St. -> Winner: Mississippi St.
        Seton Hall vs Bowling Green -> Winner: Bowling Green
        Ohio St. vs Northern Iowa -> Winner: Northern Iowa
        Louisville vs Murray St. -> Winner: Louisville
Round 2:

...

Final Four: East Tennessee St., Vermont, Gonzaga, Liberty

Playoff Finals: East Tennessee St. vs Gonzaga

NCAA D1 Division Champs: East Tennessee St.
```

The output is cut here to save space, but the display would include each region's rounds, 1-4, with each returning a team to send to the Final Four.

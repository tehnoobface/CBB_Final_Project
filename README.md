# CBB_Final_Project
## By: Kayla Tansiongco and Maclean Sherren

## 11/10
- Ideate and create plan for project (What do we want to achieve? How do we want to achieve it? How do we plan to present it? Refer to Presentation Outline)
- Read cbb.csv (includes NCAA seasons 2013 to 2021, excluding 2020) and cbb.20 (just NCAA 2020 season) and define two separate dataframes, cbb and cbb20
- Identify columns we want to see in a final merged dataframe: YEAR, TEAM, CONF, G, W, BARTHAG, POSTSEASON (initially empty for 2020), SEASON_FINAL (derived from POST_SEASON variable)

## 11/15
- Create numerically coded column, SEASON_FINAL, for POSTSEASON (which is string data type) for cbb.csv dataframe
- Initialize variables POSTSEASON and SEASON_FINAL as NaN for cbb20.csv dataframe (this is what we hope to fill in through our prediction methods)
- Merge cbb and cbb20 with variables we previously identified (YEAR == '2020' should have NaN values for POSTSEASON and SEASON_FINAL) and define as dataframe cbb_all
- Using cbb dataframe, plot and find correlation coefficient (Spearman method) for variables BARTHAG (power ranking statistic) and SEASON_FINAL, SEED and SEASON_FINAL, W and SEASON_FINAL, W/L (variable derived from W and G) and SEASON_FINAL
- Save this EDA to guide next steps/transition into prediction methods

## 11/20
- Tested "BracketManager" package found on https://github.com/cristiean/bracket/tree/master
- Put in place bracket_package folder, with BracketMaker's github copied inside in folder "BracketMaker-0.4.0"
- Created __init__.py and bracket_module.py, the end goal package.
- New Goal: Get BracketManager to work with my data and use bracket.py as the foundation of our package.

- ## TO DO:
- Introduce different methods of prediction (3 total methods)
-- Show results of each method
-- Potential for python package: combines each method and with equal weight to determine overall outcome
-- Assign weight to different methods based on Std. Error and/or correlation coefficients
- Create playoff bracket
-- If possible, make the methods of prediction simulate the playoff bracket (run outcomes of each game one at a time)
-- Other potential for python package; Takes bracket and prediction method as inputs and generates a table or bracket of results as an output.
- Show results, discuss outcomes, and potential draw backs or other methods of prediction not included in our Presentation

## Presentation Outline:
- Start by presenting the data from Kaggle folder, note columns and differences between 2020 and the rest of the data, introduce inital goal
- Initial Goal: Make predictions for 2020 post-season based on data from other years. Want to use various predictors/columns such as: W/L Ratio, BARTHAG (power ranking statistic), SEED, and RK (maybe). Combine our findings to come up with a final prediction method.
- Show how we merged the raw data, present initial EDA (correlation plots/coefficients)
- Show how inital EDA guided methods to achieve prediction goals (some predictors are not as strong as we thought, will adjust and take into consideration as we build a final, all encompassing formula)
- Introduce different methods of preliminary prediction (3 total methods)
- Show results of each method
- Assess each model/method and show how it may relate to final formula/method for prediction
- Show results, discuss outcomes, and potential draw backs or other methods of prediction not included in our Presentation

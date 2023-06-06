import pandas as pd
import numpy as np

# Define the size of the dataset
n = 2000

# Set the seed for the randomness
np.random.seed(0)

# Define the IMDbRating which is the target variable
IMDbRating = np.random.normal(loc=6.5, scale=1.5, size=n)
IMDbRating = np.clip(IMDbRating, 0, 10)  # Clip to ensure ratings are between 0 and 10

# Define the strong positive correlated variable CharacterDevelopment
CharacterDevelopment = IMDbRating + np.random.normal(loc=0, scale=0.5, size=n)
CharacterDevelopment = np.clip(CharacterDevelopment, 0, 10)  # Clip to ensure values are within a reasonable range

# Define the strong negatively correlated variables EpisodeDuration and HiatusDuration
EpisodeDuration = 60 - (IMDbRating + np.random.normal(loc=0, scale=0.5, size=n))
EpisodeDuration = np.clip(EpisodeDuration, 15, 60)  # Clip to ensure values are within a reasonable range

HiatusDuration = 12 - (IMDbRating + np.random.normal(loc=0, scale=0.5, size=n))
HiatusDuration = np.clip(HiatusDuration, 0, 12)  # Clip to ensure values are within a reasonable range

# Define the Budget variable which has no relationship with the target
Budget = np.random.uniform(low=1e6, high=1e9, size=n)  # Chose values to represent a range of budget values

# Define the slightly positively correlated variables Cliffhangers and PlotTwists
Cliffhangers = IMDbRating/2 + np.random.normal(loc=0, scale=0.5, size=n)
Cliffhangers = np.clip(Cliffhangers, 0, 10)  # Clip to ensure values are within a reasonable range

PlotTwists = IMDbRating/2 + np.random.normal(loc=0, scale=0.5, size=n)
PlotTwists = np.clip(PlotTwists, 0, 10)  # Clip to ensure values are within a reasonable range

# Define the slightly negatively correlated variable EpisodeBinging
EpisodeBinging = 10 - IMDbRating/2 + np.random.normal(loc=0, scale=0.5, size=n)
EpisodeBinging = np.clip(EpisodeBinging, 0, 10)  # Clip to ensure values are within a reasonable range

# Define the RottenTomatoesRating which is correlated with IMDbRating
RottenTomatoesRating = IMDbRating * 10 + np.random.normal(loc=0, scale=5, size=n)
RottenTomatoesRating = np.clip(RottenTomatoesRating, 0, 100)  # Clip to ensure ratings are between 0 and 100

# Create the dataframe
df = pd.DataFrame({
    'CharacterDevelopment': CharacterDevelopment,
    'EpisodeDuration': EpisodeDuration,
    'Budget': Budget,
    'Cliffhangers': Cliffhangers,
    'PlotTwists': PlotTwists,
    'EpisodeBinging': EpisodeBinging,
    'HiatusDuration': HiatusDuration,
    'RottenTomatoesRating': RottenTomatoesRating,
    'IMDbRating': IMDbRating
})

# Save the dataframe to a CSV file
df.to_csv('tv_show_dataset.csv', index=False)

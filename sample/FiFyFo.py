
# Dataset: https://www.kaggle.com/karangadiya/fifa19/downloads/data.csv/4

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style = 'dark')

fifa = pd.read_csv('data.csv',index_col=0)

plt.figure(figsize=(18,10))
sns.countplot(fifa['Overall'], palette='rocket')
plt.show()

fifa.sort_values(by = 'Age' , ascending = False)[['Name','Club','Nationality','Overall', 'Age' ]].head(5)
fifa.sort_values(by = 'Age' , ascending = True)[['Name','Club','Nationality','Overall', 'Age','Potential' ]].head(5)
fifa.sort_values(by = 'FKAccuracy' , ascending = False)[['Name','Club','Nationality','Overall', 'Age','FKAccuracy']].head(5)
fifa.sort_values(by = 'Penalties' , ascending = False)[['Name','Club','Nationality','Overall', 'Age','Penalties']].head(5)
fifa.sort_values(by = 'BallControl' , ascending = False)[['Name','Club','Nationality','Overall', 'Age','BallControl']].head(5)
fifa.sort_values(by = 'SprintSpeed' , ascending = False)[['Name','Club','Nationality','Overall', 'Age','SprintSpeed']].head(5)

clubs = ['Chelsea' , 'Arsenal', 'Juventus', 'Paris Sain-Germain' ,'FC Bayern München',
       'Real Madrid' , 'FC Barcelona' , 'Borussia Dortmund' , 'Manchester United' ,
       'FC Porto', 'Liverpool', 'Manchester City']
       
fifa_club_age = fifa.loc[fifa['Club'].isin(clubs) & fifa['Age']]
plt.figure(1 , figsize = (15 ,7))
sns.violinplot(x = 'Club' , y = 'Age' , data = fifa_club_age,palette='rocket')
plt.title('Age Distribution in famous clubs')
plt.xticks(rotation = 50)
plt.show()


fifa_club_rating = fifa.loc[fifa['Club'].isin(clubs) & fifa['Overall']]
plt.figure(1 , figsize = (15 ,7))
sns.violinplot(x = 'Club' , y = 'Overall' , data = fifa_club_rating, palette='rocket')
plt.title('Overall Rating Distribution in famous clubs')
plt.xticks(rotation = 50)
plt.show()

best_dict = {}
for club in fifa['Club'].unique():
    overall_rating = fifa['Overall'][fifa['Club'] == club].sum()
    best_dict[club] = overall_rating
best_club = pd.DataFrame.from_dict(best_dict,orient='index', columns = ['overall'])
best_club['club'] = best_club.index
best_club = best_club.sort_values(by = 'overall' , ascending =  False)

plt.figure(1 , figsize = (15 , 6))
sns.barplot(x = 'club' , y  = 'overall' , data = best_club.head(5),palette='rocket')  
plt.xticks(rotation = 70)
plt.xlabel("Club")
plt.ylabel('Sum of Overall Rating of players in club')
plt.title('Clubs with best Players (sum of overall ratings of players per club)')
plt.ylim(2450 , 2600)
plt.show()


countries = ['England' , 'Brazil' , 'Portugal' ,'Argentina',
             'Italy' , 'Spain' , 'Germany' ,'Netherlands','India']
             
fifa_country_age = fifa.loc[fifa['Nationality'].isin(countries) & fifa['Age']]
plt.figure(1 , figsize = (15 ,7))
sns.violinplot(x = 'Nationality' , y = 'Age' , data = fifa_country_age, palette='rocket')
plt.title('Age Distribution in famous clubs')
plt.xticks(rotation = 50)
plt.show()

fifa_country_rating = fifa.loc[fifa['Nationality'].isin(countries) & fifa['Overall']]
plt.figure(1 , figsize = (15 ,7))
sns.violinplot(x = 'Nationality' , y = 'Overall' , data = fifa_country_age, palette='rocket')
plt.title('Overall Rating Distribution in famous clubs')
plt.xticks(rotation = 50)
plt.show()


best_dict = {}
for country in fifa['Nationality'].unique():
    overall_rating = fifa['Overall'][fifa['Nationality'] == country].sum()
    best_dict[country] = overall_rating
best_country = pd.DataFrame.from_dict(best_dict,orient='index', columns = ['overall'])
best_country['club'] = best_country.index
best_country = best_country.sort_values(by = 'overall' , ascending =  False)

plt.figure(1 , figsize = (15 , 6))
sns.barplot(x = 'club' , y  = 'overall' , data = best_country.head(10),palette='rocket')  
plt.xticks(rotation = 70)
plt.xlabel("Country")
plt.ylabel('Sum of Overall Rating of players in a country')
plt.title('Countries with best Players (sum of overall ratings of players per club)')
plt.show()

best_dict = {}

for country in countries:
    count = fifa['Overall'][fifa['Nationality'] == country].count()
    best_dict[country] = count
best_country = pd.DataFrame.from_dict(best_dict,orient='index', columns = ['count'])
best_country['club'] = best_country.index

sns.barplot(x = 'club' , y  = 'count' , data = best_country, palette='rocket')  
plt.xticks(rotation = 70)
plt.xlabel("Country")
plt.ylabel('Count of players in a country')
plt.show()

best_dict = {}

for country in countries:
    overall = fifa['Overall'][fifa['Nationality'] == country].sum()
    count = fifa['Overall'][fifa['Nationality'] == country].count()
    country_overall = overall / count
    best_dict[country] = country_overall
best_country = pd.DataFrame.from_dict(best_dict,orient='index', columns = ['country_overall'])
best_country['club'] = best_country.index

sns.barplot(x = 'club' , y  = 'country_overall' , data = best_country, palette='rocket')  
plt.xticks(rotation = 70)
plt.xlabel("Country")
plt.ylabel('Count of players in a country')
plt.show()

plt.figure(1 , figsize = (15 , 6))
sns.countplot(x = 'Position' , data = fifa , palette = 'rocket' )
plt.title('Count Plot of Postions of player')
plt.show()


# Let's define the various player features
player_features = ['Crossing', 'Finishing', 'HeadingAccuracy',
       'ShortPassing', 'Volleys', 'Dribbling', 'Curve', 'FKAccuracy',
       'LongPassing', 'BallControl', 'Acceleration', 'SprintSpeed',
       'Agility', 'Reactions', 'Balance', 'ShotPower', 'Jumping',
       'Stamina', 'Strength', 'LongShots', 'Aggression', 'Interceptions',
       'Positioning', 'Vision', 'Penalties', 'Composure', 'Marking',
       'StandingTackle', 'SlidingTackle', 'GKDiving', 'GKHandling',
       'GKKicking', 'GKPositioning', 'GKReflexes']

for i, val in fifa.groupby(fifa['Position'])[player_features].mean().iterrows():
    print('Position {}: {}, {}, {}, {}, {}'.format(i, *tuple(val.nlargest(5).index)))
    
    
    fifa_best_players = pd.DataFrame.copy(fifa.sort_values(by = 'Overall' , ascending = False ).head(10))

plt.figure(1 , figsize = (15 , 5))
sns.barplot(x ='Name' , y = 'Overall' , data = fifa_best_players,palette='rocket')

plt.ylim(87 , 95)
plt.show()


def normalizing_wage(x):
    if '€' in str(x) and 'M' in str(x):
        c = str(x).replace('€' , '')
        c = str(c).replace('M' , '')
        c = float(c) * 1000000

    else:
        c = str(x).replace('€' , '')
        c = str(c).replace('K' , '')
        c = float(c) * 1000

    return c

fifa['Normalized_Wage'] = fifa['Wage'].apply(lambda x : normalizing_wage(x))
fifa.sort_values(by = 'Normalized_Wage' , ascending = False)[['Name','Club','Nationality','Overall',
'Age','Normalized_Wage','Wage']].head(5)

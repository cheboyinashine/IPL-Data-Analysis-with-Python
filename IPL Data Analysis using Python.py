#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


data = pd.read_csv(r"C:\Users\shine\Downloads\IPLData.csv")


# In[3]:


data.head(50)
#used to look the first 5 rows in the dataset


# In[4]:


data.describe()
#desctibe shows the information like count,mean,standard_deviation,min etc;


# In[5]:


data.isna().sum()
#shows the sum of the null values in the column


# In[6]:


data.info()
#this function shows non-null values count and the datatype of the column


# # Cleaning the data
# ## --> We focus on the capped players since the uncapped players are playing the IPL for the first time or the relevant data is not sufficient 
# ## --> Capped - Batters,Bowlers,Allrounders,Wicker Keeper

# In[7]:


batters = data.loc[( data["Player_Type"] == "Batter")]
#This batters dataframe is created to get the batters data
batters_new = batters.loc[( batters["Capped"] == 1 )]
#batters_new dataframe is created to get the data of batsmen who is having capped at least once

Capped_Batters = batters_new [[ 'Player Name' ,
                               'Team',
                               'Nationality',
                               'Matches_Played',
                               'Runs',
                               'Average',
                               'Strike_Rate']]


# In[8]:


Capped_Batters.head()


# In[9]:


bowlers = data.loc[( data["Player_Type"] == "Bowler ")]
#This bowlers dataframe is created to get the bowlers data
bowlers_new = bowlers.loc[( bowlers["Capped"] == 1 )]
#bowlers_new dataframe is created to get the data of bowler who is having capped at least once

Capped_Bowlers = bowlers_new [[ 'Player Name' ,
                               'Team',
                               'Nationality',
                               'Matches_Played',
                               'Wickets',
                               'Bowling_average',
                               'Economy',
                              'Bowling_Strike_Rate']]


# In[10]:


Capped_Bowlers.head()


# In[11]:


Keepers = data.loc[(data ["Player_Type"] == "Keeper")]
Keepers_new = Keepers.loc[(Keepers["Capped"] == 1)]

Capped_Keepers = Keepers_new [[ 'Player Name' ,
                               'Team',
                               'Nationality',
                               'Matches_Played',
                               'Runs',
                               'Average',
                               'Strike_Rate',
                               'Catches',
                               'Run_outs',
                               'Stumps' ]]


# In[12]:


Capped_Keepers.head()


# In[13]:


Allrounders = data.loc[ (data["Player_Type"] == "Allrounder")]
Allrounders_new = Allrounders.loc[(Allrounders["Capped"] == 1)]

Capped_Allrounders = Allrounders_new[[ 'Player Name' ,
                               'Team',
                               'Nationality',
                               'Matches_Played',
                                'Runs',
                               'Average',
                               'Strike_Rate',
                            'Wickets',
                               'Bowling_average',
                               'Economy',
                              'Bowling_Strike_Rate' ]]


# In[14]:


Capped_Allrounders.head()


# In[15]:


#making the null values to 0 to maken the data consistent and clean

Capped_Batters = Capped_Batters.fillna(0)
Capped_Bowlers = Capped_Bowlers.fillna(0)
Capped_Keepers = Capped_Keepers.fillna(0)
Capped_Allrounders = Capped_Allrounders.fillna(0)


# In[16]:


#checking null values in the data

print(Capped_Batters.isna().sum())
print(Capped_Bowlers.isna().sum())
print(Capped_Keepers.isna().sum())
print(Capped_Allrounders.isna().sum())


# #  Initial Analysis
# ## now we will analyse data for batters, bowlers , allrounders

# In[17]:


#analyzing the batters data
#here we are taking the data of the batsmen whose average is more than 32

top_batters = Capped_Batters.loc[(Capped_Batters["Average"] >= 32.0)]

#now sorting the data to descending order
top_batters_average = top_batters.sort_values('Average',ascending = False)
top_batters_strike_rate = top_batters.sort_values('Strike_Rate',ascending = False)
top_batters_runs = top_batters.sort_values('Runs',ascending = False)
top_batters_matches = top_batters.sort_values('Matches_Played',ascending = False)


# In[18]:


#data of the average in descending order
top_batters_average


# In[19]:


#data of the strike rate in descending order
top_batters_strike_rate


# In[20]:


#data of the batters having top runs
top_batters_runs


# In[21]:


#Data of the players who played more matches
top_batters_matches


# # From the analysis the top 3 players are
# ## 1) David Warner
# ## 2) KL Rahul
# ## 3) Virat Kohli

# In[22]:


#Analyzing the Bowlers data
#data is taken such that the average of the bowlers is to be less than or equal to 24
top_bowlers = Capped_Bowlers.loc[( Capped_Bowlers["Bowling_average"] <= 24 )]

top_bowlers_average = top_bowlers.sort_values('Bowling_average')
top_bowlers_strike_rate = top_bowlers.sort_values('Bowling_Strike_Rate')
top_bowlers_wickets = top_bowlers.sort_values('Wickets', ascending  = False )
top_bowlers_economy = top_bowlers.sort_values('Economy')
top_bowlers_matches = top_bowlers.sort_values('Matches_Played' , ascending = False)


# In[23]:


#top bowlers average since it is bowling it should be in ascending order
top_bowlers_average


# In[24]:


#the data contain the top strike rate in ascending order
top_bowlers_strike_rate


# In[25]:


#in descending order
top_bowlers_wickets


# In[26]:


#the ascending order
top_bowlers_economy


# In[27]:


#in descending order
top_bowlers_matches


# # From the analysis the top bowlers are
# ## 1) Kagiso Rabada
# ## 2) Jasprit Bumrah
# ## 3) Yuzvendra Chahal
# ## 4) Nathan Coulter-Nile

# In[28]:


#Analyzing the Allrounders
#arranged in the allrounders order based on the strike_rate >= 140
top_allrounders = Capped_Allrounders.loc[( Capped_Allrounders["Strike_Rate"] >= 140 )]

top_allrouners_average = top_allrounders.sort_values('Average' , ascending = False ) 
top_allrouners_strike_rate = top_allrounders.sort_values('Strike_Rate' , ascending = False )
top_allrouners_runs = top_allrounders.sort_values('Runs' , ascending = False )
top_allrouners_matches = top_allrounders.sort_values('Matches_Played' , ascending = False )
top_allrouners_bowling_average = top_allrounders.sort_values('Bowling_average')
top_allrouners_bowling_strike_rate = top_allrounders.sort_values('Bowling_Strike_Rate')
top_allrouners_wickets = top_allrounders.sort_values('Wickets' , ascending = False )
top_allrouners_economy = top_allrounders.sort_values('Economy')


# In[29]:


#this dataframe consists of players average in descending order for the top_allrounders
top_allrouners_average


# In[30]:


#thsi dataframe consists of players strike_rate in descending order from the top_allrounders
top_allrouners_strike_rate


# In[31]:


#thsi dataframe consists of players runs in descending order from the top_allrounders
top_allrouners_runs


# In[32]:


#this dataframe consists of the matches played by each players like most played to lease from the top_allrounders
top_allrouners_matches


# In[33]:


#thsi dataframe consists of the bowling_average in ascending order from the top_allrounders
top_allrouners_bowling_average


# In[34]:


#this dataframe contains the bowling_strike_rate information in ascending order from the top_allrounders
top_allrouners_bowling_strike_rate


# In[35]:


top_allrouners_wickets


# In[36]:


#this dataframe contains the economy of the top_allrounders in ascending order
top_allrouners_economy


# # From the analysis the top allrounders are
# ## 1)Andre Russell
# ## 2)Sunil Narine	
# ## 3)Hardik Pandya
# ## 4)Jofra Archer

# In[37]:


#Analyzing the keepers data 
#to get the top_keepers data we took the players having their average >= 25.0
top_keepers = Capped_Keepers.loc[(Capped_Keepers["Average"] >= 25.0 )]

top_keepers_average = top_keepers.sort_values('Average' , ascending = False)
top_keepers_strike_rate = top_keepers.sort_values('Strike_Rate' , ascending = False)
top_keepers_runs = top_keepers.sort_values('Runs' , ascending = False)
top_keepers_matches = top_keepers.sort_values('Matches_Played' , ascending = False)
top_keepers_catches = top_keepers.sort_values('Catches' , ascending = False)
top_keepers_runouts = top_keepers.sort_values('Run_outs' , ascending = False)
top_keepers_stumps = top_keepers.sort_values('Stumps' , ascending = False)


# In[38]:


#this dataframe consists of the average of the wicket_keepers in descending order
top_keepers_average


# In[39]:


#this dataframe consists of the strike_rate of the wicket_keepers in descending order
top_keepers_strike_rate


# In[40]:


#this dataframe consists of the runs scored by wicket_keepers in descending order
top_keepers_runs


# In[41]:


#this dataframe consists of the matches played by wicket_keepers in descending order
top_keepers_matches


# In[42]:


#this dataframe consists of no the catches taken by wicket_keepers in descending order
top_keepers_catches 


# In[43]:


#this dataframe consists of no of runouts done by each wicket_keepers in descending order
top_keepers_runouts


# In[44]:


#this dataframe consists of the stumpings done by wicket_keepers in descending order
top_keepers_stumps


# # From the alalysis the top wicket keepers are
# ## 1)MS Dhoni
# ## 2)Dinesh Karthik
# ## 3)Rishabh Pant	

# # Visualization based on the segregated data

# In[45]:


#Visualization of the batters data
#this plot shows the strike_rate of the each batsmen

plt.figure(figsize = (20,10) )
sns.barplot(x='Player Name' , y = 'Strike_Rate', data= top_batters )


# In[46]:


#batsmen
#this plot shows the runs made by each batsmen

plt.figure(figsize = (20,10) )
sns.barplot(x='Player Name' , y = 'Runs', data= top_batters )


# In[47]:


#batsmen
#this plot shows the average of each batsmen

plt.figure(figsize = (20,10) )
sns.barplot(x='Player Name' , y = 'Average', data= top_batters )


# In[48]:


#batsmen
#this plot shows the matches_played by each batsmen

plt.figure(figsize = (20,10) )
sns.barplot(x='Player Name' , y = 'Matches_Played', data= top_batters )


# by looking at the graphs also we can deside the top batters
# 1) David Warner
# 2) KL Rahul
# 3) Virat Kohli

# In[49]:


#Visualization of the bowlers data
#this plot shows bowling_average of the top_bowlers

plt.figure(figsize = (20,10) )
sns.barplot(x='Player Name' , y = 'Bowling_average', data= top_bowlers )


# In[50]:


#bowlers
#this plot shows the economy of the top_bowlers

plt.figure(figsize = (20,10) )
sns.barplot(x='Player Name' , y = 'Economy', data= top_bowlers )


# In[51]:


#bowlers
#this plot shows the wickets taken by the top_bowlers

plt.figure(figsize = (20,10) )
sns.barplot(x='Player Name' , y = 'Wickets', data= top_bowlers )


# In[52]:


#bowlers
#this plot shows number of matches_played by each top_bowlers

plt.figure(figsize = (20,10) )
sns.barplot(x='Player Name' , y = 'Matches_Played', data= top_bowlers )


# from this plots also we can get the top bowlers as 
# 1) Kagiso Rabada
# 2) Jasprit Bumrah
# 3) Yuzvendra Chahal
# 4) Nathan Coulter-Nile

# In[53]:


#Visualization of the allrounders data
#this plot shows the strike_rate of the top_allrounders

plt.figure(figsize = (20,10) )
sns.barplot(x='Player Name' , y = 'Strike_Rate', data= top_allrounders )


# In[54]:


#allrounders
#this plot shows the strike_rate of the top_allrounders

plt.figure(figsize = (20,10) )
sns.barplot(x='Player Name' , y = 'Average', data= top_allrounders )


# In[55]:


#allrounders
#this plot shows the matches_played by the top_allrounders

plt.figure(figsize = (20,10) )
sns.barplot(x='Player Name' , y = 'Matches_Played', data= top_allrounders )


# In[56]:


#allrounder
#this plot shows the runs made by top_allrounders

plt.figure(figsize = (20,10) )
sns.barplot(x='Player Name' , y = 'Runs', data= top_allrounders )


# In[57]:


#allrounders
#this plot shows the bowling_average of the top_allrounders

plt.figure(figsize = (20,10) )
sns.barplot(x='Player Name' , y = 'Bowling_average', data= top_allrounders )


# In[58]:


#allrounders
#this plot shows the Economy of the top_allrounders

plt.figure(figsize = (20,10) )
sns.barplot(x='Player Name' , y = 'Economy', data= top_allrounders )


# In[59]:


#allrounders
#this plot shows the Bowling_strike_rate of the top_allrounders

plt.figure(figsize = (20,10) )
sns.barplot(x='Player Name' , y = 'Bowling_Strike_Rate', data= top_allrounders )


# In[60]:


#allrounder
#this plot shows the Wickes taken by top_allrounders

plt.figure(figsize = (20,10) )
sns.barplot(x='Player Name' , y = 'Wickets', data= top_allrounders )


# from the above plots we can deside the top allrounders
#  
#  1)Andre Russell 2)Sunil Narine	3)Hardik Pandya 4)Jofra Archer

# In[61]:


#Visualization of the keepers data (1)
#this plot shows the average of the top_keepers

plt.figure(figsize = (20,10) )
sns.barplot(x='Player Name' , y = 'Average', data= top_keepers )


# In[62]:


#wicket_keepers (2)
#this plot shows the average of the top_keepers

plt.figure(figsize = (20,10) )
sns.barplot(x='Player Name' , y = 'Runs', data= top_keepers )


# In[63]:


#wicket_keepers (3)
#this plot shows the average of the top_keepers

plt.figure(figsize = (20,10) )
sns.barplot(x='Player Name' , y = 'Strike_Rate', data= top_keepers )


# In[64]:


#wicket_keepers (4)
#this plot shows the average of the top_keepers

plt.figure(figsize = (20,10) )
sns.barplot(x='Player Name' , y = 'Catches', data= top_keepers )


# In[65]:


#wicket_keepers (5)
#this plot shows the average of the top_keepers

plt.figure(figsize = (20,10) )
sns.barplot(x='Player Name' , y = 'Run_outs', data= top_keepers )


# In[66]:


#wicket_keepers (6)
#this plot shows the average of the top_keepers

plt.figure(figsize = (20,10) )
sns.barplot(x='Player Name' , y = 'Stumps', data= top_keepers )


# In[67]:


#wicket_keepers (7)
#this plot shows the average of the top_keepers

plt.figure(figsize = (20,10) )
sns.barplot(x='Player Name' , y = 'Matches_Played', data= top_keepers )


# # Forming the best 11 from the analyzed data
# 
# for our final best 11 lets consider the players ratio as :
# 3-Batters ; 3-Allrounders ; 4-Bowlers( 2-Spin option ) ; 1-Wicketkeeper

# In[68]:


#Batters on the final 11 are - KL Rahul , Virat Kohli , David Warner
top_batters.reset_index(drop = True)
matches_values=[top_batters.iloc[6]['Matches_Played'],top_batters.iloc[2]['Matches_Played'],top_batters.iloc[5]['Matches_Played']]
runs_values=[top_batters.iloc[6]['Runs'],top_batters.iloc[2]['Runs'],top_batters.iloc[5]['Runs']]
average_values=[top_batters.iloc[6]['Average'],top_batters.iloc[2]['Average'],top_batters.iloc[5]['Average']]
strike_rate_values=[top_batters.iloc[6]['Strike_Rate'],top_batters.iloc[2]['Strike_Rate'],top_batters.iloc[5]['Strike_Rate']]
Lables = ['KL RAhul' , 'David Warner' , 'Virat Kohli']

fig, axes = plt.subplots(2,2,figsize=(10,10))
axes[0][0].set_title("Matches Played")
axes[0][1].set_title("Runs in the IPL Carrer")
axes[1][0].set_title("Strike Rate")
axes[1][1].set_title("Average")
sns.barplot(x=Lables,y=matches_values,ax=axes[0][0])
sns.barplot(x=Lables,y=runs_values,ax=axes[0][1])
sns.barplot(x=Lables,y=strike_rate_values,ax=axes[1][0])
sns.barplot(x=Lables,y=average_values,ax=axes[1][1])


# In[69]:


#Allrounders for the final 11 are - Andre Russell , Sunil Narine , Hardik Pandya

top_allrounders.reset_index(drop = True)
matches_values = [top_allrounders.iloc[5]['Matches_Played'],top_allrounders.iloc[9]['Matches_Played'],top_allrounders.iloc[6]['Matches_Played']]
runs_values = [top_allrounders.iloc[5]['Runs'],top_allrounders.iloc[9]['Runs'],top_allrounders.iloc[6]['Runs']]
average_values = [top_allrounders.iloc[5]['Average'],top_allrounders.iloc[9]['Average'],top_allrounders.iloc[6]['Average']]
strike_rate_values = [top_allrounders.iloc[5]['Strike_Rate'],top_allrounders.iloc[9]['Strike_Rate'],top_allrounders.iloc[6]['Strike_Rate']]
bowling_strike_rate_values = [top_allrounders.iloc[5]['Bowling_Strike_Rate'],top_allrounders.iloc[9]['Bowling_Strike_Rate'],top_allrounders.iloc[6]['Bowling_Strike_Rate']]
bowling_average_values = [top_allrounders.iloc[5]['Bowling_average'],top_allrounders.iloc[9]['Bowling_average'],top_allrounders.iloc[6]['Bowling_average']]
wickets_values = [top_allrounders.iloc[5]['Wickets'],top_allrounders.iloc[9]['Wickets'],top_allrounders.iloc[6]['Wickets']]
economy_values = [top_allrounders.iloc[5]['Economy'],top_allrounders.iloc[9]['Economy'],top_allrounders.iloc[6]['Economy']]

Lables = ['Andre Russell' , 'Sunil Narine' , 'Hardik Pandya']

fig , axes = plt.subplots(4,2,figsize=(20,20))
axes[0][0].set_title("matches")
axes[0][1].set_title("Runs")
axes[1][0].set_title("Average")
axes[1][1].set_title("Strike Rate")
axes[2][0].set_title("Bowling Strike Rate")
axes[2][1].set_title("Bowling Average")
axes[3][0].set_title("Wickets")
axes[3][1].set_title("Economy")

sns.barplot(x=Lables , y=matches_values , ax=axes[0][0])
sns.barplot(x=Lables , y=runs_values , ax=axes[0][1])
sns.barplot(x=Lables , y=average_values , ax=axes[1][0])
sns.barplot(x=Lables , y=strike_rate_values , ax=axes[1][1])
sns.barplot(x=Lables , y=bowling_strike_rate_values , ax=axes[2][0])
sns.barplot(x=Lables , y=bowling_average_values , ax=axes[2][1])
sns.barplot(x=Lables , y=wickets_values , ax=axes[3][0])
sns.barplot(x=Lables , y=economy_values , ax=axes[3][1])


# In[70]:


#bowlers for the final 11 - Jasprit Bumrah , Kagiso Rabada , Nathan Coulter-Nile , Yuzi Chahal

top_bowlers.reset_index(drop = True)
matches_values = [top_bowlers.iloc[10]['Matches_Played'],top_bowlers.iloc[0]['Matches_Played'],top_bowlers.iloc[7]['Matches_Played'],top_bowlers.iloc[1]['Matches_Played']]
wickets_values = [top_bowlers.iloc[10]['Wickets'],top_bowlers.iloc[0]['Wickets'],top_bowlers.iloc[7]['Wickets'],top_bowlers.iloc[1]['Wickets']]
bowling_average_values = [top_bowlers.iloc[10]['Bowling_average'],top_bowlers.iloc[0]['Bowling_average'],top_bowlers.iloc[7]['Bowling_average'],top_bowlers.iloc[1]['Bowling_average']]
bowling_strike_rate_values = [top_bowlers.iloc[10]['Bowling_Strike_Rate'],top_bowlers.iloc[0]['Bowling_Strike_Rate'],top_bowlers.iloc[7]['Bowling_Strike_Rate'],top_bowlers.iloc[1]['Bowling_Strike_Rate']]
economy_values = [top_bowlers.iloc[10]['Economy'],top_bowlers.iloc[0]['Economy'],top_bowlers.iloc[7]['Economy'],top_bowlers.iloc[1]['Economy']]
Labels = ['Jasprit Bumrah' , 'Kagiso Rabada' , 'Nathan Coulter-Nile' , 'Yuzi Chahal']

fig , axes = plt.subplots(3,2, figsize=(15,15))
axes[0][0].set_title("Matches Played")
axes[0][1].set_title("Wickets")
axes[1][0].set_title("Bowling Average")
axes[1][1].set_title("Bowling Strike Rate")
axes[2][0].set_title("Economy")


sns.barplot(x=Labels, y= matches_values , ax=axes[0][0])
sns.barplot(x=Labels, y= wickets_values , ax=axes[0][1])
sns.barplot(x=Labels, y= bowling_average_values , ax=axes[1][0])
sns.barplot(x=Labels, y= bowling_strike_rate_values , ax=axes[1][1])
sns.barplot(x=Labels, y= economy_values , ax=axes[2][0])


# In[72]:


#wicket Keeper for the final 11 - MS Dhoni

matches_values = [top_keepers.iloc[8]['Matches_Played'],top_keepers.iloc[8]['Runs']]
average_values = [top_keepers.iloc[8]['Average'],top_keepers.iloc[8]['Strike_Rate']]
keeping_values = [top_keepers.iloc[8]['Catches'] ,top_keepers.iloc[8]['Stumps'],top_keepers.iloc[8]['Run_outs']]

Lable1 = ['Matches' , 'Runs']
Lable2 = ['Average','Strike Rate']
Lable3 = ['Catches' , 'Stumps' , 'Run_outs']

fig, axes = plt.subplots(1,3, figsize=(20,10) )
axes[0].set_title("Matches And Runs")
axes[1].set_title("Average and Strike Rate")
axes[2].set_title("keeping Stats")

sns.barplot(x=Lable1 , y=matches_values , ax=axes[0])
sns.barplot(x=Lable2 , y=average_values , ax=axes[1])
sns.barplot(x=Lable3 , y=keeping_values , ax=axes[2])


# In[84]:


batter1 = top_batters.loc[(top_batters["Player Name"] == 'KL Rahul ')]
batter2 = top_batters.loc[(top_batters["Player Name"] == 'David Warner ')]
batter3 = top_batters.loc[(top_batters["Player Name"] == 'Virat Kohli')]

bowler1 = top_bowlers.loc[(top_bowlers["Player Name"] == "Yuzvendra Chahal ")] 
bowler2 = top_bowlers.loc[(top_bowlers["Player Name"] == "Jasprit Bumrah")]
bowler3 = top_bowlers.loc[(top_bowlers["Player Name"] == "Nathan Coulter-Nile")]
bowler4 = top_bowlers.loc[(top_bowlers["Player Name"] == "Kagiso Rabada ")]

allrounder1 = top_allrounders.loc[(top_allrounders["Player Name"] == 'Andre Russell')]
allrounder2 = top_allrounders.loc[(top_allrounders["Player Name"] == 'Sunil Narine ')]
allrounder3 = top_allrounders.loc[(top_allrounders["Player Name"] == 'Hardik Pandya')]

keeper = top_keepers.loc[(top_keepers["Player Name"] == 'MS Dhoni')]

final = [batter1,batter2,batter3,allrounder1,allrounder2,allrounder3,keeper,bowler1,bowler2,bowler3,bowler4]
final_team = pd.concat(final)
final_team = final_team.drop(labels=['Matches_Played' , 'Runs' , 'Average' , 'Strike_Rate' , 'Wickets' , 'Bowling_average' ,
                                    'Economy' , 'Bowling_Strike_Rate' , 'Catches' , 'Run_outs' , 'Stumps'] , axis = 1 )
final_team.reset_index(drop = True)


# In[87]:


#this players are the best final 11 from all the teams 
final_team.reset_index(drop=True)


# In[ ]:





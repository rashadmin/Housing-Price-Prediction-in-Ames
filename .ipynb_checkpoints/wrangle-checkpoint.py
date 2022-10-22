#Wrangle Function
import pandas as pd
def wrangle(filename):
    df = pd.read_csv(filename)
    #Dropping High Cardinality and Low Cardinality Catergorical Features
    df.drop(['PID','Pool_QC','Street','Utilities','Condition_2','Roof_Matl'],axis=1,inplace=True)
    #Dropping High Cardinality and Low Cardinality Numerical Features
    df.drop(['Misc_Val','BsmtFin_SF_2','Enclosed_Porch','Three_season_porch',
                     'Screen_Porch','Pool_Area','Low_Qual_Fin_SF'],axis=1,inplace=True)
    # Filling Missing Values
    df['Garage_Yr_Blt'] = df['Garage_Yr_Blt'].fillna(df['Garage_Yr_Blt'].mode()[0])
    # Remove Outlier 
    mask = df['Garage_Yr_Blt']==2207
    index = df[mask].index
    df.drop(index = index,inplace=True)
    #We trimm lot area to 75k
    df['Lot_Area'] = df['Lot_Area'].apply(lambda x: 30000 if x > 30000 else x)
    #We trim Lot frontage to 200
    df['Lot_Frontage'] = df['Lot_Frontage'].apply(lambda x: 150 if x > 150 else x)
    #We trim Mas_Vnr_Area to 800
    df['Mas_Vnr_Area'] = df['Mas_Vnr_Area'].apply(lambda x: 500 if x > 500 else x)
    #We trim Total_Bsmt_SF to 2500
    df['Total_Bsmt_SF']= df['Total_Bsmt_SF'].apply(lambda x: 2500 if x>2500 else x)
    #We trim First_Flr_SF to 2500
    df['First_Flr_SF'] = df['First_Flr_SF'].apply(lambda x: 2500 if x >2500 else x)
    #We trim Second_Flr_SF to 1500
    df['Second_Flr_SF'] = df['Second_Flr_SF'].apply(lambda x : 1750 if x > 1750 else x)
    #We trim Gr_Liv_Area to 3000
    df['Gr_Liv_Area'] = df['Gr_Liv_Area'].apply(lambda x: 2500 if x >2500 else x)
    #We trim Wood_Deck_SF to 500
    df['Wood_Deck_SF'] = df['Wood_Deck_SF'].apply(lambda x: 400 if x>400 else x)
    #We trim Open Porch to 250
    df['Open_Porch_SF'] = df['Open_Porch_SF'].apply(lambda x : 200 if x>200 else x)
    # We map the Ordinality of Kitchen Qual to Integers
    Kitchen_Qual_Map = {'Poor':1,'Fair':2,'Typical':3,'Good':4,'Excellent':5}
    df['Kitchen_Qual'].replace(Kitchen_Qual_Map,inplace=True)
    # We map the Ordinality of Heating Qual to Integers
    Heating_Qual_Map = {'Poor':1,'Fair':2,'Typical':3,'Good':4,'Excellent':5}
    df['Heating_QC'].replace(Heating_Qual_Map,inplace=True)
    # We map the Ordinality of Garage Cond to Integers
    Garage_Cond_Map = {'Poor':1,'Fair':2,'Typical':3,'Good':4,'Excellent':5}
    df['Garage_Cond'].replace(Garage_Cond_Map,inplace=True)
    #  We map the Ordinality of Exter Cond to Integers
    Exter_Cond_Map = {'Poor':1,'Fair':2,'Typical':3,'Good':4,'Excellent':5}
    df['Exter_Cond'].replace(Exter_Cond_Map,inplace=True)
    # We map the Ordinality of Exter Qual to Integers
    Exter_Qual_Map = {'Poor':1,'Fair':2,'Typical':3,'Good':4,'Excellent':5}
    df['Exter_Qual'].replace(Exter_Qual_Map,inplace=True)
    # We map the Ordinality of Bsmt Qual to Integers
    Basement_Qual_Map = {'No_Basement':0,'Poor':1,'Fair':2,'Typical':3,'Good':4,'Excellent':5}
    df['Bsmt_Qual'].replace(Basement_Qual_Map,inplace=True)
    # We map the Ordinality of Garage Qual to Integers
    Garage_Qual_Map = {'No_Garage':0,'Poor':1,'Fair':2,'Typical':3,'Good':4,'Excellent':5}
    df['Garage_Qual'].replace(Garage_Qual_Map,inplace=True)
    # We map the Ordinality of Fireplace Qual to Integers
    Fireplace_Qu_Map = {'No_Fireplace':0,'Poor':1,'Fair':2,'Typical':3,'Good':4,'Excellent':5}
    df['Fireplace_Qu'].replace(Fireplace_Qu_Map,inplace=True)
    # We map the Ordinality of Overall Cond to Integers
    Overall_Cond_Map = {'Very_Poor':1,'Poor':2,'Fair':3,'Below_Average':4,'Average':5,'Above_Average':6,'Good':7,'Very_Good':8,'Excellent':9}
    df['Overall_Cond'].replace(Overall_Cond_Map,inplace=True)
    #  We map the Ordinality of Overall Qual to Integers
    Overall_Qual_Map = {'Very_Poor':1,'Poor':2,'Fair':3,'Below_Average':4,'Average':5,'Above_Average':6,'Good':7,'Very_Good':8,'Excellent':9,'Very_Excellent':10}
    df['Overall_Qual'].replace(Overall_Qual_Map,inplace=True)
    # We drop Multi Colinearity Feature
    df.drop(['Garage_Yr_Blt','Exter_Qual','Kitchen_Qual','Fireplaces','Garage_Area','First_Flr_SF','TotRms_AbvGrd'],axis=1,inplace = True)
    return df
import re
def cat_num_segregator(df):
    cat_col = df.select_dtypes(include='object')
    num_col = df.select_dtypes(exclude='object')
    discrete_col = []
    for i in num_col.columns:
        if re.match(r'\w+Yr|Year',i) or ((len(num_col.loc[:,i].unique()))<10):
            discrete_col.append(i)
    continuous_col  = num_col.drop(discrete_col,axis=1).columns
    ordinal_col = []
    for i in cat_col.columns:
        if re.match(r'Overall|Bsmt_Qual|Heating_QC|Kitchen_Qual|Fireplace_Qu|Garage_Qual|Garage_Cond|Pool_QC|Exter_Cond|Exter_Qual|Mo_Sold',i):
            ordinal_col.append(i)
    nominal_col  = cat_col.drop(ordinal_col,axis=1).columns
    return continuous_col,discrete_col,ordinal_col,nominal_col
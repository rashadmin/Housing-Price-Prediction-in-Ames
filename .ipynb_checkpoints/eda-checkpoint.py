from ipywidgets import Dropdown,interact
import matplotlib.pyplot as plt
import pandas as pd
def make_nominal_plots(df):
    print('SELECT FEATURE TO EXPLORE BELOW: ')
    def make_nominal_plot(feature):
        data = df.loc[:,feature].value_counts(normalize=True).sort_index()
        fig,ax = plt.subplots(ncols=2,figsize=(25,9))
        ax[0].barh(data.index,data.values)
        ax[1].pie(data.values,labels = data.index,autopct='%1.1f%%',explode=([0.1]*len(data.index)),startangle=90)
        bar_string = f'A barplot of {data.name}'
        pie_string = f'A barplot of {data.name}'
        ax[0].set_title(bar_string)
        ax[1].set_title(pie_string)
        ax[0].set_ylabel(str(data.name))
        ax[1].set_xlabel(str(data.name))
        plt.tight_layout()
    thresh_widget = Dropdown(options=df.columns,value = df.columns[0])
    interact(make_nominal_plot,feature=thresh_widget)
def make_ordinal_plots(df):
    print('SELECT FEATURE TO EXPLORE BELOW: ')
    def make_ordinal_plot(feature):
        data = df.loc[:,feature].value_counts(normalize=True).sort_index()
        fig,ax = plt.subplots(ncols=2,figsize=(25,9))
        ax[0].barh(data.index,data.values)
        ax[1].pie(data.values,labels = data.index,autopct='%1.1f%%',
                      explode=([0.1]*len(data.index)),startangle=90)
        bar_string = f'A barplot of {data.name}'
        pie_string = f'A pieplot of {data.name}'
        ax[0].set_title(bar_string)
        ax[1].set_title(pie_string)
        ax[0].set_ylabel(str(data.name))
        ax[1].set_xlabel(str(data.name))
    thresh_widget = Dropdown(options=df.columns,value = df.columns[0])
    interact(make_ordinal_plot,feature=thresh_widget)
def make_discrete_plots(df):
    print('SELECT FEATURE TO EXPLORE BELOW: ')
    def make_discrete_plot(feature):
        data = df.loc[:,feature].value_counts(normalize=True).sort_index()
        fig,ax = plt.subplots(ncols=2,figsize=(25,9))
        ax[0].barh(data.index,data.values)
        ax[1].pie(data.values,labels = data.index,autopct='%1.1f%%',explode=([0.1]*len(data.index)),startangle=90)
        bar_string = f'A barplot of {data.name}'
        pie_string = f'A pieplot of {data.name}'
        ax[0].set_title(bar_string)
        ax[1].set_title(pie_string)
        ax[0].set_ylabel(str(data.name))
        ax[1].set_xlabel(str(data.name))
    thresh_widget = Dropdown(options=df.columns,value = df.columns[0])
    interact(make_discrete_plot,feature=thresh_widget)
def make_continuous_plots(df):
    print('SELECT FEATURE TO EXPLORE BELOW: ')
    def make_continuous_plot(feature):
        data = df.loc[:,feature]
        fig,ax = plt.subplots(ncols=2,figsize=(25,9))
        ax[0].hist(data)
        ax[1].boxplot(data)
        bar_string = f'A Histplot of {data.name}'
        box_string = f'A Boxplot of {data.name}'
        ax[0].set_title(bar_string)
        ax[1].set_title(box_string)
        ax[0].set_xlabel(str(data.name))
        ax[1].set_xlabel(str(data.name))
    thresh_widget = Dropdown(options=df.columns,value = df.columns[0])
    interact(make_continuous_plot,feature=thresh_widget)
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import seaborn as sns

def has_an_account(data):

    def classify_account(x):    
        if x['account_fin'] == 1 and x['account_mob'] == 1:
            return 'has_both_acct'
        elif x['account_fin'] == 1 and x['account_mob'] == 0:
            return 'only_fin_acct'
        elif x['account_fin'] == 0 and x['account_mob'] == 1:
            return 'only_mob_acct'
        else:
            return 'no_acct'

    ph_data['Number of accounts'] = ph_data.apply(classify_account , axis = 1)
    subset_account = ph_data[['wpid_random','account','Number of accounts']]
    account_class_mapping = {
    'no_acct': 'has no accounts',
    'only_fin_acct': 'financial institution only',
    'only_mob_acct': 'mobile money only',
    'has_both_acct': 'has both accounts',
    0 : 'No',
    1 : 'Yes'
    }
    subset_account = subset_account.replace({'Number of accounts':account_class_mapping})
    subset_account = subset_account.replace({'account':account_class_mapping})

    figure = plt.figure(figsize=(7,5)  , dpi= 150)

    ax = sns.countplot(data = subset_account, x ='account', 
            hue = 'Number of accounts',
            dodge = False)

    ax.set(xlabel='Has access to an account', ylabel='count')

    # for p in ax.patches:
    #     percentage = '{:.1f}%'.format(100 * p.get_height()/float(len(ph_data)))
    #     x = p.get_x() + p.get_width()
    #     y = p.get_height()
    #     ax.annotate(percentage, (x, y),ha='left')

    return figure    
    
    
def plot_account_activity(data):
    
    ## data wrangling
    fin_activity = ph_data[['wpid_random', 'account', 'account_fin', 'fin9', 'fin10']]

    wide_fin = pd.melt(
        fin_activity,
        id_vars=['wpid_random', 'account', 'account_fin'],
        value_vars=['fin9', 'fin10']
    ).reset_index()

    ## map variables
    fin_mapping = {
        'fin9': 'Deposit',
        'fin10': 'Withdrawal',
        1 : 'Yes',
        2 : 'No',
        3 : 'Don\'t know',
        4 : 'Refused'
    }

    wide_fin = wide_fin.replace({'variable':fin_mapping})
    wide_fin = wide_fin.replace({'value':fin_mapping})
    wide_fin.rename(columns = {'value':'Had at least 1 transaction'}, inplace = True)

    ## creating the plot
    figure = plt.figure(figsize=(7,4)  , dpi= 150)

    ax = sns.countplot(data = wide_fin, y = 'variable', hue ='Had at least 1 transaction', dodge = True)

    ax.set(title='Account activity of those with bank accounts', xlabel='count', ylabel = 'transaction')

    for p in ax.patches:
        percentage = '{:.0f}'.format(p.get_width().round(0))
        x = p.get_x() + p.get_width() + 6
        y = p.get_y() + 0.14
        ax.annotate(percentage, (x, y),ha='center')

    sns.move_legend(ax, "lower right", ncol =2)
        
    return figure


def plot_mobile_activity(data):
    ## data wrangling
    wide_mob = pd.melt(
        data,
        id_vars=['wpid_random', 'account', 'account_fin'],
        value_vars=['fin5']
    ).reset_index()

    ## map variables
    mob_mapping = {
        'fin5': 'Mobile/internet services\nfor financial transactions',
        1 : 'Yes',
        2 : 'No'
    }

    wide_mob = wide_mob.replace({'variable':mob_mapping})
    wide_mob = wide_mob.replace({'value':mob_mapping})
    wide_mob.rename(columns = {'value':'Used service?'}, inplace = True)
        
    ## creating the plot
    figure = plt.figure(figsize=(7,2), dpi= 150)

    ax = sns.countplot(data = wide_mob, y = 'variable', hue ='Used service?', dodge = True)

    ax.set(title='Mobile phone and internet usage', xlabel='count', ylabel = '')

    for p in ax.patches:
        percentage = '{:.0f}'.format(p.get_width().round(0))
        x = p.get_x() + p.get_width() + 6
        y = p.get_y() + 0.14
        ax.annotate(percentage, (x, y),ha='center')

    sns.move_legend(ax, "lower right", ncol =2)
        
    return figure
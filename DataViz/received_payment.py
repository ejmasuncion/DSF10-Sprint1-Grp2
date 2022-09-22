import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import seaborn as sns


def received_payment(ph_data):
    ph_data['Wage received in cash'] = ph_data.apply(
    lambda x: 1 if x['fin34c1'] == 1  else 0,
    axis=1
    )
    ph_data['Government support or Pension received in cash'] = ph_data.apply(
    lambda x: 1 if x['fin39c1'] == 1  else 0,
    axis=1
    )
    ph_data['Agricultural payment received in cash'] = ph_data.apply(
    lambda x: 1 if x['fin43c1'] == 1  else 0,
    axis=1
    )
    ph_data['Busines, servicess, or goods payment received in cash'] = ph_data.apply(
    lambda x: 1 if x['fin47c1'] == 1  else 0,
    axis=1
    )
    ph_data['Wage received in account'] = ph_data.apply(
    lambda x: 1 if x['fin34a'] == 1  else 0,
    axis=1
    )
    ph_data['Government support or Pension received in account'] = ph_data.apply(
    lambda x: 1 if x['fin39a'] == 1  else 0,
    axis=1
    )
    ph_data['Agricultural payment received in account'] = ph_data.apply(
    lambda x: 1 if x['fin43a'] == 1  else 0,
    axis=1
    )
    ph_data['Busines, servicess, or goods payment received in account'] = ph_data.apply(
    lambda x: 1 if x['fin47a'] == 1  else 0,
    axis=1
    )
    ph_data['Wage received through mobile'] = ph_data.apply(
    lambda x: 1 if x['fin34b'] == 1  else 0,
    axis=1
    )
    ph_data['Government support or Pension received through mobile'] = ph_data.apply(
    lambda x: 1 if x['fin39b'] == 1  else 0,
    axis=1
    )
    ph_data['Agricultural payment received through mobile'] = ph_data.apply(
    lambda x: 1 if x['fin43b'] == 1  else 0,
    axis=1
    )
    ph_data['Busines, servicess, or goods payment received through mobile'] = ph_data.apply(
    lambda x: 1 if x['fin47b'] == 1  else 0,
    axis=1
    )
    ph_data['Wage received to a card'] = ph_data.apply(
    lambda x: 1 if x['fin34c2'] == 1  else 0,
    axis=1
    )
    ph_data['Government support or Pension received to a card'] = ph_data.apply(
    lambda x: 1 if x['fin39c2'] == 1  else 0,
    axis=1
    )
    ph_data['Agricultural payment received to a card'] = ph_data.apply(
    lambda x: 1 if x['fin43c2'] == 1  else 0,
    axis=1
    )
    ph_data['Busines, servicess, or goods payment received to a card'] = ph_data.apply(
    lambda x: 1 if x['fin47c2'] == 1  else 0,
    axis=1
    )
    wages = ph_data.groupby(['account']).agg(
    account = ('Wage received in account', 'sum'),
    mob = ('Wage received through mobile', 'sum'),
    cash = ('Wage received in cash', 'sum'),
    card = ('Wage received to a card', 'sum')
    )
    gov = ph_data.groupby(['account']).agg(
    account = ('Government support or Pension received in account', 'sum'),
    mob = ('Government support or Pension received through mobile', 'sum'),
    cash = ('Government support or Pension received in cash', 'sum'),
    card = ('Government support or Pension received to a card', 'sum')
    )
    bus = ph_data.groupby(['account']).agg(
    account = ('Busines, servicess, or goods payment received in account', 'sum'),
    mob = ('Busines, servicess, or goods payment received through mobile', 'sum'),
    cash = ('Busines, servicess, or goods payment received in cash', 'sum'),
    card = ('Busines, servicess, or goods payment received to a card', 'sum')
    )
    agri = ph_data.groupby(['account']).agg(
    account = ('Agricultural payment received in account', 'sum'),
    mob = ('Agricultural payment received through mobile', 'sum'),
    cash = ('Agricultural payment received in cash', 'sum'),
    card = ('Agricultural payment received to a card', 'sum')
    )
    receive = ph_data.iloc[:, -16:].sum()
    pieces = (wages, gov, bus, agri)

    # Give the columns the same labels in each sub dataframe
    # I've used numbers for convenience - you can give more descriptive names if you want
    for sub_df in pieces:
        sub_df.columns= ('FI account', 'mobile phone', 'cash', 'card')
    
    df_final = pd.concat(pieces)

    df_final.index = ['wages', 'wages', 'gov.support or pension', 'gov.support or pension', 'business, services, goods', 'business, services, goods', 'agricultural payment', 'agricultural payment']
    Has_account = ['Has no account', 'Has account', 'Has no account', 'Has account', 'Has no account', 'Has account', 'Has no account', 'Has account']
    df_final['Has account'] = Has_account

    figure = plt.figure(figsize=(15, 10))
    axs = figure.subplots(2,1)
    for ax, (c, channel_group) in zip(axs, df_final.groupby("Has account")):
        ax = channel_group.plot(kind='barh', ax=ax, stacked=True, subplots=False )
        ax.set_title(c)
        ax.legend(title = 'Channel')

    return figure

import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import seaborn as sns

def reasons_no_account(ph_data):
    ph_data['FI are too far away'] = ph_data.apply(
        lambda x: 1 if x['fin11a'] == 1  else 0,
        axis=1
    )
    ph_data['FS are too expensive'] = ph_data.apply(
        lambda x: 1 if x['fin11b'] == 1  else 0,
        axis=1
    )
    ph_data['No necessary documentation'] = ph_data.apply(
        lambda x: 1 if x['fin11c'] == 1  else 0,
        axis=1
    )
    ph_data['No trust in FI'] = ph_data.apply(
        lambda x: 1 if x['fin11d'] == 1  else 0,
        axis=1
    )
    ph_data['Religious reasons'] = ph_data.apply(
        lambda x: 1 if x['fin11e'] == 1  else 0,
        axis=1
    )
    ph_data['Not enough money to use FI'] = ph_data.apply(
        lambda x: 1 if x['fin11f'] == 1  else 0,
        axis=1
    )
    ph_data['Family already has account'] = ph_data.apply(
        lambda x: 1 if x['fin11g'] == 1  else 0,
        axis=1
    )
    ph_data['No need for FS at a formal institution'] = ph_data.apply(
        lambda x: 1 if x['fin11h'] == 1  else 0,
        axis=1
    )
    
    reasons = ph_data.groupby(['economy']).agg(
        FI_are_too_far_away=('FI are too far away', 'sum'),
        FS_are_too_expensive = ('FS are too expensive', 'sum'),
        No_necessary_documentation = ('No necessary documentation', 'sum'),
        No_trust_in_FI = ('No trust in FI', 'sum'),
        Religious_reasons = ('Religious reasons', 'sum'),
        Not_enough_money_to_use_FI = ('Not enough money to use FI', 'sum'),
        Family_already_has_account = ('Family already has account', 'sum'),
        No_need_for_FS = ('No need for FS at a formal institution', 'sum')  
    ).reset_index()
    reasons
    
    reason_table = pd.melt(
        reasons,
        id_vars=['economy'],
        value_vars=['FI_are_too_far_away', 'FS_are_too_expensive', 'No_necessary_documentation', 'No_trust_in_FI', 'Religious_reasons', 'Not_enough_money_to_use_FI',
                'Family_already_has_account', 'No_need_for_FS' ]
    )

    reason_table = reason_table.replace(
    {
            'FI_are_too_far_away' : 'FI are too far away',
            'FS_are_too_expensive' : 'FS are too expensive',
            'No_necessary_documentation' : 'No necessary documentation',
            'No_trust_in_FI' : 'No trust in FI',
            'Religious_reasons': 'Religious reasons',
            'Not_enough_money_to_use_FI': 'Not enough money to use FI',
            'Family_already_has_account': 'Family already has an account',
            'No_need_for_FS': 'No need for formal FI'
            }
    )
    
    reason_table = reason_table.sort_values('value', ascending=True).head(10).reset_index(drop=True)
    # Set figure size
    figure = plt.figure(figsize=(6,3)  , dpi=200)

    plt.barh(
        reason_table['variable'],
        reason_table['value']
    )

    # Set title
    plt.title('Reasons for Not Having an Account at a Bank/FI')

    return figure

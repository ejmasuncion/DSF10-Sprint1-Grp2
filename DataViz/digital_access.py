import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import seaborn as sns


def digital_access(data):
    data['fin14'] = data['fin14a'] + data['fin14b']
    data['has_digital access'] = data['fin14'].apply(
    lambda x:1 if (x >= 1 and x <= 3) else 0
    )

    data['Digital Access'] = data['has_digital access'].apply(
        lambda x:'Yes' if (x >= 1 and x <= 3) else 'No'
    )
    PH_data = data[data['economy']=='Philippines']

    fig, ax = plt.subplots(figsize=(10, 5))
    sns.countplot(x='Digital Access', data=PH_data)
    
    # Annotate percentage
    total = len(PH_data['Digital Access'])
    for p in ax.patches:
        percentage = '{:.1f}%'.format(100 * p.get_height()/total)
        x = p.get_x() + p.get_width() - 0.5
        y = p.get_height() + 0.5
        ax.annotate(percentage, (x, y))
        
    return fig

def digital_access_sea(data):
    data['fin14'] = data['fin14a'] + data['fin14b']

    #Filter mobile/internet access (FI access)
    data['has_digital access'] = data['fin14'].apply(
        lambda x:1 if (x >= 1 and x <= 3) else 0
    )

    digital_grouped_data = data.groupby(['economy','regionwb']).agg(
    with_digitalaccess=('has_digital access', 'sum'),
    total_population=('wpid_random', 'count'))

    digital_grouped_data['percent of banked with digital access'] = digital_grouped_data['with_digitalaccess'] * 100.0 / digital_grouped_data['total_population']
    digital_grouped_data = digital_grouped_data.reset_index()  

    SEA_data = digital_grouped_data[digital_grouped_data['regionwb']=='East Asia & Pacific (excluding high income)']
    SEA_data = SEA_data.sort_values('percent of banked with digital access', ascending=[False])

    figure = plt.figure(figsize=(6,3)  , dpi=200)
    plt.bar(
        SEA_data['economy'],
        SEA_data['percent of banked with digital access']
    )
    plt.title("People with Digital Access in Southeast Asia")

    # Set labels
    plt.xlabel('SEA Country')
    plt.ylabel('Percentage')

    plt.xticks(rotation=45)
        
    return figure
import matplotlib.pyplot as plt
import seaborn as sns

from utils import format_number

def plot_top_streamed_artists(data):
    artists_streams = data.groupby('artist(s)_name')['streams'].sum().reset_index().sort_values(by='streams', ascending=False)
    top_artists = artists_streams.head(10)
    top_artists['formatted_streams'] = top_artists['streams'].apply(format_number)

    plt.figure(figsize=(10,6))
    sns.barplot(data=top_artists, x='streams', y='artist(s)_name', hue='artist(s)_name', palette='magma', dodge=False, legend=False)
    plt.title('Top 10 Most Streamed Artists')
    plt.xlabel('Total Streams')
    plt.ylabel('Artists')

    for index, value in enumerate(top_artists['streams']):
        plt.text(value, index, top_artists['formatted_streams'].iloc[index], va='center', ha='left', color='black')

    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()
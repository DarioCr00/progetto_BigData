import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from utils import format_number

def plot_top_streamed_songs(data):
    data['streams'] = pd.to_numeric(data['streams'], errors='coerce')

    # Raggruppamento e somma degli stream per traccia
    top_streamed_songs = data.groupby('track_name')['streams'].sum().reset_index()
    top_streamed_songs = top_streamed_songs.sort_values(by='streams', ascending=False).head(10)
    top_streamed_songs['formatted_streams'] = top_streamed_songs['streams'].apply(format_number)

    # Creazione del grafico
    plt.figure(figsize=(12,8))
    sns.barplot(data=top_streamed_songs, x="streams", y='track_name', hue='track_name', palette='viridis', dodge=False, legend=False)
    plt.title('Top 10 Most Streamed Songs of All Time')
    plt.xlabel('Total Streams')
    plt.ylabel('Track Name')

    for index, value in enumerate(top_streamed_songs['streams']):
        plt.text(value, index, top_streamed_songs['formatted_streams'].iloc[index], va='center', ha='left', color='black')
    
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()
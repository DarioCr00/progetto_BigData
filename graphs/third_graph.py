import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from utils import chromatic_circle_palette

def plot_playlist_and_charts_analysis(data):
    top_10_songs = data.nlargest(10, 'streams')
    top_10_songs = data.sort_values('streams', ascending=False).head(10)
    top_10_songs['track_and_artist'] = top_10_songs['track_name'] + ' - ' + top_10_songs['artist(s)_name']
    print(top_10_songs)

    # Estrazione dei valori per le playlist e le classifiche
    song_names_and_authors = top_10_songs['track_and_artist']
    playlist_counts = top_10_songs['in_spotify_playlists']
    chart_ranks = top_10_songs['in_spotify_charts']

    # Palette
    chart_palette = sns.color_palette("flare", len(song_names_and_authors)) 

    # Creazione della figura e della griglia
    fig = plt.figure(figsize=(14, 16))

    # Playlist - Grafico a torta
    ax1 = plt.subplot2grid((2, 2), (0, 0), colspan=2)
    wedges = ax1.pie(playlist_counts, 
                     autopct='%1.1f%%', 
                     startangle=90, 
                     colors=chromatic_circle_palette(len(top_10_songs)), 
                     pctdistance=0.75,
                     wedgeprops={'edgecolor': 'white', 'linewidth': 0.5})  
    ax1.set_title('Distribuzione del Numero di Playlist Spotify', pad=20, ha='center')

    ax1.legend(wedges, song_names_and_authors, title="Tracce", loc="center left", bbox_to_anchor=(1, 0.5), fontsize="small", title_fontsize="small", ncol=1, frameon=False)

    # Classifiche - Grafico a barre
    ax2 = plt.subplot2grid((2, 2), (1, 0), colspan=2)
    sns.barplot(x=chart_ranks, y=song_names_and_authors, ax=ax2, palette=chart_palette)
    ax2.set_title('Posizione in Classifica Spotify', pad=20)
    ax2.set_xlabel('Posizione (1 è la più alta)', labelpad=20)

    ax2.set_ylabel('')
    ax2.tick_params(axis='y', labelsize=5.5)

    ax2.invert_xaxis()
    ax2.set_xlim(ax2.get_xlim()[0], ax2.get_xlim()[1] * 1.3)
    ax2.margins(y=0.01)
    ax2.tick_params(axis='x', pad=15)

    plt.tight_layout()
    plt.subplots_adjust(left=0.2, right=0.8, top=0.9, bottom=0.1)
    plt.show()
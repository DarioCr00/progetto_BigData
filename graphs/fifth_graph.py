import matplotlib.pyplot as plt
import seaborn as sns

def plot_platforms_confront(data):

    # Verifica dei valori mancanti/nulli per assicurarsi che i dati siano completi per l'analisi
    print(data.isnull().sum())

    # a. Distribuzione del numero di playlist per Spotify e Apple Music (affiancato)
    fig, axs = plt.subplots(1, 2, figsize=(16, 6))

    sns.histplot(data['in_spotify_playlists'], kde=True, color='blue', bins=30, alpha=0.3, ax=axs[0])
    sns.histplot(data['in_apple_playlists'], kde=True, color='red', bins=30, alpha=0.5, ax=axs[1])

    axs[0].set_title('Distribuzione del Numero di Playlist - Spotify')
    axs[0].set_xlabel('Numero di Playlist')
    axs[0].set_ylabel('Conteggio')
    
    axs[1].set_title('Distribuzione del Numero di Playlist - Apple Music')
    axs[1].set_xlabel('Numero di Playlist')
    axs[1].set_ylabel('Conteggio')

    plt.tight_layout()
    plt.show()

    # b. Boxplot per il confronto tra Spotify e Apple Music (affiancato)
    fig, axs = plt.subplots(1, 2, figsize=(16, 6))

    sns.boxplot(data=data[['in_spotify_playlists']], palette=['blue'], ax=axs[0])
    axs[0].set_title('Numero di Playlist - Spotify')
    axs[0].set_xlabel('Spotify')
    axs[0].set_ylabel('Numero di Playlist')

    sns.boxplot(data=data[['in_apple_playlists']], palette=['red'], ax=axs[1])
    axs[1].set_title('Numero di Playlist - Apple Music')
    axs[1].set_xlabel('Apple Music')
    axs[1].set_ylabel('Numero di Playlist')

    plt.tight_layout()
    plt.show()

    # c. Scatterplot per visualizzare la correlazione tra le playlist (grafico singolo)
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=data, x='in_spotify_playlists', y='in_apple_playlists', alpha=0.5)
    plt.xlabel('Spotify Playlists')
    plt.ylabel('Apple Music Playlists')
    plt.title('Correlazione tra Playlist di Spotify e Apple Music')
    plt.show()

    # d. Heatmap per visualizzare la matrice di correlazione (grafico singolo)
    correlation = data[['in_spotify_playlists', 'in_apple_playlists']].corr()
    print("\n\nCorrelazione tra Spotify e Apple Music Playlists:")
    print(correlation)
    
    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation, annot=True, cmap='viridis', fmt='.2f', linewidths=.5, vmin=0, vmax=1)
    plt.title('Correlazione tra Spotify e Apple Music Playlists')
    plt.show()

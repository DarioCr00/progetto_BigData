import matplotlib.pyplot as plt
import seaborn as sns

def plot_artist_count_distribution(data):

    plt.figure(figsize=(10, 6))
    sns.histplot(data['artist_count'], bins=range(1, data['artist_count'].max() + 2), kde=True, discrete=True) # kde rimane per visualizzare la densità stimata
    plt.title('Distribuzione del Numero di Artisti per Brano')
    plt.xlabel('Numero di Artisti')  # indica il numero di artisti che hanno partecipato in un singolo brano
    plt.ylabel('Numero di Brani')  # indica l'effettivo numero di brani che hanno quel numero di artisti featured
    plt.ylim(0, data['artist_count'].value_counts().max() + 50)  # i 50 sono per la spaziatura
    plt.yticks(range(0, data['artist_count'].value_counts().max() + 50, 50))
    plt.show()
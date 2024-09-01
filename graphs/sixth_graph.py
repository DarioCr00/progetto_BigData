import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

figsize_single = (12, 6)
figsize_double = (18, 6)

def plot_correlation_matrix(data):
    fig1, axs1 = plt.subplots(1, 2, figsize=figsize_double)
    numeric_cols = data.filter(like='%')
    corr = numeric_cols.corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm', ax=axs1[0], cbar=False)
    axs1[0].set_title('Matrice di Correlazione', loc='center')
    description1 = (
    "La matrice di correlazione mostra la relazione tra le variabili numeriche. "
    "I valori vanno da -1 a 1, dove valori vicini a 1 indicano una forte correlazione positiva, "
    "mentre valori vicini a -1 indicano una forte correlazione negativa."
    )
    axs1[1].text(0.1, 0.5, description1, ha='left', va='center', fontsize=12, wrap=True)
    axs1[1].axis('off')
    plt.tight_layout()
    plt.show()


def plot_histograms(data):
    fig2, axs2 = plt.subplots(1, 3, figsize=figsize_double)
    sns.histplot(data['danceability_%'], kde=True, ax=axs2[0])
    sns.histplot(data['valence_%'], kde=True, ax=axs2[1])
    sns.histplot(data['energy_%'], kde=True, ax=axs2[2])
    for ax, label in zip(axs2, ['Danceability', 'Valence', 'Energy']):
        ax.set_xlim(0, 100)
        ax.set_xlabel('Percentuale (%)')
        ax.set_title(f'Distribuzione {label}', loc='center')
    descriptions2 = [
        "Distribuzione della danceability:\nmisura quanto un brano è adatto per ballare.",
        "Distribuzione della valence:\nmisura la positività percepita della musica.",
        "Distribuzione dell'energy:\nmisura l'intensità e l'attività percepita del brano."
    ]
    for ax, desc in zip(axs2, descriptions2):
        ax.text(0.5, -0.2, desc, ha='center', va='center', transform=ax.transAxes, fontsize=10)
    plt.tight_layout()
    plt.show()


def plot_boxplot(data): 
    fig3, axs3 = plt.subplots(1, 2, figsize=figsize_double)
    sns.boxplot(x=data['acousticness_%'], ax=axs3[0])
    sns.boxplot(x=data['liveness_%'], ax=axs3[1])
    for ax, label in zip(axs3, ['Acousticness', 'Liveness']):
        ax.set_xlabel('Percentuale (%)')
        ax.set_ylabel(f'{label} (%)')
        median = data[f'{label.lower()}_%'].median()
        ax.axvline(median, color='red', linestyle='--', label=f'Mediana: {median:.2f}')
        ax.legend()
        ax.set_title(f'Distribuzione {label}', loc='center')
    descriptions3 = [
        "Distribuzione dell'acousticness:\nmisura quanto il brano è acustico.",
        "Distribuzione della liveness:\nmisura la probabilità che il brano sia stato registrato dal vivo."
    ]
    for ax, desc in zip(axs3, descriptions3):
        ax.text(0.5, -0.2, desc, ha='center', va='center', transform=ax.transAxes, fontsize=10)
    plt.tight_layout()
    plt.show()


def plot_positive_correlation_scatterplots(data):
    fig4, axs4 = plt.subplots(1, 2, figsize=figsize_double)
    sns.scatterplot(x=data['valence_%'], y=data['danceability_%'], ax=axs4[0], alpha=0.75)
    sns.scatterplot(x=data['danceability_%'], y=data['energy_%'], ax=axs4[1], alpha=0.75)
    axs4[0].set_xlabel('Valence (%)')
    axs4[0].set_ylabel('Danceability (%)')
    axs4[0].set_title('Scatterplot: Valence vs Danceability  (0.41)', loc='center')
    axs4[1].set_xlabel('Danceability (%)') 
    axs4[1].set_ylabel('Energy (%)')
    axs4[1].set_title('Scatterplot: Danceability vs Energy (0.2)', loc='center')
    descriptions4 = [
        "Relazione tra positività e danceability:\ncorrelazione moderata e positiva.",
        "Relazione tra danceability e intensità:\ncorrelazione debole e positiva."
    ]
    for ax, desc in zip(axs4, descriptions4):
        ax.text(0.5, -0.2, desc, ha='center', va='center', transform=ax.transAxes, fontsize=10)
    plt.subplots_adjust(left=0.1, right=0.5, top=0.9, bottom=0.1, wspace=0.1, hspace=0.4)
    plt.tight_layout()
    plt.show()


def plot_around_zero_correlation_scatterplots(data):
    fig5, axs5 = plt.subplots(1, 2, figsize=figsize_double)
    sns.scatterplot(x=data['valence_%'], y=data['liveness_%'], ax=axs5[0], alpha=0.75)
    sns.scatterplot(x=data['instrumentalness_%'], y=data['energy_%'], ax=axs5[1], alpha=0.75)
    axs5[0].set_xlabel('Valence (%)')
    axs5[0].set_ylabel('Liveness (%)')
    axs5[0].set_title('Scatterplot: Valence vs Liveness (0.021)', loc='center')
    axs5[1].set_xlabel('Instrumentalness (%)')
    axs5[1].set_ylabel('Energy (%)')
    axs5[1].set_title('Scatterplot: Instrumentalness vs Energy (-0.039)', loc='center')
    descriptions5 = [
        "Relazione tra positività vivacità:\n correlazione positiva ma molto debole, quasi inesistente.",
        "Relazione tra strumentalità intensità:\ncorrelazione negativa ma molto debole, quasi inesistente."
    ]
    for ax, desc in zip(axs5, descriptions5):
        ax.text(0.5, -0.2, desc, ha='center', va='center', transform=ax.transAxes, fontsize=10)
    plt.subplots_adjust(left=0.1, right=0.5, top=0.9, bottom=0.1, wspace=0.1, hspace=0.4)
    plt.tight_layout()
    plt.show()


def plot_negative_correlation_scatterplot(data):
    fig6, ax6 = plt.subplots(1, 1, figsize=figsize_single)
    sns.scatterplot(x=data['energy_%'], y=data['acousticness_%'], ax=ax6, alpha=0.75)
    ax6.set_aspect('equal') 
    ax6.set_xlabel('Energy (%)')
    ax6.set_ylabel('Acousticness (%)')
    ax6.set_title('Scatterplot: Energy vs Acousticness (-0.58)', loc='center')
    description6 = "Relazione tra intensità componente acustica: \ncorrelazione moderata e negativa."
    ax6.text(0.5, -0.2, description6, ha='center', va='center', transform=ax6.transAxes, fontsize=10)
    plt.subplots_adjust(left=0.06, right=0.5, top=0.9, bottom=0.1, wspace=0.1, hspace=0.4)
    plt.tight_layout()
    plt.show()


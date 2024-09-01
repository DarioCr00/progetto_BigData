import pandas as pd

from graphs.first_graph import plot_top_streamed_songs
from graphs.second_graph import plot_top_streamed_artists
from graphs.third_graph import plot_playlist_and_charts_analysis
from graphs.fourth_graph import plot_artist_count_distribution
from graphs.fifth_graph import plot_platforms_confront
from graphs.sixth_graph import plot_correlation_matrix, plot_histograms, plot_boxplot, plot_positive_correlation_scatterplots, plot_around_zero_correlation_scatterplots, plot_negative_correlation_scatterplot

data = pd.read_csv('dataset/spotify-2023.csv', delimiter=',', encoding='ISO-8859-1')

plot_top_streamed_songs(data) #1

plot_top_streamed_artists(data) #2

plot_playlist_and_charts_analysis(data) #3

plot_artist_count_distribution(data) #4

plot_platforms_confront(data) #5

plot_correlation_matrix(data) #6a

plot_histograms(data) #6b

plot_boxplot(data) #6c

plot_positive_correlation_scatterplots(data) #6d

plot_around_zero_correlation_scatterplots(data) #6e

plot_negative_correlation_scatterplot(data) #6f

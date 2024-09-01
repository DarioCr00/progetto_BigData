import matplotlib.pyplot as plt


def format_number(num):
    if num >= 1_000_000_000_000:
        return f'{num/ 1_000_000_000_000:.1f}T' #trilioni con una cifra decimale
    elif num >= 1_000_000_000:
        return f'{num/ 1_000_000_000:.1f}B' #miliardi con una cifra decimale
    elif num >= 1_000_000:
        return f'{num/ 1_000_000:.1f}M' #milioni con una cifra decimale
    elif num >= 1_000:
        return f'{num / 1_000:.1f}K' #migliaia con una cifra decimale
    else:
        return str(num)
    
def chromatic_circle_palette(n_colors):
    cmap = plt.get_cmap("hsv") # usa una mappa colori con Hue, Saturation e Value
    return [cmap(i / n_colors) for i in range(n_colors)]
    
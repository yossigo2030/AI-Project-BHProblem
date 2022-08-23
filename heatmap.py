# library
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def show_map(array, save = False, results_path = 'results.png'):
    plt.close("all")
    df = pd.DataFrame(array)
    if save:
        plt.savefig(results_path)
    sns.heatmap(df)
    plt.show()
# library
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def show_map(array, save=True, results_path='results.png'):
    plt.close("all")
    df = pd.DataFrame(array)
    sns.heatmap(df)
    if save:
        try:
            plt.savefig(results_path)
        except Exception:
            pass
    else:
        plt.show()
    plt.close()

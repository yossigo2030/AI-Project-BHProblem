# library
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def show_map(array_list, save=True, results_path='results.png'):
    fig, axs = plt.subplots(nrows=2, ncols=10, figsize=(44, 10))
    for j, arrays in enumerate(array_list):
        for i, array in enumerate(arrays):
            # df = pd.DataFrame(array)
            sns.heatmap(array, cbar=False, ax=axs[i][j])
    if save:
        try:
            plt.savefig(results_path)
        except Exception:
            pass
    else:
        plt.show()
    plt.close()

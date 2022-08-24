# library
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# FFMPEG party trick: ffmpeg -framerate 30 -pattern_type glob -i '*.png' filename.mp4
def show_map(array_list, save=True, results_path='results.png'):
    fig, axs = plt.subplots(nrows=2, ncols=5, figsize=(22, 10))
    for j, arrays in enumerate(array_list):
        for i, array in enumerate(arrays):
            # df = pd.DataFrame(array)
            sns.heatmap(array, cbar=False, ax=axs[j // 5][j % 5])
            break
    if save:
        try:
            plt.savefig(results_path)
        except Exception:
            pass
    else:
        plt.show()
    plt.close()

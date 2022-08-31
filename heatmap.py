# library
import matplotlib.pyplot as plt
import seaborn as sns


# FFMPEG party trick: ffmpeg -framerate 30 -pattern_type glob -i '*.png' filename.mp4
def show_map(array_list, save=True, results_path='results.png'):
    fig, axs = plt.subplots(nrows=2, ncols=5, figsize=(22, 10))
    for i, array in enumerate(array_list):
        # df = pd.DataFrame(array)
        sns.heatmap(array, cbar=False, ax=axs[i // 5][i % 5])
    if save:
        try:
            plt.savefig(results_path)
        except Exception:
            pass
    else:
        plt.show()
    plt.close()

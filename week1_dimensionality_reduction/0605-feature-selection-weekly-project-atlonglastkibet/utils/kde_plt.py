import matplotlib.pyplot as plt
import seaborn as sns

def kde_plt_grid(df, cols, user_title=None, color='Green',rows=8, cols_per_row=5,figsize=(20,12)):
    fig, ax = plt.subplots(rows, cols_per_row, figsize=figsize)
    ax = ax.flatten()

    for i,col in enumerate (cols):
        if i<len(ax):
            sns.kdeplot (df[col], fill=True, color=color, ax=ax[i])
            ax[i].set_title(col)
            # Customize subplot appearance
            ax[i].set_title(col, fontsize=10)  # Smaller title font
            ax[i].tick_params(axis='both', labelsize=8)  # Adjust tick label size
            ax[i].grid(True, linestyle='--', alpha=0.6)

    for j in range(i+1, len(ax)):
        fig.delaxes(ax[j])
    
    fig.suptitle(user_title, fontsize=14, fontweight='bold', y=1.02)
    
    plt.tight_layout()
    plt.show()
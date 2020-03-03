from .core import BaseHist
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches


class Hist(BaseHist):
    
    def pull_plot(self, func, *, ax=None, pull_ax=None, figsize=(8, 8), labelsize=12): 
        '''
        add more formatting options here as needed!
        If ax and pull_ax are none, make a new figure and add the two axes with the proper ratio between them.
        Otherwise, just use ax and pull_ax.
        '''
        
        if callable(func) == False:
            raise TypeError(
                    "Only callable parameter is accepted in pull plot."
                )
        
        # Compute PDF values
        values = func(*self.axes.centers)*self.sum()*self.axes[0].widths
        yerr = np.sqrt(self.view())
        
        # Compute Pulls
        pulls = (self.view() - values) / yerr
        # Convert inf pulls to 0
        pulls = [x if np.abs(x) != np.inf else 0 for x in pulls]
        
        plt.figure(figsize=figsize, dpi=80)
        grid = plt.GridSpec(4, 4, wspace=0.5, hspace=0.5)
        
        '''
        Main: plot the pulls using Matplotlib errorbar method
        '''
        ax = plt.subplot(grid[0:3, :])
        
        plt.errorbar(self.axes.centers[0], self.view(), yerr, fmt='o', ecolor='lightsteelblue',        
                                                     ms=3,mfc='wheat',mec='salmon',capsize=3)
        plt.plot(self.axes.centers[0], values, color='orange', lw=2)
        plt.ylabel("Counts", size=labelsize)
        
        
        
        '''
        Pull: plot the pulls using Matplotlib bar method
        '''
        pull_ax = plt.subplot(grid[3, :], sharex=ax)
        left_edge = self.axes.edges[0][0]
        right_edge = self.axes.edges[-1][-1]
        width = (right_edge - left_edge) / len(pulls)

        rect0 = patches.Rectangle([left_edge, 0], width * len(pulls), 1, color='blue', alpha=0.4)
        pull_ax.add_patch(rect0)
        rect1 = patches.Rectangle([left_edge, -1], width * len(pulls), 1, color='blue', alpha=0.4)
        pull_ax.add_patch(rect1)
        rect2 = patches.Rectangle([left_edge, -2], width * len(pulls), 1, color='blue', alpha=0.2)
        pull_ax.add_patch(rect2)
        rect3 = patches.Rectangle([left_edge, -3], width * len(pulls), 1, color='blue', alpha=0.1)
        pull_ax.add_patch(rect3)
        rect4 = patches.Rectangle([left_edge, 1], width * len(pulls), 1, color='blue', alpha=0.2)
        pull_ax.add_patch(rect4)
        rect5 = patches.Rectangle([left_edge, 2], width * len(pulls), 1, color='blue', alpha=0.1)
        pull_ax.add_patch(rect5)
        
        plt.xticks(size=labelsize)
        plt.yticks(size=labelsize)
        plt.xlim(-3, 3)
        plt.xlim(-3, 3)
        plt.xlabel(self.axes[0].metadata["title"], size=labelsize)
        plt.ylabel("Pull", size=labelsize)
        plt.bar(self.axes.centers[0], pulls, width=width)
        
        plt.show()
        
        return ax, pull_ax
    
    pass

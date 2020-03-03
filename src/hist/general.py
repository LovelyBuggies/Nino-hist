from .core import BaseHist
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches


class Hist(BaseHist):
    
    def pull_plot(self, func, ax=None, pull_ax=None, size="Large", theme="Chrome"): 
        
        # Type judgement
        if callable(func) == False:
            raise TypeError(
                    "Only callable parameter is accepted in pull plot."
                )
        
        '''
        Size conversion:
        We support the following options:
            'H' -- huge figure, figuer size = (32, 32);
            'L' -- large figure, figuer size = (16, 16);
            'M' -- medium figure, figuer size = (8, 8);
            'S' -- small figure, figuer size = (4, 4);
            'T' -- tiny figure, figuer size = (2, 2);
        '''
        if size.lower() == "huge" or size.lower() == "h":
            figsize = (32, 32)
            labelsize = 48
        elif size.lower() == "large" or size.lower() == "l":
            figsize = (16, 16)
            labelsize = 24
        elif size.lower() == "medium" or size.lower() == "m":
            figsize = (8, 8)
            labelsize=12
        elif size.lower() == "small" or size.lower() == "s":
            figsize = (4, 4)
            labelsize = 6
        elif size.lower() == "tiny" or size.lower() == "t":
            figsize = (2, 2)
            labelsize = 3
        else:
            raise NameError(
                    f"Size parameter {size} is not support." 
                )
            
        '''
        Theme conversion:
        We support the following options:
            'Chrome' -- Chrome theme;
            ...
            ...
            ...
        '''
        if theme.lower() == "chrome":
            eb_ecolor = eb_mfc = eb_mec = 'forestgreen'
            eb_fmt, eb_ms, eb_capsize, eb_capthick, eb_alpha = \
                                    'o', labelsize/4, labelsize/12, labelsize/12, .8         # error bar
            vp_color, vp_ls, vp_lw, vp_alpha = 'orange', '-', labelsize/3*2, .4              # values plot
            mp_color, mp_lw = 'indianred', labelsize/6                                       # mean plot
            pp_color, pp_alpha, pp_ec = 'cornflowerblue', .4, None                           # patches plot
            lgs_size = labelsize                                                            # legend size
        
        
        # Compute PDF values
        values = func(*self.axes.centers)*self.sum()*self.axes[0].widths
        yerr = np.sqrt(self.view())
        
        # Compute Pulls
        pulls = (self.view() - values) / yerr
        # Convert inf pulls to 0
        pulls = [x if np.abs(x) != np.inf else 0 for x in pulls]
        
        plt.figure(figsize=figsize)
        grid = plt.GridSpec(4, 4, wspace=0.5, hspace=0.5)
        
        '''
        Main: plot the pulls using Matplotlib errorbar method
        '''
        ax = plt.subplot(grid[0:3, :])
        
        plt.errorbar(self.axes.centers[0], self.view(), yerr,\
                     fmt=eb_fmt, ecolor=eb_ecolor, ms=eb_ms, mfc=eb_mfc, mec=eb_mec,\
                     capsize=eb_capsize, capthick=eb_capthick, alpha=eb_alpha, label='Observation')
        plt.plot(self.axes.centers[0], values, color=vp_color, ls=vp_ls, lw=vp_lw, alpha=vp_alpha, label='Values')
        plt.plot(self.axes.centers[0], (self.view()+values)/2, color=mp_color, lw=mp_lw, label='Mean')
        ax.legend(prop={'size': lgs_size})
        plt.xticks(size=labelsize)
        plt.yticks(size=labelsize)
        plt.ylabel("Counts", size=labelsize)
        
        
        '''
        Pull: plot the pulls using Matplotlib bar method
        '''
        pull_ax = plt.subplot(grid[3, :], sharex=ax)
        left_edge = self.axes.edges[0][0]
        right_edge = self.axes.edges[-1][-1]
        width = (right_edge - left_edge) / len(pulls)

        rect0 = patches.Rectangle([left_edge, 0], width * len(pulls), 1, color=pp_color, ec=pp_ec, alpha=pp_alpha)
        pull_ax.add_patch(rect0)
        rect1 = patches.Rectangle([left_edge, -1], width * len(pulls), 1, color=pp_color, ec=pp_ec, alpha=pp_alpha)
        pull_ax.add_patch(rect1)
        rect2 = patches.Rectangle([left_edge, -2], width * len(pulls), 1, color=pp_color, ec=pp_ec, alpha=pp_alpha/2)
        pull_ax.add_patch(rect2)
        rect3 = patches.Rectangle([left_edge, -3], width * len(pulls), 1, color=pp_color, ec=pp_ec, alpha=pp_alpha/4)
        pull_ax.add_patch(rect3)
        rect4 = patches.Rectangle([left_edge, 1], width * len(pulls), 1, color=pp_color, ec=pp_ec, alpha=pp_alpha/2)
        pull_ax.add_patch(rect4)
        rect5 = patches.Rectangle([left_edge, 2], width * len(pulls), 1, color=pp_color, ec=pp_ec, alpha=pp_alpha/4)
        pull_ax.add_patch(rect5)
        
        plt.xticks(size=labelsize)
        plt.yticks(size=labelsize)
        plt.xlim(left_edge, right_edge)
        plt.xlim(left_edge, right_edge)
        plt.xlabel(self.axes[0].metadata["title"], size=labelsize)
        plt.ylabel("Pull", size=labelsize)
        plt.bar(self.axes.centers[0], pulls, width=width)
        
        plt.show()
        
        return ax, pull_ax
    
    pass

from .core import BaseHist

__all__ = ("Theme",)

from .theme import Theme
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from scipy.optimize import curve_fit


class Hist(BaseHist):
    
    def pull_plot(self, func, fig=None, ax=None, pull_ax=None, size="Large", theme="Chrome"): 
        '''
            Make a pull plot. Inputing the figure (new figure if None),\
            ax (new axis if None), pull_ax (new axis if None), size \
            (default "Large"), and theme (default "Chrome") to this func\
            will generate a pull plot and return the figure and axes.
        '''
        # Type judgement
        if callable(func) == False:
            raise TypeError(
                    "Callable parameter func is supported in pull plot."
                )
        
        '''
        Sizes:
            - 'H': huge figure, figuer size = (32, 32);
            - 'L': large figure, figuer size = (16, 16);
            - 'M': medium figure, figuer size = (8, 8);
            - 'S': small figure, figuer size = (4, 4);
            - 'T': tiny figure, figuer size = (2, 2);
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
                    f"Size paramerter size {size} is not support." 
                )
         
        '''
        Themes:
            - 'Chrome'
            - 'Spring'
            - 'Summer'
            - 'Autumn'
            - 'Winter'
            - 'Cool'
            - 'Hot'
        '''
        eb_ecolor, eb_mfc,eb_mec, eb_fmt, eb_ms, eb_capsize, eb_capthick, eb_alpha,\
        vp_color, vp_ls, vp_lw, vp_alpha, mp_color, mp_ls, mp_lw, mp_alpha, fp_color,\
        fp_ls, fp_lw, fp_alpha, lg_size, pp_color, pp_alpha, pp_ec, bar_color = Theme(theme).to_param(labelsize)
        
        
        '''
        Computation and Fit
        '''
        # Compute PDF values
        values = func(*self.axes.centers)*self.sum()*self.axes[0].widths
        yerr = np.sqrt(self.view())
        
        # Compute fit values: using func as fit model
        popt, pcov = curve_fit(f=func, xdata=self.axes.centers[0], ydata=self.view())
        fit = func(self.axes.centers[0], *popt)
        
        # Compute pulls: containing no INF values
        pulls = (self.view() - values) / yerr
        pulls = [x if np.abs(x) != np.inf else 0 for x in pulls]
        
        
        '''
        Figure Construction: construct the figure and axes
        '''
        if fig == None:
            fig = plt.figure(figsize=figsize)
            grid = fig.add_gridspec(4, 4, wspace=0.5, hspace=0.5)
        else:
            grid = fig.add_gridspec(4, 4, wspace=0.5, hspace=0.5)
            
        if ax == None:
            ax = fig.add_subplot(grid[0:3, :])
        else:
            pass
        
        if pull_ax == None:
            pull_ax = fig.add_subplot(grid[3, :], sharex=ax)
        else:
            pass
        
        
        '''
        Main: plot the pulls using Matplotlib errorbar and plot methods
        '''
        ax.errorbar(self.axes.centers[0], self.view(), yerr,\
                     fmt=eb_fmt, ecolor=eb_ecolor, ms=eb_ms, mfc=eb_mfc, mec=eb_mec,\
                     capsize=eb_capsize, capthick=eb_capthick, alpha=eb_alpha, label='Observation')
        ax.plot(self.axes.centers[0], values, color=vp_color, ls=vp_ls, lw=vp_lw, alpha=vp_alpha, label='Prediction')
        ax.plot(self.axes.centers[0], (self.view()+values)/2, color=mp_color, ls = mp_ls,\
                                                        lw=mp_lw, alpha=mp_alpha, label='Arith-mean')
        ax.plot(self.axes.centers[0], fit, color=fp_color, ls = fp_ls,lw=fp_lw, alpha=fp_alpha, label='Guass-fit')
        ax.legend(prop={'size': lg_size})

        ax.set_ylabel("Counts", size=labelsize)
        plt.xticks(size=labelsize)
        plt.yticks(size=labelsize)
        
        fig.add_axes(ax)
        
        
        '''
        Pull: plot the pulls using Matplotlib bar method
        '''
        left_edge = self.axes.edges[0][0]
        right_edge = self.axes.edges[-1][-1]
        width = (right_edge - left_edge) / len(pulls)
        pull_ax.bar(self.axes.centers[0], pulls, color=bar_color, width=width)

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
        
        pull_ax.set_xlabel(self.axes[0].title, size=labelsize)
        pull_ax.set_ylabel("Pull", size=labelsize)
        plt.xlim(left_edge, right_edge)
        plt.xticks(size=labelsize)
        plt.yticks(size=labelsize)
        
        fig.add_axes(pull_ax)
        
        return fig, ax, pull_ax

    
    
    def pull_plot_pro(self, func, fig=None, ax=None, pull_ax=None, **kwargs):
        # Type judgement
        if callable(func) == False:
            raise TypeError(
                    "Callable parameter func is supported in pull plot."
                )
        
        '''
        Computation and Fit
        '''
        # Compute PDF values
        values = func(*self.axes.centers)*self.sum()*self.axes[0].widths
        yerr = np.sqrt(self.view())
        
        # Compute fit values: using func as fit model
        popt, pcov = curve_fit(f=func, xdata=self.axes.centers[0], ydata=self.view())
        fit = func(self.axes.centers[0], *popt)
        
        # Compute pulls: containing no INF values
        pulls = (self.view() - values) / yerr
        pulls = [x if np.abs(x) != np.inf else 0 for x in pulls]
        
        
        '''
        Default Figure: construct the figure and axes
        '''
        if fig == None:
            fig = plt.figure(figsize=(8, 8))
            grid = fig.add_gridspec(4, 4, wspace=0.5, hspace=0.5)
        else:
            grid = fig.add_gridspec(4, 4, wspace=0.5, hspace=0.5)
            
        if ax == None:
            ax = fig.add_subplot(grid[0:3, :])
        else:
            pass
        
        if pull_ax == None:
            pull_ax = fig.add_subplot(grid[3, :], sharex=ax)
        else:
            pass
        
        
        '''
        Keyword Argument Conversion: convert the keywork arguments to several independent arguments
        '''
        # error bar keyword arguments
        eb_kwargs = dict()
        for kw in kwargs.keys():
            if kw[:2] == 'eb':
                eb_kwargs[kw[3:]] = kwargs[kw]
                
        for k in eb_kwargs:
            kwargs.pop('eb_' + k)
        
        # value plot keyword arguments
        vp_kwargs = dict()
        for kw in kwargs.keys():
            if kw[:2] == 'vp':
                vp_kwargs[kw[3:]] = kwargs[kw]
        
        for k in vp_kwargs:
            kwargs.pop('vp_' + k)
        
        # mean plot keyword arguments
        mp_kwargs = dict()
        for kw in kwargs.keys():
            if kw[:2] == 'mp':
                mp_kwargs[kw[3:]] = kwargs[kw]
        
        for k in mp_kwargs:
            kwargs.pop('mp_' + k)
        
        # fit plot keyword arguments
        fp_kwargs = dict()
        for kw in kwargs.keys():
            if kw[:2] == 'fp':
                fp_kwargs[kw[3:]] = kwargs[kw]
        
        for k in fp_kwargs:
            kwargs.pop('fp_' + k)
        
        # bar plot keyword arguments
        bar_kwargs = dict()
        for kw in kwargs.keys():
            if kw[:3] == 'bar':
                # disable bar width arguments
                if kw == 'bar_width': 
                    raise KeyError("'bar_width' not needed.")
                bar_kwargs[kw[4:]] = kwargs[kw]
        
        for k in bar_kwargs:
            kwargs.pop('bar_' + k)
        
        # patch plot keyword arguments
        pp_kwargs, pp_num = dict(), 3
        for kw in kwargs.keys():
            if kw[:2] == 'pp':
                # allow pp_num
                if kw == 'pp_num':
                    pp_num = kwargs[kw]
                    continue
                pp_kwargs[kw[3:]] = kwargs[kw]
        
        if 'pp_num' in kwargs:
            kwargs.pop('pp_num')
        for k in pp_kwargs:
            kwargs.pop('pp_' + k)
                
        # judge whether some arguements left
        if len(kwargs):
            raise TypeError(f"\'{list(kwargs.keys())[0]}\' not needed.")
        
        
        '''
        Main: plot the pulls using Matplotlib errorbar and plot methods
        '''
        ax.errorbar(self.axes.centers[0], self.view(), yerr, **eb_kwargs)
        ax.plot(self.axes.centers[0], values, **vp_kwargs)
        ax.plot(self.axes.centers[0], (self.view()+values)/2, **mp_kwargs)
        ax.plot(self.axes.centers[0], fit, **fp_kwargs)
        
        fig.add_axes(ax)
        
        
        '''
        Pull: plot the pulls using Matplotlib bar method
        '''
        left_edge = self.axes.edges[0][0]
        right_edge = self.axes.edges[-1][-1]
        width = (right_edge - left_edge) / len(pulls)
        pull_ax.bar(self.axes.centers[0], pulls, width=width, **bar_kwargs)
        
        patch_height = max(np.abs(pulls)) / pp_num
        patch_width = width * len(pulls)
        for i in range(pp_num):
            # gradient color patches
            if "alpha" in pp_kwargs:
                pp_kwargs["alpha"] *= np.power(.618,i)
            else:
                pp_kwargs["alpha"] = .618 * np.power(.618,i)
                
            upRect_startpoint = [left_edge, i*patch_height]
            upRect = patches.Rectangle(upRect_startpoint, patch_width, patch_height, **pp_kwargs)
            pull_ax.add_patch(upRect)
            downRect_startpoint = [left_edge, -(i+1)*patch_height]
            downRect = patches.Rectangle(downRect_startpoint, patch_width, patch_height, **pp_kwargs)
            pull_ax.add_patch(downRect)

        plt.xlim(left_edge, right_edge)
        
        fig.add_axes(pull_ax)
        
        return fig, ax, pull_ax
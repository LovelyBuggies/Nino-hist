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

    
    
    def pull_plot_pro(self, func, fig=None, ax=None, pull_ax=None,\
                    eb_fmt='o', eb_ecolor='forestgreen', eb_elinewidth=2, eb_capsize=2, eb_barsabove=False,\
                    eb_lolims=False, eb_uplims=False, eb_xlolims=False, eb_xuplims=False, eb_errorevery=1,\
                    eb_capthick=2, eb_data=None, eb_alpha=.9, eb_aa=False, eb_c=None, eb_ds=None, eb_ls=None, eb_lw=1.,\
                    eb_mec='forestgreen', eb_mew=1., eb_mfc='forestgreen', eb_mfcalt=None, eb_ms=8.,\
                    vp_scalex=True, vp_scaley=True, vp_data=None, vp_alpha=.4, vp_aa=False, vp_c='gold', vp_ds=None,\
                    vp_ls='-', vp_lw=16., vp_mec=None, vp_mew=0., vp_mfc=None, vp_mfcalt=None, vp_ms=0.,\
                    mp_scalex=True, mp_scaley=True, mp_data=None, mp_alpha=.8, mp_aa=False, mp_c='indianred', mp_ds=None,\
                    mp_ls=':', mp_lw=4., mp_mec=None, mp_mew=0., mp_mfc=None, mp_mfcalt=None, mp_ms=0.,\
                    fp_scalex=True, fp_scaley=True, fp_data=None, fp_alpha=.8, fp_aa=False, fp_c='cornflowerblue',\
                    fp_ds=None, fp_ls='-', fp_lw=4., fp_mec=None, fp_mew=0., fp_mfc=None, fp_mfcalt=None, fp_ms=0.,\
                    bar_bottom=None, bar_align='center', bar_data=None, bar_alpha=1., bar_aa=None, bar_ec=None,\
                    bar_fc='cornflowerblue', bar_ls=None, bar_lw=0.,\
                    pp_num=3, pp_angle=0., pp_alpha=.618, pp_aa=None, pp_ec=None, pp_fc='cornflowerblue', pp_ls=None,\
                    pp_lw=0.,\
                    # other plot params
                     ): 
        '''
            Pull plot pro, receiving specific params to construct pull plot.\
            Kwargs are not thorough currently, abbr and alpha are included.\
            Reference: MPL Axes.errorbar, Axes.plot, Axes.bar, 
        '''
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
        Default Construction: construct the figure and axes
        '''
        if fig == None:
            fig = plt.figure(figsize=(16, 16))
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
                    fmt=eb_fmt, ecolor=eb_ecolor, elinewidth=eb_elinewidth, capsize=eb_capsize, barsabove=eb_barsabove,\
                    lolims=eb_lolims, uplims=eb_uplims, xlolims=eb_xlolims, xuplims=eb_xuplims, errorevery=eb_errorevery,\
                    capthick=eb_capthick, data=eb_data, alpha=eb_alpha, aa=eb_aa, c=eb_c, ds=eb_ds, ls=eb_ls, lw=eb_lw,\
                    mec=eb_mec, mew=eb_mew, mfc=eb_mfc, mfcalt=eb_mfcalt, ms=eb_ms)
        ax.plot(self.axes.centers[0], values, scalex=vp_scalex, scaley=vp_scaley, data=vp_data, alpha=vp_alpha, aa=vp_aa,\
                    c=vp_c, ds=vp_ds, ls=vp_ls, lw=vp_lw, mec=vp_mec, mew=vp_mew, mfc=vp_mfc, mfcalt=vp_mfcalt, ms=vp_ms)
        ax.plot(self.axes.centers[0], (self.view()+values)/2, scalex=mp_scalex, scaley=mp_scaley, data=mp_data,\
                    alpha=mp_alpha, aa=mp_aa, c=mp_c, ds=mp_ds, ls=mp_ls, lw=mp_lw, mec=mp_mec, mew=mp_mew, mfc=mp_mfc,\
                    mfcalt=mp_mfcalt, ms=mp_ms)
        ax.plot(self.axes.centers[0], fit, scalex=fp_scalex, scaley=fp_scaley, data=fp_data, alpha=fp_alpha, aa=fp_aa, \
                    c=fp_c, ds=fp_ds, ls=fp_ls, lw=fp_lw, mec=fp_mec, mew=fp_mew, mfc=fp_mfc, mfcalt=fp_mfcalt, ms=fp_ms)
        
        fig.add_axes(ax)
        
        
        '''
        Pull: plot the pulls using Matplotlib bar method
        '''
        left_edge = self.axes.edges[0][0]
        right_edge = self.axes.edges[-1][-1]
        width = (right_edge - left_edge) / len(pulls)
        pull_ax.bar(self.axes.centers[0], pulls, width=width, bottom=bar_bottom, align=bar_align, data=bar_data,\
                    alpha=bar_alpha, aa=bar_aa, ec=bar_ec, fc=bar_fc, ls=bar_ls, lw=bar_lw)
        
        patch_height = max(np.abs(pulls)) / pp_num
        patch_width = width * len(pulls)
        for i in range(pp_num):
            upRect_startpoint = [left_edge, i*patch_height]
            upRect = patches.Rectangle(upRect_startpoint, patch_width, patch_height, angle=pp_angle,\
                                       alpha=pp_alpha*np.power(.618,i), aa=pp_aa, ec=pp_ec, fc=pp_fc, ls=pp_ls, lw=pp_lw)
            pull_ax.add_patch(upRect)
            downRect_startpoint = [left_edge, -(i+1)*patch_height]
            downRect = patches.Rectangle(downRect_startpoint, patch_width, patch_height, angle=pp_angle,\
                                       alpha=pp_alpha*np.power(.618,i), aa=pp_aa, ec=pp_ec, fc=pp_fc, ls=pp_ls, lw=pp_lw)
            pull_ax.add_patch(downRect)

        plt.xlim(left_edge, right_edge)
        
        fig.add_axes(pull_ax)
        
        return fig, ax, pull_ax
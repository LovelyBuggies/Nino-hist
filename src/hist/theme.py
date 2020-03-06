class Theme(object):
    
    def __init__(self, theme):
        self._theme = theme
        
    def to_param(self, size): 
        '''
        Change theme to params.
        '''

        '''
        Name Standard:
            - eb: error bar plot
            - vp: value plot
            - mp: mean plot
            - fp: fit plot
            - lg: lengend plot
            - pp: patch plot
            - bar: bar plot
        '''
        if self._theme.lower() == "chrome":
            eb_ecolor = eb_mfc = eb_mec = 'forestgreen'
            eb_fmt, eb_ms, eb_capsize, eb_capthick, eb_alpha = \
                                    'o', size/2, size/12, size/12, .8                   # error bar
            vp_color, vp_ls, vp_lw, vp_alpha = 'orange', '-', size/3*2, .4              # values plot
            mp_color, mp_ls, mp_lw, mp_alpha = 'indianred', ':', size/6, .8             # mean plot
            fp_color, fp_ls, fp_lw, fp_alpha = 'cornflowerblue', '-', size/6, 1.        # fit plot
            lg_size = size                                                             # legend size
            pp_color, pp_alpha, pp_ec = 'cornflowerblue', .4, None                      # patches plot
            bar_color = 'cornflowerblue'
        elif self._theme.lower() == "light":
            eb_ecolor = eb_mfc = eb_mec = 'lightslategray'
            eb_fmt, eb_ms, eb_capsize, eb_capthick, eb_alpha = \
                                    'o', size/2, size/12, size/12, .8
            vp_color, vp_ls, vp_lw, vp_alpha = 'gainsboro', '-', size/3*2, .6
            mp_color, mp_ls, mp_lw, mp_alpha = 'dimgray', ':', size/4, 1.
            fp_color, fp_ls, fp_lw, fp_alpha = 'gray', '-', size/6, 1.
            lg_size = size
            pp_color, pp_alpha, pp_ec = 'gray', .4, None
            bar_color = 'gray'
        elif self._theme.lower() == "dark":
            eb_ecolor = eb_mfc = eb_mec = 'slategray'
            eb_fmt, eb_ms, eb_capsize, eb_capthick, eb_alpha = \
                                    'o', size/2, size/12, size/12, .8
            vp_color, vp_ls, vp_lw, vp_alpha = '#606060', '-', size/3*2, .6
            mp_color, mp_ls, mp_lw, mp_alpha = 'dimgray', ':', size/4, 1.
            fp_color, fp_ls, fp_lw, fp_alpha = '#303030', '-', size/6, 1.
            lg_size = size
            pp_color, pp_alpha, pp_ec = '#303030', .4, None
            bar_color = '#303030'
        elif self._theme.lower() == "spring":
            eb_ecolor = eb_mfc = eb_mec = 'goldenrod'
            eb_fmt, eb_ms, eb_capsize, eb_capthick, eb_alpha = \
                                    'o', size/2, size/12, size/12, .8
            vp_color, vp_ls, vp_lw, vp_alpha = 'plum', '-', size/3*2, .6
            mp_color, mp_ls, mp_lw, mp_alpha = 'blueviolet', ':', size/4, 1.
            fp_color, fp_ls, fp_lw, fp_alpha = 'orange', '-', size/4, 1.
            lg_size = size
            pp_color, pp_alpha, pp_ec = 'plum', .4, None
            bar_color = 'plum'
        elif self._theme.lower() == "summer":
            eb_ecolor = eb_mfc = eb_mec = 'orange'
            eb_fmt, eb_ms, eb_capsize, eb_capthick, eb_alpha = \
                                    'o', size/2, size/12, size, .8
            vp_color, vp_ls, vp_lw, vp_alpha = 'green', '-', size/3*2, .2
            mp_color, mp_ls, mp_lw, mp_alpha = 'darkgreen', ':', size/4, 1.
            fp_color, fp_ls, fp_lw, fp_alpha = 'darkgreen', '-', size/4, 1.
            lg_size = size
            pp_color, pp_alpha, pp_ec = 'darkgreen', .4, None
            bar_color = 'darkgreen'
        elif self._theme.lower() == "autumn":
            eb_ecolor = eb_mfc = eb_mec = 'crimson'
            eb_fmt, eb_ms, eb_capsize, eb_capthick, eb_alpha = \
                                    'o', size/2, size/12, size/6, .8
            vp_color, vp_ls, vp_lw, vp_alpha = 'gold', '-', size/3*2, .6
            mp_color, mp_ls, mp_lw, mp_alpha = 'darkorange', ':', size/3, 1.
            fp_color, fp_ls, fp_lw, fp_alpha = 'chocolate', '-', size/4, 1.
            lg_size = size
            pp_color, pp_alpha, pp_ec = 'orange', .4, None
            bar_color = 'orange'
        elif self._theme.lower() == "winter":
            eb_ecolor = eb_mfc = eb_mec = 'steelblue'
            eb_fmt, eb_ms, eb_capsize, eb_capthick, eb_alpha = \
                                    'o', size/2, size/12, size/6, .8
            vp_color, vp_ls, vp_lw, vp_alpha = 'green', '-', size/3*2, .2
            mp_color, mp_ls, mp_lw, mp_alpha = 'lightseagreen', ':', size/3, 1.
            fp_color, fp_ls, fp_lw, fp_alpha = 'seagreen', '-', size/4, 1.
            lg_size = size
            pp_color, pp_alpha, pp_ec = 'lightseagreen', .4, None
            bar_color = 'lightseagreen'
        elif self._theme.lower() == "cool":
            eb_ecolor = eb_mfc = eb_mec = 'plum'
            eb_fmt, eb_ms, eb_capsize, eb_capthick, eb_alpha = \
                                    'o', size/2, size/12, size/2, .8
            vp_color, vp_ls, vp_lw, vp_alpha = 'darkturquoise', '-', size/3*2, .4
            mp_color, mp_ls, mp_lw, mp_alpha = 'steelblue', ':', size/3, 1.
            fp_color, fp_ls, fp_lw, fp_alpha = 'purple', '-', size/4, 1.
            lg_size = size
            pp_color, pp_alpha, pp_ec = 'steelblue', .4, None
            bar_color = 'steelblue'
        elif self._theme.lower() == "hot":
            eb_ecolor = eb_mfc = eb_mec = 'orangered'
            eb_fmt, eb_ms, eb_capsize, eb_capthick, eb_alpha = \
                                    'o', size/2, size/12, size/2, .8
            vp_color, vp_ls, vp_lw, vp_alpha = 'gold', '-', size/2, .6
            mp_color, mp_ls, mp_lw, mp_alpha = 'sienna', ':', size/3, 1.
            fp_color, fp_ls, fp_lw, fp_alpha = '#606060', '-', size/4, 1.
            lg_size = size
            pp_color, pp_alpha, pp_ec = 'sienna', .4, None
            bar_color = 'sienna'
        else:
            raise NameError(
                    f"Theme paramerter theme {self._theme} is not support." 
                )
        
        
        return eb_ecolor, eb_mfc,eb_mec, eb_fmt, eb_ms, eb_capsize, eb_capthick, eb_alpha,\
        vp_color, vp_ls, vp_lw, vp_alpha, mp_color, mp_ls, mp_lw, mp_alpha, fp_color,\
        fp_ls, fp_lw, fp_alpha, lg_size, pp_color, pp_alpha, pp_ec, bar_color
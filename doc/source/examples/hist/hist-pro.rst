
Hist Pro
=========================

.. toctree::
   :maxdepth: 2
   :titlesonly:
   :glob:

::

	import hist
	import numpy as np
	import matplotlib.pyplot as plt

	def pdf(x, a=1/np.sqrt(2*np.pi), x0=0, sigma=1, offset=0):
	    return a * np.exp(-(x-x0)**2/(2*sigma**2)) + offset

	h = hist.Hist(
	    hist.axis.Regular(50, -4, 4, name="S", title="s [units]", underflow=False, overflow=False)
	)

	data = np.random.normal(size=1_000)
	h.fill(data)

	h.pull_plot_pro(pdf, eb_ecolor='crimson', eb_mfc='crimson', eb_mec='crimson', eb_fmt='o', eb_ms=6,\
	                eb_capsize=1, eb_capthick=2, eb_alpha=.8, vp_c='gold', vp_ls='-', vp_lw=8,\
	                vp_alpha=.6, mp_c='darkorange', mp_ls=':', mp_lw=4, mp_alpha=1.,\
	                fp_c='chocolate', fp_ls='-', fp_lw=3, fp_alpha=1., bar_fc='orange',\
	                pp_num=6, pp_fc='orange', pp_alpha=.618, pp_ec=None)


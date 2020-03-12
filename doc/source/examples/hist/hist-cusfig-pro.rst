
Hist Customized Figure Pro
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

	fig = plt.figure(figsize=(12, 12))
	grid = fig.add_gridspec(5, 5, wspace=0.3, hspace=0.3)
	ax = fig.add_subplot(grid[0:3, 1:4])
	pull_ax = fig.add_subplot(grid[3:4, :], sharex=ax)

	fig, ax, pull_ax = h.pull_plot_pro(pdf, fig=fig, ax=ax, pull_ax=pull_ax, bar_fc='steelblue',\
	                pp_fc='steelblue', pp_num=8, pp_alpha=.7)

	ax.set_ylabel("Counts")
	pull_ax.set_xlabel(h.axes[0].title)
	pull_ax.set_ylabel("Pull")

	fig.savefig("img/ax-img-pro.png")


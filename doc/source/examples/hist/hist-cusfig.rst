
Hist Customized Figure
=======================

.. toctree::
   :maxdepth: 2
   :titlesonly:
   :glob:

::

	def pdf(x, a=1/np.sqrt(2*np.pi), x0=0, sigma=1, offset=0):
	    return a * np.exp(-(x-x0)**2/(2*sigma**2)) + offset


	h = hist.Hist(
	    hist.axis.Regular(50, -4, 4, name="S", title="s [units]", underflow=False, overflow=False)
	)

	data = np.random.normal(size=1_000)

	h.fill(data)

	fig = plt.figure(figsize=(10, 10))
	grid = fig.add_gridspec(5, 5, wspace=0.3, hspace=0.3)
	ax = fig.add_subplot(grid[0:3, 2:])
	pull_ax = fig.add_subplot(grid[3:4, :], sharex=ax)

	h.pull_plot(pdf, size="m", fig=fig, ax=ax, pull_ax=pull_ax, theme='winter')
	fig.savefig("img/ax-img.png")


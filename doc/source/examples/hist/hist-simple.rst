
Hist Simple
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

	fig, ax, pull_ax = h.pull_plot(pdf, size='m', theme='Chrome')


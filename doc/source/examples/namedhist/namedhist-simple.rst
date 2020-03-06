

NamedHist Simple
====================

.. toctree::
   :maxdepth: 2
   :titlesonly:
   :glob:

::

	import boost_histogram as bh
	import hist
	import numpy as np
	import matplotlib.pyplot as plt


	h = hist.NamedHist(
	    hist.axis.Regular(50, -3, 3, name="x"),
	    hist.axis.Regular(50, -3, 3, name="y"),
	)

	x = np.random.randn(1_000_000)
	y = np.random.randn(1_000_000)
	h.fill(y=y, x=x)

	fig, ax = plt.subplots(figsize=(8,5))
	w, x, y = h.to_numpy()
	mesh = ax.pcolormesh(x, y, w.T, cmap='autumn')
	ax.set_xlabel('x')
	ax.set_ylabel('y')
	fig.colorbar(mesh)
	fig.show()




NamedHist Descartes
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
	    hist.axis.Regular(100, -1, 1, name="X"),
	    hist.axis.Regular(100, -1, 1, name="Y"),
	    hist.axis.Bool(name="V"),
	)

	x, y = np.random.random_sample([2, 1_000_000])*2 - 1
	valid = np.abs(x)**2 + (y + .2 - np.power(np.abs(x), 2/3))**2 < .5
	h.fill(Y=y, X=x, V=valid)

	valid_only = h[:, :, bh.loc(True)]

	fig, ax = plt.subplots(figsize=(8,5))
	W, X, Y = valid_only.to_numpy()
	mesh = ax.pcolormesh(X, Y, W.T, cmap='autumn')
	ax.set_xlabel('X')
	ax.set_ylabel('Y')
	fig.colorbar(mesh)
	fig.show()



Bool Axes
====================

.. toctree::
   :maxdepth: 2
   :titlesonly:
   :glob:

Use `boost_histogram <https://boost-histogram.readthedocs.io/en/latest/index.html>`_ imitate ``Bool`` axes::

	import boost_histogram as bh
	import numpy as np
	import matplotlib.pyplot as plt

	h = bh.Histogram(
	    bh.axis.Regular(50, -1, 1),
	    bh.axis.Regular(50, -1, 1),
	    bh.axis.Integer(0, 2, underflow=False, overflow=False),
	)

	x, y = np.random.random_sample([2, 1_000_000])*2 - 1
	valid = (x**2 + y**2) < .5

	h.fill(x, y, valid)
	valid_only = h[:, :, bh.loc(True)]

	fig, ax = plt.subplots(figsize=(8,5))
	W, X, Y = valid_only.to_numpy()
	mesh = ax.pcolormesh(X, Y, W.T)
	ax.set_xlabel('x')
	ax.set_ylabel('y')
	fig.colorbar(mesh)
	fig.show()

`Nino-hist <https://nino-hist.site>`_ ``Bool`` axes::

	import boost_histogram as bh
	import hist
	import numpy as np
	import matplotlib.pyplot as plt


	h = hist.NamedHist(
	    hist.axis.Regular(50, -1, 1, name="X"),
	    hist.axis.Regular(50, -1, 1, name="Y"),
	    hist.axis.Bool(name="V"),
	)

	x, y = np.random.random_sample([2, 1_000_000])*2 - 1
	valid = (x**2 + y**2) < .5
	h.fill(Y=y, X=x, V=valid)

	valid_only = h[:, :, bh.loc(True)]

	fig, ax = plt.subplots(figsize=(8,5))
	W, X, Y = valid_only.to_numpy()
	mesh = ax.pcolormesh(X, Y, W.T, cmap='spring')
	ax.set_xlabel('X')
	ax.set_ylabel('Y')
	fig.colorbar(mesh)
	fig.show()
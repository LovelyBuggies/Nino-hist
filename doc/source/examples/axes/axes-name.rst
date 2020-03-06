
Axes Name
====================

.. toctree::
   :maxdepth: 2
   :titlesonly:
   :glob:

::

	import hist
	import numpy as np
	import matplotlib.pyplot as plt

	h = hist.NamedHist(
	    hist.axis.Regular(10, 0, 1, name='myRegular'),
	    hist.axis.Integer(-1, 1, name='myInteger')
	)

	regular = [.15, .15, .25, .35, .55, .55]
	integer = [-1, -1, 0, 0, 0, 0]

	h.fill(myRegular=regular, myInteger=integer)

	fig, ax = plt.subplots(figsize=(8,5))
	w, x, y = h.to_numpy()
	mesh = ax.pcolormesh(x, y, w.T)
	ax.set_xlabel(h.axes[0].metadata["name"])
	ax.set_ylabel(h.axes[1].metadata["name"])
	fig.colorbar(mesh)
	fig.show()
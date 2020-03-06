

NamedHist Coin Games
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
	    hist.axis.Bool(name='USD', title='usd font'),
	    hist.axis.Bool(name='EUR', title='eur font')
	)
	usd = np.random.rand(1_000_000) > 0.5
	eur = np.random.rand(1_000_000) > 0.5

	h.fill(USD=usd, EUR=eur)

	bar = [h[0, 0], h[0, 1], h[1, 0], h[1, 1]]
	x = range(len(bar))
	bar_color = ['steelblue', 'indianred', 'violet', 'orange']
	fig, ax = plt.subplots(figsize=(8,5))
	ax.bar(x, bar, color=bar_color)
	plt.xticks(x, ("usd+, eur+", "usd+, eur-", "usd-, eur+",\
	                                    "usd-, eur-"), size=16)
	plt.ylabel("Counts", size=16)


	fig.show()
from .core import BaseHist
import numpy as np


class NamedHist(BaseHist):
    
    def fill(self, **args):
        """
            Insert data into the histogram using names and return a \
            NamedHist object. Params must contain the name\/s of the \
            axis\/es. Note that this is only the fill method for \
            NamedHist object. This method doesn't support Hist object.
        """
                
        indices = []
        values = []
        for name, val in args.items():
            for index, axis in enumerate(self.axes):
                if name == axis.name:
                    indices.append(index)
                    values.append(val)

        d = dict(zip(indices, values))
        d = sorted(d.items(), key=lambda item:item[1], reverse=True)
        nd = np.asarray(d, dtype=object)
        super().fill(*(nd.ravel()[1::2]))

        return self



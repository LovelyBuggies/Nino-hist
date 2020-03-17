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
        d = sorted(d.items(), key=lambda item:item[0])
        nd = np.asarray(d, dtype=object)
        super().fill(*(nd.ravel()[1::2]))

        return self

    
    def __getitem__(self, index):
        """
            Get histogram item.
        """
        if isinstance(index, dict):
            k = list(index.keys())
            if isinstance(k[0], str):
                for key in k:
                    for idx, axis in enumerate(self.axes):
                        if key == axis.name:
                            index[idx] = index.pop(key)
                            break
        
        return super().__getitem__(index)

    
    
    def __setitem__(self, index, value):
        """
            Set histogram item.
        """
        if isinstance(index, dict):
            k = list(index.keys())
            if isinstance(k[0], str):
                for key in k:
                    for idx, axis in enumerate(self.axes):
                        if key == axis.name:
                            index[idx] = index.pop(key)
                            break
        
        return super().__setitem__(index, value)

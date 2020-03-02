from .core import BaseHist
import boost_histogram as bh
import numpy as np

class NamedHist(BaseHist):
    
    
    def fill(self, **args):
        """
        Insert data into the histogram.
        Parameters
        ----------
        *args : Union[Array[float], Array[int], Array[str], float, int, str]
            Provide one value or array per dimension.
        weight : List[Union[Array[float], Array[int], Array[str], float, int, str]]]
            Provide weights (only if the histogram storage supports it)
        sample : List[Union[Array[float], Array[int], Array[str], float, int, str]]]
            Provide samples (only if the histogram storage supports it)
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
    
    pass


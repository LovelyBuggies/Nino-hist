from boost_histogram import Histogram
import warnings

warnings.filterwarnings('ignore')

class BaseHist(Histogram):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # throw name duplicated exception
        names = list(l.name for l in self.axes)
        if len(set(names)) != len(self.axes):
            raise Exception("Name duplicated.")
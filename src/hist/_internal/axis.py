import boost_histogram.axis as bha


class Regular(bha.Regular):
    
    def __init__(
        self,
        bins,
        start,
        stop,
        *,
        name=None,
        title=None,
        underflow=True,
        overflow=True,
        growth=False,
        circular=False,
        transform=None
    ):
        metadata = dict(name=name)
        metadata["title"] = title
        super().__init__(
            bins,
            start,
            stop,
            metadata=metadata,
            underflow=underflow,
            overflow=overflow,
            growth=growth,
            circular=circular,
            transform=transform,
        )
    
    @property
    def name(self):
        return self.metadata["name"]

    @name.setter
    def name(self, value):
        self.metadata["name"] = value
        
    @property
    def title(self):
        return self.metadata["title"]

    @title.setter
    def title(self, value):
        self.metadata["title"] = value


        
class Bool(bha.Regular):
    def __init__(
        self,
        *,
        name=None,
        title=None,
        underflow=False,
        overflow=False,
        growth=False,
        circular=False,
        transform=None
    ):
        metadata = dict(name=name)
        metadata["title"] = title
        super().__init__(
            2, 0, 2,              # bins, start, stop
            metadata=metadata,
            underflow=underflow,
            overflow=overflow,
            growth=growth,
            circular=circular,
            transform=transform,
        )
    
    def __repr__(self):
        return "{self.__class__.__name__}({args}{kwargs})".format(
            self=self, args=self._repr_args(), kwargs=self._repr_kwargs()
        )
    
    @property
    def name(self):
        return self.metadata["name"]

    @name.setter
    def name(self, value):
        self.metadata["name"] = value
        
    @property
    def title(self):
        return self.metadata["title"]

    @title.setter
    def title(self, value):
        self.metadata["title"] = value


class Variable(bha.Variable):
    pass


class Integer(bha.Integer):
    pass


class IntCategory(bha.IntCategory):
    pass


class StrCategory(bha.StrCategory):
    pass

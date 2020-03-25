import hist
import boost_histogram as bh
import pytest


def test_basic_usage():
    '''
        Test basic usage -- whether Axes are properly derived from\
        boost-histogram Axes. We do not modify their super classes's\
        methods (except for repr and add new features), so this would\
        pass.
    '''
    assert isinstance(hist.axis.Regular(1, 2, 3, name="R"), bh.axis.Regular)
    assert isinstance(hist.axis.Variable((1, 2, 3), name="V"), bh.axis.Variable)
    assert isinstance(hist.axis.Integer(1, 2, name="I"), bh.axis.Integer)
    assert isinstance(hist.axis.IntCategory((1, 2, 3), name="IC"), bh.axis.IntCategory)
    assert isinstance(hist.axis.StrCategory(tuple("ABC"), name="SC"), bh.axis.StrCategory)


def test_bool_axis():
    '''
        Test bool axis -- whether Bool is enabled and work properly.\
        As our bool axis is derived from boost-histogram.axis.Regular,\
        we won't test all thoses features. If it is justified as the\
        subclass of boost-histogram.axis.Regular, then it should pass\
        those axis tests.
    '''
    
    # Test bool axis
    assert isinstance(hist.axis.Bool(name="B"), bh.axis.Regular)
    
    # Test histograms with bool axes
    h = hist.NamedHist(hist.axis.Bool(name="S"), 
                       hist.axis.Bool(name="L"))

    valid_s = [True, True, True, False]
    valid_l = [True, True, False, False]
    h.fill(L=valid_l, S=valid_s)
    assert h[0, 0] == 1
    assert h[1, 0] == 1
    assert h[1, 1] == 2
    
    s_valid_only = h[{'S':bh.loc(True)}]
    assert s_valid_only[0] == 1
    assert s_valid_only[1] == 2
    
    l_valid_only = h[{'L':bh.loc(True)}]
    assert l_valid_only[0] == 0
    assert l_valid_only[1] == 2


class test_axis_name():
    '''
        Test axis name -- whether the axis name concords to the name\
        convention.
    '''
    
    # name convention tests
    def test_name_convention(self):
        
        assert hist.axis.Integer(-1, 1, name='my_Integer')
        assert hist.axis.Regular(10, -1, 1, name='myRegular_')
        assert hist.axis.Bool(name='myBool_0')
        
        with pytest.raises(Exception):
              hist.axis.Integer(-1, 1, name='my-Integer')
                
        with pytest.raises(Exception):
            ist.axis.Integer(-1, 1, name='_myInteger')
            
        with pytest.raises(Exception):
            hist.axis.Integer(-1, 1, name='__myInteger')

            
class test_hist_names():
    '''
        Test hist names -- whether the hist names are unique.
    '''
    
    # duplication tests
    def test_name_duplication(self):
        
        assert hist.NamedHist(
                    hist.axis.Regular(10, 0, 1, name='myRegular_1'),
                    hist.axis.Regular(10, 0, 1, name='myRegular2'),
                    hist.axis.Regular(10, -1, 1, name='myRegular_3')
                )
        
        with pytest.raises(Exception):
            h = hist.NamedHist(
                    hist.axis.Regular(10, 0, 1, name='myRegular'),
                    hist.axis.Regular(10, 0, 1, name='myRegular'),
                    hist.axis.Regular(10, -1, 1, name='myRegular')
                )

        with pytest.raises(Exception):
            h = hist.NamedHist(
                    hist.axis.Regular(10, 0, 1, name='myRegular_1'),
                    hist.axis.Regular(10, 0, 1, name='myRegular_2'),
                    hist.axis.Regular(10, -1, 1, name='myRegular_2')
                )
        
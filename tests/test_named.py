from hist import axis, NamedHist
import boost_histogram as bh


def test_basic_usage():
    '''
        Test basic usage -- whether NamedHist are properly derived from\
        boost-histogram and whether it can be filled by names.
    '''
    
    # Test normal NamedHist
    h = NamedHist(
        axis.Regular(10, 0, 1, name="x")
    )
    h.fill(x=[0.35, 0.35, 0.45])

    assert h[2] == 0
    assert h[3] == 2
    assert h[4] == 1
    assert h[5] == 0

    assert h[{0:2}] == 0 
    assert h[{0:3}] == 2 
    assert h[{0:4}] == 1 
    assert h[{0:5}] == 0 
    
    assert h[{'x':2}] == 0 
    assert h[{'x':3}] == 2 
    assert h[{'x':4}] == 1 
    assert h[{'x':5}] == 0
    
    # Test multi-axis NamedHist
    h = NamedHist(
        axis.Regular(10, 0, 1, name="x"),
        axis.Regular(10, 0, 1, name="y"),
        axis.Integer(0, 2, name="z")
    )

    h.fill(x=[0.35, 0.35, 0.35, 0.45, 0.55, 0.55, 0.55], 
           y=[0.35, 0.35, 0.45, 0.45, 0.45, 0.45, 0.45],
           z=[0, 0, 1, 1, 1, 1, 1])
    
    z_one_only = h[{'z':bh.loc(1)}]
    assert z_one_only[{'x':3, 'y':4}] == 1
    assert z_one_only[{'x':4, 'y':4}] == 1
    assert z_one_only[{'x':5, 'y':4}] == 3
    assert z_one_only[{'x':5, 'y':5}] == 0
    assert z_one_only[{'x':6, 'y':5}] == 0

    assert z_one_only[3,4] == 1
    assert z_one_only[4,4] == 1
    assert z_one_only[5,4] == 3
    assert z_one_only[5,5] == 0
    assert z_one_only[6,5] == 0
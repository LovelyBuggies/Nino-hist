from hist import Hist, axis
import boost_histogram as bh


def test_basic_usage():
    '''
        Test basic usage -- whether Hist are properly derived from\
        boost-histogram.
    '''
    
    # Test normal Hist
    h = Hist(axis.Regular(10, 0, 1, name='x'))

    h.fill([0.35, 0.35, 0.45])

    assert h[2] == 0
    assert h[3] == 2
    assert h[4] == 1
    assert h[5] == 0

    assert h[{0:2}] == 0 
    assert h[{0:3}] == 2 
    assert h[{0:4}] == 1 
    assert h[{0:5}] == 0 
    
    # Test multi-axis Hist
    h = Hist(
        axis.Regular(10, 0, 1, name="x"),
        axis.Regular(10, 0, 1, name="y"),
        axis.Integer(0, 2, name="z")
    )

    h.fill([0.35, 0.35, 0.35, 0.45, 0.55, 0.55, 0.55], 
           [0.35, 0.35, 0.45, 0.45, 0.45, 0.45, 0.45],
           [0, 0, 1, 1, 1, 1, 1])
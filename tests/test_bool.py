import hist
import boost_histogram as bh


def test_basic_usage():
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
import hist


def test_basic_usage():
    h = hist.NamedHist(hist.axis.Bool(name="S"))

    valid = [True, True, True, False]
    h.fill(S=valid)

    assert h[0] == 1
    assert h[1] == 3
    
    
    h = hist.NamedHist(
        hist.axis.Bool(name="S"),
        hist.axis.Bool(name="L"),
        hist.axis.Bool(name="F"))
    
    valid_s = [True, True, True, True]
    valid_l = [True, True, False, False]
    valid_f = [False, False, False, True]
    h.fill(L=valid_l, S=valid_s, F=valid_f)

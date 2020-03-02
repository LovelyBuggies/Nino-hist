import hist


def test_basic_usage():
    h = hist.NamedHist(hist.axis.Bool(name="S"))

    valid = [True, True, True, False]
    h.fill(S=valid)

    assert h[0] == 1
    assert h[1] == 3
    
    


from hist import axis, NamedHist


def test_basic_usage():
    h = NamedHist(
        axis.Regular(10, 0, 1, name="x")
    )  # NamedHist should require axis.Regular to have a name set

    h.fill([0.35, 0.35, 0.45])  # Fill should be keyword only, with the names

    # Optional if you want these to fail
    assert h[2] == 0
    assert h[3] == 2
    assert h[4] == 1
    assert h[5] == 0

    # Example of a test that should be made to pass:
    # assert h[{'x':2}] == 0 # Should work
    # assert h[{'x':3}] == 2 # Should work
    # assert h[{'x':4}] == 1 # Should work
    # assert h[{'x':5}] == 0 # Should work

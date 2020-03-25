import hist


def test_version():
    '''
        Test version -- whether there is a version.
    '''
    assert hist.__version__ is not None
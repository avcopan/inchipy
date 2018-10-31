""" test the inchipy module
"""
import inchipy

MOLTEXT = """
 OpenBabel10311810453D

  6  5  0  0  0  0  0  0  0  0999 V2000
    0.9347   -0.0047    0.0959 F   0  0  0  0  0  0  0  0  0  0  0  0
    2.2782    0.0419    0.0574 C   0  0  0  0  0  0  0  0  0  0  0  0
    2.9240    0.9345   -0.6804 C   0  0  0  0  0  0  0  0  0  0  0  0
    4.2675    0.9811   -0.7189 F   0  0  0  0  0  0  0  0  0  0  0  0
    2.7249   -0.7154    0.6834 H   0  0  0  0  0  0  0  0  0  0  0  0
    2.4774    1.6919   -1.3063 H   0  0  0  0  0  0  0  0  0  0  0  0
  1  2  1  0  0  0  0
  2  3  2  3  0  0  0
  2  5  1  0  0  0  0
  3  4  1  0  0  0  0
  3  6  1  0  0  0  0
M  END

"""


def test__makeinchifrommolfiletext():
    """ test inchipy.MakeINCHIFromMolfileText
    """
    options = '-SUU'
    result = inchipy.inchi_Output()
    ret = inchipy.MakeINCHIFromMolfileText(MOLTEXT, options, result)
    print(ret)
    print(result.szInChI)
    print(result.szAuxInfo)
    print(result.szMessage)
    print(result.szLog)


if __name__ == '__main__':
    test__makeinchifrommolfiletext()

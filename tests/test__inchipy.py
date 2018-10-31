""" test the inchipy module
"""
import inchipy

MOL_STR = """
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


def test__inchi_from_mol_string():
    """ test inchipy.inchi_from_mol_string
    """
    inch_str, aux_str = inchipy.inchi_from_mol_string(MOL_STR)
    assert inch_str == 'InChI=1S/C2H2F2/c3-1-2-4/h1-2H'
    assert aux_str.startswith('AuxInfo=1/0/N:2,3,1,4')
    inch_str, aux_str = inchipy.inchi_from_mol_string(MOL_STR,
                                                      with_stereo=True)
    assert inch_str == 'InChI=1/C2H2F2/c3-1-2-4/h1-2H/b2-1?'
    assert aux_str.startswith('AuxInfo=1/0/N:2,3,1,4')


def test__inchi_key():
    """ test inchipy.inchi_key
    """
    inch_key = inchipy.inchi_key('InChI=1S/C2H2F2/c3-1-2-4/h1-2H')
    assert inch_key == 'WFLOTYSKFUPZQB-UHFFFAOYSA-N'

    inch_key = inchipy.inchi_key('InChI=1S/C2H2F2/c3-1-2-4/h1-2H/b2-1+')
    assert inch_key == 'WFLOTYSKFUPZQB-OWOJBTEDSA-N'


if __name__ == '__main__':
    test__inchi_from_mol_string()
    test__inchi_key()

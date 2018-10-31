#include <tuple>
#include <string>
#include <pybind11/pybind11.h>
#include "inchi_api.h"

namespace py = pybind11;


std::tuple<std::string, std::string> inchi_from_mol_string(
        const char* mol_str, bool with_stereo) {
    int ret_code;
    inchi_Output outp;

    if (with_stereo) {
        char options[4096] = " -SUU";
        ret_code = MakeINCHIFromMolfileText(mol_str, options, &outp);
    }
    else {
        char options[4096];
        ret_code = MakeINCHIFromMolfileText(mol_str, options, &outp);
    }

    return std::make_tuple(outp.szInChI, outp.szAuxInfo);
}


std::string inchi_key(const char* inch_str) {
    int ret_code;
    char inch_key[28], _1[256], _2[256];

    ret_code = GetINCHIKeyFromINCHI(inch_str, 0, 0, inch_key, _1, _2);

    return inch_key;
}


PYBIND11_MODULE(inchipy, module) {
    module.def("inchi_from_mol_string", &inchi_from_mol_string,
               py::arg("mol_str"), py::arg("with_stereo")=false);
    module.def("inchi_key", &inchi_key,
               py::arg("inch_str"));
}

#include <pybind11/pybind11.h>
#include "inchi_api.h"

namespace py = pybind11;


PYBIND11_MODULE(inchipy, module) {
    py::class_<inchi_Output>(module, "inchi_Output")
        .def(py::init<>())
        .def_readwrite("szInChI", &inchi_Output::szInChI)
        .def_readwrite("szAuxInfo", &inchi_Output::szAuxInfo)
        .def_readwrite("szMessage", &inchi_Output::szMessage)
        .def_readwrite("szLog", &inchi_Output::szLog);
   module.def("MakeINCHIFromMolfileText", &MakeINCHIFromMolfileText,
              py::arg("moltext"), py::arg("options"), py::arg("result"));
}

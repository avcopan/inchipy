project(InChI C CXX)
cmake_minimum_required(VERSION 3.0)
find_package(PythonInterp REQUIRED)
execute_process(
    COMMAND "${PYTHON_EXECUTABLE}" -c
    "from distutils.sysconfig import get_python_lib; print(get_python_lib())"
    OUTPUT_VARIABLE PYTHON_SITE_PACKAGES OUTPUT_STRIP_TRAILING_WHITESPACE)
set(CMAKE_C_STANDARD 11)
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_POSITION_INDEPENDENT_CODE ON)
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -DTARGET_API_LIB -DCOMPILE_ANSI_ONLY")
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -DTARGET_API_LIB -DCOMPILE_ANSI_ONLY")

add_subdirectory(pybind11)

include_directories(
    ${PROJECT_SOURCE_DIR}/src/INCHI_BASE/src
    ${PROJECT_SOURCE_DIR}/src/INCHI_API/libinchi/src)

add_library(inchi SHARED
    ${PROJECT_SOURCE_DIR}/src/INCHI_BASE/src/ichican2.c
    ${PROJECT_SOURCE_DIR}/src/INCHI_BASE/src/ichicano.c
    ${PROJECT_SOURCE_DIR}/src/INCHI_BASE/src/ichi_io.c
    ${PROJECT_SOURCE_DIR}/src/INCHI_BASE/src/ichierr.c
    ${PROJECT_SOURCE_DIR}/src/INCHI_BASE/src/ichicans.c
    ${PROJECT_SOURCE_DIR}/src/INCHI_BASE/src/ichiisot.c
    ${PROJECT_SOURCE_DIR}/src/INCHI_API/libinchi/src/ichilnct.c
    ${PROJECT_SOURCE_DIR}/src/INCHI_BASE/src/ichimak2.c
    ${PROJECT_SOURCE_DIR}/src/INCHI_BASE/src/ichimake.c
    ${PROJECT_SOURCE_DIR}/src/INCHI_BASE/src/ichimap1.c
    ${PROJECT_SOURCE_DIR}/src/INCHI_BASE/src/ichimap2.c
    ${PROJECT_SOURCE_DIR}/src/INCHI_BASE/src/ichimap4.c
    ${PROJECT_SOURCE_DIR}/src/INCHI_BASE/src/ichinorm.c
    ${PROJECT_SOURCE_DIR}/src/INCHI_BASE/src/ichiparm.c
    ${PROJECT_SOURCE_DIR}/src/INCHI_BASE/src/ichiprt1.c
    ${PROJECT_SOURCE_DIR}/src/INCHI_BASE/src/ichiprt2.c
    ${PROJECT_SOURCE_DIR}/src/INCHI_BASE/src/ichiprt3.c
    ${PROJECT_SOURCE_DIR}/src/INCHI_BASE/src/ichiqueu.c
    ${PROJECT_SOURCE_DIR}/src/INCHI_BASE/src/ichiring.c
    ${PROJECT_SOURCE_DIR}/src/INCHI_BASE/src/ichisort.c
    ${PROJECT_SOURCE_DIR}/src/INCHI_BASE/src/ichister.c
    ${PROJECT_SOURCE_DIR}/src/INCHI_BASE/src/ichitaut.c
    ${PROJECT_SOURCE_DIR}/src/INCHI_BASE/src/ichi_bns.c
    ${PROJECT_SOURCE_DIR}/src/INCHI_API/libinchi/src/inchi_dll.c
    ${PROJECT_SOURCE_DIR}/src/INCHI_BASE/src/ichiread.c
    ${PROJECT_SOURCE_DIR}/src/INCHI_BASE/src/ichirvr1.c
    ${PROJECT_SOURCE_DIR}/src/INCHI_BASE/src/ichirvr2.c
    ${PROJECT_SOURCE_DIR}/src/INCHI_BASE/src/ichirvr3.c
    ${PROJECT_SOURCE_DIR}/src/INCHI_BASE/src/ichirvr4.c
    ${PROJECT_SOURCE_DIR}/src/INCHI_BASE/src/ichirvr5.c
    ${PROJECT_SOURCE_DIR}/src/INCHI_BASE/src/ichirvr6.c
    ${PROJECT_SOURCE_DIR}/src/INCHI_BASE/src/ichirvr7.c
    ${PROJECT_SOURCE_DIR}/src/INCHI_BASE/src/ikey_dll.c
    ${PROJECT_SOURCE_DIR}/src/INCHI_BASE/src/ikey_base26.c
    ${PROJECT_SOURCE_DIR}/src/INCHI_API/libinchi/src/inchi_dll_main.c
    ${PROJECT_SOURCE_DIR}/src/INCHI_API/libinchi/src/inchi_dll_a.c
    ${PROJECT_SOURCE_DIR}/src/INCHI_API/libinchi/src/inchi_dll_a2.c
    ${PROJECT_SOURCE_DIR}/src/INCHI_API/libinchi/src/inchi_dll_b.c
    ${PROJECT_SOURCE_DIR}/src/INCHI_BASE/src/mol_fmt1.c
    ${PROJECT_SOURCE_DIR}/src/INCHI_BASE/src/mol_fmt2.c
    ${PROJECT_SOURCE_DIR}/src/INCHI_BASE/src/mol_fmt3.c
    ${PROJECT_SOURCE_DIR}/src/INCHI_BASE/src/mol2atom.c
    ${PROJECT_SOURCE_DIR}/src/INCHI_BASE/src/mol_fmt4.c
    ${PROJECT_SOURCE_DIR}/src/INCHI_BASE/src/readinch.c
    ${PROJECT_SOURCE_DIR}/src/INCHI_BASE/src/runichi.c
    ${PROJECT_SOURCE_DIR}/src/INCHI_BASE/src/runichi2.c
    ${PROJECT_SOURCE_DIR}/src/INCHI_BASE/src/runichi3.c
    ${PROJECT_SOURCE_DIR}/src/INCHI_BASE/src/runichi4.c
    ${PROJECT_SOURCE_DIR}/src/INCHI_BASE/src/sha2.c
    ${PROJECT_SOURCE_DIR}/src/INCHI_BASE/src/strutil.c
    ${PROJECT_SOURCE_DIR}/src/INCHI_BASE/src/util.c)

pybind11_add_module(inchipy SHARED ${PROJECT_SOURCE_DIR}/src/inchipy.cc)
target_link_libraries(inchipy PRIVATE inchi)
install(TARGETS inchi LIBRARY DESTINATION lib)
install(TARGETS inchipy DESTINATION ${PYTHON_SITE_PACKAGES})

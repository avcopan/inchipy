#!/usr/bin/env bash
mkdir build
cd build
cmake .. -DCMAKE_INSTALL_PREFIX=$PREFIX -DCMAKE_C_COMPILER=$CC -DCMAKE_CXX_COMPILER=$CXX
make
make install

#!/bin/bash
COMBI=./c-source/combinadics/
PERM=./c-source/permanent/

cd $COMBI
python setup.py build_ext
cd ../../

cd $PERM
python setup.py build_ext
cd ../../

cp $COMBI/build/lib.linux-x86_64-2.7/combi.so ./linear_optics
cp $COMBI/build/lib.win32-2.7/combi.pyd ./linear_optics
cp $PERM/build/lib.linux-x86_64-2.7/perm.so ./linear_optics
cp $PERM/build/lib.win32-2.7/perm.pyd ./linear_optics

rm ./**/*.pyc
rm bundle.zip
zip -r bundle.zip ./*

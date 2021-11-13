#!/bin/sh

[ -d ./tmp ] && rm -rf ./tmp

DEVKIT_ROOT=/opt/dmm/oe1.5/dm7025/build/tmp
CROSS=${DEVKIT_ROOT}/cross/mipsel-linux/bin/

export CFLAGS+="-I${DEVKIT_ROOT}/staging/mipsel-linux/include \
 -I${DEVKIT_ROOT}/staging/mipsel-linux/include/python2.5"
export LDFLAGS="-L${DEVKIT_ROOT}/staging/mipsel-linux/lib"
export CC=${CROSS}gcc
export STRIP=${CROSS}strip
export SWIG=${DEVKIT_ROOT}/staging/i686-linux/bin/swig
export D=./tmp

make && make install

if [ $? != 0 ]; then
	echo compile error
	exit 1
fi

mkdir -p tmp/CONTROL
cp contrib/control tmp/CONTROL/
echo "Package: enigma2-plugin-systemplugins-lcnscanner-oe1.5" >> tmp/CONTROL/control
echo "Architecture: mipsel" >> tmp/CONTROL/control

sh ipkg-build -o root -g root tmp/

[ ! -d out ] && mkdir out
mv *.ipk out
echo "Package moved in `pwd`/out folder"


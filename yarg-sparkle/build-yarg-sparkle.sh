#!/bin/bash

YARGINSTALLDIR="../../yarg-lang"
HOSTYARG="$YARGINSTALLDIR/bin/hostyarg"

TARGETUF2="yarg-sparkle.uf2"
if [ -e $TARGETUF2 ]
then
    rm $TARGETUF2
fi

cp $YARGINSTALLDIR/build/yarg-lang.uf2 $TARGETUF2
$HOSTYARG addfile -fs $TARGETUF2 -add randomsparkles.ya
$HOSTYARG addfile -fs $TARGETUF2 -add main.ya
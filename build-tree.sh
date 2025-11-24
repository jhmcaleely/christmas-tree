#!/bin/bash

HOSTYARG="../yarg-lang/bin/hostyarg"
TARGETUF2="tree.uf2"


if [ -e $TARGETUF2 ]
then
    rm $TARGETUF2
fi

cp ../yarg-lang/build/yarg-lang.uf2 $TARGETUF2
$HOSTYARG addfile -fs $TARGETUF2 -add randomsparkles.ya

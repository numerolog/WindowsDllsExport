#!/usr/bin/env bash

echo "Build dumper..."

i686-w64-mingw32-gcc -s -Os -m32 DUMPEXPO.c -o DUMPEXPO.EXE || { echo "Failed to build." ; exit 1; }

echo "Done."



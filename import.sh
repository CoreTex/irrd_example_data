#!/usr/bin/env bash
./generate.py
cat *.dat |pbcopy
echo "copied to clipboard"

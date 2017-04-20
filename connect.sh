#!/bin/bash


bluetoothctl connect 00:0D:18:3A:67:89

rfcomm  bind /dev/rfcomm1 00:0D:18:3A:67:89
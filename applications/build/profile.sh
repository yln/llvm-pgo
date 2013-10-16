#!/bin/bash
if [ -z "$1" ]; then
	echo usage: $0 "source.c"
	exit	
fi

path="$1"
file_ext=$(basename "$path")
filename="${file_ext%.*}"

./clean.sh "$filename"

# This is duplicated in clean.sh
file_bc="$filename.bc"
file_profile_bc="$filename.profile.bc"
file_profile_s="$filename.profile.s"
file_profile="$filename.profile"

profiling="-insert-edge-profiling"

./clang -c -O1 -emit-llvm "$path" -o $file_bc
./opt $profiling $file_bc -o $file_profile_bc

./llc $file_profile_bc -o $file_profile_s

./clang -o $file_profile $file_profile_s ../../build/Debug+Asserts/lib/libprofile_rt.dylib

./$file_profile

./llvm-prof $file_profile_bc
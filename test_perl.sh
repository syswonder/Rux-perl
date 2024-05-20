#!/bin/sh
cd ./apps/c/rux-perl
if test ! -d "./rootfs/perl-5.38.2"; then
    echo "download perl"
    # get source code
    wget https://www.cpan.org/src/5.0/perl-5.38.2.tar.gz 
    # Extract the tarball
    tar -xzvf perl-5.38.2.tar.gz -C ./rootfs
    find ./rootfs/perl-5.38.2/t -type d -exec chmod 777 {} \;
    find ./rootfs/perl-5.38.2/t -type f -exec chmod 777 {} \;
fi

cp ./rootfs/perl ./rootfs/perl-5.38.2

# go to ruxos root dir
cd ../../..

# run test script
python3 ./apps/c/rux-perl/test.py
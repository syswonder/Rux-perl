app-objs=main.o

ARGS = perl,your_perl.t
ENVS = 
V9P_PATH=${APP}/rootfs
# make run ARCH=aarch64 A=apps/c/dl V9P=y MUSL=y LOG=debug
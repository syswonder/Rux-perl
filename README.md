# rux-perl
  Rux-perl is a project that supports Perl on Ruxos
## Easy run:
### Step1：
You need to successfully run [Ruxos](https://github.com/syswonder/ruxos) on your device.
### Step2:
  Go to Ruxos root dir and run:
  
```bash
git clone https://github.com/syswonder/rux-perl.git ./apps/c/rux-perl
make A=apps/c/rux-perl ARCH=aarch64 V9P=y NET=y MUSL=y LOG=info SMP=1 run
```

also you can run by `Rux-go`
```bash
ruxgo -b
ruxgo -r
```

## Perl test
  Because Ruxos is not support `fork()` now, so I used another way to run the test program.
  if you want to run the test program, you need to cancel code comments in ` main.c` :
```c
  // The following section of code is used only during Perl testing:

  // int fd = open("test_result.txt", O_WRONLY | O_CREAT | O_APPEND, 0644);
  // char *data = argv[1];
  // // wirte test filename
  // write(fd, "\n", 1);
  // write(fd, data, strlen(data));
  // write(fd, "\n", 1);
  // if (fd == -1) {
  //     perror("open failed");
  //     return 1;
  // }
  // // io redirect
  // if (dup2(fd, STDOUT_FILENO) == -1) {
  //     perror("dup2 failed");
  //     return 1;
  // }
  // chdir("/perl-5.38.2");
```
 and go to Ruxos root dir and run:

```bash
sh apps/c/rux-perl/test_perl.sh
```
The test results will be saved in `/rux-perl/test_result.txt`

You can see more information in [Ruxos-Book](https://ruxos.syswonder.org/chap02/apps/perl.html)
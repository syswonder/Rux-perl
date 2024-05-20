#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>

int main(int argc, char** argv, char**envp) {
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

	execv(argv[0], argv);
	return 0;
}
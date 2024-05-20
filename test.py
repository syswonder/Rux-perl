import os
# 定义要处理的文件夹列表
folders = ["./apps/c/rux-perl/rootfs/perl-5.38.2/t/base"
            ,"./apps/c/rux-perl/rootfs/perl-5.38.2/t/class"
            ,"./apps/c/rux-perl/rootfs/perl-5.38.2/t/cmd"
            ,"./apps/c/rux-perl/rootfs/perl-5.38.2/t/io"
            ,"./apps/c/rux-perl/rootfs/perl-5.38.2/t/japh"
            ,"./apps/c/rux-perl/rootfs/perl-5.38.2/t/mro"
            ,"./apps/c/rux-perl/rootfs/perl-5.38.2/t/opbasic"
            ,"./apps/c/rux-perl/rootfs/perl-5.38.2/t/re"
            ,"./apps/c/rux-perl/rootfs/perl-5.38.2/t/comp"]

# 打开输出文件
with open("./apps/c/rux-perl/filenames.txt", "w") as output_file:
    # 遍历文件夹列表
    for folder in folders:
        print(f"Processing files in {folder}...")
        # 使用 os 模块遍历文件夹中的文件
        for root, _, files in os.walk(folder):
            # 找到以 .t 结尾的文件，并将文件名写入输出文件
            for file in files:
                if file.endswith(".t"):
                    output_file.write(os.path.join(root, file) + "\n")

with open("./apps/c/rux-perl/rootfs/test_result.txt", 'w') as file:
    # 打开输出文件
    file.write("test result:")

# 打开输出文件，读取文件名并执行 make 命令
with open("./apps/c/rux-perl/filenames.txt", "r") as filenames_file:
    for filename in filenames_file:
        filename = filename.strip()  # 去除行末的换行符
        # 提取文件名并执行 make 命令
        file = filename[24:]  # 去除文件路径
        os.system(f"make A=apps/c/rux-perl ARCH=aarch64 V9P=y NET=y MUSL=y SMP=1 ARGS=perl,{file} run")

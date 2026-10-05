# Command Line Basics

The command line (terminal/shell) lets you interact with your computer by typing commands instead of clicking icons. It's faster for repetitive tasks, essential for using Git and most dev tools, and is usually the only interface available on remote servers.

## Navigating the Filesystem

`pwd` prints your current directory, `ls` (or `dir` on Windows) lists its contents, and `cd` changes into another directory.

```bash
pwd                 # /home/alex/projects
ls                  # list files in the current directory
cd my-project       # move into a folder
cd ..               # move up one level
cd ~                # jump to your home directory
```

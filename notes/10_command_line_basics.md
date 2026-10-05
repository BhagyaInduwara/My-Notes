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

`..` means "the parent directory" and `.` means "the current directory" — both are useful in paths like `cd ../sibling-folder`.

## Creating and Removing Files

`mkdir` creates a directory, `touch` creates an empty file, and `rm` removes files (use `rm -r` for directories, carefully — there's no trash can).

```bash
mkdir notes
touch notes/todo.txt
rm notes/todo.txt
rm -r notes
```

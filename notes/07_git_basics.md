# Git Basics

Git is a distributed version control system: it tracks changes to files over time, lets multiple people collaborate without overwriting each other's work, and lets you go back to any previous state of the project.

## Initializing a Repository

`git init` turns a folder into a Git repository by creating a hidden `.git` directory that stores all history.

```bash
git init
git status
```

`git status` shows what's changed, what's staged, and what's untracked — it's the command you'll run constantly.

## The Staging Area

Git has three areas: the working directory (your actual files), the staging area (changes you've marked to include in the next commit), and the repository (committed history). `git add` moves changes into staging.

```bash
git add file.txt        # stage one file
git add .                # stage everything in the current directory
```

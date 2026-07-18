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

## Committing

A commit is a snapshot of the staged changes, saved permanently in history with a message describing what changed.

```bash
git commit -m "Add user login form"
```

Good commit messages are short, specific, and written in the imperative mood ("Add", "Fix", "Update") rather than describing what you did ("Added", "Fixed").

## Viewing History

`git log` shows the commit history; `git diff` shows exact line-by-line changes.

```bash
git log --oneline
git diff              # unstaged changes
git diff --staged     # staged changes not yet committed
```

## Branches

A branch is an independent line of development. The default branch is usually called `main`. Creating a branch lets you work on a feature without affecting the main codebase until it's ready.

```bash
git branch feature-login       # create a branch
git checkout feature-login     # switch to it
git checkout -b feature-login  # create and switch in one step
```

Newer Git versions also support `git switch` for changing branches, which is a bit clearer than overloaded `checkout`.

```bash
git switch feature-login
git switch -c feature-login  # create and switch
```

## Merging

Once a branch's work is ready, `git merge` combines it back into another branch (commonly `main`).

```bash
git checkout main
git merge feature-login
```

If both branches changed the same lines, Git can't automatically decide which version to keep — this is a **merge conflict**, and Git marks the conflicting lines in the file for you to resolve manually before committing the merge.

```
<<<<<<< HEAD
Your version of the line
=======
Their version of the line
>>>>>>> feature-login
```

After editing the file to keep the correct content and removing the conflict markers, stage and commit the resolution.

## Remotes

A remote is a version of your repository hosted elsewhere (like GitHub). `git clone` copies a remote repo locally; `git push` sends local commits to the remote; `git pull` fetches and merges remote changes into your local branch.

```bash
git clone https://github.com/user/repo.git
git push origin main
git pull origin main
```

`origin` is just the conventional name for the primary remote — you could name it anything.

## Undoing Changes

Git offers several ways to undo things, each with a different scope. `git restore` reverts an unstaged file to its last committed state. `git reset` moves the branch pointer, optionally undoing commits. `git revert` creates a new commit that undoes a previous one, which is safer for shared history.

```bash
git restore file.txt              # discard unstaged changes to a file
git reset --soft HEAD~1           # undo last commit, keep changes staged
git revert abc1234                # safely undo a specific past commit
```

Avoid `git reset --hard` on commits that have already been pushed and shared with others — rewriting shared history can break their local copies.

## .gitignore

A `.gitignore` file lists patterns for files Git should never track, like build output, dependencies, or secrets.

```
node_modules/
*.log
.env
```

## Key takeaways

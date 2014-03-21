## Basics

git clone <repository url>

git status # Shows sttatus of local repsitory, untracked changes, staged changes etc.

git diff # Shows untracked changes

git diff --cached # Shows tracked changes that will be commited.

git commit -a # Will automatically stage every file that is already tracked.

git add # To add new or modified files for tracking.

git rm <filename> # Will remove a file from the workspace and stage the removal.
Just deleting the file will not stage the removal for commiting.

git rm --cached <filename> # Will remove the file from the staging area but keep it on your hard drive.

git mv <filename> <newfile> # Stages this as a rename. A short cut to avoid mv; git rm; git add.

## Logs

git log # By default lists commits with latest first

git log -p # Shows the diff introduced in each commit.

git log -p -2 # Shows the diff for the last two commits.

git log --word-diff # Shows changes by word rather than by line.

git log -U1 # Removes the default three lines of context

git log --stat # Shows a list of modified files, the number of files changed and how many lines in those files, for each commit.

git log --pretty # Allows different formating of log output.

git log --pretty=oneline # Prints each commit on a single line.

git log --pretty=format: "%h - %an, %ar : %s" # This a formatted string which translates as the following:

%h  Abbreviated commit hash

%an Authors name

%ar Author date, relative # Example "6 years ago"

:   This is just inserting a colon before the next string.

%s  Subject

A full list of format options can be found here: http://git-scm.com/book/en/Git-Basics-Viewing-the-Commit-History

gitk # A graphical tool to visualize logs that can take all the options of git log. Part of git but on Debian had to explicitly install with apt-get install gitk.

## Undoing Things

From the git book: "Here, we’ll review a few basic tools for undoing changes that you’ve made. Be careful, because you can’t always revert some of these undos. This is one of the few areas in Git where you may lose some work if you do it wrong."

git commit --amend # Overwrites a previous commit. Useful if you want to change the commit message or add more files to a commit.

git reset HEAD <filename> # Will unstage a staged file.

git checkout -- <file> # Will overwrite a local file with the file from the repository.
From the git book: "Don’t ever use this command unless you absolutely know that you don’t want the file. If you just need to get it out of the way, we’ll go over stashing and branching in the next chapter; these are generally better ways to go."

git remote -v # Shows urls of remote repositories.

git remote add pb git://github.com/paulboone/ticgit.git # This add the ticgit repository with a short name of pb inside the repository you are in.

git remote -v
origin  git://github.com/schacon/grit.git (fetch)
origin  git://github.com/schacon/grit.git (push)
pb  git://github.com/paulboone/ticgit.git (fetch)
pb  git://github.com/paulboone/ticgit.git (push)

git fetch # Grabs any data from remote that you don't yet have.

git pull # Will fetch and then merge a remote branch into your current branch.

git push [remote-name] [branch-name]

git push origin master

git remote show # Gives information about the remote repository, URL, branches, which branches will be merged and where you will push to by default.

git remote rename # Renames a remote reference.


git remote rm # Will REMOVE a remote reference. DO NOT DO THIS!!!  

## Tagging

git tag # List all available tags

git tag -a v1.0 -m "Version 1.4" # Creates a tag with a comment.

git tag -s # Signs a tag with gpg

git tag v1.4 # Creates a light weight tag containing only the commit checksum.

git tag -v [tag-name] # verifies the gpg signature of a signed tag.



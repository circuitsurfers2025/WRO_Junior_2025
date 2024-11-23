Microsoft Windows [Version 10.0.26100.2314]
(c) Microsoft Corporation. All rights reserved.

C:\Users\Urvish loser>cd C:\Users\Tavish\Documents\dev

C:\Users\Tavish\Documents\dev>git init
Initialized empty Git repository in C:/Users/Tavish/Documents/dev/.git/

C:\Users\Tavish\Documents\dev>git clone https://github.com/circuitsurfers2025/CircuitSurfers.git
Cloning into 'CircuitSurfers'...
remote: Enumerating objects: 3, done.
remote: Counting objects: 100% (3/3), done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 0), reused 3 (delta 0), pack-reused 0 (from 0)
Receiving objects: 100% (3/3), 23.75 KiB | 2.97 MiB/s, done.

C:\Users\Tavish\Documents\dev>git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        CircuitSurfers/

nothing added to commit but untracked files present (use "git add" to track)

C:\Users\Tavish\Documents\dev>
C:\Users\Tavish\Documents\dev>git branch -b develop_circuit_surfer_v1_0
error: unknown switch `b'
usage: git branch [<options>] [-r | -a] [--merged] [--no-merged]
   or: git branch [<options>] [-f] [--recurse-submodules] <branch-name> [<start-point>]
   or: git branch [<options>] [-l] [<pattern>...]
   or: git branch [<options>] [-r] (-d | -D) <branch-name>...
   or: git branch [<options>] (-m | -M) [<old-branch>] <new-branch>
   or: git branch [<options>] (-c | -C) [<old-branch>] <new-branch>
   or: git branch [<options>] [-r | -a] [--points-at]
   or: git branch [<options>] [-r | -a] [--format]

Generic options
    -v, --[no-]verbose    show hash and subject, give twice for upstream branch
    -q, --[no-]quiet      suppress informational messages
    -t, --[no-]track[=(direct|inherit)]
                          set branch tracking configuration
    -u, --[no-]set-upstream-to <upstream>
                          change the upstream info
    --[no-]unset-upstream unset the upstream info
    --[no-]color[=<when>] use colored output
    -r, --remotes         act on remote-tracking branches
    --contains <commit>   print only branches that contain the commit
    --no-contains <commit>
                          print only branches that don't contain the commit
    --[no-]abbrev[=<n>]   use <n> digits to display object names

Specific git-branch actions:
    -a, --all             list both remote-tracking and local branches
    -d, --[no-]delete     delete fully merged branch
    -D                    delete branch (even if not merged)
    -m, --[no-]move       move/rename a branch and its reflog
    -M                    move/rename a branch, even if target exists
    --[no-]omit-empty     do not output a newline after empty formatted refs
    -c, --[no-]copy       copy a branch and its reflog
    -C                    copy a branch, even if target exists
    -l, --[no-]list       list branch names
    --[no-]show-current   show current branch name
    --[no-]create-reflog  create the branch's reflog
    --[no-]edit-description
                          edit the description for the branch
    -f, --[no-]force      force creation, move/rename, deletion
    --merged <commit>     print only branches that are merged
    --no-merged <commit>  print only branches that are not merged
    --[no-]column[=<style>]
                          list branches in columns
    --[no-]sort <key>     field name to sort on
    --[no-]points-at <object>
                          print only branches of the object
    -i, --[no-]ignore-case
                          sorting and filtering are case insensitive
    --[no-]recurse-submodules
                          recurse through submodules
    --[no-]format <format>
                          format to use for the output


C:\Users\Tavish\Documents\dev>
C:\Users\Tavish\Documents\dev>git checkout -b develop_circuit_surfer_v1_0
Switched to a new branch 'develop_circuit_surfer_v1_0'

C:\Users\Tavish\Documents\dev>git add main_code.py
fatal: pathspec 'main_code.py' did not match any files

C:\Users\Tavish\Documents\dev>dir
 Volume in drive C is Local Disk
 Volume Serial Number is E83E-CB80

 Directory of C:\Users\Tavish\Documents\dev

23/11/2024  16:41    <DIR>          .
23/11/2024  16:35    <DIR>          ..
23/11/2024  16:43    <DIR>          CircuitSurfers
               0 File(s)              0 bytes
               3 Dir(s)  404.415.148.032 bytes free

C:\Users\Tavish\Documents\dev>cd CircuitSurfers

C:\Users\Tavish\Documents\dev\CircuitSurfers>git add main_code.py

C:\Users\Tavish\Documents\dev\CircuitSurfers>git commit -m "added new python file"
Author identity unknown

*** Please tell me who you are.

Run

  git config --global user.email "you@example.com"
  git config --global user.name "Your Name"

to set your account's default identity.
Omit --global to set the identity only in this repository.

fatal: unable to auto-detect email address (got 'Tavish@INF-MS-SurfaceLaptop5.(none)')

C:\Users\Tavish\Documents\dev\CircuitSurfers>git config --global user.email "urvishlanje25@gmail.com"

C:\Users\Tavish\Documents\dev\CircuitSurfers>git config --global user.name "circuitsurfers2025"

C:\Users\Tavish\Documents\dev\CircuitSurfers>git commit -m "added new python file"
[main 04e62fc] added new python file
 1 file changed, 1 insertion(+)
 create mode 100644 main_code.py

C:\Users\Tavish\Documents\dev\CircuitSurfers>git push origin
info: please complete authentication in your browser...
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 12 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 313 bytes | 39.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/circuitsurfers2025/CircuitSurfers.git
   4958186..04e62fc  main -> main

C:\Users\Tavish\Documents\dev\CircuitSurfers>git pull
remote: Enumerating objects: 5, done.
remote: Counting objects: 100% (5/5), done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
Unpacking objects: 100% (3/3), 989 bytes | 29.00 KiB/s, done.
From https://github.com/circuitsurfers2025/CircuitSurfers
   04e62fc..2b65572  main       -> origin/main
Updating 04e62fc..2b65572
Fast-forward
 main_code.py | 3 ++-
 1 file changed, 2 insertions(+), 1 deletion(-)

C:\Users\Tavish\Documents\dev\CircuitSurfers>git pull
remote: Enumerating objects: 8, done.
remote: Counting objects: 100% (8/8), done.
remote: Compressing objects: 100% (5/5), done.
remote: Total 6 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
Unpacking objects: 100% (6/6), 1.90 KiB | 25.00 KiB/s, done.
From https://github.com/circuitsurfers2025/CircuitSurfers
   2b65572..a8077c6  main       -> origin/main
Updating 2b65572..a8077c6
Fast-forward
 main_code.py | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)

C:\Users\Tavish\Documents\dev\CircuitSurfers>git pull
remote: Enumerating objects: 8, done.
remote: Counting objects: 100% (8/8), done.
remote: Compressing objects: 100% (5/5), done.
remote: Total 6 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
Unpacking objects: 100% (6/6), 2.83 KiB | 34.00 KiB/s, done.
From https://github.com/circuitsurfers2025/CircuitSurfers
   a8077c6..bde6df7  main       -> origin/main
Updating a8077c6..bde6df7
Fast-forward
 main_code.py | 89 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++--
 1 file changed, 87 insertions(+), 2 deletions(-)

C:\Users\Tavish\Documents\dev\CircuitSurfers>git push
To https://github.com/circuitsurfers2025/CircuitSurfers.git
 ! [rejected]        main -> main (fetch first)
error: failed to push some refs to 'https://github.com/circuitsurfers2025/CircuitSurfers.git'
hint: Updates were rejected because the remote contains work that you do not
hint: have locally. This is usually caused by another repository pushing to
hint: the same ref. If you want to integrate the remote changes, use
hint: 'git pull' before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.

C:\Users\Tavish\Documents\dev\CircuitSurfers>git pull
remote: Enumerating objects: 5, done.
remote: Counting objects: 100% (5/5), done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 3 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
Unpacking objects: 100% (3/3), 1010 bytes | 21.00 KiB/s, done.
From https://github.com/circuitsurfers2025/CircuitSurfers
   bde6df7..070d468  main       -> origin/main
Updating bde6df7..070d468
Fast-forward
 main_code.py | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)

C:\Users\Tavish\Documents\dev\CircuitSurfers>

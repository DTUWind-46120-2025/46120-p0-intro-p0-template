1. What is the difference between git and GitLab?
Git is a distributed version control software and GitLab/GitHub is "just" used to host the online/remote repositories. 
2. What is the difference between GitLab, GitHub, and BitBucket?
To our understanding GitLab and GitHub are pretty similar, though one difference is that you can host your own GitLab server. Regarding Bitbucket it seems that it is mostly used for private repositories when you do not want to share your code with others. Also GitLab/GitHub has a large open-source community whereas Bitbucket does not.
3. Why would I ever want to use git, but not GitLab?
Probably in the case where we do not need to collaborate with others.
4. What are the steps to update the GitLab server with some changes I made on my computer?
For GitHub (it may be the same for GitLab): 'git add <file-name>', 'git commit -m “<message>”', 'git push origin main'. It is a good idea to use 'git branch' or 'git status' inbetween these commands.
5. What is a branch and why would I use one?
A branch is kind of like a fork but on the same repository. It allows for multiple people to diverge from main and then adding each person’s contribution as an entirety instead of everyone working in the same files at once.
6. How could you visualize a branch with 3 commits, and then another branch that breaks off after the second commit and has a single commit?
See image file.
7. Give an example of a set of git commands that would result in a merge conflict.
If two people in a group are each working on their own branches and then they both edit the same file in the same line. Then when the second person adds, commits and then 'git push origin main', then they should receive an error. Then because they edited the same line the second person cannot just 'git pull' but has to review the changes manually.
8. Is Git suitable for latex documents?
In general: no. LaTeX documents are binary documents, so there may be issues with these in git. However, it seems that it should actually still work according to some users on online forums.
9. Should I from now on version my word and powerpoint slides using git? Why/why not?
This is related to the previous question. Word and powerpoint files are binary files and git may have issues with these, so then no.
10. What could happen when I push my latest commit to the remote repository without pulling first?
You would probably be told that you are not up to date with the remote repository and it will ask you to pull first.
11. What happens when I pull without commiting my local changes first?
You get the remote repository so that you are up to date locally, but it won't remove your local changes. So then after pulling you should still push to apply your local changes to the remote repository.
12. What is the difference between branching and forking?
When you fork you create a copy of the repo as a new repo. When you branch you create a new version of the repo inside the current repo. So forking gets you two distinct repos whereas with branching you still only have a single repo.

Questions

1.What is the difference between git and GitLab?
Git is a distributed version control system, while GitLab is a web-based platform which integrates Git repository management with continuous integration.
(Mariel-GitHub is a platform that hosts Git repositories online, providing remote services for version control and collaboration)
(Rehab: Git is the software program and gitlab is an online hosting service)

2.What is the difference between GitLab, GitHub, and BitBucket?
(Rehab: They are differnet hosting services which ...)
The difference between GitLab, GitHub, and BitBucket is that they have three different ways of dealing with the merge request process. 
(Mariel- GitLab, GitHub, and BitBucket also have different capabilities - collaboration features, automation, tools, integrations etc. GitHub is mostly used at the company level when you have to collaborate with developers around the globe. On the other hand, GitLab is best when you need comprehensive features that support the end-to-end development process. BitBucket is best for teams that want to collaborate on private software. BitBucket is also more flexible (easy access CI and option to integrate various APIs with services))

3.Why would I ever want to use git, but not GitLab?
Git can be used for solo coding, while GitLab is a collaborative platform.
(Rehab: Git is perfect for offline use)

4.What are the steps to update the GitLab server with some changes I made on my computer?
I need to pull the file I updated on my computer to the remote on GitHub/GitLab so that the other team members can get it by pushing it. 
(Mariel-push and pull mixed up-I need to push the file I updated on my computer to the remote on GitHub/GitLab so that the other team members can pull it)

5.What is a branch and why would I use one?
A branch is an independent line of development, and it is used to avoid confusion between different parts of a project. 
(Mariel- confusion->conflicts)

6.How could you visualize a branch with 3 commits, and then another branch that breaks off after the second commit and has a single commit?
Let's sat that there are A,B and C branches, D is the new branch which hass spilt off the second commit and it has a single commit. 

7.Give an example of a set of git commands that would result in a merge conflict.
git push TextFilev1.txt
git push TextFilev2.txt
(Mariel- Maybe this is better example?-git pull origin master and git push origin master.
This create a conflict if there are changes in the same part of the file that weren’t merged properly.)

8.Is Git suitable for latex documents?
Yes, it is.

9.Should I from now on version my word and powerpoint slides using git? Why/why not?
No, as the use of binary files in GitHub increases the used space. 
(Rehab: add: binary files makes Git inefficinet where it is hard to track changes and hard to merge.

10.What could happen when I push my latest commit to the remote repository without pulling first?
It is likely that conflicts can arise as the changes made in the pulled file are likely not being included in the pushed one. 
(Mariel- Maybe a bit better wording?- It is likely that conflicts could arise, as the changes made in the pulled file may not be included in the pushed one)
(Rehab: no problem if there is no changes on remote and also conflict as described before)

11.What happens when I pull without commiting my local changes first?
Uncommitted local changes when pulling a file lead to not recording the changes in the repository, so the pulled file might be incomplete.

12.What is the difference between branching and forking?
Branching is the creation of an independent line, while forking is a copy of a project in your directory so that the original one is not affected.
(Mariel- Maybe a bit better?- Branching creates an independent line of development within the same repository, while forking creates a copy of the repository in your own directory, so the original one is not affected.)
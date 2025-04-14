# Git questions to answer
## What is the difference between git and GitLab?
**Git** is a distributed version control system that helps you to track changes in files, while working on a local computer. On the other hand, **GitLab** is an online platfrom that gived the opportunity to share your changes with other people.

## What is the difference between GitLab, GitHub, and BitBucket?
All of them are online platforms that give the opportunity to work on a same project with other peopole while thaking track of the changes made. The main difference between the three is the owner (GitLab Inc., Microsoft, and Atlassian) and the popularity.

## Why would I ever want to use git, but not GitLab?
You don't need to work on GitLab if:
- you are working on a personal project and don't need to share it with other people;
- you use a different online server.

## What are the steps to update the GitLab server with some changes I made on my computer?
The key passages to do in order to update the online server after you have done changes locally are:
1. Use the commnad **add** to prepare the file to be updated;
2. Use the command **commit** with **-m "Message"** to update the new changes made in Git;
3. **Push** your changes in the online server.

## What is a branch and why would I use one?
A branch is a lateral path from the main where a user can apply changes without modifying the master branch. The reason behind using a branch instead of just changing the main is that the applied changes might not work. Thus, if you create your own branch, the failure affects just you (and who is using your branch) but not the entire work, while a modification on the main would affect everyone.

## How could you visualize a branch with 3 commits, and then another branch that breaks off after the second commit and has a single commit?
![Branch Visualization](/branch.jpg)


## Give an example of a set of git commands that would result in a merge conflict.
For instance, let's take the following line of a python script written in two different ways from two different users:
```python
WindData = data[2]
```
```python
WindData = data[1]
```
As shown, if one of the two tries to pull the changes from the online server, it will receive a **Marge Conflict**.

## Is Git suitable for latex documents?
If the file is saved as *.tex*, then probably Git can be used to store the changes apported, while it's not suitable if the file is saved as a PDF, because binary files can't be compared easily.

## Should I from now on version my word and powerpoint slides using git? Why/why not?
As just stated in the previous answer, binary files can't be compared easily. Hence, it's not a good idea to use Git for Word and PowerPoint.

## What could happen when I push my latest commit to the remote repository without pulling first?
Usually you will receive an error message saying that your local repository is not up to date with the online one, and it will ask you to pull first the changes, and then push yours.

## What happens when I pull without commiting my local changes first?
Git should save your changes for a later add/commit, but only if there are not any merge conflicts. Otherwise, you might have to change something in your file (ore the one pulled) to resolve conflicts.

## What is the difference between branching and forking?
**Forking** creates a new repository from one existing in GitLab/GitHub, which later can be cloned locally. **Branch** just create another branch from the master one, in order to work on your project without affecting other people. 
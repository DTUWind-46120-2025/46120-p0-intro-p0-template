1.	What is the difference between git and GitLab?  
git is the distributed version control system (VCS) that works locally on the computer, and gitlab is the server where we can store a remote repository
VCS: track cahnges to files and collaborate 
manage different versions of code/files locally / remotely

gitlab: repo management service (web based platform)


=======
Veronica Answers:
    1. Git: version control system: save your work, update, and keep track of changes. Saves "snapshots".
    (https://www.bairesdev.com/blog/git-github-and-gitlab-whats-the-difference/)
    GitLab: For DevOps, meaning instead of using different plaforms for Issue Tracking, Source Control, CI/CD (continous integrating/continous deployment) Testing, Monitoring, GitLab compines everything in one platform. It alos uses packages to store your code.
    Essentially GitLab is building --> Testing --> Deploying. 
    (Gitlab Explained: What is Gitlab and Why Use It?)


2.	What is the difference between GitLab, GitHub, and BitBucket?  
different services that provide servers and interfaces for storing repos remotely

GitLab → Best for self-hosting, DevOps, and CI/CD automation.
GitHub → Best for open-source collaboration, large community, and general development.
Bitbucket → Best for small teams & enterprises, integrates well with Jira & Atlassian products.


3.	Why would I ever want to use git, but not GitLab?  
if you are only working on one computer alone and dont need to collaborate 

4.	What are the steps to update the GitLab server with some changes I made on my computer?  
=======
Veronica Answer:
    2. GitHub: owned by Microsoft. Integration offered by third-party vendors. Focusies on a strong community and encoureges collaboration. Older so more users. 
    GitLab: owned by GitLab Inc. Build-in integrations. Is more all in one. 
    (https://www.bairesdev.com/blog/git-github-and-gitlab-whats-the-difference/)
    BitBucket: owned by Eficode. Somehow basic, and ideally for integrations from Atlassian like Jira, Confluence, and Trello. So, this is to choose when you already work on these platforms. 

3.	Why would I ever want to use git, but not GitLab?  
if you are only working on one computer alone and dont need to collaborate 

Veronica Answers:
    3. When you want to view projects locally, and not have the versions in a cloud. But essentially GitLab has the same features (and more) than Git. 
    (https://kodekloud.com/blog/git-vs-github-vs-gitlab/)

4.	What are the steps to update the GitLab server with some changes I made on my computer?  
Veronica Answers:
        a. Stage changes:
            git add
        b. Commit changes:
            git commit -m ">Change message<"
        c. Puch changes to GitLab 
            git push origin >branch name<
            Branch name typically main or master

0. git status
1. git add (files) (staging)
2. git commmit (write what was done)
3. git push

5.	What is a branch and why would I use one?  
my explanation:
its your own parallel universe you can work on without affecting the other collaborators branches or the main branch. 
it is useful if you wanna go off in a direction without having to stay in sync with the main branch or the others

chat explanation:
A branch is a separate version of your code within a Git repository.  

Why use one?  
1. Isolate new features without affecting the main code.  
2. Work on bug fixes without disrupting the stable version.  
3. Collaborate safely, allowing multiple people to work on different parts of a project.  
4. Experiment freely without risking the main branch.  

6.	How could you visualize a branch with 3 commits, and then another branch that breaks off after the second commit and has a single commit?  
seperate figure made (breakout_branch_visualized)
in git bash:
git log --oneline --graph --all


7.	Give an example of a set of git commands that would result in a merge conflict.  
user 1: makes a change to line 3
user 1: adds to staging area
user 1: commits 

user 2: makes a change to line 3
user 2: adds to staging area
user 2: commits 

user 1: pushes to remote server
user 2: pushes to remote server -> error
user 2: pulls from remote server -> error

solution: resolve conflict before pushing

8.	Is Git suitable for latex documents? 

yes, but no PDFs (binary files) 

9.	Should I from now on version my word and powerpoint slides using git? Why/why not?  

word/pp are binary files, they are large and are difficult to merge
instead of pp use latex (beamer)
convert word to markdown or use latex/google docs / word online

10.	What could happen when I push my latest commit to the remote repository without pulling first?  

there might be a conflict with a file if someone has worked on the same thing as you 

therefore, always pull first, resovle potential conflicts and then push
=======
therefore, always pull first, resolve potential conflicts and then push



11.	What happens when I pull without commiting my local changes first?  
If you pull without committing your local changes first, Git will try to merge your local changes with the remote changes. Here's what could happen:

If there are no conflicts, Git will automatically merge your local changes with the pulled changes.
If there are conflicts, Git will pause the merge process and mark the conflicted files. You'll need to resolve the conflicts manually.
If your changes aren't staged, Git will prevent the pull and show a warning to commit or stash your changes first.
Best practice:

Always commit or stash your changes before pulling to avoid conflicts and ensure a clean merge process.

12.	What is the difference between branching and forking?

Branching and forking are both used to create independent development paths, but they serve different purposes:

 Branching:
- Used within a single repository.
- Creates a separate line of development to work on new features or bug fixes.
- Changes are typically merged back into the main branch once development is complete.
- Best for collaborative work within the same project.

 Forking:
- Creates a copy of a repository under your own account (usually from someone else's project).
- Allows you to experiment or contribute without affecting the original project.
- Common in open-source projects where contributions are made via pull requests.
- Best for contributing to external projects.

In short:  
- Branching is for working within the same repo, while forking is for copying and working on someone else's project.



this is an edit that im making just to test a pull request, to merge my changed gitanswers.md file onto the main branch
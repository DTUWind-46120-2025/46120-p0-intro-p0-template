What is the difference between Git and GitLab?
Git is a version control system that tracks changes in code, while GitLab is a web-based platform that provides Git repository hosting, CI/CD, and collaboration tools.

What is the difference between GitLab, GitHub, and BitBucket?
GitLab offers full DevOps integration and self-hosting options, GitHub is widely used with a strong open-source community, and BitBucket is popular for private repositories, especially in enterprise settings.

Why would I ever want to use Git, but not GitLab?
You might use Git alone if you only need local version control without remote collaboration, a web interface, or CI/CD features.

What are the steps to update the GitLab server with some changes I made on my computer?
Commit your changes with git commit -m "message", push them with git push origin branch-name, and optionally create a merge request in GitLab.

What is a branch and why would I use one?
A branch is an independent line of development that allows multiple features or fixes to be developed in parallel without affecting the main codebase.

How could you visualize a branch with 3 commits, and then another branch that breaks off after the second commit and has a single commit?
A---B---C  (main branch)
    \
     D  (new branch after B)
This shows the main branch progressing through A, B, and C, while a second branch splits off at B and adds commit D.

Give an example of a set of git commands that would result in a merge conflict.
git init
echo "Hello" > file.txt
git add file.txt && git commit -m "Initial commit"
git checkout -b new-branch
echo "Change in new branch" > file.txt
git commit -am "Edit in new branch"
git checkout main
echo "Change in main branch" > file.txt
git commit -am "Edit in main"
git merge new-branch  # Conflict occurs

Is Git suitable for LaTeX documents?
Yes, Git is useful for LaTeX documents, especially when using plain text .tex files, as it tracks changes effectively and facilitates collaboration.

Should I from now on version my Word and PowerPoint slides using Git? Why/why not?
Not necessarily, since .docx and .pptx are binary files, making Git's version tracking less effective and diffs hard to interpret.

What could happen when I push my latest commit to the remote repository without pulling first?
If the remote has new changes, your push will be rejected, and you may need to pull and resolve conflicts before pushing.

What happens when I pull without committing my local changes first?
Git will attempt to merge the remote changes with your local changes; if there are conflicts, you'll need to resolve them before proceeding.

What is the difference between branching and forking?
Branching creates a separate development line within the same repository, while forking creates a copy of a repository under a different owner, allowing independent modifications.
---
layout: page
title: GIT
---

## Start with GitHub

Text from [web site](http://pbiecek.github.io/Przewodnik/Programowanie/jak_korzystac_z_serwisu_github_i_waffle.html)



When You working on a project, e.g. a master's thesis, (alone or in a team) you often need to check what changes, when and by whom were introduced to the project.
The "version control system" or [GIT](https://git-scm.com) works great for this task.

You can download and install Git like a regular program on any computer.
However, most often (small projects) you use websites with some kind of git system.
One of the most recognized is [GitHub] (www.github.com) which allows you to use the git system without installing it on your computer.

In the free version of the `GitHub` website, you can store your files in public (everyone has access) repositories.
We will only focus on the free version of GitHub:

```{bash}
git --version
```

## GitHub

At the highest level, there are individual accounts (eg. [http://github.com/sebkaz](http://github.com/sebkaz) or those set up by organizations.
Individual users can create ** repositories ** public (`public`) or private (` private`).

One file should not exceed 100 MB.

**Repo** (shortcut to repository) is created with `Create a new repository`.
 Each repo should have an individual name.

### Branches

The main (created by default) branch of the repository is named `master`.


### Most important commends

* _clone of Your repository_

```{bash}
git clone https://adres_repo.git
```

> In github case, you can download the repository as a 'zip' file.

* _Repository for local directory_

```{bash}
# new directory
mkdir datamining
cd datamining
# init repo
git init
# there sould be a .git new directory
# add file
echo "Info " >> README.md
```

* local and web version connection 

```{bash}
git remote add origin https://github.com/<twojGit>/nazwa.git
```

* 3 steps

```{bash}
# status check
git status
# 1. add all changes
git add .
# 2. commit all changes with message
git commit -m " message "
# 3. and
git push origin master
```
You can watch [Youtube course](https://www.youtube.com/watch?v=HVsySz-h9r4).

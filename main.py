from git import Repo
import subprocess


repos = [ui_repo_path]

def get_commits(commits):
    print(len(commits))
    for line in commits:
        commit_number = line.split()
        #print(len(author))

        print(commit_number)

x = ""
for repo in repos:

    out, err = subprocess.Popen(['git shortlog -sn --all -w' ],
                  cwd=repo,  shell=True, stdin=subprocess.PIPE,
                  stdout=subprocess.PIPE).communicate()

    x = out.splitlines()


print(x)
get_commits(x)




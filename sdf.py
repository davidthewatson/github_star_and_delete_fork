from github import Github
import os

username = os.environ['GITHUB_USERNAME']
password = os.environ['GITHUB_PASSWORD']

g = Github(username, password)

"""
for each repository in my resositories, if the repository has a parent,
star the repository and delete it, leaving only my original repositories
"""
for repo in g.get_user().get_repos():
    if repo.parent is not None:
        print repo.name
        g.get_user().add_to_starred(repo.parent)
        repo.delete()
    else:
        print 'repository ' + repo.name + ' has no parent'

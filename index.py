import git
from git_contributions_importer import *

repo = git.Repo("/home/rafael/Desktop/work/bizorRepo/bizor-next")
mock_repo = git.Repo("/home/rafael/Desktop/sandbox/gitRepos/contributionImporter")

importer = Importer([repo], mock_repo)
importer.set_author(["rcontreraspimentel@gmail.com"])

importer.import_repository()
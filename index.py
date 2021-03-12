import git
from git_contributions_importer import *

repo = git.Repo("https://Rcontre360@bitbucket.org/bizor/bizor-next.git")
mock_repo = git.Repo("https://github.com/Rcontre360/mock-repo.git")

importer = Importer([repo], mock_repo)
importer.set_author(["rcontreraspimentel@gmail.com","sphere@bizor.io"])

importer.import_repository()
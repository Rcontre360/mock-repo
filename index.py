import git
from git_contributions_importer import *

repo = git.Repo("/home/rafael/Desktop/work/bizor/demo-pago-movil")
mock_repo = git.Repo("/home/rafael/Desktop/repos/mock-repo")

importer = Importer([repo], mock_repo)
importer.set_author(["rcontreraspimentel@gmail.com"])

importer.import_repository()

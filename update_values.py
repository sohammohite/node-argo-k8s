
from github import Github
from github import Auth
import os
import yaml

token = os.environ.get('GIT_TOKEN')
sha = os.environ.get('GITHUB_SHA')

github_sha = sha[0:7]

print(token)
auth = Auth.Token(str(token))
g = Github(auth=auth)
repo = g.get_repo("sohammohite/node-argo-k8s")
contents = repo.get_contents("node-argo-k8s-helm/values.yaml")

f = open("values.yaml", "w")
f.write(contents.decoded_content.decode("utf-8"))
f.close()

file = open("values.yaml", "r")
data = yaml.load(file, Loader=yaml.FullLoader)
file.close()

data["image"]["tag"] = github_sha
file = open("values.yaml", "w")
yaml.dump(data, file)
file.close()

commit_msg = "Updated values.yaml for " + github_sha
repo.update_file("node-argo-k8s-helm/values.yaml", commit_msg, open("values.yaml", "r").read(), contents.sha)

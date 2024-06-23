
from github import Github
from github import Auth
import os
import yaml

token = os.environ.get('GIT_TOKEN')
github_sha = os.environ.get('GIT_SHA')

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

repo.update_file("node-argo-k8s-helm/values.yaml", "Updated values.yaml", open("values.yaml", "r").read(), contents.sha)

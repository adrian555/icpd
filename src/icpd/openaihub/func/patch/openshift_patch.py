import yaml

def argo_patch(path):
  y = yaml.safe_load(open(path))
  del y["metadata"]
  y["metadata"] = dict()
  y["metadata"]["labels"] = dict()
  y["metadata"]["labels"]["app"] = "argo"
  y["metadata"]["name"] = "argo"
  for x in y["rules"]:
    if "pods" in x["resources"]:
      x["verbs"].append('delete')
    elif "workflows" in x["resources"]:
      x["resources"].append('workflows/finalizers')
  yaml.dump(y, open(path,'w'), default_flow_style=False)

def studyjob_patch(path):
  y = yaml.safe_load(open(path))
  del y["metadata"]
  y["metadata"] = dict()
  y["metadata"]["name"] = "studyjob-controller"
  for x in y["rules"]:
    if "jobs" in x["resources"]:
      x["resources"].append('jobs/finalizers')
    elif "tfjobs" in x["resources"]:
      x["resources"].append('tfjobs/finalizers')
      x["resources"].append('pytorchjobs/finalizers')
  yaml.dump(y, open(path,'w'), default_flow_style=False)
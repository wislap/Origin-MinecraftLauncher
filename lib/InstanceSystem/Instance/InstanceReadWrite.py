import json


def InstanceRead(file):
    InstanceData = open(file, "r")
    InstanceData_dirt = json.loads(InstanceData.read())
    InstanceData.close()
    return InstanceData_dirt


def InstanceWrite(file, InstanceObject):
    InstanceData = open(file, "w")
    InstanceData.write(json.dumps(InstanceObject))
    InstanceData.close()

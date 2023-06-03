import hashlib
import os
import json
import time

NodePath = r"D:\\Python_program\\起源启动器2.0\\data\\Node\\"


def MD5(Name: str) -> str:
    Name_utf8 = (Name + str(time.time())).encode("utf8")
    m2 = hashlib.md5()
    m2.update(Name_utf8)
    # print(m2.hexdigest())
    return m2.hexdigest()


class Node:
    def __init__(self, NodeName: str, FatherNode: list = [None], SubNode: list = [None], InstanceUUID=None) -> None:
        self.NodeName = NodeName
        self.FatherNode = FatherNode
        self.SubNode = SubNode
        self.NodeUUID = MD5(NodeName)

    @property
    def getNodeName(self):
        return self.NodeName

    @property
    def getFatherNode(self):
        return self.FatherNode

    def setInstanceName(self, newFatherNode):
        self.FatherNode = newFatherNode

    @property
    def getSubNode(self):
        return self.SubNode

    def setSubNode(self, newSubNode):
        self.SubNode = newSubNode

    def __del__(self):
        pass


def Node_Write(NodePath, NodeName, NodeUUID, FatherNode=[None], SubNode=[None], InstanceUUID=None):
    if os.path.exists(NodePath + NodeUUID) == False:
        with open(NodePath + NodeUUID, "w+") as NodeFile:
            NodeFile.write(json.dumps(
                [{"NodeName": NodeName, "NodeUUID": NodeUUID, "FatherNode": FatherNode, "SubNode": SubNode,
                  "InstanceUUID": InstanceUUID}]))
    else:
        print("error")


def Node_Read(NodePath):
    NodeList = os.listdir(NodePath)
    NodeList_Object = {}
    for i in NodeList:
        with open(NodePath + i, "r+") as NodeFile:
            Node_json = json.loads(NodeFile.read())
            Node_object = Node(NodeName=Node_json[0]["NodeName"], FatherNode=Node_json[0]["FatherNode"],
                               SubNode=Node_json[0]["SubNode"], InstanceUUID=Node_json[0]["InstanceUUID"])
            NodeList_Object[i] = Node_object
            print(NodeList_Object)


class Node_Search:
    def __init__(self, NodeUUID) -> str:
        pass


# a = Node('''"e6e"''')
c = "e2e"
# b = Node_Write(NodePath=NodePath, NodeName=c, NodeUUID=MD5(c))
d = Node_Read(NodePath=NodePath)
NodeUUID = MD5(c)

import json

# jsonBinaryTree = '{"tree": { "nodes": [ {"id": "1", "left": "2", "right": "3", "value": "1"}, {"id": "2", "left": "4", "right": "5", "value": "2"}, {"id": "3", "left": "6", "right": "7", "value": "3"}, {"id": "4", "left": "8", "right": "9", "value": "4"}, {"id": "5", "left": null, "right": null, "value": "5"}, {"id": "6", "left": null, "right": null, "value": "6"}, {"id": "7", "left": null, "right": null, "value": "7"}, {"id": "8", "left": null, "right": null, "value": "8"}, {"id": "9", "left": null, "right": null, "value": "9"}], "root": "1"}}'
jsonBinaryTree = '{"tree":{"nodes":[{"id":"1","left":"2","right":null,"value":1},{"id":"2","left":"3","right":null,"value":2},{"id":"3","left":"4","right":null,"value":3},{"id":"4","left":"5","right":null,"value":4},{"id":"5","left":"6","right":null,"value":5},{"id":"6","left":null,"right":"7","value":6},{"id":"7","left":null,"right":null,"value":7}],"root":"1"}}'
# {"tree":{"nodes":[{"id":"1","left":null,"right":null,"value":1}],"root":"1"}}
binTree = json.loads(jsonBinaryTree)

class newNode:
  def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
  
def getNextLevel(node, value, level):
    if (node == None):
        return 0
    if (node.value == value):
        return level
    nextLevel = getNextLevel(node.left, value, level + 1)
    if (nextLevel != 0):
        return nextLevel
    nextLevel = getNextLevel(node.right, value, level + 1)
    return nextLevel
  
def getLevel(node, value):
    return getNextLevel(node, value, 0)
  
def jsonToTree(binTree):
    numNodes = len(binTree["tree"]["nodes"])
    nodeArray = []
    for i in range(numNodes):
        nodeArray.append(newNode(i))
    for i in range(numNodes):
        nodeArray[i].value = int(binTree["tree"]["nodes"][i]["value"]) 
        nodeArray[i].left = nodeArray[int(binTree["tree"]["nodes"][i]["left"])-1] if binTree["tree"]["nodes"][i]["left"] != None else None 
        nodeArray[i].right = nodeArray[int(binTree["tree"]["nodes"][i]["right"])-1] if binTree["tree"]["nodes"][i]["right"] != None else None
    root = nodeArray[int(binTree["tree"]["root"])-1]
    return root, numNodes

if __name__ == '__main__': 
    root, numNodes = jsonToTree(binTree)
    depthSum = 0
    for x in range(1, numNodes+1):
        level = getLevel(root, x) 
        if (level):
            depthSum += getLevel(root, x)
    print(depthSum)
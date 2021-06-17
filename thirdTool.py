import json
from ast import parse
from ast2json import ast2json
from graphviz import Digraph
#print('Avaiblable Test Programs :\n evenNumbers.py \n Factorial.py \n Fibonacci.py \n leapyear.py \n PositiveNagativeCount.py')
#val = input("Enter python program Name: ") 

Assignments = ""
conditions = ""
loop = ""
basicBlocks = {}
blockNumber=0
links={}
ifAssignments = ""
Assignmentss = ""
ast = ast2json(parse(open('Simpal1.py').read()))
#print (json.dumps(ast, indent=4))

# the json file where the output must be stored
out_file = open("myfile.json", "w")

json.dump(json.dumps(ast, indent=4), out_file, indent=6)

out_file.close()


#opening AST tree in JSON format
with open("myfile.json") as f:
    data = json.load(f)

jsondata = json.loads(data)




# Defining Global variables to Store output statements



#converting english operations to math operations
def mathOpps(argument):
    switcher = {
        "Add": "+",
        "Mult": "*",
        "Sub": "-",
        "Eq": "==",
        "Gt": ">",
        "Lt": "<",
        "GtE": ">=",
        "LtE": "<=",
        "BitAnd": "&",
        "NotEq": "!=",
        "Mod": "%",
        "Div": "/"

    }
    return switcher.get(argument, "N/A")

#Handling '_type=Compare' Operations ex a=b>c
def CompareOpp(BinaryTree):
    BinaryAssignment = ""
    leftOprand = ""
    rightOprand = ""
    #if BinaryTree["left"]["_type"] == "BinOp":
        #leftOprand += CompareOpp(BinaryTree["left"])
    try:
        if BinaryTree["left"]["_type"] == "Constant" or BinaryTree["left"]["_type"] == "Name":
            leftOprand = (
                str(BinaryTree["left"]["n"])
                if BinaryTree["left"]["_type"] == "Constant"
                else BinaryTree["left"]["id"]
            )

        Operation = mathOpps(BinaryTree["ops"][0]["_type"])

        #if BinaryTree["right"]["_type"] == "BinOp":
            #rightOprand += CompareOpp(BinaryTree["right"])

        if (BinaryTree["comparators"][0]["_type"] == "Constant" or BinaryTree["comparators"][0]["_type"] == "Name"):
            rightOprand = (
                str(BinaryTree["comparators"][0]["n"])
                if BinaryTree["comparators"][0]["_type"] == "Constant"
                else BinaryTree["comparators"][0]["id"]
            )

        BinaryAssignment += BinaryAssignment + leftOprand + Operation + rightOprand
    except:
        print('Error in CompareOpp ')
    return BinaryAssignment

def callhandle(BinaryTree):
    callStatement=''
    oprands=''
    
    if BinaryTree['func']['_type'] == 'Name':
        callStatement+=BinaryTree['func']['id'] + '('
    oprandarray=BinaryTree['args']
    for op in oprandarray:
        if op['_type']=='Name':
            callStatement+=op['id'] +','
        elif op['_type']=='Constant':
            callStatement+=str(op['value']) +','
    indexofcomma=callStatement.rfind(',')
    finalString=callStatement[0:indexofcomma]
    finalString+=')'
    return finalString

        
       
def BinaryOpp(BinaryTree):
    BinaryAssignment = ""
    leftOprand = ""
    rightOprand = ""
    try:
        if BinaryTree["left"]["_type"] == "BinOp":
            leftOprand += BinaryOpp(BinaryTree["left"])

        elif BinaryTree["left"]["_type"] == "Constant" or BinaryTree["left"]["_type"] == "Name":
            leftOprand = (
                str(BinaryTree["left"]["n"])
                if BinaryTree["left"]["_type"] == "Constant"
                else BinaryTree["left"]["id"]
            )

        Operation = mathOpps(BinaryTree["op"]["_type"])

        if BinaryTree["right"]["_type"] == "BinOp":
            rightOprand += BinaryOpp(BinaryTree["right"])

        elif (
            BinaryTree["right"]["_type"] == "Constant" or BinaryTree["right"]["_type"] == "Name"
        ):
            rightOprand = (
                str(BinaryTree["right"]["n"])
                if BinaryTree["right"]["_type"] == "Constant"
                else BinaryTree["right"]["id"]
            )

        BinaryAssignment += BinaryAssignment + leftOprand + Operation + rightOprand
    except:
        print('Error in BinaryOpp')
    return BinaryAssignment

#Handling Logical operation such as (num%4) < 5
def handleLogicalCompare(ifdata):
    con=''
    try:
        if ifdata["left"]['_type'] == "Constant" or ifdata["left"]['_type']=="Name":
                    LHS = (
                    str(ifdata["left"]["n"])
                    if ifdata["left"]['_type'] == "Constant"
                    else ifdata["left"]["id"] 
                    )
                
        elif ifdata["left"]['_type'] == "BinOp":
                    LHS=BinaryOpp(ifdata["left"])
                    
        operation = mathOpps(ifdata["ops"][0]["_type"]) 

        comparator = (
                str(ifdata["comparators"][0]["n"])
                if ifdata["comparators"][0]["_type"] == "Constant"
                else ifdata["comparators"][0]["id"]
                )

                
        con= LHS + ' '+ operation+' ' + comparator 
    except:
        print('error in handleLogicalCompare')

    return con

    



#handling Logical comparisson such as (num < 5 And num > 2)
def BooleanCompare(ifdata):
    Compare=""
    leftOprand = ""
    rightOprand = ""
    try:
        if ifdata["values"][0]['_type'] == "BoolOp":
            leftOprand += BooleanCompare(ifdata["values"][0])
        elif ifdata["values"][0]['_type']=='Compare':

            if ifdata["values"][0]["comparators"][0]["_type"] == "Constant" or ifdata["values"][0]["comparators"][0]["_type"] == "Name":
                leftOprand= handleLogicalCompare(ifdata["values"][0]) 
                
                
        Oprand=ifdata['op']['_type']

        if ifdata["values"][1]['_type'] == "BoolOp":
            rightOprand += BooleanCompare(ifdata["values"][1])
        elif ifdata["values"][1]['_type']=='Compare':

            if ifdata["values"][1]["comparators"][0]["_type"] == "Constant" or ifdata["values"][1]["comparators"][0]["_type"] == "Name":
                rightOprand= handleLogicalCompare(ifdata["values"][1])
                
                
                
        
        Compare=leftOprand+' '+Oprand+' '+rightOprand
    except:
        print('error in BooleanCompare')
    return Compare



#handling Branch conditions for If,elif,while loop
def handleCompare(ifdata):
    con=""
    try:
        if ifdata['_type']=='Compare':
            if ifdata["comparators"][0]["_type"] == "Constant" or ifdata["comparators"][0]["_type"] == "Name":
                con+= handleLogicalCompare(ifdata)
        if ifdata['_type']=='BoolOp':
            con +=BooleanCompare(ifdata) + "\n"
    except:
        print('error in handleCompare')
        
    return con

#Handling assignment statments a=5 etc 
def SimpleAssignment(Jdata):
    global Assignments
    
    LHS = Jdata["targets"][0]["id"] + "="
    if Jdata["value"]["_type"] == "Constant" or Jdata["value"]["_type"] == "Name":
        Assignments += (
            LHS + str(Jdata["value"]["n"]) + " "
            if Jdata["value"]["_type"] == "Constant"
            else LHS + str(Jdata["value"]["id"] + " ")
        )
    elif Jdata["value"]["_type"] == "BinOp":
        Assignments += LHS + BinaryOpp(Jdata["value"]) + "  "
        
    elif Jdata["value"]["_type"] == "Compare":
        Assignments += LHS + CompareOpp(Jdata["value"]) + "  "
    elif Jdata["value"]["_type"] == "Call":
            print('came to call')
            Assignments += LHS + callhandle(Jdata["value"]) + "  "

       
    return Assignments

#handling lambda assignment ex a+=b
def AugAssignment(Jdata):
    global Assignments
    try:
        LHS = Jdata["target"]["id"]
        Operation=mathOpps(Jdata['op']['_type']) + '='
        if Jdata["value"]["_type"] == "Constant" or Jdata["value"]["_type"] == "Name":
            Assignments += (
                LHS + Operation + str(Jdata["value"]["n"]) + " "
                if Jdata["value"]["_type"] == "Constant"
                else LHS + Operation + str(Jdata["value"]["id"] + " ")
            )
        elif Jdata["value"]["_type"] == "BinOp":
            Assignments += LHS + Operation + BinaryOpp(Jdata["value"]) + " "
    except:
        print('error in AugAssignment')        

#handling node with type if condition
def handleIf(ifdata,connect):
    global conditions
    global Assignments
    global basicBlocks
    global blockNumber
    mainBlock=connect
    branchblock=''
     
    
    if ifdata["_type"] == "If":
        Assignments=''
        blockNumber +=1
        basicBlocks['BB'+str(blockNumber)] = "Branch[" + ifdata["test"]["id"] + "]"
        #links['BB'+str(mainBlock)]=['BB'+str(blockNumber)]
        if links.get('BB'+str(mainBlock)):
            links['BB'+str(mainBlock)].append('BB'+str(blockNumber))
        else:
            links['BB'+str(mainBlock)]=['BB'+str(blockNumber)]
        branchblock=blockNumber
        blockNumber +=1
        branchif=blockNumber
        ifBody = ifdata["body"]
        ifassign=''
        for Jdata in ifBody:
            if Jdata["_type"] == "Assign":
                
                basicBlocks['BB'+str(blockNumber)] = SimpleAssignment(Jdata)
                ifassign=blockNumber
            elif Jdata["_type"] == "AugAssign":
                AugAssignment(Jdata)
            
            elif Jdata["_type"] == "While":
                handleWhile(Jdata)
            elif Jdata["_type"] == "If":
                handleIf(Jdata,ifassign)
            
        
        if links.get('BB'+str(branchblock)):
            
            links['BB'+str(branchblock)].append('BB'+str(branchif))
        else:
            links['BB'+str(branchblock)]=['BB'+str(branchif)]
        
        
        
    
    if ifdata["orelse"]:
        ifBody = ifdata["orelse"]
        Assignments=''
        blockNumber +=1
        branchif=blockNumber
        isiffalse=True
        isAssignfalse=True
        for Jdata in ifBody:
           
            if Jdata["_type"] == "If":
                if isAssignfalse:
                    
                    blockNumber -=1
                    print(blockNumber)
                    handleIf(Jdata,branchblock)
                    isiffalse=False
                    
                    
                else:
                    handleIf(Jdata,blockNumber)
                
                
            elif Jdata["_type"] == "Assign":
                basicBlocks['BB'+str(blockNumber)] = SimpleAssignment(Jdata)
                isAssignfalse=False
            elif Jdata["_type"] == "AugAssign":
                AugAssignment(Jdata)
            elif Jdata["_type"] == "While":
                handleWhile(Jdata)
                
            '''
            if Jdata["_type"] == "If":
                handleIf(Jdata,elseassign)    
            '''
        if isiffalse:
            if links.get('BB'+str(branchblock)):
                links['BB'+str(branchblock)].append('BB'+str(branchif))
            else:
                links['BB'+str(branchblock)]=['BB'+str(branchif)]
            

    
    if ifdata["test"]:
        conditions+=handleCompare(ifdata["test"])


        

#handling node with type whiile
def handleWhile(fordata):
    global loop
    global Assignments
    global handleIf
    try:
        if fordata["_type"] == "While":
            ifBody = fordata["body"]
            for Jdata in ifBody:
                if Jdata["_type"] == "Assign":
                    SimpleAssignment(Jdata)
                elif Jdata["_type"] == "AugAssign":
                    AugAssignment(Jdata)
                elif Jdata["_type"] == "If":
                    handleIf(Jdata)
                elif Jdata["_type"] == "While":
                    handleWhile(Jdata)
            

        if fordata["test"]:
            loop+=handleCompare(fordata["test"])
    except:
        print('error in handlewhile')
        


def iteratetree(BB):
    lk=[]
    if links.get(BB):
        ar=links.get(BB)
        
        for word in ar:
            if links.get(word):
                
                lk.extend(iteratetree(word))
                
            else:
                lk.append(word)
        return lk
        

        
            
        
        
    


    
        



#main section to parse each Node recieved from the tree
def MainSection(jsonBody):
    global conditions
    global Assignments
    global basicBlocks
    global blockNumber
    global Assignmentss
    
    for Jdata in jsonBody:
        if Jdata["_type"] == "If":
            ifBlock=blockNumber+1
            handleIf(Jdata,blockNumber)
            leafs=iteratetree('BB'+str(ifBlock))
            blockNumber+=1
            Assignments=''
            basicBlocks['BB'+str(blockNumber)] = 'Exit'
            for word in leafs:
                links[word]=['BB'+str(blockNumber)]


            
            
        elif Jdata["_type"] == "Assign":
            somedata=SimpleAssignment(Jdata)
            
            basicBlocks['BB'+str(blockNumber)] = somedata
            #SimpleAssignment(Jdata)
        elif Jdata["_type"] == "AugAssign":
            basicBlocks['BB'+str(blockNumber)] = AugAssignment(Jdata)
        elif Jdata["_type"] == "While":
            basicBlocks['BB'+str(blockNumber)] = handleWhile(Jdata)
        elif Jdata["_type"] == "FunctionDef":
            basicBlocks['BB'+str(blockNumber)] = MainSection(Jdata['body'])


jsonBody = jsondata["body"]
MainSection(jsonBody)



    
        

    
        
    


dot = Digraph(comment='CFG')


print(basicBlocks)
print(links)


for key in links:
    a=links[key]
    a.sort()
    #a=list(dict.fromkeys(a))
    
    for value in a:
        
        dot.edge(basicBlocks[key], basicBlocks[value])
        



dot.render('CFG.pdf', view=True)  

'''
dot.edge('run', 'intr')
dot.edge('intr', 'runbl')
dot.edge('runbl', 'run')




dot.node('A', 'King Arthur')
dot.node('B', 'Sir Bedevere the Wise')
dot.node('L', 'Sir Lancelot the Brave')

dot.edges(['AB','BL'])
#dot.edge('B', 'L', constraint='false')
'''
#print(dot.source)



'''
print('All The Assignment,Branch,Loop Statements of '+val+' python Program is as below \n')

print("Assignment Statements:")
print(Assignments)

print("Branch Conditions:")
print(conditions)
print("\n")
print("Loop Conditions:")
print(loop)
'''

# print(type(firstindex))

# print(jsondata['body'][1])
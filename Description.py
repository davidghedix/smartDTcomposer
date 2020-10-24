from PDDLUtils import *



class Description:

    def __init__(self,services,capabilities,

                 instances,tasks,

                 atomicTerms,groundAtomicTerms):

        self.services = services

        self.capabilities = capabilities

        self.instances = instances

        self.tasks = tasks

        self.atomicTerms = atomicTerms

        self.groundAtomicTerms = groundAtomicTerms



    def getPDDLDomain(self,domainName,requirements):

        res = "(define" + " " + "(domain" + " " \

              + domainName + ")" + "\n"

        res += getRequirements(requirements)

        res += getTypes(self.instances)

        res += getPredicates(self.atomicTerms)

        res += getActions(self.tasks)

        #res += "(:functions (total-cost))" + "\n"

        res += "\n"

        res += ")"

        return res



    def getPDDLProblem(self,domainName,problemName,goal):

        res = "(define" + " " + "(problem" + " " \

              + problemName + ")" + "\n"

        res += "(:domain" + " " + domainName + ")" + "\n"

        res += getObjects(self.instances, self.tasks)

        res += getInit(self.groundAtomicTerms, self.tasks)

        res += getGoal(goal)

        #res += "(:metric minimize (total-cost))" + "\n"

        res += "\n"

        res += ")"

        return res



    def getGroundedEffect(self, name, inp):

        for t in self.tasks:

            if t.name == name:

                addEff = list(t.addEff)

                added = []



                for a in t.addEff:

                    temp = a.strip().split(":")[1]

                    if temp == "true" or temp == "false":

                        added.append(a)

                i = 0

                for p in t.params:

                    p = p.strip().split(" - ")[1]

                    for a in t.addEff:

                        temp = a.strip().split(":")

                        if p == temp[1]:

                            added.append(temp[0] + ":" + inp[i])

                    i += 1



                added2 = []

                for a in added:

                    if not("." in a):

                        added2.append(a)

                        

                i = 0

                for p in t.params:

                    p = p.strip().split(" - ")[1]

                    for a in added:

                        if "." in a:

                            temp = a.strip().split(".")

                            if p == temp[0]:

                                added2.append(inp[i] + "." + temp[1])

                    i += 1

                    

                delEff = list(t.delEff)

                deleted = []



                for a in t.delEff:

                    temp = a.strip().split(":")[1]

                    if temp == "true" or temp == "false":

                        deleted.append(a)

                i = 0

                for p in t.params:

                    p = p.strip().split(" - ")[1]

                    for a in t.delEff:

                        temp = a.strip().split(":")

                        if p == temp[1]:

                            deleted.append(temp[0] + ":" + inp[i])

                    i += 1



                deleted2 = []

                for a in deleted:

                    if not("." in a):

                        deleted2.append(a)

                        

                i = 0

                for p in t.params:

                    p = p.strip().split(" - ")[1]

                    for a in deleted:

                        if "." in a:

                            temp = a.strip().split(".")

                            if p == temp[0]:

                                deleted2.append(inp[i] + "." + temp[1])

                    i += 1



                return dict(added = added2, deleted = deleted2)

                

                        

class Task:

    def __init__(self, name, params,\

                 posPrec, negPrec, addEff,\

                 delEff,providedBy, capability, cost):

        self.name = name             #"move"

        self.params = params         #["Location - from", "Location - to"]

        self.posPrec = posPrec       #["o.at:from"]

        self.negPrec = negPrec       #["at:to"]

        self.addEff = addEff

        self.delEff = delEff

        self.providedBy = providedBy  # "rb1"

        self.capability = capability  # "movement"

        self.cost = cost



    def getGroundedEffect(self, inp):

        

        addEff = list(self.addEff)

        added = []



        for a in self.addEff:

            temp = a.strip().split(":")[1]

            if temp == "true" or temp == "false":

                added.append(a)

        i = 0

        for p in self.params:

            p = p.strip().split(" - ")[1]

            for a in self.addEff:

                temp = a.strip().split(":")

                if p == temp[1]:

                    added.append(temp[0] + ":" + inp[i])

            i += 1



        added2 = []

        for a in added:

            if not("." in a):

                added2.append(a)

                

        i = 0

        for p in self.params:

            p = p.strip().split(" - ")[1]

            for a in added:

                if "." in a:

                    temp = a.strip().split(".")

                    if p == temp[0]:

                        added2.append(inp[i] + "." + temp[1])

            i += 1

            

        delEff = list(self.delEff)

        deleted = []



        for a in self.delEff:

            temp = a.strip().split(":")[1]

            if temp == "true" or temp == "false":

                deleted.append(a)

        i = 0

        for p in self.params:

            p = p.strip().split(" - ")[1]

            for a in self.delEff:

                temp = a.strip().split(":")

                if p == temp[1]:

                    deleted.append(temp[0] + ":" + inp[i])

            i += 1



        deleted2 = []

        for a in deleted:

            if not("." in a):

                deleted2.append(a)

                

        i = 0

        for p in self.params:

            p = p.strip().split(" - ")[1]

            for a in deleted:

                if "." in a:

                    temp = a.strip().split(".")

                    if p == temp[0]:

                        deleted2.append(inp[i] + "." + temp[1])

            i += 1



        return dict(added = added2, deleted = deleted2)



            



class groundAtomicTerm:

    def __init__(self, name, inp, out):

        self.name = name    #"at"

        self.inp = inp      #"s"

        self.out = out      #"l"



class atomicTerm:

    def __init__(self, name, inp, out):

        self.name = name    #"at"

        self.inp = inp      #"s - Service"

        self.out = out      #"l - Location"



if __name__ == "__main__":

     



    services = ["rb1"]

    capabilities = ["movement"] 

    subclasses = {"Robot":["rb1","rb2"]}

    #####

    name = "move"

    params = ["Object - o", "Location - l"]

    posPrec = []

    negPrec = []

    addEff = ["o.at:l","carries:o","o.movable:true"]

    delEff = ["o.at:l"]

    providedBy = "rb1 - Robot"

    capability = "movement"

    cost = 5

    move = Task(name, params,posPrec,negPrec,addEff,delEff,providedBy,capability,cost)

    print(move.getGroundedEffect(["o1","x"]))

    

    tasks = [move]

    #####

    name = "at"

    inp = "s:Service"

    out = "l:Location"

    at1 = atomicTerm(name,inp,out)

    atomicTerms = [at1]

    #####

    instances = {"Object":["ball","box"]}

    #####

    name = "at"

    inp = "s"

    out = "l"

    at1 = groundAtomicTerm(name,inp,out)

    groundAtomicTerms = [at1]

    #####

    desc = Description(services,capabilities,subclasses,

                       instances,tasks,atomicTerms,

                       groundAtomicTerms)

    print(desc.getPDDLDomain("factory",["strips"]))

    print(desc.getPDDLProblem("factory_p","factory_d",[]))

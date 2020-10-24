def getInit(groundAtomicTerms, tasks):

    res = "(:init \n"

    

    for t in tasks:

        res += "(provides" + " " + \

               t.providedBy + \

               " " + t.capability + ")\n"

        

    for a in groundAtomicTerms:

        if a.out == None:

            continue

        res += "(" + a.name + " " + a.inp + " " + a.out + ")\n"



    #res += "(= (total-cost) 0)" + "\n"

    res += ")\n"

    return res



def getGoal(goal):

    res = "(:goal \n"

    res += "(and \n"

    for a in goal:

        res += "(" + a.name + " " + a.inp + " " + a.out + ")\n"



    res += ")\n"

    res += ")\n"

    return res



def getObjects(instances, tasks):  #{"Object":["ball","box"]}

    res = "(:objects \n"

    

    for k in instances:

        for v in instances[k]:

            res += v + " - " + k + "\n"



    capabilities = []

    for t in tasks:

        if t.capability in capabilities:

            continue

        res += t.capability + " - " + "Capability" + "\n"

        capabilities.append(t.capability)



    services = []

    for t in tasks:

        if t.providedBy in services:

            continue

        res += t.providedBy + " - " + "Service" + "\n"

        services.append(t.providedBy)

        

    res += ")\n"



    return res



def getTypes(instances):

    res = "(:types \nService - Thing\nCapability\n"



    for k in instances:

        if k == "Object":

            res += k + " - " + "Thing" + "\n"

            continue

        res += k + "\n"



    res += ")\n"



    return res

        

def getFormula(f):

    res = ""

    for p in f:

        l = p.strip().split(":")

        if "." in l[0]:

            s = l[0].strip().split(".")

            res += "(" + s[1] +  " " + "?" + s[0] + " " + "?" + l[1] + ")" + " "

            continue

        res += "(" + l[0] +  " " + "?srv" + " " + "?" + l[1] + ")" + " "

    res = res.replace("?true","true")

    res = res.replace("?false","false")

    return res



def getNegativeFormula(f):

    res = ""

    for p in f:

        l = p.strip().split(":")

        if "." in l[0]:

            s = l[0].strip().split(".")

            res += "(not(" + s[1] +  " " + "?" + s[0] + " " + "?" + l[1] + "))" + " "

            continue

        res += "(not(" + l[0] +  " " + "?srv" + " " + "?" + l[1] + "))" + " "

    res = res.replace("?true","true")

    res = res.replace("?false","false")

    return res



def getActions(tasks):

    res = ""

    names = []

    for t in tasks:

        if t.name in names:

            continue

        names.append(t.name)

        

        params = ":parameters (?srv - " + "Service"

        for p in t.params:

            params += " " + "?" + \

                      p.strip().split(" - ")[1] + " - " + \

                      p.strip().split(" - ")[0]

        params += ")\n"

        prec = ":precondition (and (provides ?srv " + t.capability + ")" + " "

        prec += getFormula(t.posPrec)

        prec += getNegativeFormula(t.negPrec)

        prec += ")" + "\n"



        eff = ":effect (and "

        eff += getFormula(t.addEff)

        eff += getNegativeFormula(t.delEff)

        #eff += "(increase (total-cost)" + " " + str(t.cost) + ")"

        eff += ")" + "\n"

        res += "(:action" + " " + t.name + "\n" + params + prec + eff + ")\n"

    return res

      

def getPredicates(atomicTerms):

    res = "(:predicates \n" + \

          "(provides ?srv - Service ?c - Capability) \n"



    names = []

    for a in atomicTerms:

        if a.name in names:

            continue

        names.append(a.name)

        inp = "?" + a.inp.strip().replace(":", " - ")

        out = "?" + a.out.strip().replace(":", " - ")

        s = "(" + a.name + " " + \

            inp + " " + out + ")" + "\n"

        res += s

        

    res += ")\n"

    return res





def getRequirements(requirements):

    res =  "(:requirements"

    for r in requirements:

        res += " " + ":" + r

    res += ")\n"

    return res     

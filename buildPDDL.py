from Description import *

from ThingsAPI import *

import config

import context



def buildPDDL():

    things = searchThings(config.ThingsAPI["namespace"])



    services = [] 

    capabilities = [] 

    instances = context.instances 

    tasks = [] 

    atomicTerms = context.atomicTerms 

    groundAtomicTerms = context.groundAtomicTerms



    goal = context.goal

    requirements = context.requirements



    for t in things:

        

        s = t["thingId"].split(":")[1]

        services.append(s)

        



        features = t["features"]

        

        for f in features:

            feature = features[f]

            props = features[f]["properties"]

            featureType = props["type"]

            

            if featureType == "state":

                 domain = props["domain"]

                 valueType = props["value"]["type"]

                 a = atomicTerm(f,

                        domain[0].lower()+":"+domain,

                        valueType[0].lower()+":"+valueType,

                        )

                 atomicTerms.append(a)

                 g = groundAtomicTerm(f,s,

                        props["value"]["current"]

                        )

                 groundAtomicTerms.append(g)        

                                

            elif featureType == "operation":

                capabilities.append(f)

                name = props["command"]

                print(t["thingId"])

                cost = props["cost"]

                params = props["parameters"]

                

                posPrec = []

                negPrec = []

                addEff = []

                delEff = []

                try:

                    posPrec = props["requirements"]["positive"]

                except KeyError:

                    pass

                try:

                    negPrec = props["requirements"]["negative"]

                except KeyError:

                    pass

                try:

                    addEff = props["effects"]["added"]

                except KeyError:

                    pass

                try:

                    delEff = props["effects"]["deleted"]

                except KeyError:

                    pass



                providedBy = s 

                

                task = Task(name,

                            params,

                            posPrec,

                            negPrec,

                            addEff,

                            delEff,

                            providedBy,

                            f,

                            cost

                            )

                tasks.append(task)

                

    desc = Description(services,capabilities,

                       instances,tasks,atomicTerms,

                       groundAtomicTerms)



    domainFile = open(config.PDDL["domainFile"], 'w+')

    domainFile.write(desc.getPDDLDomain(config.PDDL["domainName"],requirements))

    domainFile.close()



    problemFile = open(config.PDDL["problemFile"], 'w+')

    problemFile.write(desc.getPDDLProblem(config.PDDL["domainName"],config.PDDL["problemName"],goal))

    problemFile.close()



    return desc

    

if __name__ == "__main__":

    buildPDDL()             

    

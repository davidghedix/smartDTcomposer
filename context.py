from Description import *

#Sample context data

instances = {"Object":["o1","o2"],\

             "Location":["l00","l01","l02","l03","l04","l05","l06",\

                         "l10","l11","l12","l13","l14","l15","l16",\

                         "l20","l21","l22","l23","l24","l25","l26",\

                         "l30","l31","l32","l33","l34","l35","l36"],

             "Boolean":["true","false"]}

atomicTerms = [atomicTerm("heated","o - Object", "b - Boolean"),

               atomicTerm("processed","o - Object", "b - Boolean"),

               atomicTerm("cooled","o - Object", "b - Boolean"),

               atomicTerm("movable","o - Object", "b - Boolean")]

groundAtomicTerms = [groundAtomicTerm("at","o1","l00"),

                     groundAtomicTerm("at","o2","l00"),

                     groundAtomicTerm("movable","o1","true"),

                     groundAtomicTerm("movable","o2","true")]



requirements = ["strips","equality","typing"]



goal = [groundAtomicTerm("at","o1","l36"),groundAtomicTerm("at","o2","l36"),

        groundAtomicTerm("cooled","o1","true"),

        groundAtomicTerm("cooled","o2","true")]

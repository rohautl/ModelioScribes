def indent(nb, character=' '):
    return character*nb


if len(selectedElements)==0:
    print "Vous n'avez pas d'element selectionne"

else:
    for element in selectedElements:
        if isinstance(element, Class):
            print "Classes : \n"
            print "Le concept de %s est pertinent." % (element.name)
            print

            # Attributs
            attributes = element.ownedAttribute
            for attribute in attributes:
                print indent(4) + "Le %s de %s est un %s" % (attribute.name, element.name, attribute.type.name)
            print

            # Methodes
            methods = element.getOwnedOperation()
            if len(methods) > 0:
                print "Methodes de la classe : \n"
                print indent(4) + "Pour un %s donne il est possible de :" % (element.name)
                for method in methods:
                    string = "- %s" % (method.name)
                    parameters = method.getIO()
                    for parameter in parameters:
                        string = string + " avec un(e) %s" % (parameter.name)
                    print indent(8) + string + "."
                print


            # Associations
            associations = element.compositionChildren
            for children in associations:
                if children.getMClass().toString() == 'AssociationEnd SmClass' and children.association:
                    print "Association : \n"
                    print indent(4) + "Un(e) %s %s un ou des %s." % (element.name, children.association.name, children.target.name)
                    print indent(4) + "L'element %s de %s est un  %s." % (children.name, children.association.name, children.target.name)
                    print indent(4) + "L'element %s de %s est un  %s." % (children.opposite.name, children.association.name, element.name)
                    # Cardinalite
                    maxi = children.multiplicityMax
                    mini = children.multiplicityMin
                    if mini == maxi:
                        print indent(8) + "Un(e) %s a toujours %s %s." % (element.name, mini, children.name)
                    else:
                        if mini == "0":
                            print indent(8) + "Un(e) %s peut ne pas avoir de %s." % (element.name, children.name)
                        else:
                            print indent(8) + "Un(e) %s doit avoir au moins %s %s." % (element.name, mini, children.name)
                        if maxi == "*":
                            print indent(8) + "Un(e) %s peut avoir plusieurs %s." % (element.name, children.name)
                        else:
                            print indent(8) + "Un(e) %s peut avoir au plus %s %s." % (element.name, maxi, children.name)
                    print indent(8) + "Tous les %s d'un(e) %s sont des %s." % (children.name, element.name, children.target.name)

                    maxi = children.opposite.multiplicityMax
                    mini = children.opposite.multiplicityMin
                    if mini == maxi:
                        print indent(8) + "Un(e) %s a toujours %s %s." % (children.target.name, mini, children.opposite.name)
                    else:
                        if mini == "0":
                            print indent(8) + "Un(e) %s peut ne pas avoir de %s." % (children.target.name, children.opposite.name)
                        else:
                            print indent(8) + "Un(e) %s doit avoir au moins %s %s." % (children.target.name, mini, children.opposite.name)
                        if maxi == "*":
                            print indent(8) + "Un(e) %s peut avoir plusieurs %s." % (children.target.name, children.opposite.name)
                        else:
                            print indent(8) + "Un(e) %s peut avoir au plus %s %s." % (children.target.name, maxi, children.opposite.name)
                    print indent(8) + "Tous les %s d'un(e) %s sont des %s." % (children.opposite.name, children.target.name, element.name)
                    print

            # Heritage

            parents = element.parent
            if len(parents) > 0:
                print "Heritage :\n"
                print indent(4) + "%s est aussi un(e) :" % (element.name)
            for parent in parents:
                print indent(8) + "- un(e) %s." % (parent.superType.name)
            print
            

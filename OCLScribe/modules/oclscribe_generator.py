#===================================================================================
# oclscribe_generator
#
# This module generates USEOCL text for the following uml constructs:
#  - Enumeration
#  - Class
#  - AssociationClass
#  - Attribute
#  - Operation
#  - TypedElement
#  - Association
#  - NAryAssciation
#  - Constraint
#  - CommentClass
#  - CommentAttribute
# In each case a function "compileXXX" is provided
#===================================================================================



#-----------------------------------------------------------------------------------
#   Module Interface
#-----------------------------------------------------------------------------------
# Exported symbols for this module. Only these symbols are visible from outside.
# Other symbols are symbols that can be used localy within this module.
__all__ = [
  "compileEnumerations",
  "compileClasses",
  "compileAssociations",
  "compileConstraints"
]



#-----------------------------------------------------------------------------------
#   Module Implementation
#-----------------------------------------------------------------------------------

from org.modelio.metamodel.uml.statik import *
from org.modelio.metamodel.uml.infrastructure import *
from org.modelio.metamodel.mda import Project

def noSpaceNames(name):
	return  "".join(name.split())

def completeName(element):
	projectElement = element
	completeName = element.getName()
	while not isinstance(projectElement, Project):
		projectElement = projectElement.getCompositionOwner()
		completeName = projectElement.getName() + "." + completeName
	return completeName[len(projectElement.getName())+1:len(completeName)]

def doesNaryAssociationExist(listNAssociations, listNAssociation):
	existsNum = 0
	for listN in listNAssociations:
		if(len(listN) == len(listNAssociation)):
			for element in listNAssociation:
				for comparedElement in listN:
					if (element == comparedElement):
						existsNum = existsNum +1
	if(existsNum == len(listNAssociation)):
		return 1			
	else:
		return 0
    
    
#-----------------------------------
#   XXX Enumeration
#-----------------------------------

def compileEnumeration(enumerationElement):
	returnEnum = "<i><b>enum </b></i>" + noSpaceNames(completeName(enumerationElement)) + "{"
	if (enumerationElement.getCompositionChildren().size()>0):
		for literal in (enumerationElement.getCompositionChildren()):
			if (isinstance(literal, EnumerationLiteral)):
				returnEnum = returnEnum + noSpaceNames(literal.getName()) + ", "
		returnEnum = returnEnum[0:len(returnEnum)-2] + "}<br>"
	else:
		returnEnum = returnEnum + "}<br>"
	return returnEnum

#-----------------------------------
#   XXX Class
#-----------------------------------
 
def compileClass(classElement):
	if (classElement.isIsAbstract()):
		returnClass = "<i><b>abstract class </b></i>" + noSpaceNames(completeName(classElement))
	else:
		returnClass = "<i><b>class </b></i>" + noSpaceNames(completeName(classElement))
	if (classElement.getParent().size()>0):
		returnClass = returnClass + " < "
		for parent in (classElement.getParent()):
			if (isinstance(parent, Generalization)):
				returnClass = returnClass + completeName(parent.getSuperType()) + ", "
		returnClass = returnClass[0:len(returnClass)-2] 
	if (classElement.getOwnedAttribute().size()>0):
		returnClass = returnClass + "<br><i class=\"tab2\"><b>attributes</b></i>"
		for attribute in (classElement.getOwnedAttribute()):
			returnClass = returnClass + compileAttribute(attribute) 
	if (classElement.getOwnedOperation().size()>0):
		returnClass = returnClass + "<br><i class=\"tab2\"><b>operations</b></i>"
		for operation in (classElement.getOwnedOperation()):
			returnClass = returnClass + compileOperation(operation)
	if (classElement.getConstraintDefinition().size()>0):
		isItInvariantConstraint = 0
		for constraint in (classElement.getConstraintDefinition()):
			if (constraint.getExtension().size() > 0):
				if (constraint.getExtension().get(0).getName() == "invariant"):
					if (isItInvariantConstraint == 0):
						returnClass = returnClass + "<br><i class=\"tab2\"><b>constraints</b></i>"
					isItInvariantConstraint = 1
					returnClass = returnClass + "<br><i class=\"tab3\">inv </i>" + constraint.getBody()
	returnClass = returnClass + "<br><i class =\"tab\"><b>end</b></i><br>"
	return returnClass

  
#-----------------------------------
#   XXX AssociationClass
#-----------------------------------  

def compileAssociationClass(classElement):
	if (classElement.isIsAbstract()):
		returnClass = "<i><b>abstract class </b></i>" + noSpaceNames(completeName(classElement))
	else:
		returnClass = "<i><b>class </b></i>" + noSpaceNames(completeName(classElement))
	if (classElement.getParent().size()>0):
		returnClass = returnClass + " < "
		for parent in (classElement.getParent()):
			if (isinstance(parent, Generalization)):
				returnClass = returnClass + parent.getSuperType().getName() + ", "
		returnClass = returnClass[0:len(returnClass)-2] 
	if(classElement.getLinkToAssociation().getNaryAssociationPart() == None):
		firstEnd = None
		for ends in classElement.getLinkToAssociation().getAssociationPart().getEnd():
			if (ends.getSource() != None):
				firstEnd = ends
		if (firstEnd != None):
			returnClass = returnClass + "<br><i class=\"tab2\"><b>between</b></i><br>"
			returnClass = returnClass + "<span class=\"tab3\">" +completeName(firstEnd.getSource()) + "[" + firstEnd.getOpposite().getMultiplicityMin() + ".."+ firstEnd.getOpposite().getMultiplicityMax()+ "] "
			if(firstEnd.getOpposite().getName() != ""):
				returnClass = returnClass + "<i><b>role</b></i> " + firstEnd.getOpposite().getName()
			if(firstEnd.getOpposite().isIsOrdered()):
				returnClass = returnClass + " <i><b>ordered</b></i> "
			returnClass = returnClass + "<br><span class=\"tab3\">" +completeName(firstEnd.getOpposite().getOwner()) + "[" + firstEnd.getMultiplicityMin() + ".."+ firstEnd.getMultiplicityMax()+ "] "
			if(firstEnd.getName() != ""):
				returnClass = returnClass + "<i><b>role</b></i> " + firstEnd.getName()
			if(firstEnd.isIsOrdered()):
				returnClass = returnClass + " <i><b>ordered</b></i>"
	else:
		returnClass = returnClass + "<br><i class=\"tab2\"><b>between</b></i>"
		for end in classElement.getLinkToAssociation().getNaryAssociationPart().getNaryEnd():
			returnClass = returnClass + "<br><span class=\"tab3\">" +completeName(end.getOwner()) + "[" + end.getMultiplicityMin() + ".."+ end.getMultiplicityMax()+ "] "
			if(end.getName() != ""):
				returnClass = returnClass + "<i><b>role</b></i> " + end.getName()
			if(end.isIsOrdered()):
				returnClass = returnClass + " <i><b>ordered</b></i> "		
	if (classElement.getOwnedAttribute().size()>0):
		returnClass = returnClass + "<br><i class=\"tab2\"><b>attributes</b></i>"
		for attribute in (classElement.getOwnedAttribute()):
			returnClass = returnClass + compileAttribute(attribute) 
	if (classElement.getOwnedOperation().size()>0):
		returnClass = returnClass + "<br><i class=\"tab2\"><b>operations</b></i>"
		for operation in (classElement.getOwnedOperation()):
			returnClass = returnClass + compileOperation(operation)
	if (classElement.getConstraintDefinition().size()>0):
		isItInvariantConstraint = 0
		for constraint in (classElement.getConstraintDefinition()):
			if (constraint.getExtension().size() > 0):
				if (constraint.getExtension().get(0).getName() == "invariant"):
					if (isItInvariantConstraint == 0):
						returnClass = returnClass + "<br><i class=\"tab2\"><b>constraints</b></i>"
					isItInvariantConstraint = 1
					returnClass = returnClass + "<br><i class=\"tab3\">inv </i>" + constraint.getBody()
	returnClass = returnClass + "<br><i class =\"tab\"><b>end</b></i><br>"
	return returnClass

  
#-----------------------------------
#   XXX Attribute
#-----------------------------------    
def compileAttribute(attributeElement):
	returnAttribute = "<br>"	
	for classchildren in (attributeElement.getCompositionChildren()):
			if(isinstance(classchildren, Note) and classchildren.getExtension() != None and classchildren.getExtension().size() ==0):
				returnAttribute = returnAttribute  + compileCommentAttribute(classchildren) + "</br>"	
	return returnAttribute + "<span class=\"tab3\">"+attributeElement.getName()+" : "+compileType(attributeElement) + "</span>"

  
#-----------------------------------
#   XXX Operation
#-----------------------------------    	
def compileOperation(operationElement):
	returnOperation = "<br>"
	for classchildren in (operationElement.getCompositionChildren()):
			if(isinstance(classchildren, Note) and classchildren.getExtension() != None and classchildren.getExtension().size() ==0):
				returnOperation = returnOperation  + compileCommentAttribute(classchildren) + "</br>"
	returnOperation = returnOperation + "<span class=\"tab3\">" + operationElement.getName()+ "("
	if (operationElement.getIO().size()>0):
		for inParam in (operationElement.getIO()):
			if (isinstance(inParam, Parameter)):
				returnOperation = returnOperation + noSpaceNames(inParam.getName()) + " : " +compileType(inParam) + ", "
		returnOperation = returnOperation[0:len(returnOperation)-2] 
	returnOperation = returnOperation + ")"
	if (operationElement.getReturn()):
		if (isinstance(operationElement.getReturn(), Parameter)):
			returnOperation = returnOperation + " : " +  compileType(operationElement.getReturn())
	if (operationElement.getConstraintDefinition().size()>0):
		for constraint in (operationElement.getConstraintDefinition()):
			if (constraint.getExtension().size() > 0):
				if (constraint.getExtension().get(0).getName() == "precondition"):
					returnOperation = returnOperation + "<br><i class=\"tab4\">pre:</i> " + constraint.getBody()
				if (constraint.getExtension().get(0).getName() == "postcondition"):
					returnOperation = returnOperation + "<br><i class=\"tab4\">post:</i> " + constraint.getBody()
	return returnOperation + "</span>"

  
#-----------------------------------
#   XXX TypedElement
#-----------------------------------    
def compileType (typedElement):
	if (typedElement.getMultiplicityMin() != typedElement.getMultiplicityMax()):
		if(typedElement.isIsOrdered() and typedElement.isIsUnique()):
			returnType ="Set(Sequence(" + noSpaceNames(typedElement.getType().getName()) + "))"
		elif (typedElement.isIsOrdered()):
			returnType ="Sequence(" + noSpaceNames(typedElement.getType().getName()) + ")"
		elif ( typedElement.isIsUnique()):
			returnType ="Set(" + noSpaceNames(typedElement.getType().getName()) + ")"
		else :
			returnType ="Bag(" + noSpaceNames(typedElement.getType().getName()) + ")"
	else:
		returnType = noSpaceNames(typedElement.getType().getName())
	return returnType


#-----------------------------------
#   XXX Association
#-----------------------------------  
def compileAssociation (associationEndElement):
	returnAssociation = ""
	isItValid = 0
	if(associationEndElement.getAggregation().getName() == "KindIsAssociation"):
		returnAssociation = returnAssociation + "<i><b>association </b></i>"
		isItValid = 1
	elif(associationEndElement.getAggregation().getName() == "KindIsComposition"):
		returnAssociation = returnAssociation + "<i><b>composition </b></i>"
		isItValid = 1
	elif(associationEndElement.getAggregation().getName() == "KindIsAggregation"):
		returnAssociation = returnAssociation + "<i><b>aggregation </b></i>"
		isItValid = 1
	if (isItValid == 1):
		returnAssociation = returnAssociation +associationEndElement.getAssociation().getName() + "<i><b> between</b></i><br>"
		returnAssociation = returnAssociation + "<span class=\"tab2\">" +completeName(associationEndElement.getSource()) + "[" + associationEndElement.getOpposite().getMultiplicityMin() + ".."+ associationEndElement.getOpposite().getMultiplicityMax()+ "] "
		if(associationEndElement.getOpposite().getName() != ""):
			returnAssociation = returnAssociation + "<i><b>role</b></i> " + associationEndElement.getOpposite().getName()
		if(associationEndElement.getOpposite().isIsOrdered()):
			returnAssociation = returnAssociation + " <i><b>ordered</b></i> "
		returnAssociation = returnAssociation + "<br><span class=\"tab2\">" +completeName(associationEndElement.getOpposite().getOwner()) + "[" + associationEndElement.getMultiplicityMin() + ".."+ associationEndElement.getMultiplicityMax()+ "] "
		if(associationEndElement.getName() != ""):
			returnAssociation = returnAssociation + "<i><b>role</b></i> " + associationEndElement.getName()
		if(associationEndElement.isIsOrdered()):
			returnAssociation = returnAssociation + " <i><b>ordered</b></i> "
		returnAssociation = returnAssociation + "<br><i class =\"tab\"><b>end</b></i><br></span>"
	return returnAssociation
	
  
#-----------------------------------
#   XXX NAryAssciation
#-----------------------------------  
def compileNAryAssociation (naryEnd):
	returnNAryAssociation = "<i><b>association </b></i>"
	returnNAryAssociation = returnNAryAssociation +naryEnd.getNaryAssociation().getName() + "<i><b> between</b></i>"
	for end in naryEnd.getNaryAssociation().getNaryEnd():
		returnNAryAssociation = returnNAryAssociation + "<br><span class=\"tab2\">" +completeName(end.getOwner()) + "[" + end.getMultiplicityMin() + ".."+ end.getMultiplicityMax()+ "] "
		if(end.getName() != ""):
			returnNAryAssociation = returnNAryAssociation + "<i><b>role</b></i> " + end.getName()
		if(end.isIsOrdered()):
			returnNAryAssociation = returnNAryAssociation + " <i><b>ordered</b></i> "
	returnNAryAssociation = returnNAryAssociation + "<br><i class =\"tab\"><b>end</b></i><br></span>"
	return returnNAryAssociation


#-----------------------------------
#   XXX Constraint
#-----------------------------------  
def compileConstraint(constraintElement):
	returnConstraint = ""
	i = 0
	while i < len( constraintElement.getContent()) :
		if(constraintElement.getContent()[i] == "\n"):
   			returnConstraint = returnConstraint + "<i>"+ constraintElement.getContent()[i] +"</i></br>"
   		else:
   			if( i>0 and  constraintElement.getContent()[i-1] == "\n"):
   				returnConstraint = returnConstraint + "<i class =\"tab2\">"+ constraintElement.getContent()[i] +"</i>"
   			elif (i == 0) :
   				returnConstraint = returnConstraint + "<i class =\"tab2\">"+ constraintElement.getContent()[i] +"</i>"
   			else :
   				returnConstraint = returnConstraint + "<i>"+ constraintElement.getContent()[i] +"</i>"
    		i += 1
	return returnConstraint + "</br>"

#-----------------------------------
#   XXX CommentClass
#-----------------------------------  
def compileCommentClass(commentElement):
	returnComment = ""
	i = 0
	while i < len( commentElement.getContent()) :
		if(commentElement.getContent()[i] == "\n"):
   			returnComment = returnComment + "<i>"+ commentElement.getContent()[i] +"</i></br>"
   		else:
   			if( i>0 and  commentElement.getContent()[i-1] == "\n"):
   				returnComment = returnComment + "<i class =\"tab\">--"+ commentElement.getContent()[i] +"</i>"
   			elif (i == 0) :
   				returnComment = returnComment + "<i class =\"tab\">--"+ commentElement.getContent()[i] +"</i>"
   			else :
   				returnComment = returnComment + "<i>"+ commentElement.getContent()[i] +"</i>"
    		i += 1
	return returnComment

  
#-----------------------------------
#   XXX CommentAttribute
#-----------------------------------    
def compileCommentAttribute(commentElement):
	returnComment = ""
	i = 0
	words = 0
	while i < len( commentElement.getContent()) :
		if(commentElement.getContent()[i] == "\n"):
   			returnComment = returnComment + "<i>"+ commentElement.getContent()[i] +"</i></br>"
   		else:
   			if( i>0 and  commentElement.getContent()[i-1] == "\n"):
   				returnComment = returnComment + "<i class =\"tab3\">--"+ commentElement.getContent()[i] +"</i>"
   			elif (i == 0) :
   				returnComment = returnComment + "<i class =\"tab3\">--"+ commentElement.getContent()[i] +"</i>"
   			else :
   				returnComment = returnComment + "<i>"+ commentElement.getContent()[i] +"</i>"
    		i += 1
	return returnComment

  
  
  
  
  
#-----------------------------------------------------------------------------------
#   Main functions called from client modules
#-----------------------------------------------------------------------------------
  
  
#-----------------------------------
#   XXX Enumerations
#-----------------------------------  
def compileEnumerations(enumerationElements):
	returnEnumerations = ""
	if (isinstance(enumerationElements, Package)):
		for children in (enumerationElements.getCompositionChildren()):
			returnEnumerations = returnEnumerations  + compileEnumerations(children)
	elif (isinstance(enumerationElements, Enumeration)):
		returnEnumerations = returnEnumerations + "<span class=\"tab\">" + compileEnumeration(enumerationElements) + "</span><br>"
	return returnEnumerations
  
#-----------------------------------
#   XXX Classes
#-----------------------------------  
def compileClasses(classElements):
	returnClasses = ""
	if (isinstance(classElements, Package)):
		for children in (classElements.getCompositionChildren()):
			returnClasses = returnClasses  + compileClasses(children)
	elif (isinstance(classElements, Class)):
		for classchildren in (classElements.getCompositionChildren()):
			if(isinstance(classchildren, Note) and classchildren.getExtension() != None and classchildren.getExtension().size() ==0):
				returnClasses = returnClasses  + compileCommentClass(classchildren) + "</br>"				
		if(classElements.getLinkToAssociation() == None):
			returnClasses = returnClasses + "<span class=\"tab\">" + compileClass(classElements)+ "</span><br>"
		else:
			returnClasses = returnClasses + "<span class=\"tab\">" + compileAssociationClass(classElements)+ "</span><br>"
	return returnClasses

#-----------------------------------
#   XXX Associations
#-----------------------------------  
def compileAssociations(associationElements, nAssociations_list, associationList):
	returnAssociations = ""
	if (isinstance(associationElements, Package)):
		for children in (associationElements.getCompositionChildren()):
			returnAssociations = returnAssociations  + compileAssociations(children, nAssociations_list, associationList)
	elif (isinstance(associationElements, Class) or isinstance(associationElements, Interface)):
		for children in (associationElements.getCompositionChildren()):
			if (isinstance(children, AssociationEnd) and (children.getAssociation() != None)):
				listAssociation = []
				listAssociation.append(children.getAssociation().getEnd().get(0))
				listAssociation.append(children.getAssociation().getEnd().get(1))
				listAssociation.append(children.getAssociation().getName())
				if (doesNaryAssociationExist(associationList,listAssociation) == 0):
					associationList.insert(0,listAssociation)
					returnAssociations = returnAssociations +"<span class=\"tab\">" + compileAssociation(children)+ "</span><br>"
		if(associationElements.getOwnedNaryEnd() != None):
			for naryEnd in (associationElements.getOwnedNaryEnd()):
				listNAssociation = []
				for end in naryEnd.getNaryAssociation().getNaryEnd():
					listNAssociation.append(end.getOwner().getName())
				if (doesNaryAssociationExist(nAssociations_list,listNAssociation) == 0):
					nAssociations_list.insert(0,listNAssociation)
					returnAssociations = returnAssociations +"<span class=\"tab\">" + compileNAryAssociation(naryEnd)+ "</span><br>"
	return returnAssociations

#-----------------------------------
#   XXX Constraints
#-----------------------------------  
def compileConstraints(constraintElements):
	returnConstraints = ""
	if (isinstance(constraintElements, Package)):
		for children in (constraintElements.getCompositionChildren()):
			returnConstraints = returnConstraints  + compileConstraints(children)
	elif (isinstance(constraintElements, Class)):
		classContextSet = 0
		for classchildren in (constraintElements.getCompositionChildren()):
			if(isinstance(classchildren, Note) and classchildren.getExtension() != None and classchildren.getExtension().size() !=0 and classchildren.getExtension().get(0).getName() == "Invariant" ):
				if (classContextSet == 0):
					returnConstraints = returnConstraints  + "<i class =\"tab\"><b>context </b></i>" + completeName(classchildren.getSubject()) + "</br>"
					classContextSet = 1
				returnConstraints = returnConstraints  + compileConstraint(classchildren) + "</br>"
			if(isinstance(classchildren, Operation)):
				operationContextSet = 0
				for operationchildren in (classchildren.getCompositionChildren()):
					if(isinstance(operationchildren, Note) and operationchildren.getExtension() != None and operationchildren.getExtension().size() !=0):
						if( operationchildren.getExtension().get(0).getName() == "Postcondition" or operationchildren.getExtension().get(0).getName() == "Precondition" ):
							if (operationContextSet == 0):
								returnOperation =  classchildren.getName()+ "("
								if (classchildren.getIO().size()>0):
									for inParam in (classchildren.getIO()):
										if (isinstance(inParam, Parameter)):
											returnOperation = returnOperation + noSpaceNames(inParam.getName()) + " : " +compileType(inParam) + ", "
									returnOperation = returnOperation[0:len(returnOperation)-2] 
								returnOperation = returnOperation + ")"
								if (classchildren.getReturn()):
									if (isinstance(classchildren.getReturn(), Parameter)):
										returnOperation = returnOperation + " : " +  compileType(classchildren.getReturn())
								returnConstraints = returnConstraints  + "<i class =\"tab\"><b>context </b></i>" + completeName(constraintElements) + " :: "+returnOperation+"</br>"
								operationContextSet = 1
							returnConstraints = returnConstraints  + compileConstraint(operationchildren) + "</br>"
	return returnConstraints
  
print "module generator loaded from",__file__
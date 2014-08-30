from ooss import OOSSSchema,OOSSTable,OOSSColumn
from org.modelio.metamodel.uml.statik import Class,Enumeration,AggregationKind

def macro_oossmapper(scribe):
  print "launching the OOSS mapper"
  print "Select a package containing classes to avoid failure of the macro"
  root = scribe.selectedElements[0]   # TODO provide a meaningfull element here
  schema = OOSSSchema("CyberHotel","schema",root,scribe.selectedElements)
  for p in scribe.selectedElements:
    for c in classes(p):
      class2tables(schema,c)
  print str(schema)

def classes(package):
  return package.getOwnedElement(Class)


#------ class to table level -----------------------------  

def leafClass2StandardClassTable(schema,classe):
  tableName = className2TableName(classe.getName())
  table = OOSSTable(schema,tableName,"standardClassTable",classe)
  class2OidColumn(table,classe)
  classFeatures2columns(table,classe)

def concreteSuperclass2DirectAndUnionClassTables(schema,classe):
  # create a direct table to store direct instances
  tableName = className2TableName(classe.getName(),direct=True)
  table = OOSSTable(schema,tableName,"directClassTable",classe)
  class2OidColumn(table,classe)
  classFeatures2columns(table,classe)
  # create an union table to gather together all instances
  tableName = className2TableName(classe.getName())
  subtables = [ className2TableName(sc.getName()) for sc in subclasses(classe) ]
  table = OOSSTable(schema,tableName,"unionClassTable",classe,parameters=[','.join(subtables)])
  class2OidColumn(table,classe,"unionKeyColumn")
  classFeatures2columns(table,classe,"unionColumn")

def abstractSuperclass2UnionClassTables(schema,classe):
  tableName = className2TableName(classe.getName())
  subtables = [ className2TableName(sc.getName()) for sc in subclasses(classe) ]
  table = OOSSTable(schema,tableName,"unionClassTable",classe,parameters=[','.join(subtables)])
  class2OidColumn(table,classe,"unionKeyColumn")
  classFeatures2columns(table,classe)

def classAssociation2ClassAssociationTable(schema,classe):
  tableName = className2TableName(classe.getName())
  table = OOSSTable(schema,tableName,"classAssociationTable",classe)
  class2OidColumn(table,classe)
  (source,target) = endsOfClassAssociation(classe)
  # TODO we should add here a column [[1..1] for source and for target
  classFeatures2columns(table,classe)

def endsOfClassAssociation(classassociation):
  ends = classassociation.getLinkToAssociation().getAssociationPart().getEnd()
  return (ends[0], ends[1])
  
def class2tables(schema,classe):
  if not isClassAssociation(classe):
    if not isSuperclass(classe):
      if not classe.isIsAbstract():
        leafClass2StandardClassTable(schema,classe)
      else:
        pass   # ignore abstract leaf class as they will have no instance
    else: # superclasses
      if not classe.isIsAbstract():
        concreteSuperclass2DirectAndUnionClassTables(schema,classe)
      else:
        abstractSuperclass2UnionClassTables(schema,classe)
  else: # class association
    classAssociation2ClassAssociationTable(schema, classe)    

   
def className2TableName(name,direct=False):
  return "Les"+name+"s"+("Seulement" if direct else "")
  
  
#------ feature to column level -----------------------------  
def class2OidColumn(table,classe,columnKind="keyColumn"):
  return OOSSColumn(table,"oid",columnKind,classe,parameters=["id","[1]"])
  
  
def classFeatures2columns(table,classe,colkindoverload=None):
  for a in classe.getOwnedAttribute():
    attribute2Columns(table,a,colkindoverload)
  for ae in associationEnds(classe):
    associationEnd2Column(table,ae,colkindoverload)
  
def attribute2Columns(table,attribute,colkindoverload=None):
  at = attribute.getType()
  if isEnumerationType(at):
    coltype = enumerationType(at)
    colkind = "enumerationColumn"
  else:
    coltype = at.getName()
    colkind = coltype+"Column"
  if colkindoverload is not None:
    colkind = colkindoverload
  card = cardinalityString(attribute) 
  column = OOSSColumn(table,attribute.getName(),colkind,attribute,parameters=[coltype,card])

def associationEnd2Column(table,end,colkindoverload=None):
  kindmap = {"N1":"foreignKeyColumn", 
             "1N":"backKeysColumn",
             "11":"foreignKeyColumn",
             "NN":"foreignKeyColumn"}
  colkind = colkindoverload if colkindoverload is not None else kindmap[associationEndKind(end)]
  card = cardinalityString(end)
  coltype = end.getTarget().getName()
  pos = associationEndPosition(end)
  column = OOSSColumn(table,end.getName(),colkind,end,parameters=[coltype,card,pos])
  # print ("composition " if  isCompositionEnd(end) else "") \
  #          + ("composite " if isOppositeCompositionEnd(end) else "") \

    
def enumerationType(e):
  return e.getName()+"("+",".join([v.getName() for v in e.getValue()])+")"


         

  
  
  
#------ source metamodel helper --------------
def isSuperclass(classe):
  return len(classe.getSpecialization()) >= 1
  
def subclasses(classe):
  return [s.getSubType() for s in classe.getSpecialization()]

def isClassAssociation(classe):
  return classe.getLinkToAssociation() is not None

def isClassAssociationEnd(classe):
  return classe.getAssociation().getLinkToClass() is not None
  
def isCompositionEnd(associationEnd):
  return associationEnd.getAggregation()==AggregationKind.KINDISCOMPOSITION
 
def isOppositeCompositionEnd(associationEnd):
  return isCompositionEnd(associationEnd.getOppositeOwner())
    
def isNAssociationEnd(associationEnd):
  return associationEnd.getMultiplicityMax() != "1"
  
def associationEndKind(associationEnd):
  target = "N" if isNAssociationEnd(associationEnd) else "1"
  source = "N" if isNAssociationEnd(associationEnd.getOpposite()) else "1"
  return source+target
  
def associationEndPosition(associationEnd):
  if associationEnd.getAssociation().getEnd()[0]==associationEnd:
    return "target"
  else:
    return "source"

def associationEnds(classe,endKindFilter=None,classAssociationFilter=None,backward=False):
  ends = classe.getOwnedEnd() if not backward else classe.getTargetingEnd()
  return \
    [ end for end in ends \
      if    (end.getAssociation() is not None)
        and (endKindFilter is None or associationEndKind(end)==endKindFilter) \
        and (classAssociationFilter is None or isClassAssociationEnd(end)==classAssociationFilter) ]
  
def isEnumerationType(t):
   return isinstance(t,Enumeration)
  
def cardinalityString(feature):
  min = feature.getMultiplicityMin()
  max = feature.getMultiplicityMax()
  if (min==max):
    return "["+str(min)+"]"
  else:
    return "["+min+".."+max+"]"
    
    
    
print "oossmapper module loaded"



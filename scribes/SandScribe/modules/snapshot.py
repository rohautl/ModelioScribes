

# return identifiers like a1, a2, ... cake1, cake2, ...
# The number is increased each time the given prefix is used
NB_INSTANCE_PER_ID = {}
def nextId(prefix):
  if prefix in NB_INSTANCE_PER_ID:
    n = NB_INSTANCE_PER_ID[prefix]+1
  else:
    n = 1
  NB_INSTANCE_PER_ID[prefix] = n
  return prefix+str(n)
  
def lowerFirst(name):
  return name[0].lower()+name[1:]

def attributeNamed(classe,name):
  for attribute in classe.getOwnedAttribute():
    if attribute.getName() == name:
      return attribute
  return None
  
#--------- instance and slots ----------------------

#
def createInstance(classe,name=None,package=None):
  # define in which package the instance will be created
  if package is None:
    package = classe.getOwner()
  # define a name for the instance
  if name is None:
    name = nextId(lowerFirst(classe.getName()))
  # create the instance
  instance = theUMLFactory().createInstance(name,package)
  instance.setBase(classe)
  # create instance' slots corresponding to class' attributes
  for attribute in instance.getBase().getOwnedAttribute():
    slot = theUMLFactory().createAttributeLink()
    slot.setAttributed(instance)
    slot.setName(attribute.getName())
    slot.setBase(attribute)

def slotMap(instance):
  map = {}
  for slot in instance.getSlot():
    map[slot.getName()] = slot
  return map

def slotValueMap(instance):
  map = {}
  for slot in instance.getSlot():
    map[slot.getName()] = slot.getValue()
  return map

def slotNamed(instance,name):
  map = slotMap(instance)
  try:
    return map[name]
  except:
    return None

# Set the value of the slots with a list of pairs
# (name,value). If a slot with that name does 
# not exist then create it. If value is None
# then the slot is not created, or it is removed
# if it was existing. Newly created slots are bound
# to class attribute with the same name if the instance
# specifies a class and an attribute with the same name
# exists.
def setSlots(instance,nameValueOrNoneMap):
  existingSlots = slotMap(instance)
  for name in nameValueOrNoneMap:
    value = nameValueOrNoneMap[name]
    if value is None:
      if name in existingSlots:
        existingSlots[name].delete()
    else:
      if name in existingSlots:
        slot = existingSlots[name]
      else:
        slot = theUMLFactory().createAttributeLink()
        slot.setAttributed(instance)
        slot.setName(name)
        classe = instance.getBase()
        if classe is not None:
          attribute = attributeNamed(classe,name)
          if attribute is not None:  
            slot.setBase(attribute)
      slot.setValue(value)
    
# Set the value of a named slot.
# If the slot does not exist create it.
def setSlotNamed(instance,name,value):
  setSlots(instance,{name:value})
    
#------------ links -----------------------------------

def createLink(sourceInstance,targetInstance,targetAssociationEnd,linkName=None):
  # create the link
  link = theUMLFactory().createLink(sourceInstance,targetInstance,"")
  sourceLinkEnd = link.getLinkEnd()[0]
  targetLinkEnd = link.getLinkEnd()[1]
  # set the properties of the target
  targetLinkEnd.setNavigable(True)
  targetLinkEnd.setModel(targetAssociationEnd)
  targetLinkEnd.setName(targetAssociationEnd.getName())
  targetLinkEnd.setMultiplicityMin("1")
  targetLinkEnd.setMultiplicityMax("1")
  # set the properties of the source
  sourceLinkEnd.setNavigable(True)
  sourceAssociationEnd = targetAssociationEnd.getOpposite()
  sourceLinkEnd.setName(sourceAssociationEnd.getName())
  sourceLinkEnd.setMultiplicityMin("1")
  sourceLinkEnd.setMultiplicityMax("1")
  # set the name of the link (association name or name provided)
  if linkName is None:
    linkName = nextId(lowerFirst(targetAssociationEnd.getAssociation().getName())
  link.setName(linkName)

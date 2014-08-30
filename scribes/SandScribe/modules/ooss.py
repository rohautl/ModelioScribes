from collections import OrderedDict

class Schema(object):
  def __init__(self,name="",description=None):
    self.name = name
    self.tables = OrderedDict()
    self.description = description
  def getTablesNb(self):
    return len(self.tables)
  def getNthTable(self,n):
    return self.tables[self.tables.keys()[n-1]]
  def __str__(self):
    return \
      "SCHEMA " \
        + ("" if self.name is None else self.name) \
        + ("" if self.description is None else self.description)+"\n" \
        + join("\n",[str(t) for t in self.tables])

class Table(object):
  def __init__(self,schema,name,description=None):
    self.schema = schema
    self.columns = OrderedDict()
    self.description = description 
    schema.tables[name] = self
  def getColumnsNb(self):
    return len(self.columns)
  def getNthColumn(self,n):
    return self.columns[self.columns.keys()[n-1]]
  def __str__(self):
    return \
      "  TABLE " \
        + name \
        + ("" if self.description is None else self.description)+"\n" \
        + join("",[str(c) for c in self.columns])

class Column(object):
  def __init__(self,table,name,description=None):
    self.table = table
    self.name = name
    self.description = description 
    table.columns[name] = self
  def getNumber(self):
    return self.table.columns.keys().index(self)+1
  def __str__(self):
    return \
      "    " \
        + self.name \
        + ("" if self.description is None else self.description)+"\n" 
       



       
class OOSSElement(object):
  def __init__(self,name,kind,source,parameters=[]):
    self.name = name
    self.kind = kind
    self.source = source
    self.parameters = parameters
  def __str__(self):
    return \
      self.name+":"+self.kind \
      + " from "+self.source.getName()+":"+self.source.getMClass().getName() \
      + ("" if len(self.parameters)==0 else " {"+str(self.parameters)+"} ") \  
      
class OOSSSchema(Schema,OOSSElement):
  def __init__(self,name,kind,source,parameters=[],description=None):
    Schema.__init__(self,name,description)
    OOSSElement.__init__(self,name,kind,source,parameters)
  def __str__(self):
    return \
      "" \
      + OOSSElement.__str__(self) \
      + ("" if self.description is None else self.description)+"\n" \
      + "".join([str(self.tables[tn]) for tn in self.tables.keys()])
    
class OOSSTable(Table,OOSSElement):
  def __init__(self,schema,name,kind,source,parameters=[],description=None):
    Table.__init__(self,schema,name,description)
    OOSSElement.__init__(self,name,kind,source,parameters)
  def __str__(self):
    return \
      "  " \
      + OOSSElement.__str__(self) \
      + ("" if self.description is None else self.description)+"\n" \
      + "".join([str(self.columns[cn]) for cn in self.columns.keys()])
        
class OOSSColumn(Column,OOSSElement):
  def __init__(self,table,name,kind,source,parameters=[],description=None):
    Column.__init__(self,table,name,description)
    OOSSElement.__init__(self,name,kind,source,parameters)
  def __str__(self):
    return \
      "    " \
      + OOSSElement.__str__(self) \
      + ("" if self.description is None else self.description)+"\n"    
      
print "ooss module loaded"
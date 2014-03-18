ClassScribe
===========
This script aims to simplify the input of the class models in modelio. It allows to transform a simple line-base textual notation into new created class elements (classes, attributes, operations, 
notes, etc.). If an element already exist, it is not created again, but its attributes or nested elements are modified. This is actually a "merge" operation so the script can be used to modify/extend an existing model (but *NOT* to delete elements - this operation should be realized manually through the regular interface). 

Context and nesting
-------------------
The elements created are always created into container element called  the context. The context defines which (nested) elements can be created in it. For instance in the context of a package, classes can be created  just by giving the list of names. In the context of a class, one can  attributes, operations and roles. If only names are given it is assume that attributes are to be created, otherwise the syntax of the line differ in order to indicate which kind of elements is to be created.

The "root context" corresponds to the first selected elements. Toplevel elements in the textual notation are going to be created there. Nesting (with two spaces) in the notation then indicates the context of each element to be create.

Notations
---------
Different notations are actually provided. Each notation suit different purposes:
* Structure: this notation is used to create/modify nested structures of classes, attributes, roles, operations and notes.
* Inheritance: this notation used nesting to represent hierarchies of classes or interfaces.

Structure Notation
------------------

### Syntax
TODO: More about the syntax. In the meantime the examples can be used as a reference.
TODO: Consider UseCaseScribe to see a possible way of defining the syntax.
* "+" indicates a "public" element. This is the default.
* "~" indicates a "package" element. 
* "#" indicates a "protected" element. 
* "-" indicates a "private" element. 
* "/" indicates a derived element.
* "s" stands for "string" uml datatype. This is the default if no type is indicated.
* "i" stands for "integer" uml datatype.
* "d" stands for "date" uml datatype.
* "f" stands for "float" uml datatype.
* "b" stands for "boolean" uml datatype.

### Examples
The examples below illustrate the use of the notation in different context.

TODO: Create some examples

The follwing example provide a complete view of the various possibility of
the "structure" notation. Note that this example is not really realistics:
* most of the time only a few of the possibilities will be used
* usually the same level of notation will be used for all elements, for 
instance specifying only the name and the visibility and the type.

Here is the example:

    Employee
     salary : i[0..1]
     
    Student < organization.Person, university.Stakeholder
     firstName      # this is a one line "description" note
     lastName : s
       #s This is a "summary" note (because it startswith #s) 
       #d Here this is a multi line description
       #  with multiple line as expected. They are contactenated 
       #  together. So there are three lines in total.
       #d Now this another "description" note
     +middleName : string [0..1]
     birthDate:d
     <PK> nationalId     # here we see an example of stereotype named PK
     / + age : i
     courses : Classes [*] inv students [*]
     xx/yy C 

Inheritance Notation
--------------------
Sometimes it is convenient to create hierarchies of classes and interfaces

Specification: TODO

    Person
      Men
      Women
      Professor
      Student
        FirstYearStudent
        MasterStudent
        
Hints
* "i" stands for "interface"
* "a" stands for "abstract"
    

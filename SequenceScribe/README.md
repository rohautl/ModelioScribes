SequenceScribe
==============
This script aims to simplify the input of the use case models. It allows to transform a simple line-base textual notation into new created use case elements (actors, use cases,  
notes, etc.). If an element already exist, it is not created again, but its attributes or nested elements are modified. This is actually a "merge" operation so the script can be used to modify/extend an existing model (but *NOT* to delete elements - this operation should be realized manually through the regular interface). 

Syntax
------
The syntax is based on nesting and simple line commands. Blank lines are ignored as well as separator lines containing only "*" or "=" or "-" and spaces. Lines starting with -- are comments and are ignored as well.



* Object creation
Examples
--------
    x : C1
    y : C2

    x m y
    y m x
    x m(a,b,c) y
    x create t : C3
    x delete t




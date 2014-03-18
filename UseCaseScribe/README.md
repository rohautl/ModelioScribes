UseCaseScribe
=============
This script aims to simplify the input of the use case models. It allows to transform a simple line-base textual notation into new created use case elements (actors, use cases,  
notes, etc.). If an element already exist, it is not created again, but its attributes or nested elements are modified. This is actually a "merge" operation so the script can be used to modify/extend an existing model (but *NOT* to delete elements - this operation should be realized manually through the regular interface). 

Syntax
------
The syntax is based on nesting and simple line commands. Blank lines are ignored as well as separator lines containing only "*" or "=" or "-" and spaces. Lines starting with -- are comments and are ignored as well.

* At the top-level:
  * <NameA> : create/modify an actor
  * <NameA> < <NameB> : create/modify an actor NameA inheriting from an actor NameB. Actors are created or reused if they already exist.
  * <NameA1>,<NameA2>...<NameAn> - <NameCU> : create/modify a use case and associate it with the corresponding actors. The actors are created if necessary. Association between actors and use cases are merged with previous one if already existing.
* In the context of use cases:
  * <NameC> : create/modify a collaboration named NameC
  * "t->" <NameC> : create a tracability link towards the model element NameC if it exist. If this model element does not exist, then a warning is issued.
* In the context of actors, use cases or collaborations:
  * "#s" <text> : create/modify the "summary" note (it is assumed that there at most one)
  * "#d" <text> : create/modify the "description" note (it is assumed that there at most one)
  * "# " <text> : append a space to the previous note

Examples
--------

    Actor1
      #s This is the "summary" note associated with Actor1.
      #d And now a "description" note. Actors does not have
      #  to be declared unless notes have to be attached with them
      #  or they have inheritance relationships. Otherwise
      #  they are declared "online" when found
    Actor8  
    Actor4
      #s
     
    Actor1 - UseCase1
      #s This is the "summary" of UseCase1 because "s" stands for summary.
      #d This is the "description" note attached to UseCase1.
      #  This note has various lines as each line is
      #  appended with the previous note if it start with "# " (note the space).
      #d This is another description starting here as the note type is given ("d" here).
      t->
      Collaboration11
        #s This is the "summary" of the Collaboration11
        
      Collaboration12
        #s This is the "summary" of Collaboration12
        #d This is the "description" 
        #  and it continues on
        #  multiple lines.
      Collaboration13
    Actor1,Actor2 - UseCase2
    Actor6 - UseCase3
    Actor6 - UseCase4
    Actor2,Actor1 - UseCase5    
    Actor5

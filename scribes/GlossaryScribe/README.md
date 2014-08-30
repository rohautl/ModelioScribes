GlossaryScribe
==============
This script aims to simplify the input of the glossaries in Modelio. The "import" operations transform a text written in the Simple Glossary Notation (SGN) into glossary elements (glossaries, terms, notes, etc.). On the other way around the "export" operation consists in generating glossary representations from an existing model. 

Modelio requirements
--------------------
This script works both with the "Analyst" metamodel of the commercial version of modelio or with a profiles with the open source version.

Glossary profile
----------------
With the open source version, the "Glossary" profile is defined in the local module with the following elements:
* <<Glossary>>: stereotype defined on [Package]s. [Glossary]s can be nested and can contains [Term]s. 
* <<Term>>: stereotype defined on [Class]es. [Term]s are contained in a [Glossary].
** "Definition" : note type defined on <<Term>>
** "Alternatives" : note type defined on <<Term>>
** "Shortcuts": note type defined on <<Term>>
** "Examples": note type defined on <<Term>>
** "References": note type defined on <<Term>>
A keyword is associated to each note type as explained below. If a note type is added in the profile then the keyword can be used in the SGN as well.

SGN Notation
------------
TODO: to be defined. In the meantime the examples can be used as a reference.
TODO: check the compatibility when possible with UseCaseScribe and ClassScribe

* "G" is a shortcut for "Glossary"
* "A:" is a shortcut for "Alternatives:"
* "S:" is a shortcut for "Shortcuts:"
* "E:" is a shortcut for "Examples:"
* "R:" is a shortcut for "References:"
* "D:" is a shortcut for "Description:"
* "S:" is a shortcut for "Summary:"

SGN Examples
------------
The following example provides a complete view of the various possibilities of the SGN notation. 

    G MyGlossary
      D: This is a "description" note attached to the glossary.
        
      Term1: The definition of term1 is the one on this line
           : but it continues on this one.
        D: This is a "description" note attached to the term Term1
         :  and this description has various lines.
        A: Alt1; Alt2; Alt3
        S: T1 
        E: Here we have some text which could be multiline if required.
         : This is the second line
        R: [CR001#23,45-48;CR009#24]
        
      Term2: This is the definition of Term2 and it may refer to [Term1] and [Term3].
           : The definition is on various lines in this case (note the identation).
        Description: Now we create a description which will be added to Term2.
        Alternatives: Alt4; Alt5
        Shortcuts: T2
        
      Glossary MySubGlossary
         Term3: The definition of the first term3
         Term4: Another definition
         Term5: Yet another definition
         
User Interface
--------------
The user interface provides three "commands": one interactive command and two file-based commands:

TODO: See ClassScribe for an example of specification

* **Import glossary model**: TODO
* **Export glossary model**: TODO
* **Edit glossary model**: TODO
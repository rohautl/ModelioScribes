GlossaryScribe
==============
This script aims to simplify the input of the glossaries in Modelio. The "import" operations transform a text written in the Simple Glossary Notation (SGN) into glossary elements (glossaries, terms, notes, etc.). On the other way around the "export" operation consists in generating glossary representations from an existing model. 

Modelio requirements
--------------------
This script works both with the "Analyst" metamodel of the commercial version of modelio or with a set of profiles with the open source version.

Glossary profile
----------------
* <<Glossary>>: stereotype defined on [Package]s. [Glossary]s can be nested and can contains [Term]s. 
* <<Term>>: stereotype defined on [Class]es. Contained in a [Glossary].
** "Definition" : note type defined on <<Term>>
** "Alternatives" : note type defined on <<Term>>
** "Shortcuts": note type defined on <<Term>>
** "Examples": note type defined on <<Term>>
** "References": note type defined on <<Term>>

SGN Notation
------------
TODO: to be defined. In the meantime the example can be used as a reference.
TODO: check the compatibility when possible with UseCaseScribe and ClassScribe

* "g" is a shortcut for "Glossary"
* "a:" is a shortcut for "Alternatives:"
* "s:" is a shortcut for "Shortcuts:"
* "e:" is a shortcut for "Examples:"
* "r:" is a shortcut for "References:"

SGN Examples
------------

    g MyGlossary >>>
      #d This is a "description" note attached to the glossary.
        
      Term1: 
        The definition of term1 is the one on this line.
        "d This is a "description" note attached to the term Term1
        "  and this description has various lines.
        a: Term4; Term6;Term7
        s: T1 
        Examples: 
        "  Here we have some text which could be multiline if required.
        "  
        "  In this case trailing spaces are removed.
        "  In anycase there should be enough spaces to show that it is nested.
        References: [CR001#23,45-48;CR009#24]
        
      Term2: This is the definition of Term2 and it may refer to [Term1] and [Term3].
        " The definition is on various lines in this case (note the identation).
        "d Now we create a description which will be added to Term2.
      Glossary MySubGlossary
         Term3:
         Term4:
         Term5:


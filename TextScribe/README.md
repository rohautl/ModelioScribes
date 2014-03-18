TextScribe
==========
This script aims to deal with textual resources, glossaries and requirements. It aims to simplify the input of textual ressources, glossaries and requirements and to automate the creation of traceability links between these ressources. It allows in particular to transform a simple line-base textual notation into glossary, terms, requirements and textual ressources. If an element already exist, it is not created again, but its attributes or nested elements are modified. This is actually a "merge" operation so the script can be used to modify/extend an existing model (but *NOT* to delete elements - this operation should be realized manually through the regular interface). 

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

Glossary syntax 
---------------
TODO: to be defined. In the meantime the example can be used as a reference.
TODO: check the compatibility when possible with UseCaseScribe and ClassScribe

* "a:" is a shortcut for "Alternatives:"
* "s:" is a shortcut for "Shortcuts:"
* "e:" is a shortcut for "Examples:"
* "r:" is a shortcut for "References:"

Glossary examples
-----------------
    MyGlossary >>>
      #d This is a "description" note attached to the glossary.
        
      Term1: Definition1
        #d This is a "description" note attached to the term Term1
        #  and this description has various lines.
        a: Term4; Term6;Term7
        s: T1 
        Examples: Here we have some text
          which could be multiline if required.
          In this case trailing spaces are removed.
          In anycase there should be enough spaces to show that it is nested.
        References: [CR001#23,45-48;CR009#24]
        
      Term2: This is the definition of Term2 and it may refer to [Term1] and [Term3].
        The definition is on various lines in this case (note the identation).
        #d Now we create a description which will be added to Term2.
      MySubGlossary >>>
         Term3:
         Term4:
         Term5:

         
Requirement profile
-------------------
The "Requirement" profile defines the following hierarchy of stereotype.
* <<Req>>
** <<FunctionalReq>>
** <<PerformanceReq>>
** <<InterfaceReq>>
** <<ConsistencyReq>>
** <<DevelopmentReq>>
** <<SecurityReq>>
The "Definition" note type is defined on all requirements type.
TODO: to be completed with priority and other fields if necessary.


Requirement syntax
------------------
TODO: to be defined. In the meantime the example can be used as a reference.
TODO: check the compatibility when possible with UseCaseScribe and ClassScribe


Requirement example
-------------------
TODO: to be completed
    Functional NameOfRequirement1: This is the first line of the definition.
      This is the second line of the definition of the requirement NameOfRequirement1.
      It can be on multiple lines.
    Performance NameOfRequirement2:
      Here the first line is this one as they was nothing but space in the line above.
      So we have only two lines in the definition.
      #d Now this is a "description" note on the requirment.
    Package1
      Security Req3: This definition refers to [Term1] and [Term2].
        #d This requirement is defined within a package 


Texts
-----
The following stereotypes are defined on [Artifact]:  
* <<Text>>
* <<Section>> 
* <<Paragraph>>
On each of this stereotype a "Content" note type is defined.

A function allows to decompose a [Text] in a sequence of [Paragraph]s based on each content. Each [Paragraph] is numbered sequentially (its name is a number). These elements can therefore be the target of traceability dependencies. This is necessary for instance to deal with reference like "[CR078#2]". In this case the [Paragraph] named "2" in the [Text] named "CR078" is referenced. 
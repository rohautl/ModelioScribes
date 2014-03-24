TextScribe
==========

Texts
-----
The following stereotypes are defined on [Artifact]:  
* <<Text>>
* <<Section>> 
* <<Paragraph>>
On each of this stereotype a "Content" note type is defined.

A function allows to decompose a [Text] in a sequence of [Paragraph]s based on each content. Each [Paragraph] is numbered sequentially (its name is a number). These elements can therefore be the target of traceability dependencies. This is necessary for instance to deal with reference like "[CR078#2]". In this case the [Paragraph] named "2" in the [Text] named "CR078" is referenced. 
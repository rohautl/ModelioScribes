TextScribe
==========
TODO: to be specified. The current specification is paricularily immature.

Profile
-------
The following stereotypes are defined on the Artifact metaclass:  
* \<\<Text>>
* \<\<Section>> 
* \<\<Paragraph>>

For each of these stereotype, a "Content" note type is defined.

Interface
---------
A function allows to decompose a [Text] into a sequence of [Paragraph]s based on the content of the text. Each [Paragraph] is numbered sequentially (its name is a number). These elements can therefore be the target of traceability dependencies. This is necessary for instance to deal with reference like "[CR078#2]". In this case the [Paragraph] named "2" in the [Text] named "CR078" is referenced. 
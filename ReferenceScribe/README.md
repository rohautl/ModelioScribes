ReferenceScribe
===============
This scripts automates the creation of dependencies beetween model elements based on the occurrence of references within notes or other fields of model elements. For instance if a name of an element is referenced somehow in the note of another elements, then a dependency will be created between these elements. The script is based on a .xml configuration file describing where to search references and where to search referenced elements.


TODO: This specification shold be completed

Usage
-----
Different pieces of text can refers to other entities and in particular [Text]s, [Paragraph]s, or [Term]s. References are in brackets just like in "[Name]". When such a reference is found a traceability link should be created between the element containing (the text containing) this reference and the element reference. This link created takes the form of a UML [Dependency] stereotyped <<Trace>>. Assuming that these links are not created manually, when the traceability update will run, all links originating from the elements visited will be first erased and the traceability links will be created again based on the content of the text. 

Concerning the TextScribe the following refererences should lead to traceability link
* [Term]s can refers to [Term]s via their definition, or the examples.
* [Requirement]s can refers to [Term]s via their definition.

Configuration
-------------
TODO: Specify the content of the configuration file

Examples
--------
TODO:
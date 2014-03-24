ReferenceScribe
===============
This plugin automates the creation of dependencies beetween model elements based on the occurrenced of references within notes or other fields of model elements. That is, if a name of an element is referenced somehow in the note of another elements, then a dependency will be created between these elements. For instance if the summary of a use case is "creates a [Transaction] with no [Penality]" two references to the term "Transaction" and "Penality" will be created, at least if the plugin as been configured to do so. This plugin is indeed based on a .xml configuration file describing where to search references and where to search referenced elements. In the example above reference are search in "summariy notes" of "use cases" and the elements are search as "terms".


TODO: This specification should be completed

Usage
-----
Different pieces of text can refers to other entities and in particular [Text]s, [Paragraph]s, or [Term]s. References are in brackets just like in "[Name]". When such a reference is found a traceability link is be created between the element containing (the text containing) this reference and the element reference. This link created takes the form of a UML [Dependency] stereotyped <<Trace>>. Assuming that these links are not created manually, when the traceability update will run, all links originating from the elements visited will be first erased and the traceability links will be created again based on the content of the text. 

Concerning the TextScribe the following refererences should lead to traceability link
* [Term]s can refers to [Term]s via their definition, or the examples.
* [Requirement]s can refers to [Term]s via their definition.

Configuration
-------------
TODO: Specify the content of the configuration file. See AuditScribe for some inspiration. 

The configuration allows to describe the following information: TODO to be completed and refinded:
* (1) source 
 * the type(s) of elements that could serve as source of the dependency
 * the elements or notes that are scanned to search references, e.g. notes
 * optionally the regular expressions used for locating references
* (2) dependency
 * the stereotype on the dependency to be created. A traceability dependency by default.
* (3) target path
 * the type(s) and location(s) of elements where to search the target element
 * the attribute that is used for the reference, for instance "name"s of terms 

Examples
--------
TODO:

Interfaces
----------
TODO: see ClassScribe for an example

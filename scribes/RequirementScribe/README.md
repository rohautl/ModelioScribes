RequirementScribe
=================
This script aims to simplify the input of simple requirement models in Modelio. The "import" operation transforms a text written in the Simple Requirement Notation (SRN) into requirement elements (requirements, package and notes). On the other way around the "export" operation consists in generating textual representations from an existing model.

Modelio requirements
--------------------
This script works both with the commercial and open source version of modelio.
* In the commercial version the "Analyst" metamodel is used. This metamodel already contains the notion of requirement.
* In the open source version the "Requirement" profile is created in the local module (or reused if it exist already).
         
Requirement profile
-------------------
In the case of the open source version the "Requirement" profile is installed (if not already present) in the local module. This profile defines the following hierarchy of stereotypes. The base metaclass is "Class". 
* <<Req>>
** <<FunctionalReq>>
** <<PerformanceReq>>
** <<InterfaceReq>>
** <<ConsistencyReq>>
** <<DevelopmentReq>>
** <<SecurityReq>>
The "Definition" note type is defined on all requirements types.
TODO: to be completed with priority and other fields if necessary.


SRN Notation
------------
TODO: to be defined. In the meantime the example can be used as a reference.
TODO: check the compatibility when possible with UseCaseScribe and ClassScribe


SRN Example
-----------
TODO: to be completed. Attributes of requirements should be added as well as dependencies.

    Functional NameOfRequirement1 
      : This is the first line of the definition.
      : This is the second line of the definition of the requirement NameOfRequirement1.
      : It can therefore be on multiple lines.
    Performance NameOfRequirement2
      : Only a line for the definition
      D: Now this is a "description" note on the requirment.
       : this definition is on two lines.
    Paclage MyPackage1
      Security Req3 
        : This definition refers to [Term1] and [Term2].
        S: This a "summary" note



User interface
--------------        
TODO: to be defined. See for instance ClassScribe/UseCaseScribe for an illustration. 

AuditScribe
===========
This script provides a framework to check modeling rules on existing models. The modeling rules are defined in a .xml configuration file in a rather gener. Some rule are predefined yet parametrable. Some other can be implemented as jython method. The intention of these rules is to complement those already checked by modelio with rules defining different modeling styles, naming conventions, methods, etc. The level of severity of each rule (error, warning, advice) can be configured as well as the elements on which each rule should be checked.

Rule structure
--------------
Conceptually the audit configuration is based on the following concepts (each concept is later defined in a separate subsection):
* Rule: the abstract concept corresponding to a rule in general.
* NamingRule: naming rules allows to check if the name of a model element matches a regular expression.
* JythonRule: this abstract concept corresponds to all rule implemented in jython.
* JythonBooleanRule: a JythonBooleanRule is implemented by a jython predicate indicating whether the rule is satisfyied or not.
* JythonMetricRule: a JythonNumericRule is implemented by a jython function returning an integer. The integer must be lower/greater than a constant provided or within a given range.
* ModelLocation: this concept allows to express on which elements a rule has to be checked.
* RegExpr: this concept allows to name and define regular expression for reuse in different place.

### Rule
[Rule]s is an abstract concept. This the main top-level concept. [Rule] being an abstract concept it cannot be instanciated and serve only for its sub classes. Attributes common to all rules are the following:
* "name": the name of the [Rule].
* "where": this attribute either refer to a name of a metaclass  or to a [ModelLocation]. In the first case the name of the metaclass is simply given and all elements of this metaclass will be checked. Otherwise if the value is starting with a "#" character, what remains is the name of a [ModelLocation] giving the details about which elements have to be checked (see below).
* "level": an optional the severity level of the [Rule]. One of the following values: "error", "warning", or "advice". "Warning" is the default value.
indicates on which model elements the [Rule] should be applied. This could be for instance all "Class"es with a given stereotype and with a name matching a given regular expression. See below for more information on the "where" clause.
* "message": a optional message that is produced when the [Rule] is not satisfied.
* "url": an optional URL providing more information about the [Rule].

### NamingRule
[NamingRule]s are concete rules. Their behavior consist in checking if the name of the model element match a given regular expression. If not the rule is not satisfied. 

Additionally to the attributes of [Rule]s, [NamingRule]s  include the following attributes:
* "regExpr": the regular expression to be checked on the name of the model element or a reference to a [RegExpr]. If the first character of this attribute is a "#" character, if it is followed by a CamlCase identifier, and if it corresponds to the name of [RegExpr] then the  regexpr is used. 

### JythonRule
[JythonRule] is an abstract concept that cannot be directly instanciated (see the subclasses). [JythonRule]s are [Rule]s implemented as a jython function on a given model element. If the function returns an error or raised an exception, then the rule is not satisfied. If the function does not exist then an error will be raised as this is considered as a problem in the configuration itself. Each function must takes one and only one parameter, the model element on which the rule have to be checked. In practice all functions are implemented in a single jython file (see below).

Additionally to the attributes of [Rule]s, [JythonRule]s have the following attribute:
* "function": the name of the jython function as defined in the jython file. 

### JythonBooleanRule
[JythonBooleanRule]s are [JythonRule]s implemented by a jython function returning a boolean. If the function return true then the rule is satisfied. Otherwise the rule is not satisfied. 

There is no additional attribute. 

### JythonMetricRule
[JythonMetricRule]s are [JythonRule]s implemented by a jython function returning an integer value. This kind of rule check whether the value is greater or lower than a constant, or within a given interval.

Additionally to the attributes of [JythonRule], the following attributes are defined:
* "lower": the lower bound; an integer constant. This attribute is optional. If defined, the rule is satisfied if the value returned by the function is lower or equal to this constant. 
* "upper": the upper bound; an integer constant. This attribute is optional. If defined, the rule is satisfied if the value returned by the function is greater or equel to this constant.  

### ElementLocation
A [ElementLocation] enables to define on which model elements a rule or a set of rules could be applied. For instance one may want to consider only "those 'class'es stereotyped <<View>> with a name ending with 'Panel' and that are own in a package stereotyped <<Implementation>>' and to give this expression a symbolic name such as "PanelViews". This [ElementLocation] can then be reused in different "where" clause in different rules.

The following attributes can be defined on [ElementLocation]:
* "name": A name used for this element location. This name will be used in the "where" clause of [Rule]s.
* "metaclass": The metaclass of elements to be considered. This attribute is compulsory.
* "stereotypes": Optional. A list of stereotype names separated either via '|' or '&'. In the first case, one stereotype at least must be defined on the element. In the second case, all stereotypes must be defined on the element.
* "regExpr": Optional. A regular expression to be evaluated on the name of the element or a reference to a (named) [RegExpr]s (see below).
* "ownerMetaclass": Optional attribute. The metaclass of the owner of the element considered. 
* "ownerStereotypes": Optional. Like the "stereotype" attribute but applied on the owner of the model element.
* "ownerRegExpr": Optional. Like the "regExpr" attribute but
 
### RegExpr
A [RegExpr] defines a regular expression and give it a name. This is handy to define once regular expression for naming styles (such as camlCase) and to be reuse it later in different [NamingRule]s.

[RegExpr]s have the following attributes
* "name": The name of the [RegExpr] for futher reference in other entities. 
* "regExpr": The regular expression.
  
Configuration implementation
----------------------------
From a concrete point of view the configuration is defined in a directory "config" with two files:
* "config/Rules.xml": this file contains the list of [Rule]s and associated information such as (named) [RegExpr]s. 
* "config/JythonRules.py": this file contains all the definition of the [JythonRule]

Interface
---------
TODO: to be defined
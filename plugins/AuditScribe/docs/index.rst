AuditScribe
===========
This script provides a framework to check modeling rules on Modelio_ models (which supports UML and BPMN). A list of modeling rules is defined on the ScribeQuality_ web site. The features provided by AuditScribe are very similar to those found in tools like CheckStyle_ for java. The modeling rules are defined in a configuration file in a rather generic way.

The behavior of some rules are predefined (e.g. checking the name of a model element according to a regular expression). Some other rules can be implemented as jython methods, extending therefore the expression power of rules.

The intention of all rules is to complement those already checked by modelio. Rules can be used to define different modeling styles, to check the application of naming conventions or modelling methods, etc. The level of severity of each rule (``error``, ``warning``, ``advice``) can be configured as well as the elements on which each rule should be checked.


Predefined Rule Set
-------------------

.. admonition:: TODO

    Here should come a list of common rules in a similar way as CheckStyle_ provides predefined rule sets.


Rule Specification
-------------------
Conceptually the audit configuration is based on the following concepts. Each concept is later based on a separate subsection:

* ``Rule``: abstract concept corresponding to a Rule_ in general.

* ``NamingRule``: a NamingRule_ allows to check if the name of a model element matches a RegExpr_ (see below).

* ``JythonRule``: a JythonRule_ is particular case of Rule_. This is still an *abstract* concept, the rules implemented in jython.

* ``JythonBooleanRule``: a JythonBooleanRule_ is particular kind of JythonRule_. The JythonRule_ is implemented by means of jython predicate, that is a function returning a boolean. The boolean indicates whether the rule is satisfied or not.

* ``JythonMetricRule``: a JythonRule_ implemented by a jython function returning an integer. The integer must be lower/greater than a constant provided or within a given range.

* ``location``: a Location_ express on which elements a Rule_ has to be checked.

* ``RegExpr``: a RegExpr_ allows to define a regular expression and name it for reuse in different places.

The concepts presented above are presented below.

Rule
^^^^

Rule is an abstract concept. This the main top-level concept. ``Rule`` being an abstract concept it cannot be instantiated and serve through its sub-classes. Attributes common to all rules are the following:

* ``name``: the name of the Rule_.

* ``where``: as shown below this attribute either refers to name(s) of a metaclass or a Location_:

    * *<metaclassnames>*. In this case the parameter of the ``where`` clause is a name (or list of names) of metaclass separated by a ``|`` (e.g. ``UseCase|Actor``). All the objects of these metaclasses will be checked.

    * *<ModelLocation>*. When the parameter starts with a ``#`` character, what remains is the name of a Location_ giving the details about which elements have to be checked (see below).

* ``severity``: This optional parameter indicates the severity level associated with the Rule_. One of the following values: ``error``, ``warning``, or ``advice``. The default value is ``warning``.

* ``message``: This optional parameters corresponds to a message that is produced when the Rule_ is not satisfied.

* ``url``: An optional URL providing more information about the Rule_.


NamingRule
^^^^^^^^^^

NamingRules are concrete Rule_\s. The behavior of a NamingRule_ consists in checking if the name of the model element to be checked matches a given regular expression. If not the rule is not satisfied.

Additionally to the attributes associated with Rule_, NamingRule_ includes the following attributes:

* ``regExpr``: the regular expression to be checked on the name of the model element or a reference to a RegExpr_. If the first character of this attribute is a ``#`` character, if it is followed by a CamlCase identifier corresponding to the name of RegExpr_ then this regexpr is used.

JythonRule
^^^^^^^^^^

JythonRule is an abstract concept that cannot be directly instantiated. A JythonRule is a Rule_ implemented as a jython function taking the model element to bed checked as a parameter. If the function returns an error or raised an exception, then the rule is not satisfied. If the function does not exist then an error will be raised as this is considered as a problem in the configuration itself. The function must takes one and only one parameter, the model element on which the rule have to be checked. In practice all functions are implemented in a single jython file (see below).

Additionally to the attributes of a Rule_, a JythonRule_ has the following attribute:

* ``function``: the name of the jython function as defined in the jython file.

JythonBooleanRule
^^^^^^^^^^^^^^^^^

A JythonBooleanRule is a concrete case of JythonRule_. It is implemented by means of a jython function returning a boolean. If the function returns true then the rule is satisfied. Otherwise the rule is not satisfied.

There is no additional attribute.

JythonMetricRule
^^^^^^^^^^^^^^^^

A JythonMetricRule is a concrete case of JythonRule_. It is implemented by means of jython function returning an integer value. This kind of rule checks whether the value returned by the function (a metric) is greater or lower than a constant, or within a given interval.

Additionally to the attributes of JythonRule_, the following attributes are defined:

* ``lower``: the lower bound; an integer constant. This attribute is optional. If defined, the rule is satisfied if the value returned by the function is lower or equal to this constant.

* ``upper``: the upper bound; an integer constant. This attribute is optional. If defined, the rule is satisfied if the value returned by the function is greater or equel to this constant.


Location
^^^^^^^^

An ElementLocation enables to define on which model elements a Rule_ or a set of Rule_\s have to be applied. An ElementLocation is typically used in the ``where`` clause of a Rule_. For instance one may want to consider:

     "those 'classes' stereotyped <<View>> with a name ending with 'Panel' and that are own in a package stereotyped <<Implementation>>' and to give this expression a symbolic name such as "PanelViews".

An Location_ formalize such set of elements and give it a name. This name can then be reused in different "where" clauses of different rules.

The following attributes can be defined on Location_:

* ``name``: The name og this Location_ This name is intended to be reused in the ``where`` clause of Rule_\s.

* ``metaclass``: A metaclass name, or a list of metaclass names separated by ``|``. This parameter indicates which model elements have to be considered. This attribute is compulsory.

* ``stereotype``: Optional. A list of stereotype names separated either via ``|`` or ``&``. In the first case, one stereotype at least must be defined on the model element for this element to be considered. In the second case, all stereotypes must be defined on the model element.

* ``regExpr``: Optional. A RegExpr_ to be evaluated on the name of the element or a reference to a named RegExpr_s (see below).

* ``ownerMetaclass``: Optional attribute. The metaclass(es) (separated by ``|``) of the owner of the element considered.

* ``ownerStereotypes``: Optional. Like the ``stereotype`` attribute but applied on the owner of the model element.

* ``ownerRegExpr``: Optional. Like the ``regExpr`` attribute but applied on the owner of the model element.

RegExpr
^^^^^^^

A RegExpr defines a `python regular expression`_ and gives it a name. This is handy for instance to define only once a regular expression for a naming styles (e.g. camlCase), and then to reused this name in different NamingRule_\s and/or Location_\s.

A RegExpr_s has the following attributes:

* ``name``: The name of the [RegExpr] for futher reference in other entities.

* ``regExpr``: The regular expression.

Note: the `pythex`_ web site provides a convenient way to test regular expression online.

Configuration
-------------

From a concrete point of view the audit configuration is defined in a directory "config" with two files:

* ``config/Rules.xml`` or ``config/Rules.yml``: the ``Rules`` file (either in xml or yaml) contains the list of Rule_\s and associated information such as (named) RegExpr_s and Location_s.

* ``config/JythonRules.py``: this file contains all the python functions referenced by ``JythonRule``\s.

Examples
--------

.. admonition:: TODO

   A set of examples should be given both using xml and yml formats.

User Interface
--------------

.. admonition:: TODO

   To be defined. It should be possible to launch the audit either on the
   selected elements or if no elements are selected on the whole project.


...............................................................................


.. _ScribeQuality: http://scribequality.readthedocs.org/
.. _`python regular expression`: https://docs.python.org/2/library/re.html
.. _`pythex`: http://pythex.org/
.. _CheckStyle : http://scribetools.readthedocs.org/en/latest/checkstyle/index.html
.. _Modelio : http://scribetools.readthedocs.org/en/latest/modelio/index.html

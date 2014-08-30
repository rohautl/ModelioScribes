Installation
------------
The OCLScribe directory can be installed anywhere on the disk as soon as the
environement variable SCRIBES_HOME is defined.
Each macro has to be installed in the workspace. Two procedure are possible.

### Installation with standard procedure
Each macro can be installed individually using the standard modelio procedure.
For instance in Modelio 3.1:
* "Configuration" - main menu
  * "Macros catalog" - sub menu
    * "Workspace" - element of the catalog
      * "Add macro..." - button
        * "Macro name:" - field
        * "Macro path:" - field
        * "Icon path:" - field
        * "Description:" - field
        * "Applicable on:" - field
        * "Show in contextual menu:" - field
        " "Show in toolbar:" - field
The value of the different fields depend on the macro. See the macros/catalog-entries.xml file for setting these values.
  
### Modification at once of the XML macro catalog        
Instead of using the standard procedure and installing each macro one by one, it is possible to proceed as following (assuming that $WORKSPACE is the workspace directory):
* copy each macro files (that is each .py file in the "macros" directory) in the "$WORKSPACE/macros" directory
* open the "$WORKSPACE/macros/.catalog". This file contains the already installed macros. Open the content of the "macros/catalog-entries.xml" and copy its content to the appropriate part in the .catalog respecting the xml structure.  

Installation of third parties libraries
---------------------------------------
TBC

pip install gspread --no-compil --target c:\DEV\ModelioScribes\libs\python

pip install pydrive --no-compil --target c:\DEV\ModelioScribes\libs\python

ProjectScribe
============
This module allows to import a GandttProject file into modelio. Tasks and HumanRessources are made available in the model and can therefore be referenced in modelio.

Profile
-------
The integration of gandtt project entities into modelio implies defining a "Project" profile.

TODO: Define here the list of stereotype and tag value.

Examples
--------

    <?xml version="1.0" encoding="UTF-8"?>
    <project name="" company="" webLink="" view-date="2012-12-01" 
         ... >
        <description/>
        ...
        <tasks empty-milestones="true">
            ...
          <task id="0" name="Architectural design" color="#99ccff" 
                meeting="false" start="2012-12-24" duration="22" complete="78" expand="true">
            <task id="9" name="Create draft of architecture" color="#99ccff" 
                  meeting="false" start="2012-12-24" duration="10" complete="100" expand="true">
              <depend id="10" type="2" difference="0" hardness="Strong"/>
              <depend id="12" type="2" difference="0" hardness="Strong"/>
            </task>
            <task id="10" name="Prepare construction documents" color="#99ccff" 
                  meeting="false" start="2013-01-07" duration="12" complete="60" expand="true">
              <depend id="17" type="2" difference="0" hardness="Strong"/>
            </task>
            ...
          </task>
          <task id="11" name="Interior design" color="#99ccff" 
                meeting="false" start="2013-01-07" duration="10" complete="33" expand="true">
            ...
          </task>
          ...
        </tasks>
        <resources>
          <resource id="1" name="Jack House" function="Default:1"           
                    contacts="jack.house@myselfllc.net" phone="0044 077345456"/>
          <resource id="0" name="John Black" function="4" 
                    contacts="john.black@myselfllc.net" phone="+44 0794353567"/>
          ...
        </resources>
        <allocations>
          <allocation task-id="9" resource-id="1" function="Default:1" 
                      responsible="false" load="50.0"/>
          ...
          <allocation task-id="1" resource-id="0" function="4" 
                      responsible="false" load="100.0"/>
          ...
        </allocations>
        <vacations>
          <vacation start="2009-02-02" end="2009-02-09" resourceid="1"/>
        </vacations>
        ...
        <roles roleset-name="Default"/>
        <roles>
            <role id="0" name="Architect"/>
            <role id="1" name="Bricklayer"/>
            <role id="2" name="Foreman"/>
            ...
        </roles>
    </project>

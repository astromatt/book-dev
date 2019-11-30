***************
User Management
***************


Konfiguracja
============
* Go to Jira User Server (g+g and type JIRA User Server)
* Add application
* Set application name, password and IP Addresses (paste adresses from instances which you want connect with Jira User Server)


Dobre praktyki
==============
* Always use LDAP (OpenLDAP or Active Directory)
* name groups as ``jira-users`` or ``jira-administrators``
* local administrator ``jira-administrator`` only for fixing bugs with LDAP
* use ``jira@example.com`` (for easy email fiterling)
* use ``jira.example.com`` as domain name with Firewall blocking external access
* ``/etc/resolv.conf`` ``search example.com`` -> ustawianie przez DHCP
* Internal and external users in one LDAP server
* Read only access via LDAPs
* avoid nested groups
* all tools in ``OU=ecosystem``
* use LDAP groups for project roles from ``OU=projects``
* do not use user accounts in project roles (only LDAP groups)
* Confluence page with all ``*-administrators`` + ``mailto:`` links
* Confluence page with JIRA project administrators
* Do not use technical accounts (use SSH keys)
* Use SSH keys with proper comment

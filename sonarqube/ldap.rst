LDAP Configuration
==================


Server Configuration
--------------------
.. csv-table:: Server Configuration
    :header: "Variable", "Description"

    ``SONAR_SECURITY_REALM=LDAP``, "Enable the LDAP feature"
    ``SONAR_AUTHENTICATOR_DOWNCASE=true``, "Set to true when connecting to a LDAP server using a case-insensitive setup"
    ``LDAP_URL=ldap://localhost:10389``, "URL of the LDAP server. Note that if you are using ldaps, then you should install the server certificate into the Java truststore."
    ``LDAP_BINDDN=cn=sonar,ou=users,o=mycompany``, "Bind DN is the username of an LDAP user to connect (or bind) with. Leave this blank for anonymous access to the LDAP directory (optional)"
    ``LDAP_BINDPASSWORD=secret``, "Bind Password is the password of the user to connect with. Leave this blank for anonymous access to the LDAP directory (optional)"
    ``LDAP_AUTHENTICATION=simple``, "Possible values: simple | CRAM-MD5 | DIGEST-MD5 | GSSAPI See http://java.sun.com/products/jndi/tutorial/ldap/security/auth.html (default: simple)"
    ``LDAP_REALM=example.org``, "See: http://java.sun.com/products/jndi/tutorial/ldap/security/digest.html http://java.sun.com/products/jndi/tutorial/ldap/security/crammd5.html (optional)"
    ``LDAP_CONTEXTFACTORYCLASS=com.sun.jndi.ldap.LdapCtxFactory``, "Context factory class (optional)"
    ``LDAP_STARTTLS=true``, "Enable usage of StartTLS (default : false)"
    ``LDAP_FOLLOWREFERRALS=false``, "Follow or not referrals. See http://docs.oracle.com/javase/jndi/tutorial/ldap/referral/jndi.html (default: true)"


User Mapping
------------
.. csv-table:: Server Configuration
    :header: "Variable", "Description"

    ``LDAP_USER_BASEDN=cn=users,dc=example,dc=org``, "Distinguished Name (DN) of the root node in LDAP from which to search for users (mandatory)"
    ``LDAP_USER_REQUEST=(&(objectClass=user)(sAMAccountName={login}))``, "LDAP user request. (default: (&(objectClass=inetOrgPerson)(uid={login})) )"
    ``LDAP_USER_REALNAMEATTRIBUTE=name``, "Attribute in LDAP defining the user’s real name. (default: cn)"
    ``LDAP_USER_EMAILATTRIBUTE=email``, "Attribute in LDAP defining the user’s email. (default: mail)"


Group Mapping
-------------
.. csv-table:: Server Configuration
    :header: "Variable", "Description"

    ``LDAP_GROUP_BASEDN=cn=groups,dc=example,dc=org``, "Distinguished Name (DN) of the root node in LDAP from which to search for groups. (optional, default: empty)"
    ``LDAP_GROUP_REQUEST=(&(objectClass=group)(member={dn}))``, "LDAP group request (default: (&(objectClass=groupOfUniqueNames)(uniqueMember={dn})) )"
    ``LDAP_GROUP_IDATTRIBUTE=sAMAccountName``, "Property used to specify the attribute to be used for returning the list of user groups in the compatibility mode. (default: cn)"


Further Reading
---------------
* https://docs.sonarqube.org/latest/setup/environment-variables/#header-4

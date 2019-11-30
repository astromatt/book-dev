********
Workflow
********


Dobre praktyki
==============
- Directed graph
- Complete graph
- Few vertices
- Lots of Edges
- Try simple and add statuses
- Keep transitions from all statues
- Simplified Workflow

Workflow Functions
==================

Triggers
--------

Bitbucket
^^^^^^^^^
* Pull request created
* Pull request merged
* Pull request declined
* Pull request reopened
* Branch created
* Commit created

Bamboo
^^^^^^
* Deployment successful
* Deployment failed

Crucible
^^^^^^^^
* Review started
* Review abandoned
* Review submitted for approval
* Review closed
* Review rejected
* Review summarized

Condition
---------
.. csv-table:: Condition
    :header: "Name", "Description"
    :widths: 20, 80

    "Always False Condition", "This condition always fails"
    "Block transition until approval", "Condition to block issue transition if there is a pending approval"
    "Compare Number Custom Field", "Condition to allow transition if a comparison of specified Number Custom Field to a specified value is true"
    "Hide From User Condition", "Condition to hide a transition from the user. The transition can only be triggered from a workflow function or from REST"
    "Only Assignee Condition", "Condition to allow only the assignee to execute a transition"
    "Only Bamboo Notifications Workflow Condition", "Only makes this transition available to the Bamboo build notifications"
    "Only Reporter Condition", "Condition to allow only the reporter to execute a transition"
    "Permission Condition", "Condition to allow only users with a certain permission to execute a transition"
    "Previous Status Condition", "Condition to check if the issue has transitioned through a specified status or no"
    "Separation of Duties condition", "Condition preventing a user to perform the transition, if the user has already performed a transition on the issue"
    "Sub-Task Blocking Condition", "Condition to block parent issue transition depending on sub-task status"
    "User Is In Any Group", "Condition to allow only users in a given group to execute a transition"
    "User Is In Any Project Role", "Condition to allow only users in a given project role to execute a transition"
    "User Is In", "Custom field	Allows only users in a given custom field to execute the transition"
    "User Is In Group", "Condition to allow only users in a given group to execute a transition"
    "User Is In Group Custom Field", "Condition to allow only users in a custom field-specified group to execute a transition"
    "User Is In Project Role", "Condition to allow only users in a given project role to execute a transition"
    "Value Field", "Allows to execute a transition if the given value of a field is equal to a constant value, or simply set"

Validators
----------
.. csv-table:: Validators
    :header: "Name", "Description"
    :widths: 20, 80

    "Date Compare Validator", "Compare two dates during a workflow transition"
    "Date Window Validator", "Compares two date fields, by adding a time span in days to one of them"
    "Field Required Validator", "Field must not be empty during the transition"
    "Field has been modified Validator", "Field value must be changed during the transition"
    "Field has single value Validator", "Multi-select Field has not more than one value during transition"
    "Parent Status Validator", "Validates that the parent issue is in required state"
    "Permission Validator", "Validates that the user has a permission"
    "Previous State Validator", "Validates that the issue has previously transitioned through a specific state"
    "Regular Expression Check", "Validate field contents against a regular expression during a workflow transition"
    "User Permission Validator", "Validates that the user has a permission, where the OSWorkflow variable holding the username is configurable. Obsolete"

Post Functions
--------------
.. csv-table:: Post Functions
    :header: "Name", "Description"
    :widths: 20, 80

    "Assign to Current User", "Assigns the issue to the current user if the current user has the 'Assignable User' permission"
    "Assign to Lead Developer", "Assigns the issue to the project/component lead developer"
    "Assign to Reporter", "Assigns the issue to the reporter"
    "Clear Field Value", "Clear value of a given field"
    "Copy Value From Other Field", "Copies the value of one field to another, either within the same issue or from parent to sub-task"
    "Create Crucible Review Workflow Function", "Creates a Crucible review for all unreviewed code for this issue"
    "Notify HipChat", "Send a notification to one or more HipChat rooms"
    "Set issue security level based on user's project role", "Set the issue's Security Level to the specified level if the current user is in a specified Project Role"
    "Trigger a Webhook", "If this post-function is executed, Jira will post the issue content in JSON format to the URL specified"
    "Update Issue Custom Field", "Updates an issue custom field to a given value"
    "Update Issue Field", "Updates a simple issue field to a given value"


Workflow Schemes
================


Assignments
===========

Workflow
--------
#. Dodaj do workflow status ``In Review``, ``Blocked``, ``In Test``
#. Przy przenoszeniu do statusu ``Done`` ma wyświetlać się okienko z logownaiem czasu
#. Przy przenoszeniu do statusu ``Blocked`` ma wyświetlać się okienko z komentarzem (przyczyna zablokowania)

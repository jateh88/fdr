# FDR Checker #

## Validation Rules ##
#### ID ####
- column exists (WorkItemObject)
- not empty (WorkItemObject)
- sorts alphabetically (CascadeObject)
#### Cascade Block ####
- column exists (WorkItemObject)
- one and only one cell gets marked (WorkItemObject)
- no missing steps (CascadeObject)
- all threads start w/ Procedure Step (CascadeObject)
- each thread terminates in 'F' or 'C' (CascadeObject)
- all DO Solution levels get used (CascadeObject)
#### Cascade Level ####
- column exists (WorkItemObject)
- not empty (WorkItemObject)
- validated input list (WorkItemObject)
- matches selection in Cascade Block (WorkItemObject)
#### Requirement Statement ####
- column exists (WorkItemObject)
- Not empty (WorkItemObject)
- CHILD - valid pointer (CascadeObject)
- ADDITIONALPARENT - valid pointer (CascadeObject)
- check for ______ hashtags e.g. #Function, #MatingParts (WorkItemObject)
- report on extra tags found? (WorkItemObject)
#### Requirement Rationale ####
- column exists (WorkItemObject)
- not empty (WorkItemObject)
#### VorV Strategy ####
- column exists (WorkItemObject)
- not empty (WorkItemObject)
#### VorV Results ####
- column exists (WorkItemObject)
- not empty (WorkItemObject)
#### Devices ####
- column exists (WorkItemObject)
- not empty (WorkItemObject)
#### DO Features... ####
- column exists (WorkItemObject)
- not empty (WorkItemObject)
#### CTQ ####
- column exists (WorkItemObject)
- not empty (WorkItemObject)
- validated input list (WorkItemObject)
#### Other ####
- 'N/A' check? (WorkItemObject)
- color? 

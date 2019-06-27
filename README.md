# FDR Checker #

## What to Check For ##
#### ID ####
- not empty (WorkItemObject)
- sorts alphabetically (CascadeObject)
#### Cascade Block ####
- One and only one cell gets marked (WorkItemObject)
- no missing steps (CascadeObject)
- All threads start w/ Procedure Step (CascadeObject)
- Each thread terminates in 'F' or 'C' (CascadeObject)
- All DO Solution levels get used (CascadeObject)
#### Cascade Level ####
- not empty (WorkItemObject)
- validated input list (WorkItemObject)
#### Requirement Statement ####
- Not empty (WorkItemObject)
- #Child - valid pointer (CascadeObject)
- #AdditionalParent - valid pointer (CascadeObject)
- Check for ______ hashtags e.g. #Function, #MatingParts (WorkItemObject)
#### Requirement Rationale ####
- not empty (WorkItemObject)
#### VorV Strategy ####
- not empty (WorkItemObject)
#### VorV Results ####
- not empty (WorkItemObject)
#### Devices ####
- not empty (WorkItemObject)
#### DO Features... ####
- not empty (WorkItemObject)
#### CTQ ####
- not empty (WorkItemObject)
- validated input list (WorkItemObject)
#### Other ####
- 'N/A' check? (WorkItemObject)
  
## Structure ##

### Cascade Object ###
- Container for Work Item objects
- Calls all checks (even if the check is performed within the Work Item object)
- Contains graph
  - as edge list?
  - should this be its own object? Depends on how I implement the parent/child checker

### Work Item Objects ###
- unique key = row #
- contains dictionary of entire row

## Notes ##
- openpyxl - reads empty cells as None or ''?

  

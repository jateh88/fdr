# FDR Checker #

## What to Check For ##
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
  
## Structure ##

### main.py ###
- instantiate Logger
- instantiate ExcelDataHandler object
  - future feature: allow user to input path
  - future feature: use GOOEY or other GUI emulator to make it easier.
- instantiate Cascade object
- call Cascade VALIDATE method

### ExcelDataHandler ###
- very similar to Mentoring Matchmaker
- object that stores the path, calls openpyxl
- check for duplicate headers

INIT method
- set READY to default (FALSE)
- openpyxl: read excel sheet from data folder
- report error if more than one is found
- if worksheet exists:
  - loop thru cells
  - return list of dictionaries (row not needed; will be inferred from list position)
- else: return False
- if all checks out, set READY to True

READY method
- (checked by Cascade object before it does its calculating)

### Cascade Object ###
Description: 
- container for Work Item objects
- single public function that calls all checks (even if the check is performed within the Work Item object)
- contains graph
  - as edge list?
  - should this be its own object? Depends on how I implement the parent/child checker
  
INIT method
- take list of dictionaries
- for row in list:
  - instantiate WorkItem object with row # and dictionary
  - add WorkItem object to internal list (set? list?)

VALIDATE method
- Sequentially call all Cascade-level validations
- for work_item in work_items:
  - call WorkItem-level validations
 
VALIDATE ID method (private)
- log: "Checking ID column ..."
- column exists
    - Check just first item in list
    - Found! (or)
    - ERROR: column not found
- not empty (WorkItemObject)
    - loop thru all WorkItems
    - log number of IDs found
    - log number of missing IDs
    - check that they are all unique (can do this by creating set from list and counting items)
    - use ID-LARGER-THAN to check that each ID is larger than the previous.

### Work Item Objects ###
- unique key = row #
- contains dictionary of entire row

Function:
- init takes row #, dictionary

ID-LARGER-THAN(work item that should have smaller ID)
- compare [id]
  
## Notes ##
- openpyxl - reads empty cells as None or ''?

  

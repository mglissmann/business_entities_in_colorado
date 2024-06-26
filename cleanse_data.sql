-- Step 1: Fill missing principalcountry values with 'US'
UPDATE colorado
SET principalcountry = 'US'
WHERE principalcountry IS NULL;

-- Step 2: Standardize capitalization
UPDATE colorado
SET 
    agentprincipaladdress1 = UPPER(agentprincipaladdress1),
    agentprincipalcity = UPPER(agentprincipalcity),
    agentprincipalcountry = UPPER(agentprincipalcountry),
    entityname = UPPER(entityname),
    principaladdress1 = UPPER(principaladdress1),
    principalcity = UPPER(principalcity),
    principalcountry = UPPER(principalcountry);

-- Step 3: Extract date from timestamp
UPDATE colorado
SET entityformdate = DATE(entityformdate);

-- Step 4: Create a new table without columns with majority null values
CREATE TABLE colorado_new AS
SELECT
    entityid,
    entityname,
    principaladdress1,
    principalcity,
    principalstate,
    principalzipcode,
    principalcountry,
    entitystatus,
    jurisdictonofformation,
    entitytype,
    agentfirstname,
    agentlastname,
    agentprincipaladdress1,
    agentprincipalcity,
    agentprincipalstate,
    agentprincipalzipcode,
    agentprincipalcountry,
    entityformdate
FROM colorado;

-- Drop the old table and rename the new table
DROP TABLE colorado;

ALTER TABLE colorado_new RENAME TO colorado;

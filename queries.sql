-- database: /Users/Mark1/Documents/Data Science/business_entities_in_colorado/business_entities.db

--f Use the ▷ button in the top right corner to run the entire file.

SELECT count(*) FROM colorado;

SELECT
    entityid,
    entityname
FROM colorado
LIMIT 10;
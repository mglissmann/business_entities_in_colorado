-- database: /Users/Mark1/Documents/Data Science/business_entities_in_colorado/business_entities.db

-- Use the ▷ button in the top right corner to run the entire file.

SELECT 
    principalstate,
    count(entityid) as num_businesses
FROM colorado
GROUP BY principalstate
ORDER BY num_businesses DESC;

SELECT
    MIN(entityformdate) as min_entityformdate,
    MAX(entityformdate) as max_entityformdate
FROM colorado;

    
SELECT
    entityformyear,
    count(entityid) as num_entities,
    count(DISTINCT entityid) as num_unique_entities
FROM (    
    SELECT
        entityid,
        strftime('%Y', entityformdate) as entityformyear
    FROM colorado)
GROUP BY entityformyear
ORDER BY entityformyear ASC;


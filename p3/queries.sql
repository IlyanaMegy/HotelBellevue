--1 Le prix total des commandes contenant plus de 5 articles diff é rents
-- 1.1 -> Réduction de 25% sur le prix du produit à l'unité avant multiplication à la quantité
SELECT
    *,
    ("UnitPrice" -("UnitPrice" * "Discount")) * "Quantity" as "Prix Total"
FROM
    "OrderDetail"
group by("OrderId")
ORDER BY
    count("OrderId") DESC
LIMIT
    4


-- 1.2 -> Réduction de 0.25% sur le prix du produit à l'unité avant multiplication à la quantité
SELECT
    *,
    (
        ("UnitPrice" -("UnitPrice" * ("Discount" / 100))) * "Quantity"
    ) as "Prix Total"
FROM
    "OrderDetail"
group by("OrderId")
ORDER BY
    count("OrderId") DESC
LIMIT
    4



-- 1.3 -> Réduction de 25% sur le prix total
SELECT
    *,
    (
        ("UnitPrice" * "Quantity") - (("UnitPrice" * "Quantity") * "Discount")
    ) as "Prix Total"
FROM
    "OrderDetail"
group by("OrderId")
ORDER BY
    count("OrderId") DESC
LIMIT
    4


-- 1.3 -> Réduction de 0.25% sur le prix total
SELECT
    *,
    Round(
        ("UnitPrice" * "Quantity") - (("UnitPrice" * "Quantity") * ("Discount" / 100)),
        2
    ) as "Prix Total"
FROM
    "OrderDetail"
group by("OrderId")
ORDER BY
    count("OrderId") DESC
LIMIT
    4


-----------------------------------------


--2 La liste de tous les territoires de Peacock Margaret
SELECT
    "TerritoryDescription"
FROM
    "Territory"
    inner JOIN "EmployeeTerritory" on "Territory"."Id" = "EmployeeTerritory"."TerritoryId"
WHERE
    "EmployeeId" = '4'


-----------------------------------------


--3 La liste des clients vivant à "London"
SELECT
    *
FROM
    "Customer"
WHERE
    "City" = 'London'


-----------------------------------------


--4 La liste des clients ayant commandé pour une livraison à "London" avant 2013
SELECT
    DISTINCT "CustomerId",
    "CompanyName",
    "ContactName""ContactTitle",
    "Address",
    "City",
    "Region",
    "PostalCode",
    "Country",
    "Phone",
    "Fax"
FROM
    "Customer"
    inner JOIN "Order" on "Customer"."Id" = "Order"."CustomerId"
WHERE
    "ShipCity" = 'London'
    AND "OrderDate" LIKE '2012%'


-----------------------------------------


--5 Afficher le client qui a fait le plus de commande vers le "Brazil"
SELECT
    *,
    count(CustomerId) as Occurrence
FROM
    "Order"
WHERE
    "ShipCountry" = 'Brazil'
group by("CustomerId")
ORDER BY
    count("CustomerId") DESC
LIMIT
    1


-----------------------------------------


-- 6 Afficher la valeur total de la commande avec l'id 10260
-- -> Réduction de 25% sur le prix total de chaque ligne
SELECT
    *,
    SUM(
        ("UnitPrice" -("UnitPrice" * "Discount")) * "Quantity"
    ) as "Prix Total"
FROM
    "OrderDetail"
WHERE
    "OrderId" = ' 10260 '
ORDER BY
    "Id"


-----------------------------------------


-- 7 Afficher la valeur de toutes les commandes infèrieur à la moyenne de toutes les commandes

-- /1 calcul valeur totale de tous les commandes après réduction de 25% par ligne
SELECT
    *,
    COUNT(),
    round(
        SUM(
            ("UnitPrice" -("UnitPrice" * "Discount")) * "Quantity"
        ),
        2
    ) as "PrixTotal"
FROM
    "OrderDetail";
    
    
    
-- /2 calcul de la moyenne du Prix Total sur l'occurrence
SELECT
    *,
    round(("PrixTotal" / "occurence"), 2) as MoyennePrixTotal
FROM(
        SELECT
            *,
            COUNT() as "occurence",
            round(
                SUM(
                    ("UnitPrice" -("UnitPrice" * "Discount")) * "Quantity"
                ),
                2
            ) as "PrixTotal"
        FROM
            "OrderDetail"
    );
    
    
    
-- /3 implémentation de la Moyenne pour comparer les commandes avec une valeur inférieure à la Moyenne 
-- Je n'ai pas réussi à l'implémenter dans la requête alors je laisse le brouillon que j'ai fait et j'ai continuer la 
-- requête avec la valeur de la Moyenne qui est de 587.37

-- BROUILLON : 

-- WITH "Moyenne"("OrderDetail", "MoyennePrixTotal") as (
--     SELECT
--         *,
--         round(("PrixTotal" / "occurence"), 2) as MoyennePrixTotal
--     FROM(
--             SELECT
--                 *,
--                 COUNT() as "occurence",
--                 SUM(
--                     ("UnitPrice" -("UnitPrice" * "Discount")) * "Quantity"
--                 ) as "PrixTotal"
--             FROM
--                 "OrderDetail"
--         )
-- )
-- SELECT
--     *,
--     ("UnitPrice" -("UnitPrice" * "Discount")) * "Quantity" as "PrixTotal"
-- FROM
--     "OrderDetail",
--     "Moyenne"
-- WHERE
--     "PrixTotal" > "Moyenne"



SELECT
    *,
    ("UnitPrice" -("UnitPrice" * "Discount")) * "Quantity" as "PrixTotal"
FROM
    "OrderDetail"
WHERE
    "PrixTotal" < 587.37



--------------------------------------------------------------


-- 8 Lister tous les pays de la base de données (dans les tables employee, order, customer),
-- indiquer pour chaque pays le nombre de lignes correspondantes dans toute la base de données.
-- (Chaque pays ne doit pas appara î tre en doublon)
SELECT
    DISTINCT *
FROM
    "Customer"
    join "Supplier"
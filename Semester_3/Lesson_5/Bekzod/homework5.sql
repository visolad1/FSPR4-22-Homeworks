-- Task-4
SELECT City.Name AS City, Country.Name AS Country, CountryLanguage.Language
FROM City
JOIN Country ON City.CountryCode = Country.Code
JOIN CountryLanguage ON CountryLanguage.CountryCode = Country.Code;

-- Task-5
SELECT COUNT(City.Name) as City 
FROM Country JOIN city ON Country.Code = City.CountryCode;

-- Task-6
SELECT Country.Name, Country.Population 
FROM Country JOIN city ON Country.Code = City.CountryCode 
ORDER BY Country.Population ASC;

-- Task-7
SELECT Country.Name as Country, city.Name as City, City.Population 
FROM Country JOIN city ON Country.Code = City.CountryCode 
WHERE city.Population > 500000 
GROUP BY 1 
ORDER BY 3 ASC;

-- TAsk-8
SELECT Country.Name, COUNT(CountryLanguage.Language) as Language 
FROM Country JOIN CountryLanguage ON Country.Code = CountryLanguage.CountryCode 
GROUP BY 1 
ORDER BY 2 DESC;
-- -- 4
select 
	city.CountryCode, Country.name as CountryName, city.name as CapitalName, CountryLanguage.Language
from city
	JOIN country on Country.capital = city.id
	JOIN CountryLanguage on Country.code = CountryLanguage.CountryCode
	where CountryLanguage.IsOfficial = 1
	order by 1 asc;

-- -- 5
select Country.name as CountryName, count(city.name) as NumOfCities
from City	
	join country on Country.code = city.CountryCode
	group by CountryName;

-- -- 6
select Country.name as CountryName, sum(city.Population) as CountryPopulation
from City
	join country on Country.code = city.CountryCode
	group by CountryName;
	

-- -- 7
select Country.name as CountryName, country.Population as CountryPopulation, count(city.name) as 'NumOfCities where population>500000' 
from City
	join country on Country.code = city.CountryCode
	where city.Population > 500000
	group by CountryName;

-- -- 8
select Country.name as CountryName, count(CountryLanguage.Language) as 'Number of Languages' 
from CountryLanguage
	join country on Country.code = CountryLanguage.CountryCode
	group by CountryName
	order by 2 desc;
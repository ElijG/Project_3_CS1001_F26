def population_total(counties: list[CountyDemographics]) -> int:
        total = 0 
        for county in counties:
            total = total + county.population["2014 Population"]
        return total 
# purpose is that it returns the total country population from the 2014 population list 
def filter_by_state(counties: list[CountyDemographics], state: str) -> list[CountyDemographics]:
    list = []
    for county in counties:
        if county.state == state:
            list.append(county)
    return list
#it returns a list wwith all of the counties that match the state abbreviation that is given within that part of the data
def population_by_education(counties: list[CountyDemographics], key: str) -> float:
    subPopulation = 0
    for county in counties:
        if key in county.education:
            population = county.population['2014 Population']
            percentage = county.education[key]
            subPopulation += population * percentage / 100
    return subPopulation
#returns the total estimated for the people who are in the education category takes in the list of the demographics and then key and returns a number of the people who fit 
def population_by_ethnicity(counties: list[CountyDemographics], key: str) -> float:
    total = 0.0
    for county in counties:
        if key in county.ethnicities:
            population = county.population['2014 Population']
            percentage = county.ethnicities[key]
            total += population * percentage / 100
    return total
# estimates the total amount of people in a specific ethnic category 
def population_below_poverty_level(counties: list[CountyDemographics]) -> float:
    total = 0.0
    for county in counties:
        population = county.population['2014 Population']
        percentage = county.income['Persons Below Poverty Level']
        total += population * percentage / 100
    return total
#estimates the amount of people who are below the poverty level 
def percent_by_education(counties: list[CountyDemographics], key: str) -> float:
    total_population = population_total(counties)
    if total_population == 0:
        return 0.0
    sub_population = population_by_education(counties, key)
    percentage = 100 * sub_population / total_population
    return percentage
#returns the total percentage of education 
def percent_by_ethnicity(counties: list[CountyDemographics], key: str) -> float:
    total_population = population_total(counties)
    if total_population == 0:
        return 0.0
    sub_population = population_by_ethnicity(counties, key)
    percentage = 100 * sub_population / total_population
    return percentage
# returns percentage of specific ethnicity 
def percent_below_poverty_level(counties: list[CountyDemographics]) -> float:
    total_population = population_total(counties)
    if total_population == 0:
        return 0.0
    sub_population = population_below_poverty_level(counties)
    percentage = 100 * sub_population / total_population
    return percentage
# returns the percentage who are below the poverty level within all the countys as a percentage

def education_greater_than(counties: list[CountyDemographics], key: str, threshold: float) -> list[CountyDemographics]:
    matching_counties = []
    for county in counties:
        if key in county.education and county.education[key] > threshold:
            matching_counties.append(county)
    return matching_counties
#returns the counties that match the thressholg for education percentage 
def education_less_than(counties: list[CountyDemographics], key: str, threshold: float) -> list[CountyDemographics]:
    matching_counties = []
    for county in counties:
        if key in county.education and county.education[key] < threshold:
            matching_counties.append(county)
    return matching_counties
#does the oppisite finds the ones that are below a specific threshold

def ethnicity_greater_than(counties: list[CountyDemographics], key: str, threshold: float) -> list[CountyDemographics]:
    matching_counties = []
    for county in counties:
        if key in county.ethnicities and county.ethnicities[key] > threshold:
            matching_counties.append(county)
    return matching_counties
# finds the counties with a ethnicity that is above the threshelod
def ethnicity_less_than(counties: list[CountyDemographics], key: str, threshold: float) -> list[CountyDemographics]:
    matching_counties = []
    for county in counties:
        if key in county.ethnicities and county.ethnicities[key] < threshold:
            matching_counties.append(county)
    return matching_counties
# same but finds the ethnicity within counties that are below the threshold
def below_poverty_level_greater_than(counties: list[CountyDemographics], threshold: float) -> list[CountyDemographics]:
    matching_counties = []
    for county in counties:
        if county.income['Persons Below Poverty Level'] > threshold:
            matching_counties.append(county)
    return matching_counties
# finds the counties that are above the key poverty level and returns them within a list of matching counties
def below_poverty_level_less_than(counties: list[CountyDemographics], threshold: float) -> list[CountyDemographics]:
    matching_counties = []
    for county in counties:
        if county.income['Persons Below Poverty Level'] < threshold:
            matching_counties.append(county)
    return matching_counties
# does the oppisite and finds the counties that poverty level is less than the threshold

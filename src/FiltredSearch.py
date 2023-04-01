from googlesearch import search

def googleSearchFiltred(query: str, numberOfResults: int):
    forbiddenSitesInResults = ['w3schools.com', 'geeksforgeeks.com']
    promotedSites = ["stackoverflow.com", "github.com", "cppreference.com"]
    results = []
    for site in promotedSites:
        for randomSite in search(query + " " + site, num_results=1):
            if site in randomSite:
                results.insert(0, randomSite)
                promotedSites.remove(site)
                break
    for randomSite in search(query, num_results=numberOfResults):
        if not any(site in randomSite for site in forbiddenSitesInResults):
            results.append(randomSite)
    return results

if __name__ == '__main__':   
    query = input("Enter your query: ")
    numberOfResults = int(input("Maximum number of results: "))

    results = googleSearchFiltred(query, numberOfResults)
    print("Search results:")
    for searchResult, result in enumerate(results):
        if searchResult+1 <= numberOfResults:
            print(f"{searchResult+1}. {result}")
        else:
            break

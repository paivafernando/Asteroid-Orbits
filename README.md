# REST API: Asteroid Orbits

Use the HTTP GET method to retrieve information from a database of asteroids. Query `https://jsonmock.hackerrank.com/api/asteroids` to find all the records. To use the search feature, add `/search?` followed by a parameter and keyword, which is case insensitive. If the keyword exists in the parameter's value, it is included in the response.

For example, `https://jsonmock.hackerrank.com/api/asteroids/search?parameter=(keyword)`. The query result is paginated and can be further accessed by appending to the query string `?page=num`, where `num` is the page number.

The response is a JSON object with the following five fields:

* `page`: The current page of the results. (Number)
* `per_page`: The maximum number of results returned per page. (Number)
* `total`: The total number of results. (Number)
* `total_pages`: The total number of pages with results. (Number)
* `data`: Either an empty array or an array of asteroid records.

In `data`, each asteroid object has the following schema:

* `designation`: The name of the asteroid (String)
* `discovery_date`: The date of the discovery (String)
* `period_yr`: The period of rotation in years (String)
* `orbit_class`: Orbital class of the asteroid (String)

Given the year of discovery and the value of `orbit_class`, filter the results and sort on the `period_yr` parameter. Note that `orbit_class` contains a keyword that should be present in the asteroid's orbit class parameter. In case of a tie, sort on its `designation` ascending. Return the list of designations. If `period_yr` does not exist for an asteroid, assume its value as 1.
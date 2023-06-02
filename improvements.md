# Thoughts what to improve

Using uvicorn and async django was my own initiative to play around with this solution, because I haven't had a chance to try async django yet.

Initial request takes near 30 seconds, because we need to fetch all planets and store them in DB. Further requests take on average 12-13 seconds using prefetched planets.


- Separate client and server, move to REST architecture
- For sake of performance, save homeworlds in cache for fast access, and refetch them from API using celery task once daily (consider if homeworlds are permanent or can change)

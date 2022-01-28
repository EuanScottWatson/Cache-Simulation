# Cache Modelling Simulation
A simple cache simulator done as part of my university course to model the hit and miss rate of a cache.
## Running the Simulation
To run the simulation simply install all the required modules using:
```
python -m venv env
.\env\Scripts\Activate.ps1
pip install -r requirements.txt
```
Then run the actual code with:
```
python model.py <M> <N> <T> <cacheType>
```
Where cacheType is either "LRU" or "FIFO" for the current implementation. </br>
Once the simulation has completed you will be met with a graph of the hit ratio which will also be saved as a png under the foler ./graphs </br>
To implement a new type of cache, simply inherit from the `Cache` class and implement the `hit()` and `evict()` functions, then add the type of cache to the model's conditional statement, choosing which cache to instantiate.

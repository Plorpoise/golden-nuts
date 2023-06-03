# golden-nuts
This is the repository for the golden nuts project. 

#Running Unit Tests
##Setup
We are using the pytest library for our unit tests. In order to be able to run the tests, it is recommended to clone the repository. Then, install pytest by running `pip install pytest` or `pip install -r requirements` to install all required dependencies for the entire program.  

## Running the test
To run the test, navigate to the repository directory in the command line and run `pytest`. Currently there are missing pieces of code, so the test will not complete, but the unit test framework is laid out for when the correct modules are implemented. The unit test files are located under tests/ 

#Running BDD Tests
## Setup
Setup is the same for the unit tests, but you must have the behave python library installed. Use `pip install behave` or `pip install -r requirements.txt` to install it. 

## Running the tests
To run the test, navigate to the repository directory and run `behave` from the command line. This will run through the gherkin files and run the corresponding feature tests. Similar to the unit tests, the codebase is not developed currently, so it will report missing modules. However, they are all defined in the .feature files and in the files under features/steps. 

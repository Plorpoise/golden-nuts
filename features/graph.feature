Feature: Weight flow rate graph of given ingredient is shown
	As a production manager 
	I want to visualize tree nut weight data using graphs 
	So that I can make informed decisions to optimize the production process

	Scenario: Create and display the graph over the given time interval
		Given that a manager wants to see tree nut weight flow rate
		When the graph tab is selected
		And the “tree nut” ingredient box is checked
		And the start date box filled with quarters start day
		And the end date box is filled with the last day of the quarters first month
		And the create graph button is clicked
		Then a graph is generated showing the weight flow rate of tree nuts over the "current quarters first month"
	
	Scenario: Create and display the graph from start date to current day of current quarter
		Given that a manager wants to see tree nut weight flow rate
		When the graph tab is selected
		And the “tree nut” ingredient box is checked
		And the start date box filled with quarters start day
		And the end date box is not filled out
		And the create graph button is clicked
		Then a graph is generated showing the weight flow rate of tree nuts over the "entire current quarter"

Feature: Incorrect input causes error message to display
	As a production manager 
	I want to visualize tree nut weight data using graphs 
	So that I can make informed decisions to optimize the production process
	
	Scenario: Wrong ingredient input, display error message with reason
		Given that a manager wants to see tree nut weight flow rate
		When the graph tab is selected
		And no ingredient box is checked
		And the start date box filled with quarters start day
		And the end date box filled with the current days date
		And the create graph button is clicked
		Then an error message is displayed saying to check the ingredient/s to be displayed labeled above the graph box
	
	Scenario: Wrong start date input, display error message with reason and example
		Given that a manager wants to see tree nut weight flow rate
		When the graph tab is selected
		And the “tree nut” ingredient box is checked
		And the start date box is not filled out
		And the end date box filled with the current days date
		And the create graph button is clicked
		Then an error message is displayed saying to input the start date box with the correct format example “[MM-DD-YYYY]”

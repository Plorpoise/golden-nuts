from behave import *
import GUIController
import main
import pandas as pd
from datetime import datetime

@given('that a manager wants to see tree nut weight flow rate')
def manager_nut_weight_flow_rate(context):
    context.controller = GUIController()
    context.controller.init_gui()

@when('the graph tab is selected')
def select_graph_tab(context):
    context.controller.select_tab(context.controller.Tabs.GRAPH)
    
@when('the “tree nut” ingredient box is checked')
def check_tree_nut_box(context):
    context.controller.toggle_box(context.controller.Boxes.TREE_NUT)
    
@when('the start date box filled with quarters start day')
def fill_start_date_with_quarter_start(context):
    context.controller.set_text_field(context.controller.text_field.START_DATE, "01/01/2023")

@when('the start date box is not filled')
def start_date_not_filled(context):
    context.controller.set_text_field(context.controller.text_field.START_DATE, "")

@when('the end date box filled with the current days date')
def fill_end_date_with_current_day_date(context):
    context.controller.set_text_field(context.controller.text_field.END_DATE, "04/01/2023")

@when('the create graph button is clicked')
def click_create_graph_button(context):
    context.controller.click(context.controller.Button.CREATE_GRAPH)

@then('a graph is generated showing the weight flow rate of tree nuts over the current quarter first month')
def check_graph_content_vs_model_content(context):
    graph_data = context.controller.get_model_graph_data()
    assert pd.notna(graph_data)
    assert graph_data is pd.DataFrame
    
    date_data = main.load_from_date_range("01/01/2023", "04/01/2023")

    assert graph_data.equals(date_data)

# Scenario: Create and display the graph over the given time interval
@when('the end date box is filled with the last day of the quarters first month')
def fill_end_date_with_quarter_end(context):
    context.controller.set_text_field(context.controller.text_field.END_DATE, "01/31/2023")

# Scenario: Create and display the graph from start date to current day of current quarter
@when('the end date box is not filled out')
def end_date_not_filled(context):
    context.controller.set_text_field(context.controller.text_field.END_DATE, "")

@then('a graph is generated showing the weight flow rate of tree nuts over the "entire current quarter"')
def check_graph_content_for_entire_quarter(context):
    graph_data = context.controller.get_model_graph_data()
    assert pd.notna(graph_data)
    assert graph_data is pd.DataFrame
    
    # Assuming we have a function to get the current quarter's data
    quarter_data = main.load_current_quarter_data()
    
    assert graph_data.equals(quarter_data)

# Scenario: Wrong ingredient input, display error message with reason
@when('no ingredient box is checked')
def no_ingredient_checked(context):
    context.controller.uncheck_all_boxes()

@then('an error message is displayed saying to check the ingredient/s to be displayed labeled above the graph box')
def check_error_message_for_ingredient(context):
    error_message = context.controller.get_error_message()
    expected_message = "Please check the ingredient/s to be displayed labeled above the graph box"
    assert error_message == expected_message

# Scenario: Wrong start date input, display error message with reason and example
@then('an error message is displayed saying to input the start date box with the correct format example “[MM-DD-YYYY]”')
def check_error_message_for_start_date(context):
    error_message = context.controller.get_error_message()
    expected_message = "Please input the start date box with the correct format example [MM-DD-YYYY]"
    assert error_message == expected_message



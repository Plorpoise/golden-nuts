from behave import *

@given('that a manager wants to see tree nut weight flow rate')
def step_impl(context):
    pass

@when('the graph tab is selected')
def step_impl(context):
    if context.selectedTab == graph:
        pass
    
@when('the “tree nut” ingredient box is checked')
def step_impl(context):
    pass
    
@when('the start date box filled with quarters start day')
def step_impl(context):
    pass

@when('the end date box filled with the current days date')
def step_impl(context):
    pass

@when('the create graph button is clicked')
def step_impl(context):
    pass

@then('a graph is generated showing the weight flow rate of tree nuts over the current quarter first month')
def step_impl(context):
    pass


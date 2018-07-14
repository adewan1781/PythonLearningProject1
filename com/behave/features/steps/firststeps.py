# from behave import *
from behave import given, when, then


@given(u'two nos a and b')
def step_impl(self):
    self.a = 5
    self.b = 6


@when(u'I add two numbers')
def step_impl2(self):
   self.sum = self.a + self.b

@then(u'the sum must be greater than ten')
def step_impl3(self):
    assert (self.sum>10), "sum is not greater than 10"
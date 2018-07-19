# from behave import *
from behave import given, when, then


@given(u'two nos a and b')
def step_impl(self):
    self.a = 5
    self.b = 6

@when(u'I add two numbers')
def step_impl2(self):
   self.answer = self.a + self.b

@then(u'the result must be greater than ten')
def step_impl(self):
    assert (self.answer > 10), "result is not greater than 10"


@when(u'I sub two numbers')
def step_impl(self):
    self.answer = self.a - self.b


@when(u'I multiply two numbers')
def step_impl(self):
    self.answer = self.a * self.b


@when(u'I divide two numbers')
def step_impl(self):
    self.answer = self.a / self.b

@then(u'the result must be less than ten')
def step_impl(self):
    assert (self.answer < 10), "result is not less than 10"
from ._anvil_designer import Form1Template
from anvil import *
import anvil.users
import anvil.server

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    # pass
    msg = anvil.server.call('rheaModel')
    if msg[0] >= 0.75 and msg[1] == 1:
      alert("Using our algorithm, we've deemed this user has displayed a pattern in Suicidal Ideation. We've alerted the RCMP.")
    else: 
      alert("Using our algorithm, we could not determine a pattern indicating Suicidal Ideation in the user. However, at your own discretion, please alert your local emergency center or RCMP.")
  
  def button_3_click(self, **event_args):
    open_form('Form1.Form2')

  def button_2_click(self, **event_args):
    open_form('Form1.Form3')

  def button_4_click(self, **event_args):
    open_form('ControlPanel')






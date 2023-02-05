from ._anvil_designer import Form3Template
from anvil import *
import anvil.users
import anvil.server

class Form3(Form3Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    # pass
    msg = anvil.server.call_s('rheaModel')
    if msg > 0.7:
      alert("Using our algorithm, we've deemed this user has SI (suicidal ideation). We've alerted the RCMP.")
    else:
      alert("Using our algorithm, we could not  determine a concrete pattern in user SI (suicidal ideation). However, at your own discretion, please alert your local emergency center or RCMP.")

  def button_3_click(self, **event_args):
    open_form('Form1.Form2')

  def button_4_click(self, **event_args):
    open_form('Form1')

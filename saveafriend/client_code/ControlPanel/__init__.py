from ._anvil_designer import ControlPanelTemplate
from anvil import *
import anvil.users
import tables
from tables import app_tables
import anvil.server

class ControlPanel(ControlPanelTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.repeating_panel_1.items = anvil.server.call('get_submissions')
    # self.image_1.source = media_obj
    # Any code you write here will run before the form opens.
    anvil.users.login_with_form()
    



  def button_1_click(self, **event_args):
    # pass
    msg = anvil.server.call('rheaModel')
    if msg[0] >= 0.7 and msg[1] == 1:
      alert("Using our algorithm, we've deemed this user has displayed a pattern in Suicidal Ideation. We've alerted the RCMP.")
    else:
      alert("Using our algorithm, we could not determine a pattern indicating Suicidal Ideation in the user. However, at your own discretion, please alert your local emergency center or RCMP.")

  def button_3_click(self, **event_args):
    open_form('Form1.Form2')

  def button_2_click(self, **event_args):
    open_form('Form1.Form3')

  def search(self, **event_args):
    self.repeating_panel_1.items = anvil.server.call(
      'search_submissions',
      self.text_box_search.text
    )

  def button_report_click(self, **event_args):
    open_form('ControlPanel.AccuracyReport')



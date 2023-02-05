from ._anvil_designer import AccuracyReportTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
import tables
from tables import app_tables
import anvil.server

class AccuracyReport(AccuracyReportTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    media_obj = anvil.server.call('make_plot')
    self.image_1.source = media_obj
    msg = anvil.server.call('rheaModel')
    self.label_auc.text = str(msg[0])
    # Any code you write here will run before the form opens.
    if msg[0] >= 0.75: 
      self.label_prediction.text = "Confident in its prediction."
    else: 
      self.label_prediction.text = "Less confident in its prediction."
    
  def button_3_click(self, **event_args):
    open_form('Form1.Form2')

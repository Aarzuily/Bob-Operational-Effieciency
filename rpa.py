import clr
clr.AddReference('UiPath')
from UiPath import *

# Initialize UiPath Application Scope
app = ApplicationScope('C:\\Path\\to\\Your\\UiPath\\Project')

# Example: Automate login process
app.InvokeWorkflowFile('Login.xaml')

# Example: Automate data entry in a banking form
app.InvokeWorkflowFile('DataEntry.xaml')

# Close the application scope
app.Close()

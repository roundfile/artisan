
import prettytable
import re
from PyQt5.QtWidgets import QApplication
def u(x):
    return str(x)
if True:  #here just to achieve the indent
    if True:
# ----- Cut below ---------------------------------------------

        # autogenerated help pasted below

        newline = "\n"  #@UnusedVariable
        helpstr = ""
        helpstr += "<head><style>"
        helpstr += "td, th {border: 1px solid #ddd;  padding: 6px;}"
        helpstr += "th {padding-top: 6px;padding-bottom: 6px;text-align: left;background-color: #0C6AA6; color: white;}"
        helpstr += "</style></head>"
        helpstr += "<body>"
        helpstr += "<b>" + u(QApplication.translate('HelpDlg','EVENT ANNOTATIONS',None)) + "</b>"
        tbl_Annotations = prettytable.PrettyTable()
        tbl_Annotations.field_names = [u(QApplication.translate('HelpDlg','Prefix Field',None)),u(QApplication.translate('HelpDlg','Source',None)),u(QApplication.translate('HelpDlg','Example',None))]
        tbl_Annotations.add_row(['~E1',u(QApplication.translate('HelpDlg','The value of Event type 1',None)),u(QApplication.translate('HelpDlg','Air',None))])
        tbl_Annotations.add_row(['~E2',u(QApplication.translate('HelpDlg','The value of Event type 2',None)),u(QApplication.translate('HelpDlg','Drum',None))])
        tbl_Annotations.add_row(['~E3',u(QApplication.translate('HelpDlg','The value of Event type 3',None)),u(QApplication.translate('HelpDlg','Damper',None))])
        tbl_Annotations.add_row(['~E4',u(QApplication.translate('HelpDlg','The value of Event type 4',None)),u(QApplication.translate('HelpDlg','Burner',None))])
        tbl_Annotations.add_row(['~Y1',u(QApplication.translate('HelpDlg','ET value',None)),420])
        tbl_Annotations.add_row(['~Y2',u(QApplication.translate('HelpDlg','BT value',None)),372])
        tbl_Annotations.add_row(['~dCHARGE',u(QApplication.translate('HelpDlg','Number of seconds since CHARGE',None)),522])
        tbl_Annotations.add_row(['~dFCs',u(QApplication.translate('HelpDlg','Number of seconds after FCs \nBest used inside double quotes (see notes below) \nDisplays &#39;*&#39; prior to FCs',None)),47])
        tbl_Annotations.add_row(['~preFCs',u(QApplication.translate('HelpDlg','Number of seconds before FCs \nBest used inside single quotes or back ticks (see notes below) \nDisplays &#39;*&#39; after FCs',None)),50])
        tbl_Annotations.add_row(['~DTR',u(QApplication.translate('HelpDlg','Development time ratio. Note: DTR=0 before FCs \n100*(t{Event}-t{FCs})/(t{FCs}-t{CHARGE})',None)),12])
        tbl_Annotations.add_row(['~deg',u(QApplication.translate('HelpDlg','The degree symbol',None)),'\u00b0'])
        tbl_Annotations.add_row(['~mode',u(QApplication.translate('HelpDlg','Temperature mode (&#39;C&#39; or &#39;F&#39;)',None)),'F'])
        tbl_Annotations.add_row(['~degmode',u(QApplication.translate('HelpDlg','Degree symbol with Temperature mode',None)),'\u00b0C'])
        tbl_Annotations.add_row(['~quot',u(QApplication.translate('HelpDlg','Quote symbol',None)),'"'])
        tbl_Annotations.add_row(['~squot',u(QApplication.translate('HelpDlg','Single quote symbol',None)),'&#39;'])
        helpstr += tbl_Annotations.get_html_string(attributes={"width":"100%","border":"1","padding":"1","border-collapse":"collapse"})
        tbl_Annotationsbottom = prettytable.PrettyTable()
        tbl_Annotationsbottom.header = False
        tbl_Annotationsbottom.add_row([u(QApplication.translate('HelpDlg','NOTES:',None))+newline+u(QApplication.translate('HelpDlg','-Event annotations apply for &#39;Step&#39;, &#39;Step+&#39;, and &#39;Combo&#39; Events settings',None))+newline+u(QApplication.translate('HelpDlg','',None))+newline+u(QApplication.translate('HelpDlg','-Anything between double quotes " will show only after FCs. Example: "~E1 @~DTR%"',None))+newline+u(QApplication.translate('HelpDlg','',None))+newline+u(QApplication.translate('HelpDlg','-Anything between single quotes &#39; will show only before FCs. Example: &#39;~E1 @~degmode&#39;',None))+newline+u(QApplication.translate('HelpDlg','',None))+newline+u(QApplication.translate('HelpDlg','-Anything between back ticks ` will show only within 90 seconds before FCs. Example: &#39;~E1 `FCs~dFCs sec`&#39;',None))+newline+u(QApplication.translate('HelpDlg','',None))+newline+u(QApplication.translate('HelpDlg','-When combining back ticks with single or double quotes the back ticks should be inside the quotes.',None))+newline+u(QApplication.translate('HelpDlg','',None))+newline+u(QApplication.translate('HelpDlg','-Background event annotations can be seen during a roast when &#39;Annotations&#39; is checked in the Profile Background window.',None))+newline+u(QApplication.translate('HelpDlg','',None))+newline+u(QApplication.translate('HelpDlg','-Simple scaling of the fields E1, E2, E3, and E4 is possible. Use a single math operator (&#39;*&#39;, &#39;/&#39;, &#39;+&#39; or &#39;-&#39;) immediately following the field name.',None))+newline+u(QApplication.translate('HelpDlg','Examples:',None))+newline+u(QApplication.translate('HelpDlg','&#39;~E1/10&#39; will divide the E1 value by 10.',None))+newline+u(QApplication.translate('HelpDlg','&#39;~E2+5&#39; adds 5 to the the value of E2.',None))+newline+u(QApplication.translate('HelpDlg','',None))+newline+u(QApplication.translate('HelpDlg','-Another style of annotations allows to replace an event&#39;s numeric value with a text string. One example where this can be useful is when an event is used to record sensory milestones. The value 20 might be used for &#39;Fresh Cut Grass&#39; aroma, 50 for &#39;Hay&#39;, 80 for &#39;Baking Bread&#39;, and 100 to represent the &#39;A Point&#39;. ',None))+newline+u(QApplication.translate('HelpDlg','This form of annotation must be enclosed in curly brackets &#39;{}&#39;. The first entry must be one the event fields ~E1, ~E2, ~E3, or ~E4 followed immediately by the vertical bar &#39;|&#39;, a numeric value and the text to use for the annotation. This may be followed by additional groups of vertical bars, numeric values, and text. ',None))+newline+u(QApplication.translate('HelpDlg','The following Annotation string (without the quote marks) implements this example assuming E4 is used to record the sensory milestones. Note that the BT is added to the annotation.',None))+newline+u(QApplication.translate('HelpDlg','{~E4|20Fresh Cut Grass|50Hay|80Baking Bread|100A Point} @~Y2~degmode',None))])
        helpstr += tbl_Annotationsbottom.get_html_string(attributes={"width":"100%","border":"1","padding":"1","border-collapse":"collapse"})
        helpstr += "</body>"
        helpstr = re.sub(r"&amp;", r"&",helpstr)

        # autogenerated help pasted above

# ----- Cut above ---------------------------------------------
outfile = open('../output_files/eventannotations.html','w')
outfile.write(helpstr)
outfile.close()
outfile = open('../output_files/help.html','w')
outfile.write(helpstr)
outfile.close()
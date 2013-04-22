# -*- coding: cp1252 -*-
import wx

class SemPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent,size=(200,1000))
        self.frame = parent
        self.mainSizer = wx.BoxSizer(wx.VERTICAL)
        labelSizer = wx.BoxSizer(wx.HORIZONTAL)
        g_and_uLabelSizer = wx.BoxSizer(wx.HORIZONTAL)
        g_and_uSizer = wx.BoxSizer(wx.VERTICAL)
        self.sem_no = wx.StaticText(self, label="Sem",pos = (50,10), style=wx.ALIGN_CENTRE)
        gLabel = wx.StaticText(self, label="G",pos = (30,40), style=wx.ALIGN_CENTRE)
        uLabel = wx.StaticText(self, label="U",pos = (100,40), style=wx.ALIGN_CENTRE)
        grades = ['A', 'A-', 'B', 'B-', 'C','C-','D','E']
        units = ['1', '2', '3', '4', '5']
        self.grades_cb0 = wx.ComboBox(self, pos=(20, 70), choices=grades, style=wx.CB_READONLY)
        self.units_cb0 = wx.ComboBox(self, pos=(90, 70), choices=units, style=wx.CB_READONLY)
        g_and_uSizer.Add(self.grades_cb0, 1, wx.EXPAND)
        self.units_cb0.Select(n=2)
        g_and_uSizer.Add(self.units_cb0, 1, wx.EXPAND)
        self.grades_cb1 = wx.ComboBox(self, pos=(20, 125), choices=grades, style=wx.CB_READONLY)
        self.units_cb1 = wx.ComboBox(self, pos=(90, 125), choices=units, style=wx.CB_READONLY)
        g_and_uSizer.Add(self.grades_cb1, 1, wx.EXPAND)
        self.units_cb1.Select(n=2)
        g_and_uSizer.Add(self.units_cb1, 1, wx.EXPAND)
        self.grades_cb2 = wx.ComboBox(self, pos=(20, 185), choices=grades, style=wx.CB_READONLY)
        self.units_cb2 = wx.ComboBox(self, pos=(90, 185), choices=units, style=wx.CB_READONLY)
        g_and_uSizer.Add(self.grades_cb2, 1, wx.EXPAND)
        self.units_cb2.Select(n=2)
        g_and_uSizer.Add(self.units_cb2, 1, wx.EXPAND)
        self.grades_cb3 = wx.ComboBox(self, pos=(20, 245), choices=grades, style=wx.CB_READONLY)
        self.units_cb3 = wx.ComboBox(self, pos=(90, 245), choices=units, style=wx.CB_READONLY)
        g_and_uSizer.Add(self.grades_cb3, 1, wx.EXPAND)
        self.units_cb3.Select(n=2)
        g_and_uSizer.Add(self.units_cb3, 1, wx.EXPAND)
        self.grades_cb4 = wx.ComboBox(self, pos=(20, 305), choices=grades, style=wx.CB_READONLY)
        self.units_cb4 = wx.ComboBox(self, pos=(90, 305), choices=units, style=wx.CB_READONLY)
        g_and_uSizer.Add(self.grades_cb4, 1, wx.EXPAND)
        self.units_cb4.Select(n=2)
        g_and_uSizer.Add(self.units_cb4, 1, wx.EXPAND)
        self.grades_cb5 = wx.ComboBox(self, pos=(20, 365), choices=grades, style=wx.CB_READONLY)
        self.units_cb5 = wx.ComboBox(self, pos=(90, 365), choices=units, style=wx.CB_READONLY)
        g_and_uSizer.Add(self.grades_cb5, 1, wx.EXPAND)
        self.units_cb5.Select(n=2)
        g_and_uSizer.Add(self.units_cb5, 1, wx.EXPAND)
        self.grades_cb6 = wx.ComboBox(self, pos=(20, 425), choices=grades, style=wx.CB_READONLY)
        self.units_cb6 = wx.ComboBox(self, pos=(90, 425), choices=units, style=wx.CB_READONLY)
        g_and_uSizer.Add(self.grades_cb6, 1, wx.EXPAND)
        self.units_cb6.Select(n=2)
        g_and_uSizer.Add(self.units_cb6, 1, wx.EXPAND)
        self.grades_cb7 = wx.ComboBox(self, pos=(20, 485), choices=grades, style=wx.CB_READONLY)
        self.units_cb7 = wx.ComboBox(self, pos=(90, 485), choices=units, style=wx.CB_READONLY)
        g_and_uSizer.Add(self.grades_cb7, 1, wx.EXPAND)
        self.units_cb7.Select(n=2)
        g_and_uSizer.Add(self.units_cb7, 1, wx.EXPAND)
        g_and_uLabelSizer.Add(gLabel, flag = wx.ALL)
        g_and_uLabelSizer.Add(uLabel, flag = wx.ALL)
        labelSizer.Add(self.sem_no, flag = wx.ALL)
        self.mainSizer.Add(labelSizer)
        self.mainSizer.Add(g_and_uLabelSizer)
        
class NamePanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.frame = parent
        self.nameSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.name = wx.TextCtrl(self,-1,"Enter your name",pos=(20,10), size=(120,20))
        self.nameSizer.Add(self.name, flag = wx.ALL)

class EmptyPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent,size=(200,250))

class MainAdditionalPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent,size=(250,250))

  
class PS1Panel(wx.Panel)        :
    def __init__(self, parent):
        wx.Panel.__init__(self, parent,size=(400,250))
        self.hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        
        
class AdditionalPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        units_ps2_th = ["15","18", "20"]
        ps2_th = ["PS2", "Thesis"]
        ps3_th = ["PS3", "Thesis"]
        units_ps1 = ["5", "10", "15"]
        grades = ['A', 'A-', 'B', 'B-', 'C','C-','D','E']
        self.additionalSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.hbox1 = wx.BoxSizer(wx.VERTICAL)
        self.hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        self.hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        self.hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        self.hbox5 = wx.BoxSizer(wx.HORIZONTAL)
        self.hbox1_1 = wx.BoxSizer(wx.HORIZONTAL)
        self.hbox1_2 = wx.BoxSizer(wx.HORIZONTAL)
        self.hbox1_3 = wx.BoxSizer(wx.HORIZONTAL)
        self.hbox1_4 = wx.BoxSizer(wx.HORIZONTAL)
        self.hbox1_5 = wx.BoxSizer(wx.HORIZONTAL)
        self.hbox1_11 = wx.BoxSizer(wx.VERTICAL)
        self.hbox1_12 = wx.BoxSizer(wx.HORIZONTAL)
        G_means = wx.StaticText(self, label="*G:Grade",pos = (20,20), style=wx.ALIGN_CENTRE)
        U_means = wx.StaticText(self, label="*U:No. of Units",pos = (20,50), style=wx.ALIGN_CENTRE)
        self.hbox1_11.Add(G_means, wx.ALL)
        self.hbox1_11.Add(U_means, wx.ALL)
        prevImageFile = "prev.png"
        prevImage = wx.Image(prevImageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.prevButton = wx.BitmapButton(self, id=-1, bitmap=prevImage, pos=(125, 20), size = (prevImage.GetWidth()+5, prevImage.GetHeight()+5))        
        nextImageFile = "next.png"
        nextImage = wx.Image(nextImageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.nextButton = wx.BitmapButton(self, id=-1, bitmap=nextImage, pos=(167, 20), size = (nextImage.GetWidth()+5, nextImage.GetHeight()+5))
        self.hbox1_12.Add(self.prevButton)
        self.hbox1_12.Add(self.nextButton)
        self.hbox1_1.Add(self.hbox1_11, 1, wx.EXPAND)
        self.hbox1_1.Add(self.hbox1_12, 1, wx.EXPAND)
        self.hbox1.Add(self.hbox1_1, 1, wx.EXPAND)
        G_points_label = wx.StaticText(self, label="Grade Points\nAccumulated",pos = (20,90),style=wx.ALIGN_CENTRE)
        U_points_label = wx.StaticText(self, label="Units\nCompleted",pos = (20,130), style=wx.ALIGN_CENTRE)
        self.G_points = wx.TextCtrl(self,-1,"0",pos=(120,95), size=(80,20))
        self.U_points = wx.TextCtrl(self,-1,"0",pos=(120,135), size=(80,20))
        self.hbox1_2.Add(G_points_label, wx.ALL)
        self.hbox1_2.Add(self.G_points, wx.ALL)
        self.hbox1_3.Add(U_points_label, wx.ALL)
        self.hbox1_3.Add(self.U_points, wx.ALL)
        self.cg_button = wx.Button(self, label = "Whats My CGPA?", pos=(20,170),size=(180,40))
        developer = wx.StaticText(self, label="©Sachin",pos = (20,220), style=wx.ALIGN_LEFT)
        self.hbox1_4.Add(self.cg_button, wx.ALL)
        self.hbox1.Add(self.hbox1_2, 1, wx.EXPAND)
        self.hbox1.Add(self.hbox1_3, 1, wx.EXPAND)
        self.hbox1.Add(self.hbox1_4, 1, wx.EXPAND)
        self.ps1_label = wx.StaticText(self, label="PS1:",pos = (530,40),style=wx.ALIGN_CENTRE)
        self.grades_ps1 = wx.ComboBox(self, pos=(480, 90), choices=grades, style=wx.CB_READONLY)
        self.units_ps1 = wx.ComboBox(self, pos=(550, 90), choices=units_ps1, style=wx.CB_READONLY)
        self.gLabel_ps1 = wx.StaticText(self, label="G",pos = (490,65), style=wx.ALIGN_CENTRE)
        self.uLabel_ps1 = wx.StaticText(self, label="U",pos = (560,65), style=wx.ALIGN_CENTRE)
        self.hbox2.Add(self.grades_ps1, 1, wx.EXPAND)
        self.units_ps1.Select(n=1)
        self.hbox2.Add(self.units_ps1, 1, wx.EXPAND)
        self.hbox2.Add(self.ps1_label, 1, wx.EXPAND)
        self.hbox2.Add(self.gLabel_ps1, 1, wx.EXPAND)
        self.hbox2.Add(self.uLabel_ps1, 1, wx.EXPAND)
        self.ps2_th_sem1 = wx.ComboBox(self, pos=(910, 30), choices=ps2_th, style=wx.CB_READONLY)
        self.grades_ps2_th_sem1 = wx.ComboBox(self, pos=(880, 90), choices=grades, style=wx.CB_READONLY)
        self.units_ps2_th_sem1 = wx.ComboBox(self, pos=(950, 90), choices=units_ps2_th, style=wx.CB_READONLY)
        self.gLabel_ps2_sem1 = wx.StaticText(self, label="G",pos = (890,65), style=wx.ALIGN_CENTRE)
        self.uLabel_ps2_sem1 = wx.StaticText(self, label="U",pos = (960,65), style=wx.ALIGN_CENTRE)
        self.hbox3.Add(self.grades_ps2_th_sem1, 1, wx.EXPAND)
        self.units_ps2_th_sem1.Select(n=2)
        self.ps2_th_sem1.Select(n=0)
        self.hbox3.Add(self.units_ps2_th_sem1, 1, wx.EXPAND)
        self.hbox3.Add(self.ps2_th_sem1, 1, wx.EXPAND)
        self.hbox3.Add(self.gLabel_ps2_sem1, 1, wx.EXPAND)
        self.hbox3.Add(self.uLabel_ps2_sem1, 1, wx.EXPAND)
        self.ps2_th_sem2 = wx.ComboBox(self, pos=(1050, 30), choices=ps2_th, style=wx.CB_READONLY)
        self.grades_ps2_th_sem2 = wx.ComboBox(self, pos=(1020, 90), choices=grades, style=wx.CB_READONLY)
        self.units_ps2_th_sem2 = wx.ComboBox(self, pos=(1090, 90), choices=units_ps2_th, style=wx.CB_READONLY)
        self.gLabel_ps2_sem2 = wx.StaticText(self, label="G",pos = (1030,65), style=wx.ALIGN_CENTRE)
        self.uLabel_ps2_sem2 = wx.StaticText(self, label="U",pos = (1100,65), style=wx.ALIGN_CENTRE)
        self.hbox4.Add(self.grades_ps2_th_sem2, 1, wx.EXPAND)
        self.units_ps2_th_sem2.Select(n=2)
        self.ps2_th_sem2.Select(n=0)
        self.hbox4.Add(self.units_ps2_th_sem2, 1, wx.EXPAND)
        self.hbox4.Add(self.ps2_th_sem2, 1, wx.EXPAND)
        self.hbox4.Add(self.gLabel_ps2_sem2, 1, wx.EXPAND)
        self.hbox4.Add(self.uLabel_ps2_sem2, 1, wx.EXPAND)
        #self.ps3_th = wx.ComboBox(self, pos=(1090, 60), choices=ps3_th, style=wx.CB_READONLY)
        #self.grades_ps3_th = wx.ComboBox(self, pos=(1090, 100), choices=grades, style=wx.CB_READONLY)
        #self.units_ps3_th = wx.ComboBox(self, pos=(1160, 100), choices=units_ps2_th, style=wx.CB_READONLY)
        #self.hbox5.Add(self.grades_ps3_th, 1, wx.EXPAND)
        #self.units_ps3_th.Select(n=2)
        #self.ps3_th.Select(n=0)
        #self.hbox5.Add(self.units_ps3_th, 1, wx.EXPAND)
        #self.hbox5.Add(self.ps3_th, 1, wx.EXPAND)
        self.additionalSizer.Add(self.hbox1, 0, wx.EXPAND)
        self.additionalSizer.Add(self.hbox2, 1, wx.EXPAND)
        self.additionalSizer.Add(self.hbox3, 0, wx.EXPAND)
        self.additionalSizer.Add(self.hbox4, 1, wx.EXPAND)
        

       
    
class CourseLablesPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.courseLabelSizer = wx.BoxSizer(wx.VERTICAL)
        course1 = wx.StaticText(self, label="Course 1",pos = (0,70), style=wx.ALIGN_CENTRE)
        course2 = wx.StaticText(self, label="Course 2",pos = (0,125), style=wx.ALIGN_CENTRE)
        course3 = wx.StaticText(self, label="Course 3",pos = (0,185), style=wx.ALIGN_CENTRE)
        course4 = wx.StaticText(self, label="Course 4",pos = (0,245), style=wx.ALIGN_CENTRE)
        course5 = wx.StaticText(self, label="Course 5",pos = (0,305), style=wx.ALIGN_CENTRE)
        course6 = wx.StaticText(self, label="Course 6",pos = (0,365), style=wx.ALIGN_CENTRE)
        course7 = wx.StaticText(self, label="Course 7",pos = (0,425), style=wx.ALIGN_CENTRE)
        course8 = wx.StaticText(self, label="Course 8",pos = (0,485), style=wx.ALIGN_CENTRE)
        self.courseLabelSizer.Add(course1,0,wx.EXPAND)
        self.courseLabelSizer.Add(course2,0,wx.EXPAND)
        self.courseLabelSizer.Add(course3,0,wx.EXPAND)
        self.courseLabelSizer.Add(course4,0,wx.EXPAND)
        self.courseLabelSizer.Add(course5,0,wx.EXPAND)
        self.courseLabelSizer.Add(course6,0,wx.EXPAND)
        self.courseLabelSizer.Add(course7,0,wx.EXPAND)
        self.courseLabelSizer.Add(course8,0,wx.EXPAND)
        

class MainFrame(wx.Frame):

    def __init__(self):
        self.noSemPanel = 1
        self.panelsList = []
        wx.Frame.__init__(self, parent=None, title="CGPA Calculator")
        self.fSizer = wx.BoxSizer(wx.VERTICAL)        
        self.gradesSizer = wx.BoxSizer(wx.HORIZONTAL)        
        self.namePanel = NamePanel(self)
        self.additionalPanel = AdditionalPanel(self)
        self.additionalPanel.nextButton.Bind(wx.EVT_BUTTON, self.OnNextClicked)
        self.additionalPanel.prevButton.Bind(wx.EVT_BUTTON, self.OnPrevClicked)
        self.additionalPanel.cg_button.Bind(wx.EVT_BUTTON, self.OnCGClicked)
        self.additionalPanel.prevButton.Disable()
        courseLabelPanle = CourseLablesPanel(self)
        self.panel1 = SemPanel(self)        
        self.panel2 = SemPanel(self)
        self.panel3 = SemPanel(self)        
        self.panel4 = SemPanel(self)
        self.panel5 = SemPanel(self)        
        self.panel6 = SemPanel(self)
        self.panel7 = SemPanel(self)        
        self.panel8 = SemPanel(self)
        self.panel9 = SemPanel(self)        
        self.panel10 = SemPanel(self)
        self.panel1.sem_no.SetLabel('Sem - 1')
        self.panel2.sem_no.SetLabel('Sem - 2')
        self.panel3.sem_no.SetLabel('Sem - 3')
        self.panel4.sem_no.SetLabel('Sem - 4')
        self.panel5.sem_no.SetLabel('Sem - 5')
        self.panel6.sem_no.SetLabel('Sem - 6')
        self.panel7.sem_no.SetLabel('Sem - 7')
        self.panel8.sem_no.SetLabel('Sem - 8')
        self.panel9.sem_no.SetLabel('Sem - 9')
        self.panel10.sem_no.SetLabel('Sem - 10')
        self.panel2.Show(False)
        self.panel3.Show(False)
        self.panel4.Show(False)
        self.panel5.Show(False)
        self.panel6.Show(False)
        self.panel7.Show(False)
        self.panel8.Show(False)
        self.panel9.Show(False)
        self.panel10.Show(False)
        self.additionalPanel.ps1_label.Show(False)
        self.additionalPanel.grades_ps1.Show(False)
        self.additionalPanel.units_ps1.Show(False)
        self.additionalPanel.ps2_th_sem1.Show(False)
        self.additionalPanel.grades_ps2_th_sem1.Show(False)
        self.additionalPanel.units_ps2_th_sem1.Show(False)
        self.additionalPanel.ps2_th_sem2.Show(False)
        self.additionalPanel.grades_ps2_th_sem2.Show(False)
        self.additionalPanel.units_ps2_th_sem2.Show(False)
        self.additionalPanel.gLabel_ps1.Show(False)
        self.additionalPanel.uLabel_ps1.Show(False)
        self.additionalPanel.gLabel_ps2_sem1.Show(False)
        self.additionalPanel.uLabel_ps2_sem1.Show(False)
        self.additionalPanel.gLabel_ps2_sem2.Show(False)
        self.additionalPanel.uLabel_ps2_sem2.Show(False)
        """self.panel2.Show(True)
        self.panel3.Show(True)
        self.panel4.Show(True)
        self.panel5.Show(True)
        self.panel6.Show(True)
        self.panel7.Show(True)
        self.panel8.Show(True)
        self.panel9.Show(True)
        self.panel10.Show(True)"""
        self.panelsList = [self.panel1, self.panel2, self.panel3,self.panel4, self.panel5,
                           self.panel6, self.panel7, self.panel8, self.panel9, self.panel10]
        self.SetBackgroundColour("#ededed")
        self.gradesSizer.Add(courseLabelPanle, 0, wx.EXPAND)
        self.gradesSizer.Add(self.panel1, 1, wx.EXPAND)
        self.gradesSizer.Add(self.panel2, 1, wx.EXPAND)
        self.gradesSizer.Add(self.panel3, 1, wx.EXPAND)
        self.gradesSizer.Add(self.panel4, 1, wx.EXPAND)
        self.gradesSizer.Add(self.panel5, 1, wx.EXPAND)
        self.gradesSizer.Add(self.panel6, 1, wx.EXPAND)
        self.gradesSizer.Add(self.panel7, 1, wx.EXPAND)
        self.gradesSizer.Add(self.panel8, 1, wx.EXPAND)
        self.gradesSizer.Add(self.panel9, 1, wx.EXPAND)
        self.gradesSizer.Add(self.panel10, 1, wx.EXPAND)
        self.fSizer.Add(self.namePanel, 0, wx.EXPAND)
        self.fSizer.Add(self.gradesSizer, 1, wx.EXPAND|wx.ALL, 20)
        self.fSizer.Add(self.additionalPanel, 0, wx.EXPAND)
        self.SetSizer(self.fSizer)
        self.Fit()
        self.Show()

    def OnPrevClicked(self,event):
        if self.noSemPanel > 1:
            self.additionalPanel.nextButton.Enable()
            self.panelsList[self.noSemPanel - 1].Show(False)
            self.noSemPanel = self.noSemPanel - 1
        if self.noSemPanel == 1:
            self.additionalPanel.prevButton.Disable()
        if self.noSemPanel <4:
            self.additionalPanel.ps1_label.Show(False)
            self.additionalPanel.grades_ps1.Show(False)
            self.additionalPanel.units_ps1.Show(False)
            self.additionalPanel.ps2_th_sem1.Show(False)
            self.additionalPanel.grades_ps2_th_sem1.Show(False)
            self.additionalPanel.units_ps2_th_sem1.Show(False)
            self.additionalPanel.ps2_th_sem2.Show(False)
            self.additionalPanel.grades_ps2_th_sem2.Show(False)
            self.additionalPanel.units_ps2_th_sem2.Show(False)
            self.additionalPanel.gLabel_ps1.Show(False)
            self.additionalPanel.uLabel_ps1.Show(False)
            self.additionalPanel.gLabel_ps2_sem1.Show(False)
            self.additionalPanel.uLabel_ps2_sem1.Show(False)
            self.additionalPanel.gLabel_ps2_sem2.Show(False)
            self.additionalPanel.uLabel_ps2_sem2.Show(False)
        elif 4<=self.noSemPanel <7:
            self.additionalPanel.ps1_label.Show(True)
            self.additionalPanel.grades_ps1.Show(True)
            self.additionalPanel.units_ps1.Show(True)
            self.additionalPanel.ps2_th_sem1.Show(False)
            self.additionalPanel.grades_ps2_th_sem1.Show(False)
            self.additionalPanel.units_ps2_th_sem1.Show(False)
            self.additionalPanel.ps2_th_sem2.Show(False)
            self.additionalPanel.grades_ps2_th_sem2.Show(False)
            self.additionalPanel.units_ps2_th_sem2.Show(False)
            self.additionalPanel.gLabel_ps1.Show(True)
            self.additionalPanel.uLabel_ps1.Show(True)
            self.additionalPanel.gLabel_ps2_sem1.Show(False)
            self.additionalPanel.uLabel_ps2_sem1.Show(False)
            self.additionalPanel.gLabel_ps2_sem2.Show(False)
            self.additionalPanel.uLabel_ps2_sem2.Show(False)
        elif 7<=self.noSemPanel <8:
            self.additionalPanel.ps1_label.Show(True)
            self.additionalPanel.grades_ps1.Show(True)
            self.additionalPanel.units_ps1.Show(True)
            self.additionalPanel.ps2_th_sem1.Show(True)
            self.additionalPanel.grades_ps2_th_sem1.Show(True)
            self.additionalPanel.units_ps2_th_sem1.Show(True)
            self.additionalPanel.ps2_th_sem2.Show(False)
            self.additionalPanel.grades_ps2_th_sem2.Show(False)
            self.additionalPanel.units_ps2_th_sem2.Show(False)
            self.additionalPanel.gLabel_ps1.Show(True)
            self.additionalPanel.uLabel_ps1.Show(True)
            self.additionalPanel.gLabel_ps2_sem1.Show(True)
            self.additionalPanel.uLabel_ps2_sem1.Show(True)
            self.additionalPanel.gLabel_ps2_sem2.Show(False)
            self.additionalPanel.uLabel_ps2_sem2.Show(False)
        elif self.noSemPanel >=8:
            self.additionalPanel.ps1_label.Show(True)
            self.additionalPanel.grades_ps1.Show(True)
            self.additionalPanel.units_ps1.Show(True)
            self.additionalPanel.ps2_th_sem1.Show(True)
            self.additionalPanel.grades_ps2_th_sem1.Show(True)
            self.additionalPanel.units_ps2_th_sem1.Show(True)
            self.additionalPanel.ps2_th_sem2.Show(True)
            self.additionalPanel.grades_ps2_th_sem2.Show(True)
            self.additionalPanel.units_ps2_th_sem2.Show(True)
            self.additionalPanel.gLabel_ps1.Show(True)
            self.additionalPanel.uLabel_ps1.Show(True)
            self.additionalPanel.gLabel_ps2_sem1.Show(True)
            self.additionalPanel.uLabel_ps2_sem1.Show(True)
            self.additionalPanel.gLabel_ps2_sem2.Show(True)
            self.additionalPanel.uLabel_ps2_sem2.Show(True)
        self.fSizer.Layout()
        self.Fit()

        

    def OnNextClicked(self,event):
        if self.noSemPanel < 10:
            self.additionalPanel.prevButton.Enable()
            self.panelsList[self.noSemPanel].Show(True)
            self.noSemPanel = self.noSemPanel + 1
        if self.noSemPanel == 10:
            self.additionalPanel.nextButton.Disable()
        if self.noSemPanel <4:
            self.additionalPanel.ps1_label.Show(False)
            self.additionalPanel.grades_ps1.Show(False)
            self.additionalPanel.units_ps1.Show(False)
            self.additionalPanel.ps2_th_sem1.Show(False)
            self.additionalPanel.grades_ps2_th_sem1.Show(False)
            self.additionalPanel.units_ps2_th_sem1.Show(False)
            self.additionalPanel.ps2_th_sem2.Show(False)
            self.additionalPanel.grades_ps2_th_sem2.Show(False)
            self.additionalPanel.units_ps2_th_sem2.Show(False)
            self.additionalPanel.gLabel_ps1.Show(False)
            self.additionalPanel.uLabel_ps1.Show(False)
            self.additionalPanel.gLabel_ps2_sem1.Show(False)
            self.additionalPanel.uLabel_ps2_sem1.Show(False)
            self.additionalPanel.gLabel_ps2_sem2.Show(False)
            self.additionalPanel.uLabel_ps2_sem2.Show(False)
        elif 4<= self.noSemPanel <7:
            self.additionalPanel.ps1_label.Show(True)
            self.additionalPanel.grades_ps1.Show(True)
            self.additionalPanel.units_ps1.Show(True)
            self.additionalPanel.ps2_th_sem1.Show(False)
            self.additionalPanel.grades_ps2_th_sem1.Show(False)
            self.additionalPanel.units_ps2_th_sem1.Show(False)
            self.additionalPanel.ps2_th_sem2.Show(False)
            self.additionalPanel.grades_ps2_th_sem2.Show(False)
            self.additionalPanel.units_ps2_th_sem2.Show(False)
            self.additionalPanel.gLabel_ps1.Show(True)
            self.additionalPanel.uLabel_ps1.Show(True)
            self.additionalPanel.gLabel_ps2_sem1.Show(False)
            self.additionalPanel.uLabel_ps2_sem1.Show(False)
            self.additionalPanel.gLabel_ps2_sem2.Show(False)
            self.additionalPanel.uLabel_ps2_sem2.Show(False)
        elif 7<= self.noSemPanel <8:
            self.additionalPanel.ps1_label.Show(True)
            self.additionalPanel.grades_ps1.Show(True)
            self.additionalPanel.units_ps1.Show(True)
            self.additionalPanel.ps2_th_sem1.Show(True)
            self.additionalPanel.grades_ps2_th_sem1.Show(True)
            self.additionalPanel.units_ps2_th_sem1.Show(True)
            self.additionalPanel.ps2_th_sem2.Show(False)
            self.additionalPanel.grades_ps2_th_sem2.Show(False)
            self.additionalPanel.units_ps2_th_sem2.Show(False)
            self.additionalPanel.gLabel_ps1.Show(True)
            self.additionalPanel.uLabel_ps1.Show(True)
            self.additionalPanel.gLabel_ps2_sem1.Show(True)
            self.additionalPanel.uLabel_ps2_sem1.Show(True)
            self.additionalPanel.gLabel_ps2_sem2.Show(False)
            self.additionalPanel.uLabel_ps2_sem2.Show(False)
        elif self.noSemPanel >=8:
            self.additionalPanel.ps1_label.Show(True)
            self.additionalPanel.grades_ps1.Show(True)
            self.additionalPanel.units_ps1.Show(True)
            self.additionalPanel.ps2_th_sem1.Show(True)
            self.additionalPanel.grades_ps2_th_sem1.Show(True)
            self.additionalPanel.units_ps2_th_sem1.Show(True)
            self.additionalPanel.ps2_th_sem2.Show(True)
            self.additionalPanel.grades_ps2_th_sem2.Show(True)
            self.additionalPanel.units_ps2_th_sem2.Show(True)
            self.additionalPanel.gLabel_ps1.Show(True)
            self.additionalPanel.uLabel_ps1.Show(True)
            self.additionalPanel.gLabel_ps2_sem1.Show(True)
            self.additionalPanel.uLabel_ps2_sem1.Show(True)
            self.additionalPanel.gLabel_ps2_sem2.Show(True)
            self.additionalPanel.uLabel_ps2_sem2.Show(True)
        self.fSizer.Layout()
        self.Fit()

    def OnCGClicked(self,event):
        username = self.namePanel.name.GetValue()
        if username == "Enter your name":
            username = "to the Fool who does't know his name."
        set_val = 0
        grade_points_dict = {"A":10, "A-":9, "B":8,"B-":7, "C":6, "C-":5, "D":4, "E":3}
        try:
            points_accumulated = int(self.additionalPanel.G_points.GetValue())
        except ValueError:
            points_accumulated = 0
            set_val = 1
        try:
            units_completed = int(self.additionalPanel.U_points.GetValue())
        except ValueError:
            units_completed = 0
            set_val = 1
        cgpa = 0
        if points_accumulated == 0 and units_completed == 0:
            for i in xrange(0, self.noSemPanel):
                if self.panelsList[i].grades_cb0.GetValue() != "":
                    points_accumulated += grade_points_dict[self.panelsList[i].grades_cb0.GetValue()] * int(self.panelsList[i].units_cb0.GetValue())
                    units_completed += int(self.panelsList[i].units_cb0.GetValue())
                if self.panelsList[i].grades_cb1.GetValue() != "":
                    points_accumulated += grade_points_dict[self.panelsList[i].grades_cb1.GetValue()] * int(self.panelsList[i].units_cb1.GetValue())
                    units_completed += int(self.panelsList[i].units_cb1.GetValue())
                if self.panelsList[i].grades_cb2.GetValue() != "":
                    points_accumulated += grade_points_dict[self.panelsList[i].grades_cb2.GetValue()] * int(self.panelsList[i].units_cb2.GetValue())
                    units_completed += int(self.panelsList[i].units_cb2.GetValue())
                if self.panelsList[i].grades_cb3.GetValue() != "":
                    points_accumulated += grade_points_dict[self.panelsList[i].grades_cb3.GetValue()] * int(self.panelsList[i].units_cb3.GetValue())
                    units_completed += int(self.panelsList[i].units_cb3.GetValue())
                if self.panelsList[i].grades_cb4.GetValue() != "":
                    points_accumulated += grade_points_dict[self.panelsList[i].grades_cb4.GetValue()] * int(self.panelsList[i].units_cb4.GetValue())
                    units_completed += int(self.panelsList[i].units_cb4.GetValue())
                if self.panelsList[i].grades_cb5.GetValue() != "":
                    points_accumulated += grade_points_dict[self.panelsList[i].grades_cb5.GetValue()] * int(self.panelsList[i].units_cb5.GetValue())
                    units_completed += int(self.panelsList[i].units_cb5.GetValue())
                if self.panelsList[i].grades_cb6.GetValue() != "":
                    points_accumulated += grade_points_dict[self.panelsList[i].grades_cb6.GetValue()] * int(self.panelsList[i].units_cb6.GetValue())
                    units_completed += int(self.panelsList[i].units_cb6.GetValue())
                if self.panelsList[i].grades_cb7.GetValue() != "":
                    points_accumulated += grade_points_dict[self.panelsList[i].grades_cb7.GetValue()] * int(self.panelsList[i].units_cb7.GetValue())
                    units_completed += int(self.panelsList[i].units_cb7.GetValue())
        if self.noSemPanel >=4:
            if self.additionalPanel.grades_ps1.GetValue() != "":
                points_accumulated += grade_points_dict[self.additionalPanel.grades_ps1.GetValue()] * int(self.additionalPanel.units_ps1.GetValue())
                units_completed += int(self.additionalPanel.units_ps1.GetValue())
            if 4 < self.noSemPanel <=7 and self.additionalPanel.grades_ps2_sem1.GetValue() != "":
                points_accumulated += grade_points_dict[self.additionalPanel.grades_ps2_sem1.GetValue()] * int(self.additionalPanel.units_ps2_sem1.GetValue())
                units_completed += int(self.additionalPanel.units_ps2_sem1.GetValue())
            if 7 < self.noSemPanel <=10 and self.additionalPanel.grades_ps2_sem2.GetValue() != "":
                points_accumulated += grade_points_dict[self.additionalPanel.grades_ps2_sem2.GetValue()] * int(self.additionalPanel.units_ps2_sem2.GetValue())
                units_completed += int(self.additionalPanel.units_ps2_sem2.GetValue())
        if units_completed != 0:
            cgpa = points_accumulated/(units_completed*1.0)
        if units_completed == 0 or cgpa > 10:
            wx.MessageBox("U R supposed to enter values", "U Fool", wx.OK)
        else:
            if cgpa <= 4:
                wx.MessageBox("Njoyin ACB ahhh??? your CGPA is %s"%cgpa,"ACBian",wx.OK)
            elif 4< cgpa < 6:
                wx.MessageBox("Congrats! %s OB U Hav Njoyed UR Bitsian Life To The Most ...But Plzz Do Study for the sake of ur CGPA which is %s right now" % (username,cgpa),"U Rock",wx.OK)
            elif 6<= cgpa < 8:
                wx.MessageBox("Congrats! %s Your CGPA is %s. Hey..U R an Average Bitsian at Acads." % (username,cgpa),"Average Bitsian",wx.OK)
            elif 8<= cgpa <=10:
                wx.MessageBox("Congrats! %s Your CGPA is %s. Dont study too much..." % (username,cgpa),"U BookWorm",wx.OK)
                

if __name__ == "__main__":
    app = wx.App(False)
    frame = MainFrame()
    app.MainLoop()

import Tkinter
import tkFileDialog
from Tkinter import *
import tkMessageBox
import ForExcaliburAlignV3
import ForPCOAlignV3

class myGui_tk(Tkinter.Tk):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self, parent)
        self.parent=parent
        self.initialize()
        
    def initialize(self):
        self.grid()
        
        #text entry
        self.entryVariable=Tkinter.StringVar()
        self.entry=Tkinter.Entry(self,textvariable=self.entryVariable)
        self.entry.grid(column=0,row=0,sticky='EW')
        
        #browse Excalibur
        buttonBrowse=Tkinter.Button(self,text='Browse Excalibur/Merlin file',command=self.OnBrowseClick)
        buttonBrowse.grid(column=1,row=0)  
          
        #Step in X
        self.labelVariableXsteps=Tkinter.StringVar()
        labelXsteps=Tkinter.Label(self,textvariable=self.labelVariableXsteps,anchor='w',fg='black',bg='grey')
        labelXsteps.grid(column=1, row=3, columnspan=1,rowspan=1, sticky='EW')
        self.labelVariableXsteps.set('min Row')
        
        
        self.entryVariableXsteps=Tkinter.IntVar()
        self.entryXsteps=Tkinter.Entry(self,textvariable=self.entryVariableXsteps)
        self.entryXsteps.grid(column=1,row=4,sticky='EW')
        
        #Step in Y
        self.labelVariableYsteps=Tkinter.StringVar()
        labelYsteps=Tkinter.Label(self,textvariable=self.labelVariableYsteps,anchor='w',fg='black',bg='grey')
        labelYsteps.grid(column=1, row=5, columnspan=1,rowspan=1, sticky='EW')
        self.labelVariableYsteps.set('Max row')

        
        
        self.entryVariableYsteps=Tkinter.IntVar()
        self.entryYsteps=Tkinter.Entry(self,textvariable=self.entryVariableYsteps)
        self.entryYsteps.grid(column=1,row=6,sticky='EW')
        
        #Calibration
        self.labelVariableThreshold=Tkinter.StringVar()
        labelThreshold=Tkinter.Label(self,textvariable=self.labelVariableThreshold,anchor='w',fg='black',bg='grey')
        labelThreshold.grid(column=1, row=7, columnspan=1,rowspan=1, sticky='EW')
        self.labelVariableThreshold.set('threshold')
        
        
        self.entryVariableThreshold=Tkinter.DoubleVar()
        self.entryThreshold=Tkinter.Entry(self,textvariable=self.entryVariableThreshold)
        self.entryThreshold.grid(column=1,row=8,sticky='EW')
        
        #tiltAngleExcalibur
        self.labelVariableAngle=Tkinter.StringVar()
        labelAngle=Tkinter.Label(self,textvariable=self.labelVariableAngle,anchor='w',fg='black',bg='grey')
        labelAngle.grid(column=1, row=16, columnspan=1,rowspan=1, sticky='EW')
        self.labelVariableAngle.set('Excalibur measured Angle')
        
        
        self.entryVariableAngle=Tkinter.DoubleVar()
        self.entryAngle=Tkinter.Entry(self,textvariable=self.entryVariableAngle)
        self.entryAngle.grid(column=1,row=17,sticky='EW')
        
        #tiltAngle PCO
        self.labelVariableAnglePCO=Tkinter.StringVar()
        labelAnglePCO=Tkinter.Label(self,textvariable=self.labelVariableAnglePCO,anchor='w',fg='black',bg='grey')
        labelAnglePCO.grid(column=4, row=16, columnspan=1,rowspan=1, sticky='EW')
        self.labelVariableAnglePCO.set('PCO measured Angle')
        
        
        self.entryVariableAnglePCO=Tkinter.DoubleVar()
        self.entryAnglePCO=Tkinter.Entry(self,textvariable=self.entryVariableAnglePCO)
        self.entryAnglePCO.grid(column=4,row=17,sticky='EW')
        
        

        self.entryVariable.set('/dls/i13-1/data/2017/cm16785-1/')
            
        self.entryVariableThreshold.set(1) 
        
        
        #button
        button=Tkinter.Button(self,text='process Excalibur Image',command=self.OnButtonClick)
        button.grid(column=1,row=13)
        
        
        '''
        same for PCO
        '''
        
        #text entry
        self.entryVariablePCO=Tkinter.StringVar()
        self.entryPCO=Tkinter.Entry(self,textvariable=self.entryVariablePCO)
        self.entryPCO.grid(column=3,row=0,sticky='EW')
        
        #browse Excalibur
        buttonBrowsePCO=Tkinter.Button(self,text='Browse PCO file',command=self.OnBrowsePCOClick)
        buttonBrowsePCO.grid(column=4,row=0)  
          
        #Step in X
        self.labelVariableXstepsPCO=Tkinter.StringVar()
        labelXstepsPCO=Tkinter.Label(self,textvariable=self.labelVariableXstepsPCO,anchor='w',fg='black',bg='grey')
        labelXstepsPCO.grid(column=4, row=3, columnspan=1,rowspan=1, sticky='EW')
        self.labelVariableXstepsPCO.set('Min column')
        
        
        self.entryVariableXstepsPCO=Tkinter.IntVar()
        self.entryXstepsPCO=Tkinter.Entry(self,textvariable=self.entryVariableXstepsPCO)
        self.entryXstepsPCO.grid(column=4,row=4,sticky='EW')
        
        #Step in Y
        self.labelVariableYstepsPCO=Tkinter.StringVar()
        labelYstepsPCO=Tkinter.Label(self,textvariable=self.labelVariableYstepsPCO,anchor='w',fg='black',bg='grey')
        labelYstepsPCO.grid(column=4, row=5, columnspan=1,rowspan=1, sticky='EW')
        self.labelVariableYstepsPCO.set('Max column')

        
        
        self.entryVariableYstepsPCO=Tkinter.IntVar()
        self.entryYstepsPCO=Tkinter.Entry(self,textvariable=self.entryVariableYstepsPCO)
        self.entryYstepsPCO.grid(column=4,row=6,sticky='EW')
        
        #Calibration
        self.labelVariableThresholdPCO=Tkinter.StringVar()
        labelThresholdPCO=Tkinter.Label(self,textvariable=self.labelVariableThresholdPCO,anchor='w',fg='black',bg='grey')
        labelThresholdPCO.grid(column=4, row=7, columnspan=1,rowspan=1, sticky='EW')
        self.labelVariableThresholdPCO.set('threshold')
        
        
        self.entryVariableThresholdPCO=Tkinter.DoubleVar()
        self.entryThresholdPCO=Tkinter.Entry(self,textvariable=self.entryVariableThresholdPCO)
        self.entryThresholdPCO.grid(column=4,row=8,sticky='EW')
        

        self.entryVariable.set('/dls/i13-1/data/2017/mt17254-1/raw/123845.nxs')
        self.entryVariablePCO.set('/dls/i13-1/data/2017/mt17254-1/raw/pco1-123847.hdf')
            
        self.entryVariableThreshold.set(1) 
        self.entryVariableThresholdPCO.set(200) 
        
        
        #button
        button=Tkinter.Button(self,text='process PCO image',command=self.OnButtonPCOClick)
        button.grid(column=4,row=13)
        
        
        
        
        
        
               
        self.grid_columnconfigure(0, weight=1)
        self.resizable(True, False)
        self.update()
        self.geometry(self.geometry())
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)
    '''    
    def HDF5Message(self):
        if self.v.get()==1:
            print 'HDF5'
            self.labelVariable.set('Enter below the name of the Nexus tree entry containing the data.')
            self.entryVariableData.set('data')
        else:
            print 'TIF'
            self.labelVariable.set('Enter below the name of the Nexus tree entry containing the path to the folder.')
            self.entryVariableData.set('file_name')
    '''        
    def ROIMessage(self):
        if self.v2.get()==0:
            self.v2.set(1)
            print 'Select ROI'
            #label
            
            
    def btnCallBack(self):
        #v=self.v.get()
        var=self.entryVariable.get()
        #dataFolder=self.entryVariableData.get()
        minRow=self.entryVariableXsteps.get()
        maxRow=self.entryVariableYsteps.get()
        threshold=self.entryVariableThreshold.get()
        #xc=self.entryVariableTBarrelCentreX.get()
        #yc=self.entryVariableTBarrelCentreY.get()
        #kBest=self.entryVariableTBarrelParameter.get()
        #minEnergy=self.entryVariableDataROIMin.get()
        #maxEnergy=self.entryVariableDataROIMax.get()
        excaliburAngle=ForExcaliburAlignV3.findContour(var,'data',minRow,maxRow, threshold)
        self.entryVariableAngle.set(excaliburAngle)
    def btnPCOCallBack(self):
        #v=self.v.get()
        var=self.entryVariablePCO.get()
        #dataFolder=self.entryVariableData.get()
        minCol=self.entryVariableXstepsPCO.get()
        maxCol=self.entryVariableYstepsPCO.get()
        threshold=self.entryVariableThresholdPCO.get()
        #xc=self.entryVariableTBarrelCentreX.get()
        #yc=self.entryVariableTBarrelCentreY.get()
        #kBest=self.entryVariableTBarrelParameter.get()
        #minEnergy=self.entryVariableDataROIMin.get()
        #maxEnergy=self.entryVariableDataROIMax.get()
        pcoAngle=ForPCOAlignV3.findContour(var,'data',minCol,maxCol, 0,2000,threshold)
        self.entryVariableAnglePCO.set(pcoAngle)
    
    def OnBrowseClick(self):
        filename = tkFileDialog.askopenfilename(initialdir =self.entryVariable.get(), filetypes=(("NEXUS files", "*.nxs"),
                                           ("All files", "*.*") ))
        if len(filename ) > 0:
            print "You chose %s" % filename 
            self.entry.focus_set()
            self.entry.selection_range(0, Tkinter.END)
            self.entryVariable.set(filename)
    
    def OnBrowsePCOClick(self):
        filename = tkFileDialog.askopenfilename(initialdir =self.entryVariablePCO.get(), filetypes=(("NEXUS files", "*.nxs"),
                                           ("All files", "*.*") ))
        if len(filename ) > 0:
            print "You chose %s" % filename 
            self.entry.focus_set()
            self.entry.selection_range(0, Tkinter.END)
            self.entryVariablePCO.set(filename)

    def OnButtonClick(self):
        #self.entry.focus_set()
        #self.entry.selection_range(0, Tkinter.END)
        #self.entryData.focus_set()
        #self.entryData.selection_range(0, Tkinter.END)
        self.btnCallBack()
    def OnButtonPCOClick(self):
        #self.entry.focus_set()
        #self.entry.selection_range(0, Tkinter.END)
        #self.entryData.focus_set()
        #self.entryData.selection_range(0, Tkinter.END)
        self.btnPCOCallBack()
    '''    
    def hide_me(self):
        self.widget.pack_forget()
     '''   
if __name__ == "__main__":
    app=myGui_tk(None)
    app.title('my window')
    app.mainloop()

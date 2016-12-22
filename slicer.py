import c4d # reference Cinema4D's existing library of code, called a "module"
from c4d import gui

def main(): # Define the main function of the script
    
    gui.MessageDialog('First test')
    ActiveObjects = doc.GetActiveObjects(c4d.GETACTIVEOBJECTFLAGS_0) # Look for the currently selected objecta
    
    if len(ActiveObjects) == 0:
        gui.MessageDialog('Zero Object Selected Objects')
        return # if there is no object selected, quit
    
    if len(ActiveObjects) > 2:
        gui.MessageDialog('Select only 2 Objects')
        return
    
    if len(ActiveObjects) < 2:
        gui.MessageDialog('Select only 2 Objects')
        return
    
    FirstObject = ActiveObjects[0]
    c4d.CallCommand(1011010, 1011010) # Connect
    firstConnect =  doc.GetActiveObject()
    firstConnect.SetName(FirstObject.GetName()+' Slicer')
    firstConnect[c4d.CONNECTOBJECT_LINK] = FirstObject
    doc.SetActiveObject(firstConnect)
    c4d.CallCommand(12236) #Make editable
    
    gui.MessageDialog(FirstObject)
    
    SecondObject = ActiveObjects[0]
    c4d.CallCommand(1011010, 1011010) # Connect
    secondConnect =  doc.GetActiveObject()
    secondConnect.SetName(SecondObject.GetName()+' Sliced')
    secondConnect[c4d.CONNECTOBJECT_LINK] = SecondObject
    doc.SetActiveObject(secondConnect)
    c4d.CallCommand(12236) #Make editable
    
    c4d.CallCommand(1010865, 1010865) # Boole
    BooleObject = doc.GetActiveObject()
    BooleObject()[c4d.ID_BASELIST_NAME]="Slice Main"
    BooleObject()[c4d.BOOLEOBJECT_TYPE]=1
    BooleObject()[c4d.BOOLEOBJECT_SINGLE_OBJECT]=True
    BooleObject()[c4d.BOOLEOBJECT_HIDE_NEW_EDGES]=True
    BooleObject()[c4d.BOOLEOBJECT_BREAK_CUT_EDGES]=True
    BooleObject()[c4d.BOOLEOBJECT_SEL_CUT_EDGES]=True
    
    c4d.CallCommand(1010865, 1010865) # Boole
    BooleObject2 = doc.GetActiveObject()
    BooleObject2()[c4d.ID_BASELIST_NAME]="Slice Extra"
    BooleObject2()[c4d.BOOLEOBJECT_TYPE]=2
    BooleObject2()[c4d.BOOLEOBJECT_SINGLE_OBJECT]=True
    BooleObject2()[c4d.BOOLEOBJECT_HIDE_NEW_EDGES]=True
    BooleObject2()[c4d.BOOLEOBJECT_BREAK_CUT_EDGES]=True
    BooleObject2()[c4d.BOOLEOBJECT_SEL_CUT_EDGES]=True
    
    
    firstConnect.InsertUnder(BooleObject) # Insert the removed object as a child of the following object in the manager
    secondConnect.InsertUnder(BooleObject) # Insert the removed object as a child of the following object in the manager
    
    c4d.CallCommand(1011010, 1011010) # Connect
    instFirst =  doc.GetActiveObject()
    instFirst.SetName(FirstObject.GetName()+' Instance')
    instFirst[c4d.CONNECTOBJECT_LINK] = FirstObject
    instFirst.InsertUnder(BooleObject2)
    
    c4d.CallCommand(1011010, 1011010) # Connect
    instSecond =  doc.GetActiveObject()
    instSecond.SetName(SecondObject.GetName()+' Instance')
    instSecond[c4d.CONNECTOBJECT_LINK] = SecondObject
    instSecond.InsertUnder(BooleObject2)
    
    
    doc.SetActiveObject(BooleObject2)
    c4d.CallCommand(12236) #Make editable
    
    doc.SetActiveObject(BooleObject)
    c4d.CallCommand(12236) #Make editable
    
    
    c4d.CallCommand(5140, 5140) # Null
    unSliced =  doc.GetActiveObject()
    unSliced.SetName('unSliced')
    SecondObject.InsertUnder(unSliced)
    FirstObject.InsertUnder(unSliced)
    FirstObject[c4d.ID_BASEOBJECT_VISIBILITY_RENDER]=1
    FirstObject[c4d.ID_BASEOBJECT_VISIBILITY_EDITOR]=1
    SecondObject[c4d.ID_BASEOBJECT_VISIBILITY_RENDER]=1
    SecondObject[c4d.ID_BASEOBJECT_VISIBILITY_EDITOR]=1
    

    
    
    doc.EndUndo() # Marks the end of a range of code that should be reversible
    c4d.EventAdd() # Refresh the scene to update the change

     
if __name__=='__main__': # These two lines close out the main function.  This is usually what will be used to end your script.
    main()

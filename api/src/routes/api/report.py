from fastapi import APIRouter
from fastapi.responses import FileResponse
from docxtpl import DocxTemplate
from pydantic import BaseModel
import pandas as pd


router = APIRouter(
    prefix="/report", 
    tags=["Report"]
    )  

@router.get('/{contenerID}')
def root(contenerID:str, satrt:int,end:int):
    data=pd.read_csv('static/data/_SELECT_FROM_select_from_GTERDTASNF_PHISMV_WHERE_hmdate_20221011 (1).csv', low_memory = False)
    df=data[['HMDATE','HMCONT','HMETA','HMTARE','HMPBRUT','HMPDSCTF','HMFRIGO','HMTMAXI','HMTMINI','HMDARREN','HMDDPREN','HMREFEVP','HMDANG']]
    ph=df[(df['HMCONT']==contenerID)&(df['HMDATE']>satrt)&(df['HMDATE']<end)]
        
    
    C=ph['HMTARE']
    G=ph['HMPBRUT']
    CW=ph['HMPDSCTF']
    F=ph['HMFRIGO']
    #I=ph['']
    #O=ph['']
    M=ph['HMTMAXI']
    N=ph['HMTMINI']
    D=ph['HMDARREN']
    E=ph['HMDARREN']
    EA=ph['HMDDPREN']
    ED=ph['HMDDPREN']
    CC="MASSING"
    CM=ph['HMREFEVP']
    DC=ph['HMDANG']
    doc=DocxTemplate('Static/tanger report template.docx')
    context={'id':contenerID, 'start':satrt,'end':end,'Ctare':C.values,'Gweight':G.values,'Cweight':CW.values,'Findicator':F.values,'Itemperature':"MISSING",'Otemperature':"MISSING",'MtemperatureRequested':M.values
    ,'NtemperatureRequested':N.values,'debarqdate':D.values,'embarqdate':E.values,'estimatedarrival':EA.values,'estimateddeparture':ED.values,'containercontent':CC,'containerdimensions':CM.values,'dangerouscontainerindictor':DC.values}
    doc.render(context)

    A=doc.save('static/reports/output2.docx')
    
    return FileResponse('output2.docx')
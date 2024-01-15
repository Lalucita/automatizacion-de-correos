# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 11:22:47 2023

@author: LuPerez
"""

import pandas as pd

class sucursales:
    
    
    copia_region_occidente='PGiacoman@bnb.com.bo; RRojas@bnb.com.bo; LoCabrera@bnb.com.bo; LAcha@bnb.com.bo; OQuiroga@bnb.com.bo; MoAntezana@bnb.com.bo'
    copia_region_centro='LAcha@bnb.com.bo; PGiacoman@bnb.com.bo; MPanoni@bnb.com.bo; RRojas@bnb.com.bo; LoCabrera@bnb.com.bo; MoAntezana@bnb.com.bo'
    copia_region_oriente='MoAntezana@bnb.com.bo;RRojas@bnb.com.bo;PGiacoman@bnb.com.bo;FDominguez@bnb.com.bo;LoCabrera@bnb.com.bo;LAcha@bnb.com.bo'
    
    dest_lpz='XGonzalesG@bnb.com.bo;NiRivera@bnb.com.bo;GMedeiros@bnb.com.bo;MCampos@bnb.com.bo;SVillegas@bnb.com.bo;MRLoza@bnb.com.bo'
    dest_sucre='JPari@bnb.com.bo;CSaucedo@bnb.com.bo;YSCuellar@bnb.com.bo;AArata@bnb.com.bo'
    dest_scz='EArdaya@bnb.com.bo;YSalces@bnb.com.bo;GVazquez@bnb.com.bo;ENieme@bnb.com.bo;MAPinto@bnb.com.bo;GCarrillo@bnb.com.bo'
    cba='JPAlcocer@bnb.com.bo;NChipani@bnb.com.bo;RArdaya@bnb.com.bo;MElias@bnb.com.bo'
    oruro='GAzuga@bnb.com.bo'
    tarija='JDMoscoso@bnb.com.bo'
    potosi='EGarrett@bnb.com.bo'
    beni='SUribe@bnb.com.bo'
    pando='ABonilla@bnb.com.bo'
    el_alto='FVega@bnb.com.bo'
    
    micro_centro='LAcha@bnb.com.bo;MTelleria@bnb.com.bo;RVelasco@bnb.com.bo;RRojas@bnb.com.bo;SYanez@bnb.com.bo'
    micro_oriente='MTelleria@bnb.com.bo;GMendoza@bnb.com.bo;SYanez@bnb.com.bo;LAcha@bnb.com.bo;RRojas@bnb.com.bo;LoCabrera@bnb.com.bo'
    micro_occidente='MTelleria@bnb.com.bo;LLaura@bnb.com.bo;SYanez@bnb.com.bo;LAcha@bnb.com.bo;RRojas@bnb.com.bo;LoCabrera@bnb.com.bo'
    
    sucreM ='CSaucedo@bnb.com.bo;YSCuellar@bnb.com.bo;AArata@bnb.com.bo'
    laPazM ='CaMaidana@bnb.com.bo;MTelleria@bnb.com.bo'
    cochabambaM ='SeRamirez@bnb.com.bo;SRivero@bnb.com.bo;DaSanchez@bnb.com.bo'
    oruroM ='ATaborga@bnb.com.bo;ETorrico@bnb.com.bo'
    potosiM ='RFlores@bnb.com.bo'
    tarijaM ='OPedraza@bnb.com.bo;JDMoscoso@bnb.com.bo'
    santa_cruzM ='KChavez@bnb.com.bo;LVillarroel@bnb.com.bo;DCoronado@bnb.com.bo;MCaballero@bnb.com.bo'
    beniM ='FSuarez@bnb.com.bo'
    el_altoM='RArce@bnb.com.bo;Tarismendi@bnb.com.bo;GQuenallata@bnb.com.bo'
    
    
    def getSucursalesPersonas(self):

        # Crear un diccionario con las ciudades y sus capitales
        data = {
            'Ciudad': ['LA PAZ', 'SUCRE', 'SANTA CRUZ', 'COCHABAMBA', 'ORURO', 'TARIJA', 'POTOSI', 'BENI', 'PANDO','EL ALTO'],
            'Destinatarios': [self.dest_lpz, 
                              self.dest_sucre, 
                              self.dest_scz, 
                              self.cba, 
                              self.oruro, 
                              self.tarija, 
                              self.potosi, 
                              self.beni, 
                              self.pando,
                              self.el_alto],
            'Destinatarios_en_CC': [self.copia_region_occidente, 
                                    self.copia_region_centro, 
                                    self.copia_region_oriente, 
                                    self.copia_region_centro, 
                                    self.copia_region_occidente, 
                                    self.copia_region_centro,
                                    self.copia_region_centro, 
                                    self.copia_region_oriente, 
                                    self.copia_region_oriente,
                                    self.copia_region_occidente]
            
            }

        df = pd.DataFrame(data)
        return df




    def getSucursalesMicrocreditos(self):

        # Crear un diccionario con las ciudades y sus capitales
        data = {
            'Ciudad': ['LA PAZ', 'SUCRE', 'SANTA CRUZ', 'COCHABAMBA', 'ORURO', 'TARIJA', 'POTOSI', 'BENI','EL ALTO'],
            
            'Destinatarios': [self.laPazM, 
                              self.sucreM, 
                              self.santa_cruzM, 
                              self.cochabambaM, 
                              self.oruroM, 
                              self.tarijaM, 
                              self.potosiM, 
                              self.beniM,
                              self.el_altoM],
            'Destinatarios_en_CC': [self.micro_occidente, 
                                    self.micro_centro, 
                                    self.micro_oriente, 
                                    self.micro_centro, 
                                    self.micro_occidente, 
                                    self.micro_centro,
                                    self.micro_centro, 
                                    self.micro_oriente, 
                                    self.micro_occidente]
            }

        df = pd.DataFrame(data)
        return df
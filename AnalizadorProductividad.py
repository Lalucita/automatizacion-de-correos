# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 15:23:26 2023

@author: LuPerez
"""


class AnalizadorProductividad:
    
    
    def obtener_agencias_destacadas(self,df_agencia ,porcentaje_referencia):
        return self.df_agencia[self.df_agencia['productividad'] > porcentaje_referencia][['agencia', 'productividad']]
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 21:14:02 2021

@author: Peyman
"""

Graph = {}
Graph["Peyman"] = {"Adam", "Frank", "George"}
Graph["Ema"] = {"Adam", "Bob", "Dolly"}
Graph["George"] = {"Peyman"}
Graph["Adam"] = {"Ema", "Peyman", "Bob"}
Graph["Frank"] = {"Peyman"}
Graph["Bob"] = {"Adam", "Ema", "Dolly"}
Graph["Dolly"] = {"Bob", "Ema"}

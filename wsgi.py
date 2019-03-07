# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 17:15:27 2019

@author: xutao
"""
import os

from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

from ReinDeer_web import app
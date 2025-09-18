import os 
import aiohttp
import logging
import asyncio
from typing import Dict, Any, Optional, List, Callable, Tuple 
from functools import reduce, partial 
from datetime import datetime 
from .config import WEATHER_API_KEY, LANGUAGE, BASE_WEATHER_URL 


#Configure logging 
logging.basicConfig(level=logging.INFO, format = '%(asctime)s - %(name)s - %(levename)s - %(message)s')
logger = logging.getLogger(__name__)

class WeatherAPIError(Exception):
    """Custom exception for OpenWeather API errors."""
    def __init__(self,status_code: int,message:str):
        self.status_code = status_code
        self.message = message 
        super().__init__(f"API Error {status_code}:{message}")

class ValidationError(Exception):
    """Custom Exception for OpenWeather API errors."""
    pass


# Import packages:
from sqlalchemy import create_engine; # Python application and db connect panna
# Each session lets you talk to the db, declarative_base: Base class for your orm models
from sqlalchemy.orm import sessionmaker, declarative_base; 
from dotenv import load_dotenv; # Loads environment variables from a.env file.
import os; # Python default module.
load_dotenv() #veliya iruka env files sa theadi eduthuittu vanthurum program kulla.
DATABASE_URL = os.getenv("DATABASE_URL") # load_dotenv() => ithula iruka data va access panrom 
# os.getenv moolama.
engine = create_engine(DATABASE_URL) # DB engine create pannittu atha oru variable la store panrom.
# (bind=engine) Intha marri kudutha than eppadi db connect panrathunu intha sessionmaker ku theriyum,
# autoflush=False => ithu ethuku na data automatic ka clear aagama thaduka.
SessionLocal = sessionmaker(bind=engine, autoflush=False) 
Base = declarative_base() # Intha function call panna namaku oru base class kedaikum atha vechi than ORM
# moda model classes sa extend panna moodiyum.
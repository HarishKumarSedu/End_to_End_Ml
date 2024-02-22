from src.mlProject.constants import *
from pathlib import Path 
from dataclasses import dataclass

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir : Path 
    source_url : Path 
    local_data_file: Path 
    unzip_dir: Path
    
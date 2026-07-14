import logging, sys
from pathlib import Path
from app.config import get_settings
def configure_logging():
    s=get_settings(); Path(s.log_file).parent.mkdir(parents=True,exist_ok=True)
    logging.basicConfig(level=getattr(logging,s.log_level.upper(),"INFO"),
      format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
      handlers=[logging.StreamHandler(sys.stdout),logging.FileHandler(s.log_file,encoding="utf-8")],force=True)

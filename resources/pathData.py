import os
from pathlib import Path
from webdriver_manager.chrome import ChromeDriverManager


url_path = Path("qahiring.dev.fishingbooker.com/charters/view/19612")
driver_path = ChromeDriverManager().install()
project_root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# resources path
resources_path = Path(project_root_path, "resources")
booking_number_path = Path(resources_path, "booking_number")

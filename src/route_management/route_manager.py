import json
import os

class RouteManager():
        
    def __init__(self):
        self.file_name = ""
        self.routes = {}
        
    def set_config_file(self, file_name: str):
        self.file_name = os.path.dirname(os.path.abspath(__file__)) + "/" + file_name
    
    def load_routes(self):
        with open(self.file_name) as route_config:
            parsed_config = json.load(route_config)
            if "routes" not in parsed_config:
                print("no routes found in json config")
            else:
                for route in parsed_config['routes']:
                    self.routes[route.get('name')] = route
                    
                print(self.routes)
                    
        
        
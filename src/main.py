import sys
from argparse import ArgumentParser
from route_management.route_manager import RouteManager
from tcp_proxy.proxy_server import ProxyServer

def main():
    parser = ArgumentParser()
    parser.add_argument("-r", "--routes", dest="route_config", help="JSON config with TCP forwarding routes", required=True)
    parser.add_argument("-p", "--port", dest="listen_port", help="The port the server should listen on", default=65432, type=int)
    args = parser.parse_args()
    
    print('STARTING TCP PROXY WITH ARGUMENTS:')
    for arg in vars(args):
        print(f"ARGUMENT: {arg}= {getattr(args, arg)}")
        
    # Configure Routes
    route_manager = RouteManager()
    route_manager.set_config_file(getattr(args, 'route_config'))
    route_manager.load_routes()
    
    # Start Proxy Server Instance
    proxy_server = ProxyServer(getattr(args, 'listen_port'), route_manager)
    proxy_server.start()
    
if __name__ == "__main__":
    main()
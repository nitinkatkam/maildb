import argparse
from aiosmtpd.controller import Controller
from sqlite_smtp_handler import SqliteHandler

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("--bind_ip", help="IP address to listen on")
  parser.add_argument("--port", help="TCP port to listen on")
  args = parser.parse_args()

  DEFAULT_HOSTNAME = '0.0.0.0'
  DEFAULT_PORT = 8025

  hostname = args.bind_ip if args.bind_ip else DEFAULT_HOSTNAME
  port = args.port if args.port else DEFAULT_PORT

  Controller(SqliteHandler(), hostname=hostname, port=port).start()

if __name__=='__main__':
    main()
    #time.sleep(60)
    txt = input()

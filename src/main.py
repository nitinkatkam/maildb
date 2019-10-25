import argparse
from aiosmtpd.controller import Controller
from src.sqlite_smtp_handler import SqliteHandler

def main():
  parser = argparse.ArgumentParser()
#TODO Read the bind IP and port as commandline parameters
#   parser.add_argument("--bind_ip", help="IP address to listen on")
  args = parser.parse_args()
  Controller(SqliteHandler()).start()

if __name__=='__main__':
    main()
    #time.sleep(60)
    txt = input()
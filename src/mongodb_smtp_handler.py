#************************************************************
# Title       : SMTP to Mongo
# Description : This runs an SMTP server on port 8025 and sends the body of any email it receives to a MongoDB database
# Author      : Nitin Reddy
# Date        : October 26, 2019
#************************************************************

import asyncio
from pymongo import MongoClient
import datetime

class MongoHandler:
  async def handle_DATA(self, server, session, envelope):
    db = MongoClient("192.168.0.100", 27017).pymo
    db.email.insert_one(
        {
            "from": envelope.mail_from,
            "to": envelope.rcpt_tos,
            "when_utc": datetime.datetime.utcnow(),
            "content": envelope.content.decode('utf8', errors='replace')
        }
    )
    return '250 Written to database'

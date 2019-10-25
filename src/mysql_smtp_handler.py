import mysql.connector
import datetime

class SqliteHandler:
  async def handle_DATA(self, server, session, envelope):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd=""
    )
    cur = db.cursor()
    cur.execute('create table if not exists mail(mail_from text, mail_to text, when_utc text, body text)')
    cur.execute(
        'insert into mail(mail_from, mail_to, when_utc, body) values(%s, %s, %s, %s)',
        (
            envelope.mail_from,
            ';'.join(envelope.rcpt_tos),
            datetime.datetime.utcnow(),
            envelope.content.decode('utf8', errors='replace')
        )
    )
    db.commit()
    db.close()
    return '250 Written to database'

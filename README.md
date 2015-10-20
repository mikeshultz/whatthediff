# whatthediff

Source code for whatthediff.com

## Setup

### Mailer

#### Cron Jobs

Add the following to a crontab to process mails

    *       * * * * (/path/to/your/python /path/to/your/manage.py send_mail >> ~/cron_mail.log 2>&1)
    0,20,40 * * * * (/path/to/your/python /path/to/your/manage.py retry_deferred >> ~/cron_mail_deferred.log 2>&1)
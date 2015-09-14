from datetime import datetime, timedelta
from django.core.management.base import BaseCommand, CommandError
from whatthedoc.models import WebDocumentBody, WebDocumentDuplicate

import logging
logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Updates all documents with a new body.'

    #def add_arguments(self, parser):
    #    parser.add_argument('poll_id', nargs='+', type=int)

    def handle(self, *args, **options):

        bodies = WebDocumentBody.objects.filter(web_document__modified__lt = datetime.now() - timedelta(days=1))
        
        for old_body in bodies:
            logger.debug('Attempting to update WebDocument %s.' % old_body.web_document_id)

            new_body = WebDocumentBody()
            try:
                new_body.web_document = old_body.web_document
                new_body.save()
            except WebDocumentDuplicate: 
                """ Duplicate document, so unchanged. """
                pass
            finally:
                if new_body.pk:
                    logger.info('WebDocument %s was updated.' % new_body.web_document.web_document_id)
                else:
                    logger.info('WebDocument %s was not updated.' % new_body.web_document.web_document_id)
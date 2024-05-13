import logging

from celery import shared_task


logger = logging.getLogger(__name__)

@shared_task
def send_verification_code_by_email(email, code="dummy_email_code"):
    """ Implementation to send verification code by email. """
    logger.info(f"Verification code: {code} sent to email: {email}")

@shared_task
def send_verification_code_by_sms(phone, code="dummy_phone_code"):
    """ Implementation to send verification code by phone. """
    logger.info(f"Verification code: {code} sent to phone: {phone}")

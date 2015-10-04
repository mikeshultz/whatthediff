from django.conf import settings

def settings_context_processor(request):
    """ This context processor is meant to deliver any settings from
        settings.py we want
    """
    whiteSettings = {
        'DEBUG':                            settings.DEBUG,
        'REGISTRATION_OPEN':                settings.REGISTRATION_OPEN,
    }

    return {
        'settings': whiteSettings,
    }
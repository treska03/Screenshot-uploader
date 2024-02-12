from plyer import notification


class Notification:

    @staticmethod
    def notify(title='', message='', app_name='', app_icon='', timeout=5):
        notification.notify(
            title=title,
            message=message,
            app_name=app_name,
            app_icon=app_icon,
            timeout=timeout 
        )
        
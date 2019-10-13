import datetime
from django.urls import register_converter

class PubDateConverter:
    regex = '[0-9]{4}-[0-9]{2}-[0-9]{2}'
    format = '%Y-%m-%d'

    def to_python(self, value: str) -> datetime:
        return datetime.datetime.strptime(value, self.format).date()

    def to_url(self, value: datetime) -> str:
        return value.strftime(self.format)

register_converter(PubDateConverter, 'pub_date')
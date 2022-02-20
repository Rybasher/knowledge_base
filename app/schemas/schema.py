from operator import index
from pydantic import BaseModel


class сonspect(BaseModel):
    index: int
    size: float
    title = 'Paragraph',
    description = 'this is the conspect',

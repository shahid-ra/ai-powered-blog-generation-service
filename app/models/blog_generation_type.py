from enum import Enum

class BlogGenerationType(str, Enum):
    PROFESSIONAL = "professional"
    EDUCATIONAL = "educational"
    INFORMATIONAL = "informational"
    STORYTELLING = "storytelling"

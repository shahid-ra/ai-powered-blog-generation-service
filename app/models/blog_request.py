from pydantic import BaseModel, Field
from app.models.blog_generation_type import BlogGenerationType


class BlogGenerationRequest(BaseModel):
    topic: str = Field(
        ...,
        min_length=3,
        max_length=500,
        description="The topic for the blog post"
    )
    generation_type: BlogGenerationType = Field(
        default=BlogGenerationType.INFORMATIONAL,
        description="The style/type of blog post to generate"
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "topic": "The Future of Artificial Intelligence",
                    "generation_type": "professional"
                },
                {
                    "topic": "How to Learn Python Programming",
                    "generation_type": "educational"
                }
            ]
        }
    }


class BlogGenerationResponse(BaseModel):
    topic: str = Field(description="The topic that was used for generation")
    generation_type: str = Field(description="The blog style that was used")
    content: str = Field(description="The generated blog content")
    status: str = Field(default="success", description="Status of the generation")

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "topic": "The Future of Artificial Intelligence",
                    "generation_type": "professional",
                    "content": "# The Future of Artificial Intelligence\n\n...",
                    "status": "success"
                }
            ]
        }
    }

from fastapi import APIRouter, HTTPException
from app.models.blog_request import BlogGenerationRequest, BlogGenerationResponse
from app.orchestration.blog_crew import BlogGenerationCrew

router = APIRouter(prefix="/v1/blog", tags=["Blog Generation"])


@router.post(
    "/generate",
    response_model=BlogGenerationResponse,
    summary="Generate a blog post",
    description="Generate a blog post on a given topic using AI-powered research and writing agents."
)
async def generate_blog(request: BlogGenerationRequest) -> BlogGenerationResponse:
    try:
        crew = BlogGenerationCrew(
            topic=request.topic,
            blog_type=request.generation_type
        )
        content = crew.run()

        return BlogGenerationResponse(
            topic=request.topic,
            generation_type=request.generation_type.value,
            content=content,
            status="success"
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to generate blog: {str(e)}"
        )

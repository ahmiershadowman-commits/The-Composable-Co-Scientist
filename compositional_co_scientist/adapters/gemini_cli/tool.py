"""Gemini CLI tool adapter."""


class GeminiTool:
    """Gemini CLI tool declaration adapter."""
    
    def __init__(self, name: str = "generate"):
        self.name = name
    
    def declare(self):
        """Declare tool for Gemini CLI."""
        return {"name": self.name, "description": f"Tool: {self.name}"}
    
    def invoke(self, **kwargs):
        """Invoke tool via Gemini CLI."""
        pass

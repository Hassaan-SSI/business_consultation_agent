import os
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()
PROJECT_ROOT = Path(__file__).resolve().parent.parent
class Settings:
    google_api_key: str = os.getenv("GOOGLE_API_KEY", "")
    gemini_model: str = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
    llm_mode: str = os.getenv("LLM_MODE", "live").lower()
    max_review_iterations: int = int(os.getenv("MAX_REVIEW_ITERATIONS", "2"))
    critic_debug_trigger: bool = os.getenv("CRITIC_DEBUG_TRIGGER", "false").lower() in ("1", "true", "yes")
    output_dir: Path = Path(os.getenv("OUTPUT_DIR", "outputs"))
    @classmethod
    def is_mock_llm(cls) -> bool:
        return cls.llm_mode == "mock"
settings = Settings()

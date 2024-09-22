from abc import ABC, abstractmethod
from typing import Dict, Type
from langchain.chat_models.base import BaseChatModel
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables from .env file
load_dotenv()

class AIProvider(ABC):
    @abstractmethod
    def __init__(self, model: str, stream: bool):
        pass

    @abstractmethod
    def get_chat_model(self) -> BaseChatModel:
        pass

class CerebrasProvider(AIProvider):
    def __init__(self, model: str, stream: bool):
        self.api_key = os.getenv("CEREBRAS_API_KEY")
        self.model = model
        self.stream = stream

    def get_chat_model(self) -> BaseChatModel:
        # Placeholder: Implement Cerebras chat model when available
        raise NotImplementedError("Cerebras chat model not implemented yet")

class GroqProvider(AIProvider):
    def __init__(self, model: str, stream: bool):
        self.api_key = os.getenv("GROQ_API_KEY")
        self.model = model
        self.stream = stream
        self.chat_api = ChatGroq(
            groq_api_key=self.api_key,
            model_name=self.model,
            streaming=self.stream,
            temperature=0.5
        )

    def get_chat_model(self) -> BaseChatModel:
        return self.chat_api
    
class GeminiProvider(AIProvider):
    def __init__(self, model: str, stream: bool):
        self.api_key = os.getenv("GEMINI_API_KEY")
        self.model = model
        self.stream = stream
        self.chat_api = ChatGoogleGenerativeAI(
            model=self.model,
            google_api_key=self.api_key,
            streaming=self.stream,
        )

from enum import Enum

class AIProviderType(Enum):
    CEREBRAS = "cerebras"
    GROQ = "groq"
    GEMINI = "gemini"

class AIProviderFactory:
    providers: Dict[AIProviderType, Type[AIProvider]] = {
        AIProviderType.CEREBRAS: CerebrasProvider,
        AIProviderType.GROQ: GroqProvider,
        AIProviderType.GEMINI: GeminiProvider,
    }

    @classmethod
    def create_provider(cls, provider_type: AIProviderType, model: str, stream: bool = False) -> BaseChatModel:
        provider_class = cls.providers.get(provider_type)
        if not provider_class:
            raise ValueError(f"Unsupported provider: {provider_type}")
        provider = provider_class(model, stream)
        return provider.get_chat_model()
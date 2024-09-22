from abc import ABC, abstractmethod
from langchain_community.document_loaders import PDFPlumberLoader

class Parser(ABC):
    @abstractmethod
    def parse(self, file_path: str) -> str:
        """Parse the given file and return its content as a string."""
        pass

class PDFParser(Parser):
    def parse(self, file_path: str) -> str:
        # Implementation for parsing PDF files
        pass

class TXTParser(Parser):
    def parse(self, file_path: str) -> str:
        # Implementation for parsing TXT files
        pass

# Add more parser classes for other file types as needed

class ParserFactory:
    @staticmethod
    def get_parser(file_type: str) -> Parser:
        if file_type.lower() == 'pdf':
            return PDFParser()
        elif file_type.lower() == 'txt':
            return TXTParser()
        # Add more file types as needed
        else:
            raise ValueError(f"Unsupported file type: {file_type}")

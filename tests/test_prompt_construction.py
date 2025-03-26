import os
import sys
import unittest
from unittest.mock import patch, mock_open

# Add parent directory to path so we can import our modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from obsidian_summarizer import summarize_content
from examples import FEW_SHOT_EXAMPLES

class TestPromptConstruction(unittest.TestCase):
    """Test cases for verifying prompt construction."""

    @patch('obsidian_summarizer.client.chat.completions.create')
    @patch('obsidian_summarizer.read_file_content')
    def test_few_shot_examples_included(self, mock_read_file, mock_openai):
        """Test that few-shot examples are properly included in the prompt."""
        # Setup mock file content
        mock_read_file.return_value = "This is a test note content."
        
        # Setup mock files
        test_files = ["/fake/path/test1.md", "/fake/path/test2.md"]
        
        # Call the function
        summarize_content(test_files)
        
        # Get the prompt that was sent to OpenAI
        actual_prompt = mock_openai.call_args[1]['messages'][1]['content']
        
        # Verify the examples are included
        self.assertIn(FEW_SHOT_EXAMPLES, actual_prompt)
        
        # Verify key phrases from examples are present
        key_phrases = [
            "RLHF is becoming standard",
            "Constitutional AI",
            "vector-database-comparison",
            "autonomous-agent-architecture",
            "Time-blocking technique"
        ]
        for phrase in key_phrases:
            self.assertIn(phrase, actual_prompt)
        
        # Verify the test content is included
        self.assertIn("This is a test note content", actual_prompt)
        
        # Verify the structure is correct
        self.assertIn("Now, please analyze the following content", actual_prompt)
        self.assertIn("comprehensive summary", actual_prompt)
        self.assertIn("glossary of important terms", actual_prompt)

    @patch('obsidian_summarizer.client.chat.completions.create')
    @patch('obsidian_summarizer.read_file_content')
    def test_prompt_with_multiple_files(self, mock_read_file, mock_openai):
        """Test that multiple files are properly combined in the prompt."""
        # Setup different content for each file
        file_contents = {
            "test1.md": "Content from first file",
            "test2.md": "Content from second file"
        }
        
        def mock_read_side_effect(file_path):
            filename = os.path.basename(file_path)
            return file_contents[filename]
        
        mock_read_file.side_effect = mock_read_side_effect
        
        # Setup mock files
        test_files = ["/fake/path/test1.md", "/fake/path/test2.md"]
        
        # Call the function
        summarize_content(test_files)
        
        # Get the prompt that was sent to OpenAI
        actual_prompt = mock_openai.call_args[1]['messages'][1]['content']
        
        # Verify both file contents are included
        for content in file_contents.values():
            self.assertIn(content, actual_prompt)
        
        # Verify file names are included as headers
        for filename in file_contents.keys():
            self.assertIn(f"## {filename}", actual_prompt)

if __name__ == '__main__':
    unittest.main() 
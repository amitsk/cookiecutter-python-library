import pytest
from unittest.mock import patch, MagicMock
from  {{cookiecutter.pkg_name}}.main import main


class TestMain:
    """Test cases for the main module."""

    @patch('{{cookiecutter.pkg_name}}.main.logger')
    @patch('{{cookiecutter.pkg_name}}.main.scrabble_score')
    def test_main_function_calls_scrabble_score_and_logs_result(self, mock_scrabble_score, mock_logger):
        """Test that main() calls scrabble_score with 'hello' and logs the result."""
        # Arrange
        expected_score = 8
        mock_scrabble_score.return_value = expected_score
        
        # Act
        main()
        
        # Assert
        mock_scrabble_score.assert_called_once_with("hello")
        mock_logger.info.assert_called_once_with(expected_score)

    @patch('{{cookiecutter.pkg_name}}.main.logger')
    @patch('{{cookiecutter.pkg_name}}.main.scrabble_score')
    def test_main_function_with_different_scrabble_score(self, mock_scrabble_score, mock_logger):
        """Test that main() works correctly with different scrabble score values."""
        # Arrange
        expected_score = 15
        mock_scrabble_score.return_value = expected_score
        
        # Act
        main()
        
        # Assert
        mock_scrabble_score.assert_called_once_with("hello")
        mock_logger.info.assert_called_once_with(expected_score)

    @patch('{{cookiecutter.pkg_name}}.main.logger')
    @patch('{{cookiecutter.pkg_name}}.main.scrabble_score')
    def test_main_function_handles_zero_score(self, mock_scrabble_score, mock_logger):
        """Test that main() correctly handles when scrabble_score returns 0."""
        # Arrange
        expected_score = 0
        mock_scrabble_score.return_value = expected_score
        
        # Act
        main()
        
        # Assert
        mock_scrabble_score.assert_called_once_with("hello")
        mock_logger.info.assert_called_once_with(expected_score)

    @patch('{{cookiecutter.pkg_name}}.main.logger')
    @patch('{{cookiecutter.pkg_name}}.main.scrabble_score')
    def test_main_function_exception_handling(self, mock_scrabble_score, mock_logger):
        """Test that main() properly propagates exceptions from scrabble_score."""
        # Arrange
        mock_scrabble_score.side_effect = ValueError("Test error")
        
        # Act & Assert
        with pytest.raises(ValueError, match="Test error"):
            main()
        
        mock_scrabble_score.assert_called_once_with("hello")
        mock_logger.info.assert_not_called()


    def test_main_function_return_value(self):
        """Test that main() returns None."""
        with patch('{{cookiecutter.pkg_name}}.main.logger'), \
             patch('{{cookiecutter.pkg_name}}.main.scrabble_score', return_value=8):
            result = main()
            assert result is None

    @patch('{{cookiecutter.pkg_name}}.main.logger')
    def test_main_function_integration_with_real_scrabble_score(self, mock_logger):
        """Integration test using the real scrabble_score function."""
        # Act
        main()
        
        # Assert - "hello" should score 8 points (h=4, e=1, l=1, l=1, o=1)
        mock_logger.info.assert_called_once_with(8)

class BaseValidator:
    def validate(self, user_input, expected_output):
        raise NotImplementedError("Subclasses should implement this method.")
    
    def is_valid(self, user_input, expected_output):
        return self.validate(user_input, expected_output)
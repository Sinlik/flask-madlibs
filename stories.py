"""Madlibs Stories."""


class Story:
    def __init__(self, prompts, text):
        """Create story with words and template text."""

        self.prompts = prompts
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        result = self.template
        for prompt in self.prompts:
            if prompt in answers:
                value = answers[prompt]
                if isinstance(value, list):
                    value = ', '.join(value)
                result = result.replace(f'{prompt}', value)
                    # for (key, val) in answers.items():
                    #     text = text.replace("{" + key + "}", val)
        return result


# Here's a story to get you started


# story = Story(
#     ["place", "noun", "verb", "adjective", "plural_noun"],
#     """Once upon a time in a long-ago {place}, there lived a
#        large {adjective} {noun}. It loved to {verb} {plural_noun}."""
# )

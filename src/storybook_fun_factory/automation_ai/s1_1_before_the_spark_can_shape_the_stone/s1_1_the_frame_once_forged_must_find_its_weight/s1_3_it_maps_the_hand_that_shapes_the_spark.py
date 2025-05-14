"""
Filename: s1_3_it_maps_the_hand_that_shapes_the_spark.py
(It Maps the Hand That Shapes the Spark)

This file implements the mapping system that tracks symbolic intentions,
user-generated instructions, or AI-driven decisions, and converts them
into structured traces. These traces become the foundation for recursive
template execution and automated code construction.
"""

class SparkMapper:
    """
    Tracks and stores symbolic mappings between user inputs and generated automation patterns.
    """

    def __init__(self):
        self.mapping_log = {}

    def map_spark(self, user_input: str, generated_code: str) -> None:
        """
        Stores a mapping between a symbolic user input and its associated code output.
        """
        self.mapping_log[user_input] = generated_code

    def get_mapping(self, user_input: str) -> str:
        """
        Retrieves the code previously mapped to a given user input.
        Returns a failure message if no such mapping exists.
        """
        return self.mapping_log.get(user_input, "⚠️ No mapping found for this input.")

    def has_mapping(self, user_input: str) -> bool:
        """
        Checks whether a given user input has an existing mapping.
        """
        return user_input in self.mapping_log

    def all_mappings(self) -> dict:
        """
        Returns the full mapping log.
        """
        return self.mapping_log.copy()

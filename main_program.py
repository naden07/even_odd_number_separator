from file_handler import FileHandler
from number_processor import NumberProcessor


class ParityApp:
    """Main application class to coordinate the file processing task."""

    def __init__(self):
        self.handler = FileHandler("numbers.txt")
        self.processor = NumberProcessor()

        self.output_even = "even.txt"
        self.output_odd = "odd.txt"

    def start(self):
        print("🔍 Reading numbers.txt...")
        try:
            # 1. Load data
            all_numbers = self.handler.read_integers()

            # 2. Sort data
            even_numbers = self.processor.separate_evens(all_numbers)
            odd_numbers = self.processor.separate_odds(all_numbers)

            # 3. Save data
            self.handler.write_integers(self.output_even, even_numbers)
            self.handler.write_integers(self.output_odd, odd_numbers)

            print(f"Success!")
            print(f"Created {self.output_even} with {len(even_numbers)} integers.")
            print(f"Created {self.output_odd} with {len(odd_numbers)} integers.")

        except Exception as error:
            print(f"❌ Error occurred: {error}")


if __name__ == "__main__":
    app = ParityApp()
    app.start()
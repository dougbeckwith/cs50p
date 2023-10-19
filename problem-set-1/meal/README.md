# Mealtime Detector

The Mealtime Detector is a Python program that helps you identify mealtime based on a given time input. It allows you to input a time in hours and minutes (e.g., "7:30") and checks if it's breakfast, lunch, or dinner time based on predefined time ranges.

## Usage

1. Run the program by executing the following command:

   ```bash
   python meal.py
   ```

2. You will be prompted to enter a time in the format "HH:MM" (e.g., "7:30").The program assumes that users will enter the time in the "HH:MM" format.

3. The program will convert your input into a numeric time format and check if it falls within specific time ranges to identify mealtime.

4. It will display the mealtime if your input matches one of the predefined time ranges:

   - **Breakfast time:** between 7:00 AM and 8:00 AM
   - **Lunchtime:** between 12:00 PM and 1:00 PM
   - **Dinner time:** between 6:00 PM and 7:00 PM

5. If your input doesn't match any of the predefined mealtime ranges, the program will exit without displaying a specific mealtime.

## Example

Suppose you want to check the mealtime for a specific time, for instance, 7:45 AM. Here's how you can use the Mealtime Detector program:

```plaintext
What time is it? 7:45
breakfast time
```

In this example, the program correctly identifies 7:45 AM as breakfast time.

# importing libraries for typing test
import time


sentence_25 = ( 
    "Python coding sharpens logic and creativity when you build small projects daily\n"
    "Solving problems improves focus confidence and skill"

)

sentence_40 = (
    "Building projects in Python strengthens your logic and problem solving skills and teaches you to structure code effectively\n"
    "Small exercises compound over time creating confidence and mastery in your abilities\n"
    "Practice consistently to unlock creativity and develop discipline with every line you write"
)

# formula for calculating wpm  = (total words / total time in seconds) * 60
def calculate_wpm(input_text , time_taken):
    words = input_text.split()
    num_words = len(words)
    wpm = (num_words / time_taken) * 60
    return round(wpm)

ask = input("Do you want to test your typing speed? (yes/no): ").strip().lower()
if ask == 'yes':
    print("how many words do you want to type? (25/40)")
    choice = input("Enter 25 or 40: ").strip()
    if choice == '25':
        print("rules : Type the following sentence as fast and accurately as you can. and press Enter when done.")
        print("test start here ")
        print(sentence_25)
        print("test ended here")
        input("____________Press Enter when you are ready to start__________")
        start_time = time.time()
        user_input = input()
        end_time = time.time()
        time_taken = end_time - start_time
        wpm = calculate_wpm(user_input, time_taken)
        print(f"Your typing speed is {wpm} words per minute.")
    elif choice == '40':
        print("rules : Type the following sentence as fast and accurately as you can. and press Enter when done.")
        print("test start here")
        print(sentence_40)
        print("test ended here ")
        input("Press Enter when you are ready to start...")
        start_time = time.time()
        user_input = input()
        end_time = time.time()
        time_taken = end_time - start_time
        wpm = calculate_wpm(user_input, time_taken)
        print(f"Your typing speed is {wpm} words per minute.")
    else:
        print("Invalid choice. Please enter 25 or 40.")
elif ask == 'no':
    print("Thank you! Have a great day.")
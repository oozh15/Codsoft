def process_user_input(user_input):
    user_input = user_input.lower()  
    if "timing" in user_input or "open" in user_input or "close" in user_input:
        return "The temple is open from 6:00 AM to 12:00 PM and 4:00 PM to 9:00 PM."
    elif "pooja" in user_input or "schedule" in user_input or "ritual" in user_input:
        return ("Here is the pooja schedule:\n"
                "- Morning Pooja: 7:00 AM\n"
                "- Evening Pooja: 6:30 PM\n"
                "- Special Abhishekam: Fridays at 8:00 AM.")
    elif "dress" in user_input or "attire" in user_input or "clothes" in user_input:
        return "Please wear traditional attire. Men: Dhoti, Women: Saree or Salwar Kameez."
    elif "location" in user_input or "address" in user_input or "where" in user_input:
        return "The temple is located at 123 Temple Street, CityName. Use 'TempleName' as the landmark on GPS."
    elif "offering" in user_input or "prasad" in user_input or "coconut" in user_input:
        return "You can offer flowers, fruits, or coconuts. Ensure offerings are fresh and clean."
    elif "event" in user_input or "festival" in user_input or "special" in user_input:
        return "Upcoming Event: Navratri Festival from October 15th to October 24th. Daily pooja at 6:00 PM."
    elif "slipper" in user_input or "shoe" in user_input or "footwear" in user_input:
        return "You can remove your slippers at the designated footwear stand near the temple entrance."
    elif "what time" in user_input or "when" in user_input or "best time" in user_input:
        return "You can visit the temple during pooja timings or when it's convenient within the opening hours."
    elif "thank" in user_input or "bye" in user_input or "exit" in user_input:
        return "Thank you for visiting the Temple Info Bot. Have a great day!"
    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase your question?"
def temple_chatbot():
    print("Welcome to the Temple Info Bot!")
    print("Ask me anything about the temple (e.g., timings, pooja, dress code, etc.) or type 'exit' to quit.")
    while True:
        user_input = input("\nYour question: ").strip()
        if user_input.lower() in ["exit", "quit"]:
            print("Thank you for using the Temple Info Bot. Goodbye!")
            break
        response = process_user_input(user_input)
        print(response)
temple_chatbot()


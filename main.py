# ==========================================
# GENESIS †
# Bible Guidance & Personal Growth Chatbot
# ==========================================

def welcome():
    print("\n" + "=" * 40)
    print("              GENESIS †")
    print("      Grow in faith. Grow in life.")
    print("=" * 40)

    name = input("What is your name? ")
    print(f"\nWelcome to Genesis, {name}!")

    goal = input(
        "\nChoose your personal growth goal:\n"
        "1. Grow in faith\n"
        "2. Become more patient\n"
        "3. Build confidence\n"
        "4. Practice kindness\n"
        "5. Find peace\n"
        "Choice: "
    )

    goals = {
        "1": "Grow in faith",
        "2": "Become more patient",
        "3": "Build confidence",
        "4": "Practice kindness",
        "5": "Find peace"
    }

    return name, goals.get(goal, "Personal growth")


def daily_verse():
    print("\n--- DAILY BIBLE VERSE ---")
    print('"Be strong and courageous."')
    print("Joshua 1:9")
    print("\nReflection:")
    print("Trust in God and take one step at a time.")


def faith_guide():
    print("\n--- GENESIS FAITH GUIDE † ---")
    feeling = input("How are you feeling today? ").lower()

    if "sad" in feeling:
        print("\nPsalm 34:18")
        print("God is close to the brokenhearted.")
        print("Your feelings matter. Consider talking")
        print("with someone you trust.")

    elif "angry" in feeling:
        print("\nJames 1:19")
        print("Be quick to listen and slow to speak.")
        print("Pause and choose a peaceful response.")

    elif "anxious" in feeling or "worried" in feeling:
        print("\nPhilippians 4:6-7")
        print("Bring your worries to God through prayer.")
        print("Take one step at a time and seek support.")

    elif "happy" in feeling or "grateful" in feeling:
        print("\n1 Thessalonians 5:16-18")
        print("Practice joy and gratitude.")
        print("What are you thankful for today?")

    else:
        print("\nProverbs 3:5-6")
        print("Trust in God's guidance.")
        print("Reflect on love, wisdom, and compassion.")

    print("\nGenesis is a faith reflection tool,")
    print("not a replacement for trusted human support.")


def bible_study():
    print("\n--- BIBLE STUDY ---")
    print("1. Love")
    print("2. Forgiveness")
    print("3. Courage")
    print("4. Peace")

    topic = input("Choose a topic: ")

    studies = {
        "1": (
            "Matthew 22:39",
            "Love your neighbor as yourself.",
            "Practice kindness and respect."
        ),
        "2": (
            "Matthew 6:14",
            "Reflect on the importance of forgiveness.",
            "Forgiveness can help us move toward peace."
        ),
        "3": (
            "Joshua 1:9",
            "Be strong and courageous.",
            "Face challenges with courage."
        ),
        "4": (
            "John 14:27",
            "Jesus speaks of peace.",
            "Seek peace through compassion and trust."
        )
    }

    if topic in studies:
        reference, teaching, reflection = studies[topic]
        print("\n" + reference)
        print(teaching)
        print("\nReflection:")
        print(reflection)
    else:
        print("Please select a valid topic.")


def journal():
    print("\n--- PERSONAL JOURNAL ---")
    reflection = input("What are you grateful for today? ")

    print("\nYour reflection:")
    print(reflection)
    print("\nThank you for reflecting with Genesis †.")


def show_profile(name, goal):
    print("\n--- MY PROFILE ---")
    print("Name:", name)
    print("Growth Goal:", goal)


def main():
    name, goal = welcome()

    while True:
        print("\n========== GENESIS MENU ==========")
        print("1. Daily Bible Verse")
        print("2. Faith Guide")
        print("3. Bible Study")
        print("4. Personal Journal")
        print("5. My Profile")
        print("6. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            daily_verse()
        elif choice == "2":
            faith_guide()
        elif choice == "3":
            bible_study()
        elif choice == "4":
            journal()
        elif choice == "5":
            show_profile(name, goal)
        elif choice == "6":
            print("\nThank you for using Genesis †.")
            print("Grow in faith. Grow in life.")
            break
        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()

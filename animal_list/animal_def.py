import wikipedia


def get_animal_definition(animal_name):
    try:
        summary = wikipedia.summary(animal_name, sentences=2)
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        return f"The term '{animal_name}' is ambiguous. Try one of these: {e.options[:5]}"
    except wikipedia.exceptions.PageError:
        return f"No definition found for '{animal_name}'. Please check the spelling."
    except Exception as e:
        return f"An error occurred: {str(e)}"


def main():
    print("=== Animal Definition Finder ===")
    while True:
        animal = input(
            "Enter an animal name (or type 'exit' to quit): ").strip()
        if animal.lower() == 'exit':
            print("Goodbye!")
            break
        definition = get_animal_definition(animal)
        print(f"\nDefinition of '{animal}':\n{definition}\n")


if __name__ == "__main__":
    main()

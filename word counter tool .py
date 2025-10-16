from collections import Counter

def analyze_text_file(filename):
    
    try:
        
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()

        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        line_count = len(lines)
        word_list = text.split()
        word_count = len(word_list)
        char_count = len(text)

        words = [word.strip('.,!?;:"()[]{}').lower() for word in word_list if word.isalpha() or word.isalnum()]

        word_freq = Counter(words)

        common_words = word_freq.most_common(10)

        print("\n TEXT FILE ANALYSIS REPORT ")
        
        print("-" * 40)
        
        print(f"Total Lines     : {line_count}")
        
        print(f"Total Words     : {word_count}")
        
        print(f"Total Characters: {char_count}")
        
        print("-" * 40)
        
        print("Top 10 Most Common Words:")
        
        print("-" * 40)
        
        print(f"{'Word':<15}{'Frequency'}")
        
        print("-" * 40)
        
        for word, freq in common_words:
            
            print(f"{word:<15}{freq}")
            
        print("-" * 40)

    except FileNotFoundError:
        
        print("Error: File not found. Please check the filename or path.")
        
    except Exception as e:
        
        print("An error occurred:", e)


filename = "ex.txt" 
analyze_text_file(filename)

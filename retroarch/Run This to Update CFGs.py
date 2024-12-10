import os

def main():
    # Default search string
    search_string = "/opt/retropie/configs/all/retroarch/overlay/ArcadeBezels/"
    
    # Prompt user for replacement path
    replace_string = input("Enter the replacement path: ").strip()
    
    if not replace_string:
        print("Error: Replacement path cannot be empty.")
        return

    # Get the directory where the script is located
    script_directory = os.path.dirname(os.path.abspath(__file__))

    # Walk through all files and subdirectories
    for root, _, files in os.walk(script_directory):
        for filename in files:
            if filename.endswith(".cfg"):
                file_path = os.path.join(root, filename)
                
                # Open the file in read mode
                with open(file_path, "r", encoding="utf-8") as file:
                    content = file.read()
                
                # Replace the search string with the replacement path
                updated_content = content.replace(search_string, replace_string)
                
                # Write changes back to the file if there were replacements
                if content != updated_content:
                    with open(file_path, "w", encoding="utf-8") as file:
                        file.write(updated_content)
                    print(f"Updated: {file_path}")
                else:
                    print(f"No changes needed: {file_path}")
    
    print("All replacements complete!")

if __name__ == "__main__":
    main()

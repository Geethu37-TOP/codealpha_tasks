import re

def extract_emails(input_file, output_file):
    print("--- Email Extraction Automation ---")
    try:
        # Read the content of the input file
        with open(input_file, 'r') as file:
            text = file.read()

        # Regex pattern to find email addresses
        pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        emails = re.findall(pattern, text)

        # Remove duplicates by converting to a set
        unique_emails = set(emails)

        if not unique_emails:
            print("No email addresses found in the file.")
            return

        # Write the extracted emails to the output file
        with open(output_file, 'w') as file:
            for email in unique_emails:
                file.write(email + '\n')

        print(f"Successfully extracted {len(unique_emails)} unique email addresses.")
        print(f"Saved directly to '{output_file}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found. Please create it first.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Create a quick sample file to ensure the script works out-of-the-box
    sample_filename = "sample_data.txt"
    with open(sample_filename, "w") as f:
        f.write("Reach out to our team at info@ebenixlabs.com or founders@ebenixlabs.com for more info. Do not email fake@test.")
    
    print(f"Created a test file: {sample_filename}")
    
    # Run the extraction function
    extract_emails(sample_filename, "extracted_emails.txt")

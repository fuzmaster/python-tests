# Define a function that takes a list of links and returns a sentence with the links separated by commas
def link_to_sentence(links):
    return ', '.join(links)

# Initialize an empty list to store the image links entered by the user
image_links = []

# Start a loop that continues until the user types 'done'
while True:
    # Prompt the user to enter an image link
    link = input("Enter an image link (or type 'done' to finish): ")
    
    # If the user types 'done', exit the loop
    if link == 'done':
        break
    
    # Otherwise, add the entered link to the list of image links
    image_links.append(link)

# Call the link_to_sentence function with the list of image links as input
output_sentence = link_to_sentence(image_links)

# Print the output sentence to the console
print(output_sentence)

# Contact Management System
<p align:left;>
  This Python code creates a <i>simple contact management program</i>. It uses a dictionary to store contacts, with names as keys and phone numbers as values.  Here's a breakdown of each function and its purpose:
  <ul>
    <li><b>add_contact()</b>: This function allows users to add new contacts. It takes the contacts dictionary as input.  It prompts the user for a name and phone number.  It validates the phone number to ensure it's a 10-digit integer. The function continues to prompt for contacts until the user enters "end" for the name. It then adds the new name-number pair to the contacts dictionary. Finally, it displays the updated contact list.</li>
    <br>
    <li><b>search_contact()</b>: This function searches for a contact by name. It takes the contacts dictionary as input. It prompts the user for a name to search. If the name exists in the dictionary, it displays the corresponding phone number. If not, it informs the user that the contact was not found.  It allows for multiple searches until the user enters "end."</li>
    <br>
    <li><b>del_contact()</b>: This function deletes a contact. It takes the contacts dictionary as input. It prompts the user for the name of the contact to delete. If the name exists, it removes the entry from the dictionary and displays a confirmation message.  If the name doesn't exist, it informs the user. Finally, it displays the updated contact list.</li>
    <br>
    <li><b>show_con(contacts)</b>: This function displays all contacts in the dictionary. It takes the contacts dictionary as input. It prints the total number of contacts and then iterates through the dictionary, displaying each name and phone number with a serial number.</li>
    <br>
    <li><b>rename()</b>: This function renames an existing contact. It takes the contacts dictionary as input. It prompts the user for the existing name and the new name.  It efficiently updates the dictionary by creating a new entry with the new name and transferring the value (phone number) from the old name, then deleting the old name.</li>
    <br>
    <li><b>change_number()</b>: This function changes the phone number of an existing contact.  It takes the contacts dictionary as input. It prompts the user for the name of the contact whose number needs to be changed and validates the new number is a 10 digit integer. It updates the number in the dictionary.</li>
    <br>
    <li><b>main()</b>: This is the main function that controls the program's flow. It initializes the contacts dictionary.  It presents the user with a menu of options (add, search, delete, rename, change number, show, quit). It takes user input for the desired command and calls the appropriate function.  The program continues to loop until the user chooses the "quit" option.</li>
    <br>
  </ul>
<b>Importance of this basic code:</b>
<i>This code, while simple, demonstrates fundamental programming concepts:</i><br>
<ol>
  <li><b>Data Structures</b>:  It showcases the use of dictionaries, a crucial data structure for storing and retrieving data efficiently using keys.</li>
  <br>
  <li><b>Functions</b>: It uses functions to modularize the code, making it more organized, readable, and reusable.</li>
  <br>
  <li><b>Control Flow</b>: It demonstrates control flow structures like while loops (for repetition) and if/elif/else statements (for decision-making).</li>
  <br>
  <li><b>User Input and Output</b>: It shows how to interact with the user, taking input and providing output.</li>
  <br>
  <li><b>Error Handling</b>:  It includes basic error handling (e.g., checking for invalid input) to make the program more robust.</li>
  <br>
  <li><b>Data Validation</b>: Basic data validation is performed on the phone numbers to ensure they are the correct length and format.</li>
  <br>
</ol>
<b>This type of code is a building block for more complex applications. The principles of data storage, retrieval, and user interaction are essential in many software projects.  It's a good starting point for learning how to manage data and create interactive programs.  From this foundation, you could add features like saving contacts to a file, searching by partial name, or implementing a more sophisticated user interface.</b>
</p>

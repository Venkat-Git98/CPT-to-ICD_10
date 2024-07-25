import pygetwindow as gw
import pyautogui
import time
import pyperclip

def focus_chrome_window(url):
    """
    Activates the Chrome window and navigates to a specified URL.
    
    Args:
    url (str): URL to be loaded in Chrome.
    """
    # Attempt to find and focus the Chrome window
    chrome_windows = gw.getWindowsWithTitle('Google Chrome')
    if chrome_windows:
        chrome_window = chrome_windows[0]
        chrome_window.minimize()  # Minimize and restore to ensure it comes to the foreground
        chrome_window.restore()
        time.sleep(2)  # Wait for the window to stabilize

        # Navigate to the specified URL
        pyautogui.click(4448, 600)  # Presumed location of the address bar
        pyautogui.write(url)
        pyautogui.press('enter')
    else:
        print("No Google Chrome window found.")

def enter_data(entries, url):
    """
    Enters a list of entries into a form on a webpage and submits the form.
    
    Args:
    entries (list of str): Data entries to be submitted.
    url (str): URL where data needs to be submitted.
    """
    focus_chrome_window(url)  # Ensure the Chrome window is focused and correct page is loaded
    
    # Prepare data for entry
    data_string = '\n'.join(entries)
    pyperclip.copy(data_string)  # Copy data to clipboard

    # Paste data into the form
    pyautogui.click(4955, 1266)  # Coordinates of the data entry field
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(3)  # Allow time for the text selection to occur
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)  # Allow time for the paste operation to complete

    # Submit the form
    pyautogui.click(4962, 1632)  # Coordinates of the 'Map' button
    time.sleep(150)  # Wait for processing to complete

    # Export the results
    pyautogui.click(6452, 1782)  # Coordinates of the 'Export' button
    time.sleep(10)  # Allow time for any post-operation processing

def process_chunks(entries, chunk_size=500):
    """
    Processes entries in chunks, submitting each chunk through a web form.
    
    Args:
    entries (list of str): List of all entries to be processed.
    chunk_size (int): Number of entries in each chunk.
    """
    url = "https://www.findacode.com/tools/map-a-code/cpt-hcpcs-pcs.php"
    for i in range(0, len(entries), chunk_size):
        chunk = entries[i:i + chunk_size]
        print(f'Processing chunk size: {len(chunk)}')
        enter_data(chunk, url)
        time.sleep(10)  # Wait a bit between batches

def main():
    """
    Main function to handle the workflow.
    """
    file_path = r"Directory for the text file with ICD codes."
    with open(file_path, 'r') as file:
        content = file.read()
    entries = content.split(',')  # Convert file content into a list of entries

    process_chunks(entries, 500)

if __name__ == "__main__":
    main()

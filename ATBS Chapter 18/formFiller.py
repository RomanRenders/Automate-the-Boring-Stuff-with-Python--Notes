#! python3
# Automatically fills in the form at autbor.com/form
import pyautogui, time
# Set these to the correct coordinates for your particular computer
nameField = (996, 525)
submitButton = (1003, 1118)
submitButtonColor = (26, 115, 232)
submitAnotherLink = (1064, 409)

formData = [{'name': 'Alice', 'fear': 'eavesdroppers', 'source': 'wand', 'robocop': 4, 'comments': 'Tell Bob I said hi.'},
            {'name': 'Bob', 'fear': 'bees', 'source': 'amulet', 'robocop': 4, 'comments': 'n/a'},
            {'name': 'Carol', 'fear': 'puppets', 'source': 'crystal ball', 'robocop': 1, 'comments': 'Please take the puppets out of the break room.'},
            {'name': 'Alex Murphy', 'fear': 'ED-209', 'source': 'money', 'robocop': 5, 'comments': 'Protect the innocent. Serve the public trust. Uphold the law.'},
            ]

pyautogui.PAUSE = 0.5

for person in formData:
    # Give the user a chance to kill the script
    print('>>> 4 SECOND PAUSE TO LET USER PRESS CTRL-C <<<')
    time.sleep(4)

    # Wait until form page has loaded.
    while not pyautogui.pixelMatchesColor(submitButton[0], submitButton[1], submitButtonColor):
        time.sleep(0.5)

    print('Entering %s info...' % (person['name']))
    pyautogui.click(nameField[0], nameField[1])                                                 # Clicks on Name field

    # Fill out Name field
    pyautogui.typewrite(person['name'] + '\t')                                                  # types name, press tab to move to next field

    # Fill out Greatest Fear(s) field
    pyautogui.typewrite(person['fear'] + '\t')                                                  # types fear, press tab to move to next field

    # Fill out Source of Wizard Powers field
    if person['source'] == 'wand':
        pyautogui.typewrite(['down', 'enter'])
    elif person['source'] == 'amulet':
        pyautogui.typewrite(['down', 'down', 'enter'])
    elif person['source'] == 'crystal ball':
        pyautogui.typewrite(['down', 'down', 'down', 'enter'])
    elif person['source'] == 'money':
        pyautogui.typewrite(['down', 'down', 'down', 'down', 'enter'])                          # fills source field, move on to next field
        
    # Fill out Robocop field
    pyautogui.press('\t')
    time.sleep(2)
    if person['robocop'] == 1:
        pyautogui.typewrite([' ', '\s'])
    elif person['robocop'] == 2:
        pyautogui.typewrite(['right', '\t'])
    elif person['robocop'] == 3:
        pyautogui.typewrite(['right', 'right', '\t'])
    elif person['robocop'] == 4:
        pyautogui.typewrite(['right', 'right', 'right', '\t'])
    elif person['robocop'] == 5:
        pyautogui.typewrite(['right', 'right', 'right', 'right', '\t'])

    # Fill out Additional comments
    time.sleep(3)
    pyautogui.typewrite(person['comments'], 0.2)
    pyautogui.press('\t')

    # Click Submit
    pyautogui.press('enter')

    # Wait until form page has loaded.
    print('Clicked Submit.')
    time.sleep(5)

    # Click the "Submit another response" link
    pyautogui.click(submitAnotherLink[0], submitAnotherLink[1])

















































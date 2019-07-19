import mouse
import keyboard

BUTTONS = ['left', 'right']  # valid button names


def main():
	button = input('Enter right or left: ')

	if button in BUTTONS:
		mouse.press(button=button)  # hold the button

		print('Waiting for escape key in order to stop...')
		keyboard.wait('esc')  # wait for escape key to be pressed
		mouse.release(button=button)  # stop holding
		print('Done!')
	else:
		print('Not a button...')


if __name__ == "__main__":
	main()

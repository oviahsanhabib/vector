#!/usr/bin/python3

import anki_vector
from PIL import Image
import time
import threading

IMAGE_FRAMES = [f"/home/pi/vector-python-sdk/wirepod/assets/rickroll/{i}.gif" for i in range(1, 47)]
SOUND_PATH = "/home/pi/vector-python-sdk/wirepod/assets/rickroll/rickroll.wav"

# Shared variable to signal lift motor thread to exit
stop_lift_thread = False

def show_image(robot, image_path, duration=5.0):
    resized_image = resize_image(image_path, 184, 96)
    screen_data = anki_vector.screen.convert_image_to_screen_data(resized_image)
    robot.screen.set_screen_with_image_data(screen_data, duration)

def play_sound(robot, sound_path):
    robot.audio.stream_wav_file(sound_path, 100)

def play_animation(robot, animation_name):
    robot.anim.play_animation(animation_name)

def loop_lift_motor(robot):
    while not stop_lift_thread:
        robot.motors.set_head_motor(5.0)
        time.sleep(0.5)
        robot.motors.set_lift_motor(2)
        time.sleep(0.5)
        robot.motors.set_lift_motor(-2)
        time.sleep(0.5)
        robot.motors.set_head_motor(-1.0)
        time.sleep(0.5)
        

def resize_image(image_path, target_width, target_height):
    original_image = Image.open(image_path)
    original_image = original_image.convert("RGB")
    resized_image = original_image.resize((target_width, target_height))
    return resized_image

def display_frames(robot, frames, duration_s=5.0, delay_between_frames=0.01, total_duration=60.0):
    start_time = time.time()
    while time.time() - start_time < total_duration:
        for frame_path in frames:
            show_image(robot, frame_path, duration_s)
            time.sleep(delay_between_frames)

def play_sound_in_background(robot, sound_path):
    threading.Thread(target=play_sound, args=(robot, sound_path)).start()

def main():
    global stop_lift_thread

    with anki_vector.Robot(cache_animation_lists=False) as robot:
        play_sound_in_background(robot, SOUND_PATH)
        lift_thread = threading.Thread(target=loop_lift_motor, args=(robot,))
        lift_thread.start()
        display_frames(robot, IMAGE_FRAMES, duration_s=7.0, delay_between_frames=0.01, total_duration=55.0)

        stop_lift_thread = True

        # Wait for the lift motor thread to finish before exiting the main program
        lift_thread.join()

if __name__ == "__main__":
    main()

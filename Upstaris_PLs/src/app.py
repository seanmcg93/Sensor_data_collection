import upstairs_count
import hand_stack

if __name__ == "__main__":
    sensor_up_count = upstairs_count.Sensor("upstairs_count", 0, 10)
    sensor_hand_stack = hand_stack.Sensor("hand_stack", 0, 9)
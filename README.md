# pyparrot-control-using-hand-gesture

## 📖 Description

This project is a proof of concept for controlling a drone using hand gestures. The project is based on the [pyparrot](https://pypi.org/project/pyparrot/) library.

![Parrot Bopop 2](fixtures/bepop2.jpg)


The project is divided into two parts:
1. `hand_gesture_recognition` which is responsible for detecting hand gestures and sending the appropriate command to the drone.
2. `drone_control` which is responsible for receiving the command from the `hand_gesture_recognition` and controlling the drone.

This project uses the [mediapipe](https://pypi.org/project/mediapipe/) library for hand gesture recognition.

## 🛠️ Requirements

- Ubuntu
- miniconda

## 💻 Installation


1. create `conda` virtual environment by running this command:

```
$~ make virenv
```

2. activate the environment by running this command:

```
$~ conda activate parrot-env
```



3. install requirements by running this command:

```
$~ make install
```

## 📑 Usage

1- You have to connect to the drone WiFi network. Example: `RS_XXXXXXXXXX`

2- Run the `main.py` file in the `src` directory, using this command:
    ```
    $~ python src/main.py
    ```

**BECAREFUL: BY RUNNING THIS COMMAND THE DRONE WILL TAKEOFF **

> if you want to test the `FingersCounter` class, you can run `test.py` file in the `src` directory, using this command:
    ```
    $~ python src/test.py
    ```


This is the list of commands to control the drone:
| Finger | Command |
|--|--|
| 0 | Land |
| 1 | Hover in place |
| 2 | pitch forward |
| 3 | pitch backward |
| 4 | roll right |
| 5 | roll left |
| 6 | yaw right |
| 7 | yaw left |
| 8 | go up |
| 9 | go down |

![Roll, Pitch & Yaw](fixtures/rotations.png)


## Configrable Parameters

You can change the following parameters in the `config.yaml` file:

| Parameter | Description |
|--|--|
| min detection confidence | minimum hand detection confidence |
| min tracking confidence | minimum hand tracking confidence |
| take off altitude | altitude to take off to |
| duration | duration of the command (the bigger the slower)|

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## 📚 References

- [pyparrot](https://pypi.org/project/pyparrot/)
- [mediapipe](https://pypi.org/project/mediapipe/)

## Contribution

If you want to contribute to this project, you can do it by forking the project and creating a pull request.
